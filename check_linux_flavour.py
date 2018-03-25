#!/usr/bin/env python
import platform
import sys; 
output = platform.dist()

if 'Ubuntu' in output:
    print "Its Ubuntu"
else:
    print "Its not Ubuntu"
    sys.exit(43)
    
    
    
