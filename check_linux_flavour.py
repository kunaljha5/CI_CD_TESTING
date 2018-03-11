#!/usr/bin/env python
import platform
import sys; 
output = platform.dist()


if 'Ubuntu' in output:
    print "Its Ubuntu"
elif 'redat' in output:
    print "Its not Ubuntu"
    sys.exit(43)
