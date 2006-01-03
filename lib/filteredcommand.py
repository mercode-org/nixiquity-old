#! /usr/bin/python
# -*- coding: UTF-8 -*-

import os
import debconf
try:
    from debconf import DebconfCommunicator
except ImportError:
    from espresso.debconfcommunicator import DebconfCommunicator
from espresso.debconffilter import DebconfFilter

class FilteredCommand(object):
    def __init__(self):
        self.package = 'espresso'

    def debug(self, fmt, *args):
        if 'ESPRESSO_DEBUG' in os.environ:
            message = fmt % args
            print >>sys.stderr, '%s: %s' % (self.package, message)

    def run_command(self, command, question_patterns=[]):
        self.db = DebconfCommunicator(self.package)
        widgets = {}
        for pattern in question_patterns:
            widgets[pattern] = self
        dbfilter = DebconfFilter(self.db, widgets)

        # TODO: Set as unseen all questions that we're going to ask.

        ret = dbfilter.run(command)

        if ret != 0:
            # TODO: error message if (ret / 256) != 10
            self.debug("%s exited with code %d", command, ret)

        self.db.shutdown()

        return ret

    def preseed(self, name, value, seen=True):
        try:
            self.db.set(name, value)
        except debconf.DebconfError:
            self.db.register('espresso/dummy', name)
            self.db.set(name, value)
            self.db.subst(name, 'ID', name)

        if seen:
            self.db.fset(name, 'seen', 'true')

    # User selected OK, Forward, or similar. Subclasses should override this
    # to send user-entered information back to debconf (perhaps using
    # preseed()) and return control to the filtered command. After this
    # point, self.done is set so no further user interaction should take
    # place.
    def ok_handler(self):
        self.succeeded = True
        self.done = True

    # User selected Cancel, Back, or similar. Subclasses should override
    # this to send user-entered information back to debconf (perhaps using
    # preseed()) and return control to the filtered command. After this
    # point, self.done is set so no further user interaction should take
    # place.
    def cancel_handler(self):
        self.succeeded = False
        self.done = True

if __name__ == '__main__':
    import sys
    fc = FilteredCommand()
    fc.run(sys.argv[1])
