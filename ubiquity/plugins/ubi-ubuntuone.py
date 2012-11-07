# -*- coding: utf-8; Mode: Python; indent-tabs-mode: nil; tab-width: 4 -*-

# Copyright (C) 2012 Canonical Ltd.
# Written by Michael Vogt <mvo@ubuntu.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import re
import os
import json
import syslog
import uuid

from ubiquity import plugin
#from ubiquity.plugin import InstallPlugin


NAME = 'ubuntuone'
AFTER = 'usersetup'
WEIGHT = 10

(PAGE_REGISTER,
 PAGE_LOGIN,
 PAGE_SPINNER,
 ) = range(3)

# TODO:
#  - network awareness (steal from timezone map page)
#  - rename this all to ubuntu sso instead of ubuntuone to avoid confusion
#    that we force people to sign up for payed services on install (?) where
#    what we want is to make it super simple to use our services
#  - take the username from the usersetup step when creating the token
#  - get a design for the UI
#    * to create a new account
#    * to login into a existing account
#    * deal with forgoten passwords
#    * skip account creation
#  - implement actual logic/verification etc *cough*
#    * make next button sensitive/insensitive depending on valid choice
#    * requires the logic to login/create accounts without email verify
#    * simplified way to talk to login.ubuntu.com as the installer
#      won't have twisted, either piston-mini-client based (and embedd
#      it) or entirely hand done via something like the spawn helper
#  - take the oauth token and put into the users keyring (how?)
#  - make the keyring unlocked by default


class UbuntuSSO(object):

    def login(self, email, password,
              callback, errback):
        # XXX: make it actually do something useful
        print("login: %s " % email)
        from gi.repository import GObject
        GObject.timeout_add(1500, lambda: callback({ 'token': 'none'}))

    def register(self, email, password,
                 callback, errback):
        # XXX: make it actually do something useful
        print("register: %s " % email)
        from gi.repository import GObject
        GObject.timeout_add(1500, lambda: callback({ 'token': 'none'}))


class PageGtk(plugin.PluginUI):
    plugin_title = 'ubiquity/text/ubuntuone_heading_label'
    
    OAUTH_TOKEN_FILE = '/var/lib/ubiquity/ubuntuone_oauth_token'

    def __init__(self, controller, *args, **kwargs):
        from gi.repository import Gtk
        self.controller = controller
        # add builder/signals
        builder = Gtk.Builder()
        self.controller.add_builder(builder)
        builder.add_from_file(os.path.join(os.environ['UBIQUITY_GLADE'],
            'stepUbuntuOne.ui'))
        builder.connect_signals(self)
        # make the widgets available under their gtkbuilder name
        for obj in builder.get_objects():
            if issubclass(type(obj), Gtk.Buildable):
                setattr(self, Gtk.Buildable.get_name(obj), obj)
        self.page = builder.get_object('stepUbuntuOne')
        self.notebook_main.set_show_tabs(False)
        self.plugin_widgets = self.page
        self.oauth_token = None
        self.online = False
        # the worker
        self.ubuntu_sso = UbuntuSSO()
        self.info_loop(None)

    def plugin_set_online_state(self, state):
        self.online = state

    def plugin_get_current_page(self):
        self.page.show_all()
        self.notebook_main.set_current_page(PAGE_REGISTER)
        return self.page

    def plugin_on_back_clicked(self):
        # stop whatever needs stopping
        return False

    def plugin_on_next_clicked(self, skip_creation=False):
        from gi.repository import Gtk
        if skip_creation:
            return False
        if self.notebook_main.get_current_page() == PAGE_REGISTER:
            # create a random password
            password = uuid.uuid4()
            self.ubuntu_sso.register(self.entry_email.get_text(),
                                     password,
                                     callback=self._ubuntu_sso_callback,
                                     errback=self._ubuntu_sso_errback)
        elif self.notebook_main.get_current_page() == PAGE_LOGIN:
            self.ubuntu_sso.login(self.entry_existing_email.get_text(),
                                  self.entry_existing_password.get_text(),
                                  callback=self._ubuntu_sso_callback,
                                  errback=self._ubuntu_sso_errback)
        else:
            raise AssertionError("Should never be reached happen")

        self.notebook_main.set_current_page(PAGE_SPINNER)
        self.spinner_connect.start()
        Gtk.main()
        self.spinner_connect.stop()

        if self.oauth_token is not None:
            # XXX: security, security, security! is the dir secure? if
            #      not ensure mode 0600
            with open(self.OAUTH_TOKEN_FILE, "w") as fp:
                fp.write(json.dumps(self.oauth_token))
        return False

    def plugin_translate(self, lang):
        # ???
        pass

    # callbacks 
    def _ubuntu_sso_callback(self, oauth_token):
        from gi.repository import Gtk
        self.oauth_token = oauth_token
        Gtk.main_quit()

    def _ubuntu_sso_errback(self, error):
        from gi.repository import Gtk
        syslog.syslog("ubuntu sso failed: '%s'" % error)
        Gtk.main_quit()

    # signals
    def on_button_have_account_clicked(self, button):
        self.notebook_main.set_current_page(PAGE_LOGIN)

    def on_button_need_account_clicked(self, button):
        self.notebook_main.set_current_page(PAGE_REGISTER)

    def on_button_skip_account_clicked(self, button):
        self.oauth_token = None
        self.plugin_on_next_clicked()

    def _verify_email_entry(self, email):
        EMAIL_REGEXP = "[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+"
        match = re.match(EMAIL_REGEXP, email)
        return (match is not None)

    def _verify_password_entry(self, password):
        return len(password) > 0

    def info_loop(self, widget):
        complete = False
        if self.notebook_main.get_current_page() == PAGE_REGISTER:
            email = self.entry_email.get_text()
            complete = self._verify_email_entry(email)
        elif self.notebook_main.get_current_page() == PAGE_LOGIN:
            email = self.entry_existing_email.get_text()
            password = self.entry_existing_password.get_text()
            complete = (self._verify_email_entry(email) and
                        self._verify_password_entry(password))
        self.controller.allow_go_forward(complete)

# FIXME: should we use this here instead of:
#         configure_oauth_token() in  scripts/plugininstall.py ?
#class Install(InstallPlugin):
#    def install(self, target, progress, *args, **kwargs):
#        pass
