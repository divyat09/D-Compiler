#!/usr/bin/env python2
import sys
from globalvars import *
class IRDS:
  def __init__(self):
    self.lineno = 0
    self.op = None
    self.dst = None
    self.src1 = None
    self.src2 = None
        
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
      self.dst = data[2]
      bb.append(int(self.lineno)+1)
      bb.append(int(self.dst))
    elif (data[1] == "call"):
      self.dst = data[2]
      # what about basic block???
    elif (data[1] == "ret"):  
      self.src1 = data[2]
    elif (data[1] == "="):
      self.dst = data[2]
      self.src1 = data[3]
    elif (data[1] == "!"):
      self.dst = data[2]
      self.src1 = data[3]
    elif (data[1] == "print_int"):
      self.src1 = data[2]
    elif (data[1] == "print_string"):
      self.src1 = data[2]
    elif (data[1] == "input_int"):
      self.src1 = data[2]
    elif (data[1] == "input_string"):
      self.src1 = data[2]
    elif (data[1] == "label"):
      self.src1 = data[2]
    else:
      self.dst = data[2]
      self.src1 = data[3]
      self.src2 = data[4]

filename = sys.argv[1]
f=open(filename, 'r')
bb.append(1)

for line in f.readlines():
  Data= line.split(',')
  data = [x.strip(' ') for x in Data]
  _input= []

  for param in data:
    _input.append(param)
  print _input
  
  IRepresentation= IRDS()
  statements.append(IRepresentation)
  IRepresentation.represent( _input )
  print bb
bb.append(len(statements))
print bb
  