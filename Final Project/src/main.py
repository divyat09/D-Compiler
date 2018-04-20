#!/usr/bin/env python2

import sys
from globalvars import *
from symbol_table import *
from irds import *
from nextuse import *
from registers import *
from assembly import *

filename = sys.argv[1]
f=open(filename, 'r')
bb.append(1)

for line in f.readlines():
  Data= line.split(',')
  _input= []

  for param in Data:
    param=param.strip()
    param=param.strip('\n')
    _input.append(param)

  for variables in _input[2:]:
    if(_input[1] in ["ifgoto_lt","ifgoto_leq","ifgoto_gt","ifgoto_geq","ifgoto_eq","ifgoto_neq",'print_string','ret','label','jmp'] ):
      continue
    if(isint(variables)):
      continue
    else:
      if _input[1]=='call':
        functions.append(_input[2])
      else:
        Table.addvar(variables)
  
  IRepresentation= IRDS()
  IRepresentation.represent( _input )
  statements.append(IRepresentation)

bb.append(len(statements))
bb.sort()
print bb

# Build the next use table
BuildNextUseTable( bb )

# Conver to Assembly
AssemblyConverter()

# Print AssemFile
f= open(AssemFile,'r')
content = f.read()
print content
f.close()

print "Hello, Is there anybody in there ?"