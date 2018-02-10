from globalvars import *

def isint(value):
  if (value[0]=='-'):
    value = value[1:]
    return value.isdigit()
  else:
    return value.isdigit()

class IRDS:

  def __init__(self):
    self.lineno = 0
    self.op = None
    self.dst = None
    self.src1 = None
    self.src2 = None
    self.const = None
    self.const2 = None
  
  def isValid(self):
    return [bool(self.src1),bool(self.src2),bool(self.dst)]
  
  def represent(self,data):
    # print data
    self.lineno = int(data[0])
    self.op = data[1]
  
  # build label to lineno dictionary
    if (data[1] == "ifgoto"):
      # Table.addvar(data[2])
      # pointer to variable data[2] in symbol table
      self.src1 =  Table.table[data[2]]
      # jmp address can be a label hence not addded to table
      self.const = data[3]
      bb.append(int(self.lineno)+1)
      bb.append(int(self.const))
  
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
        # Table.addvar(data[2])
        self.src1 = Table.table[data[2]]
  
    elif (data[1] == "="):
      # Table.addvar(data[2])      
      self.dst = Table.table[data[2]]
      if(isint(data[3])):
        self.const=data[3]
      else:
        # Table.addvar(data[3])
        self.src1 = Table.table[data[3]]
  
    elif (data[1] == "!"):
      # Table.addvar(data[2])
      self.dst = Table.table[data[2]]
      if(isint(data[3])):
        self.const=data[3]
      else:
        # Table.addvar(data[3])
        self.src1 = Table.table[data[3]]
  
    elif (data[1] == "print_int"):
      if(isint(data[2])):
        self.const=data[2]
      else:
        # Table.addvar(data[2])
        self.src1 =Table.table[data[2]]
  
    #here const is the address to the string 
    elif (data[1] == "print_string"):
      self.const = data[2]
  
    elif (data[1] == "input_int"):
      # Table.addvar(data[2])
      self.dst =Table.table[data[2]]
  
    # elif (data[1] == "input_string"):
    #   self.src1 = data[2]
  
    elif (data[1] == "label"):
      self.const = data[2]
  
    else:
      # Table.addvar(data[2])
      self.dst =Table.table[data[2]]
      if(isint(data[3])):
        self.const=data[3]
      else:
        # Table.addvar(data[3])
        self.src1 =Table.table[data[3]]
      if(isint(data[4])):
        self.const2=data[4]
      else:
        # Table.addvar(data[4])
        self.src2 = Table.table[data[4]]