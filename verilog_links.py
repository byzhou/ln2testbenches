#!/usr/bin/env python

#
# Usage:
#
# verilog_links.py [directory] [viewname] 
# 
# directory (optional):
#    the relative directory (such as the library root) you want for the root
#    defaults to current directory
#
# viewname (optional):
#    the naname of the cellview used in Cadence that is to be linked
#    defaults to 'verilogams'
#



import os, sys
from os.path import normpath, join

if len(sys.argv) > 1:
    libroot = sys.argv[1]
else:
    libroot = '/home/bzhou3/view_projects/adp107x/active/adp107x_ar1_rnm' #change the searching path

#cellname =  os.path.basename( os.path.dirname (os.path.dirname ( libroot ) ) ) 
#os.system ( 'echo ' + '"' + cellname + '"') 

if len(sys.argv) > 2:
    viewname1 = sys.argv[2]
    if len(sys.argv) > 3:
        viewname2 = sys.argv[3]
else:
    viewname1 = 'verilogams'
    viewname2 = 'systemVerilog'

base = os.getcwd()
rootpath = normpath(join(base, libroot))

for root, dirs, files in os.walk(rootpath):
    if (root.endswith(viewname1) or root.endswith(viewname2))\
      and ('verilog.vams' in files or 'verilog.sv' in files) \
      and 'verilog.v' not in files:
        print root
        cellname = os.path.basename(os.path.dirname(root))
        #os.chdir(root)
        if 'verilog.vams' in files: 
            os.system('ln -svf '+ root + '/verilog.vams ' + cellname + '.vams')
        elif 'verilog.sv' in files: 
            os.system('ln -svf '+ root + '/verilog.sv ' + cellname + '.sv')
        os.chdir(base)
       
