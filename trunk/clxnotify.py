#!/usr/bin/python

#Copyright

import sys
from pynotifyx import XMPPNotify

if len(sys.argv) < 4:
    print "Syntax: clxnotify JID Password DestinationJID Message"
    sys.exit(0)

user = sys.argv[1]
passwd = sys.argv[2]
tojid = sys.argv[3]
msg = sys.argv[4]