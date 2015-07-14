#!/usr/bin/env python

import os, sys
from os.path import normpath, join

if len(sys.argv) > 1:
    libroot = sys.argv[1]
else:
    libroot = '/path/to/cadence/project' #change the searching path

if len(sys.argv) > 2:
    viewname1 = sys.argv[2]
    if len(sys.argv) > 3:
        viewname2 = sys.argv[3]
else:
    viewname1 = 'verilogams'
    viewname2 = 'systemVerilog'

# ln 2 both verilogams and systemverilog

base = os.getcwd()
rootpath = normpath(join(base, libroot))

for root, dirs, files in os.walk(rootpath):
    if (root.endswith(viewname1) or root.endswith(viewname2))\
      and ('verilog.vams' in files or 'verilog.sv' in files) \
      and 'verilog.v' not in files:
        print root
        cellname = os.path.basename(os.path.dirname(root))
        if 'verilog.vams' in files: 
            os.system('ln -svf '+ root + '/verilog.vams ' + cellname + '.vams')
        elif 'verilog.sv' in files: 
            os.system('ln -svf '+ root + '/verilog.sv ' + cellname + '.sv')
        os.chdir(base)
       
