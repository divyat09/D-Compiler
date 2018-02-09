from globalvars import *

# Erase the content of a Register
def FreeRegister( reg ):

	var= RegisterData[ reg ]
	RegisterStatus[ reg ]= -1
	RegisterData[ reg ]= None
	del RegisterAssigned[ var ]	

	# Adding the assembly instruction to save the data
	f= open( AssemFile, 'a' )
	f.write( 'movl\t' + str(reg)+',\t'+ str(var) +"\n")
	f.close()

# Return a free register from the set of all registers
def GetFreeRegister():

  for register in RegisterStatus:
    if RegisterStatus[register] ==-1:
      
      RegisterStatus[register]=1
      return register

  return -1

# If no free registers available, do Register Spilling
def RegisterSpilling( lineno )

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
	FreeRegister( VictimVar )

	return VictimReg
	

# Given a Variable and LineNumber of program, assign a register
def AssignRegister(_var, lineno, LoadCase ):

	if _var in RegisterAssigned.keys():
		return RegisterAssigned[ _var ]

	reg= GetFreeRegister()	
	if reg == -1:
		reg= RegisterSpilling( lineno )	

	# Assigning the newly freed register to _var
	RegisterData[reg]= _var
	RegisterAssigned[ _var ]= reg		
	RegisterStatus[ reg ]= 1
		
	# Adding the assembly instruction to Load data into register
	if LoadCase:
		f= open( AssemFile, 'a' )
		f.write( 'movl\t' + str(_var)+',\t'+ str(reg) +"\n")
		f.close()

	return reg

def SpecialDivisorRegister( const, lineno ):

	reg= GetFreeRegister()
	if reg == -1:
		reg= RegisterSpilling( lineno )

	# Assigning the newly freed register to _var
	RegisterStatus[ reg ]= 1
	return reg

def AssignDivisionRegister( MainReg, SecReg, _var, lineno ):

	if RegisterStatus[MainReg] != -1:
		FreeRegister( MainReg )
	if RegisterStatus[SecReg] != -1:
		FreeRegister( SecReg )

	RegisterStatus[MainReg]= 1
	RegisterData[MainReg]= _var
	RegisterAssigned[MainReg]= '%eax'

	RegisterStatus[SecReg]= 1

def EndDivisionRegister( SecReg, reg, SpecialDivisor ):

	RegisterStatus[SecReg]= -1
	
	if SpecialDivisor:
		RegisterStatus[reg]= -1		


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
