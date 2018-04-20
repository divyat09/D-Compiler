#!/usr/bin/python2

InstrTAC = []
def CreateTAC( op, dst, src1, src2 ):
  InstrTAC.append( [ str(op), str(dst), str(src1), str(src2) ] )
  
def OutputTAC():

  LineNum= 1
  Comma= ", "
  
  for Instr in InstrTAC:
    if Instr[0] == 'ifgoto_eq':
      print( str(LineNum) + Comma + 'ifgoto_eq' + Comma + Instr[2] + Comma +  Instr[3] + Comma + Instr[1]) 

    if Instr[0] == 'ifgoto_neq':
      print( str(LineNum) + Comma + 'ifgoto_neq' + Comma + Instr[2] + Comma +  Instr[3] + Comma + Instr[1]) 

      # if Instr[1] == '>':
      #   print( LineNum + Comma + 'ifgoto_gt' + Comma + Instr[2] + Comma +  Instr[3])

      # if Instr[1] == '<':
      #   print( LineNum + Comma + 'ifgoto_lt' + Comma + Instr[2] + Comma +  Instr[3])

      # if Instr[1] == '>=':
      #   print( LineNum + Comma + 'ifgoto_geq' + Comma + Instr[2] + Comma +  Instr[3])

      # if Instr[1] == '<=':
      #   print(  LineNum + Comma + 'ifgoto_leq' + Comma + Instr[2] + Comma +  Instr[3])

      # if Instr[1] == '==':
      #   print(  LineNum + Comma + 'ifgoto_eq' + Comma + Instr[2] + Comma +  Instr[3])

      # if Instr[1] == '!=':
      #   print(  LineNum + Comma + 'ifgoto_neq' + Comma + Instr[2] + Comma +  Instr[3])

    elif Instr[0] == 'jmp':
      print( str(LineNum) + Comma +'jmp' +Comma + Instr[1] )

    elif Instr[0] ==  'call':
      print( str(LineNum) + Comma +'call' +Comma + Instr[1] )

    elif Instr[0] ==  'label':
      print( str(LineNum) + Comma +'label' +Comma + Instr[1] )

    elif Instr[0] == 'ret':
      print( str(LineNum) + Comma +'ret' +Comma + Instr[1])

    elif Instr[0] == 'exit':
      print( str(LineNum) + Comma +'exit' +Comma + Instr[1])

    elif Instr[0] == 'print_str':
      print( str(LineNum) + Comma +'print_str' +Comma + Instr[1])

    elif Instr[0] == 'print_int':
      print( str(LineNum) + Comma +'print_int' +Comma + Instr[1])
    
    elif Instr[0] == '=':
      print( str(LineNum) + Comma + Instr[0] + Comma + Instr[1] + Comma + Instr[2])

    elif Instr[0] == '~':
     print( str(LineNum) + Comma + Instr[0] + Comma + Instr[1] + Comma + Instr[2])

    elif Instr[0] in [ '+', '-', '*', '/', '%', '<<', '>>', '&', '|', '^','<','>','>=', '<=', '==', '!=' ] :
      print( str(LineNum) + Comma + Instr[0] + Comma + Instr[1] + Comma + Instr[2] + Comma + Instr[3])
    # else:
    #   print(str(LineNum) + Comma + Instr[0] + Comma + Instr[1] + Comma + Instr[2] + Comma + Instr[3] + Comma)
    LineNum = LineNum + 1

    # if (data[1] in ["ifgoto_lt","ifgoto_leq","ifgoto_gt","ifgoto_geq","ifgoto_eq","ifgoto_neq"]):

    #   if(isint(data[2])):
    #     self.const=data[2]
    #   else:
    #     self.src1 =  data[2]
      
    #   if(isint(data[3])):
    #     self.const2=data[3]
    #   else:
    #     self.src2 =  data[3]

    #   # jmp address can be a label hence not addded to table
    #   self.const3 = data[4]
    #   bb.append(int(self.lineno)+1)
    #   bb.append(int(self.const3[1:]))
    #   # labels[self.const3]="label"+self.const3

    # elif (data[1] == "jmp"):
    #   self.const = data[2]
    #   bb.append(int(self.lineno)+1)
    #   bb.append(int(self.const[1:]))
  
    # elif (data[1] == "call"):
    #   self.const = data[2]
    #   # what about basic block???
  
    # elif (data[1] == "ret"):  
    #   if(isint(data[2])):
    #     self.const=data[2]
    #   else:
    #     # Table.addvar(data[2])
    #     self.src1 = data[2]
        
    # elif (data[1] == "exit"):  
    #   if(isint(data[2])):
    #     self.const=data[2]
    #   else:
    #     # Table.addvar(data[2])
    #     self.src1 = data[2]
        
    # elif (data[1] == "="):
    #   # Table.addvar(data[2])      
    #   self.dst = data[2]
    #   if(isint(data[3])):
    #     self.const=data[3]
    #   else:
    #     # Table.addvar(data[3])
    #     self.src1 = data[3]
  
    # elif (data[1] == "~"):
    #   # Table.addvar(data[2])
    #   self.dst = data[2]
    #   if(isint(data[3])):
    #     self.const=data[3]
    #   else:
    #     # Table.addvar(data[3])
    #     self.src1 = data[3]
  
    # elif (data[1] == "print_int"):
    #   if(isint(data[2])):
    #     self.const=data[2]
    #   else:
    #     # Table.addvar(data[2])
    #     self.src1 = data[2]
  
    # #here const is the address to the string 
    # elif (data[1] == "print_string"):
    #   self.const = data[2]
  
    # elif (data[1] == "input_int"):
    #   # Table.addvar(data[2])
    #   self.dst = data[2]
  
    # # elif (data[1] == "input_string"):
    # #   self.src1 = data[2]
  
    # elif (data[1] == "label"):
    #   self.const = data[2]

  
    # else:
    #   # Table.addvar(data[2])
    #   self.dst = data[2]
    #   if(isint(data[3])):
    #     self.const=data[3]
    #   else:
    #     # Table.addvar(data[3])
    #     self.src1 = data[3]
    #   if(isint(data[4])):
    #     self.const2=data[4]
    #   else:
    #     # Table.addvar(data[4])
    #     self.src2 = data[4]
