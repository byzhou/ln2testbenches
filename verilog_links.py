#!/usr/bin/env python

import os, sys
from os.path import normpath, join

if len(sys.argv) > 1:
    libroot = sys.argv[1]
else:
    libroot = '/mnt/nokrb/bobzhou/summer_2015/trojantestbenches' #change the searching path

if len(sys.argv) > 2:
    viewname1 = sys.argv[2]
    if len(sys.argv) > 3:
        viewname2 = sys.argv[3]
else:
    viewname1 = 'TjIn'
    viewname2 = 'TjFree'

# ln 2 both verilogams and systemverilog

rootpath = normpath(libroot)

print libroot
os.system('cd ' + libroot ) 
os.system('pwd')
for root, dirs, files in os.walk(rootpath):
    if (root.endswith(viewname1) or root.endswith(viewname2)):
        print root
        cellname = os.path.basename(os.path.dirname(os.path.dirname(root)))
        os.system('mkdir ' + cellname ) 
        if (root.endswith(viewname1)):
            os.system('mkdir ' + cellname + '/TjIn' ) 
            os.system('cp ' + root + '/* ' + cellname + '/TjIn/' ) 
        if (root.endswith(viewname2)):
            os.system('mkdir ' + cellname + '/TjFree' ) 
            os.system('cp ' + root + '/* ' + cellname + '/TjFree/' ) 
       
