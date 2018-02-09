from globalvars import *

# Return a free register from the set of all registers
def GetFreeRegister():

  for register in RegisterStatus:
    if RegisterStatus[register] ==-1:
      
      RegisterStatus[register]=1
      return register

  return -1

# Given a Variable and LineNumber of program, assign a register
def AssignRegister(_var, lineno):

	if _var in RegisterAssigned.keys():
		return RegisterAssigned[ _var ]

	reg= GetFreeRegister()
	
	if reg == -1:
		# Register Spilling
		NextUseInfo= NextUseTable[ lineno-1 ]	# Get Next Use Dictionary for the particular line
		AssVarList= RegisterAssigned.keys()			# Get List of variables currently assigned to Registers

		NextUseList=[]							# Make a list of the nextuse of currently assigend varibles
		for variable in AssVarList:
			NextUseList.append( NextUseInfo[variable] )

		# Get Max Next Use Variable 
		MaxIndex= NextUseList.index( max(NextUseList) )
		print NextUseList
		VictimVar= AssVarList[ MaxIndex ]
		print RegisterAssigned,VictimVar
		VictimReg= RegisterAssigned[VictimVar]

		# Setting the Register holding Longest Use Varible Free
		RegisterStatus[ VictimReg ]= -1
		RegisterData[ VictimReg ]= None
		del RegisterAssigned[ VictimVar ]
		
		# Assigning the newly freed register to _var
		reg= VictimReg
		RegisterData[reg]= _var
		RegisterAssigned[ _var ]= reg		
		RegisterStatus[ reg ]= 1
		
		return reg

	else:
		RegisterData[reg]= _var
		RegisterAssigned[ _var ]= reg
		RegisterStatus[ reg ]= 1

		return reg

# Dont whether to use or not
# def MapRegisterName( _input ):

#   if _input==1:
#     return "ebx"
#   elif _input ==2:
#     return "esx"
#   elif _input ==3:
#     return "esi"
#   elif _input ==4:
#     return "edi"
#   elif _input ==5:
#     return "eax"
#   elif _input ==6:
#     return "edx"
