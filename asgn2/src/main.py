#!/usr/bin/env python2

import sys
from globalvars import *
from nextuse import *

def MapRegisterName( _input ):

  if _input==1:
    return 
  elif _input ==2:
    return
  elif _input ==3:
    return
  elif _input ==4:
    return
  elif _input ==5:
    return
  elif _input ==6:
    return

class IRDS:

  def __init__(self):
    self.lineno = 0
    self.op = None
    self.dst = None
    self.src1 = None
    self.src2 = None
    self.const = None
    self.const2 = None
  
  def isValid(_input):
    return [bool(self.src1),bool(self.src2),bool(self.dst)]
  
  def represent(self,data):
    # print data
    self.lineno = data[0]
    self.op = data[1]
  
    if (data[1] == "ifgoto"):
      self.src1 =  data[2]
      self.dst = data[3]
      bb.append(int(self.lineno)+1)
      bb.append(int(self.dst))
  
    elif (data[1] == "jmp"):
      self.const = data[2]
      bb.append(int(self.lineno)+1)
      bb.append(int(self.const))
  
    elif (data[1] == "call"):
      self.const = data[2]
      # what about basic block???
  
    elif (data[1] == "ret"):  
      if(isint(data[2])):
        self.const=data[2]
      else:
        self.src1 = data[2]
  
    elif (data[1] == "="):
      self.dst = data[2]
      if(isint(data[3])):
        self.const=data[3]
      else:
        self.src1 = data[3]
  
    elif (data[1] == "!"):
      self.dst = data[2]
      if(isint(data[3])):
        self.const=data[3]
      else:
        self.src1 = data[3]
  
    elif (data[1] == "print_int"):
      if(isint(data[2])):
        self.const=data[2]
      else:
        self.src1 = data[2]
  
    elif (data[1] == "print_string"):
      self.src1 = data[2]
  
    elif (data[1] == "input_int"):
      if(isint(data[2])):
        self.const=data[2]
      else:
        self.src1 = data[2]
  
    elif (data[1] == "input_string"):
      self.src1 = data[2]
  
    elif (data[1] == "label"):
      self.src1 = data[2]
  
    else:
      self.dst = data[2]
      if(isint(data[3])):
        self.const=data[3]
      else:
        self.src1 = data[3]
      if(isint(data[4])):
        self.const=data[4]
      else:
        self.src1 = data[4]

filename = sys.argv[1]
f=open(filename, 'r')
bb.append(1)
statements= []

for line in f.readlines():
  Data= line.split(',')
  data = [x.strip(' ') for x in Data]
  _input= []

  for param in data:
    _input.append(param)
  print _input
  
  IRepresentation= IRDS()
  IRepresentation.represent( _input )
  statements.append(IRepresentation)
  print bb

bb.append(len(statements))
bb.sort()
print bb

BuildNextUseTable( bb )

# Printing the next use table
for _item in NextUseTable:
  print _item
