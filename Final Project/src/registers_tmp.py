from globalvars import *

def SaveArray( reg, var):

	f= open( AssemFile, 'a' )
	
	Base= var.split('[')[0]
	Index= var.split('[')[1].split(']')[0]

	# Temporary Register for Base
	flag0= GetFreeRegister()
	if flag0 == -1:
		for temp in RegisterStatus:
			if  temp != reg:
				reg0= temp
				break			
		f.write( 'movl\t' + str(reg0)+',\t'+ str(RegisterData[reg0]) +"\n")
		f.write( 'movl\t$' + str(Base)+',\t'+ str(reg0) +"\n")
	else:
		reg0= flag0
		RegisterStatus[reg0]= 1
		f.write( 'movl\t$' + str(Base)+',\t'+ str(reg0) +"\n")
	
	RegisterStatus[reg0]= 1

	# Temporary Register for Index
	if isint(Index):
		Index= '$' + str(Index)
	
	flag1= GetFreeRegister()
	if flag1 == -1:
		for temp in RegisterData:
			if temp != reg and temp != reg0:
				reg1= temp
				break
		f.write( 'movl\t' + str(reg1)+',\t'+ str(RegisterData[reg1]) +"\n")			
		f.write( 'movl\t' + str(Index)+',\t'+ str(reg1) +"\n")
	else:
		reg1= flag1
		f.write( 'movl\t' + str(Index)+',\t'+ str(reg1) +"\n")
					
	# Stroing Val in memory
	f.write( "movl\t" + str(reg) +  ',\t(' + str(reg0) + ', ' + str(reg1) + ', ' + str(4) +')' +'\n' )

	RegisterStatus[reg0]= -1
	if flag0 == -1:
		f.write( 'movl\t' + str(RegisterData[reg0]) +',\t'+ str(reg0)  +"\n")

	if flag1 == -1:
		f.write( 'movl\t' +  str(RegisterData[reg1]) +',\t'+ str(reg1) +"\n")			

	f.close()	


# Erase the content of a Register
def FreeRegister( reg ):
	# print reg, RegisterData,RegisterStatus[reg]
	var= RegisterData[ reg ]

	# Adding the assembly instruction to save the data
	if '[' in var:
		SaveArray( reg, var )
	else:
		f= open( AssemFile, 'a' )
		f.write( 'movl\t' + str(reg)+',\t'+ str(var) +"\n")
		f.close()
	
	RegisterStatus[ reg ]= -1
	RegisterData[ reg ]= None
	del RegisterAssigned[ var ]	


# Return a free register from the set of all registers
def GetFreeRegister():

  for register in RegisterStatus:
    if RegisterStatus[register] ==-1:
      
      return register

  return -1

# If no free registers available, do Register Spilling
def RegisterSpilling( lineno ):
	NextUseInfo= NextUseTable[ lineno-1 ]	# Get Next Use Dictionary for the particular line
	AssVarList= RegisterAssigned.keys()			# Get List of variables currently assigned to Registers


	NextUseList=[]							# Make a list of the nextuse of currently assigend varibles
	for variable in AssVarList:
		NextUseList.append( NextUseInfo[variable] )
	
	# Get Max Next Use Variable 
	MaxIndex= NextUseList.index( max(NextUseList) )
	VictimVar= AssVarList[ MaxIndex ]
	VictimReg= RegisterAssigned[VictimVar]

	# Setting the Register holding Longest Use Varible Free
	FreeRegister( VictimReg )

	return VictimReg
	

# Given a Variable and LineNumber of program, assign a register
def AssignRegister(_var, lineno, LoadCase ):

	if _var in RegisterAssigned.keys():
		return RegisterAssigned[ _var ]

	elif '[' in _var:	# The case of Array, you first need to assing registers to Base and Index here

		BaseName= _var.split('[')[0]
		Index= _var.split('[')[1].split(']')[0]
		
		# Assigning the Register to Base Array: A
		reg1= AssignRegister( BaseName, lineno  , 0 )
		f= open( AssemFile, 'a' )
		f.write( 'movl\t$' + str(BaseName)+',\t'+ str(reg1) +"\n")
		f.close()

		# Assigning the Index to a Register: var in A[var]
		if isint(Index):	# Case of A[4]
			reg2= SpecialConstRegister( Index, lineno )
		else:				# Case of A[i]
			reg2= AssignRegister( Index, lineno , 1 )	

		# Assigning the result of A[var] to a register
		reg= GetFreeRegister()	
		if reg == -1:
			reg= RegisterSpilling( lineno )	

		# Assigning the newly freed register to _var
		RegisterData[reg]= _var
		RegisterAssigned[ _var ]= reg		
		RegisterStatus[ reg ]= 1

		f=open( AssemFile, 'a' )
		f.write( "movl\t" + '(' + str(reg1) + ', ' + str(reg2) + ', ' + str(4) +'),' + '\t' + str(reg)+'\n' )
		f.close()

		return reg

	else:

		reg= GetFreeRegister()	
		if reg == -1:
			reg= RegisterSpilling( lineno )	

		# Assigning the newly freed register to _var
		RegisterData[reg]= _var
		RegisterAssigned[ _var ]= reg		
		RegisterStatus[ reg ]= 1
			
		# Adding the assembly instruction to Load data into register
		# This Instruction is to be added only if the variable apperas on the RHS of a experession: this case LoadCase=1
		# For variable on the LHS, LoadCase=0
		if LoadCase:
			f= open( AssemFile, 'a' )
			f.write( 'movl\t' + str(_var)+',\t'+ str(reg) +"\n")
			f.close()

		return reg

def SpecialConstRegister( const, lineno ):

	reg= GetFreeRegister()
	if reg == -1:
		reg= RegisterSpilling( lineno )

	# Assigning the newly freed register to _var
	# Important here we dont change the status, do any variable-register coupling as here 
	# we just Out of Sytax need to assign a register to a constant value

	f= open( AssemFile, 'a' )
	f.write( 'movl\t$' + str(const)+',\t'+ str(reg) +"\n")
	f.close()

	return reg

def AssignDivisionRegister( MainReg, SecReg, _var, lineno ):

	if RegisterStatus[MainReg] != -1:
		FreeRegister( MainReg )
	if RegisterStatus[SecReg] != -1:
		FreeRegister( SecReg )
	
	# Preserving the eax and edx registers as they contain result of division
	RegisterStatus[MainReg]= 1
	RegisterStatus[SecReg]= 1

def EndDivisionRegister( MainReg, SecReg, _var, lineno  ):

	RegisterStatus[SecReg]= -1

	reg= AssignRegister( _var, lineno, 1)
	f= open( AssemFile, 'a' )
	f.write( 'movl\t' + str(MainReg)+',\t'+ str(reg) +"\n")
	f.close()

	RegisterStatus[MainReg]= -1


