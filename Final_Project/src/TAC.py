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

    elif Instr[0] == 'ifgoto_neq':
      print( str(LineNum) + Comma + 'ifgoto_neq' + Comma + Instr[2] + Comma +  Instr[3] + Comma + Instr[1]) 

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

    elif Instr[0] == 'print_int':
      print( str(LineNum) + Comma +'print_int' +Comma + Instr[1])
    
    elif Instr[0] == 'input_int':
      print( str(LineNum) + Comma +'input_int' +Comma + Instr[1])
    
    elif Instr[0] == '=':
      print( str(LineNum) + Comma + Instr[0] + Comma + Instr[1] + Comma + Instr[2])

    elif Instr[0] == '~':
     print( str(LineNum) + Comma + Instr[0] + Comma + Instr[1] + Comma + Instr[2])

    elif Instr[0] in [ '+', '-', '*', '/', '%', '<<', '>>', '&', '|', '^','<','>','>=', '<=', '==', '!=' ] :
      print( str(LineNum) + Comma + Instr[0] + Comma + Instr[1] + Comma + Instr[2] + Comma + Instr[3])
    
    else:
      print("Cannot convert this line of code to valid IR")
    LineNum = LineNum + 1
