#!/usr/bin/env python2
class IRDS:
  def __init__(self):
    self.lineno = 0
    self.op = None
    self.dst = None
    self.src1 = None
    self.src2 = None
        
  def represent(self,data):
  	self.lineno = data[0]
    self.op = data[1]
    if (data[1] == "ifgoto"):
      self.src1 =  data[2]
      self.dst = data[3]
      bb.append(int(self.lineno+1))
      bb.append(int(self.dst))
    elif (data[1] = "jmp"):
      self.dst = data[2]
      bb.append(int(self.lineno+1))
      bb.append(int(self.dst))
    elif (data[1] == "call"):
      self.dst = data[2]
      # what about basic block???
    elif (data[1] == "return"):  
      self.src1 = data[2]
    elif (data[1] == "="):
      self.dst = data[2]
      self.src1 = data[3]
    elif (data[1] = "!"):
      self.dst = data[2]
      self.src1 = data[3]
    elif (data[1] == "print"):
      self.src1 = data[2]
    elif (data[1] == "input"):
      self.src1 = data[2]
    else:
      self.dst = data[2]
      self.src1 = data[3]
      self.src2 = data[4]

f=open(filename, 'r')
for line in f.readlines():
	Data= line.split(',')
	_input= []

	for param in Data:
		_input.append(param)

	IRepresentation= IRDS()
	IRDS.represent( _input )
