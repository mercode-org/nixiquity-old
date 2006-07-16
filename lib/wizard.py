#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright (C) 2005, 2006 Canonical Ltd.
# Written by Colin Watson <cjwatson@ubuntu.com>.
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

import sys
import optparse

class Wizard:
    def __init__(self, frontend_name=None):
        if frontend_name is None:
            frontend_names = ['gtk-ui']
        else:
            frontend_names = [frontend_name]
        mod = __import__('oem_config.frontend', globals(), locals(),
                         frontend_names)
        for f in frontend_names:
            if hasattr(mod, f):
                ui = getattr(mod, f)
                break
        else:
            raise AttributeError, ('No frontend available; tried %s' %
                                   ', '.join(frontend_names))
        self.frontend = ui.Frontend()

    def run(self):
        return self.frontend.run()

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-f', '--frontend', metavar='FRONTEND',
                      help="Use the given frontend (gtk-ui).")
    parser.set_defaults(frontend=None)
    (options, args) = parser.parse_args()

    wizard = Wizard(frontend_name=options.frontend)
    sys.exit(wizard.run())
