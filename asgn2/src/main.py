#!/usr/bin/env python2

import sys
from globalvars import *
from symbol_table import *
from irds import *
from nextuse import *
from registers import *
from assembly import *

def isint(value):
  if (value[0]=='-'):
    value = value[1:]
    return value.isdigit()
  else:
    return value.isdigit()

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
  print _input
  for variables in _input[2:]:
    # print type(variables)
    if(_input[1] in ['ifgoto','print_string','ret'] ):
      continue
    if(isint(variables)):
      continue
    else:
      Table.addvar(variables)
  IRepresentation= IRDS()
  IRepresentation.represent( _input )
  statements.append(IRepresentation)
  # print bb

bb.append(len(statements))
bb.sort()
print bb
# print statements
BuildNextUseTable( bb )

# Conver to Assembly
AssemblyConverter()