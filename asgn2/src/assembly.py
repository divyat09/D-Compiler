from registers import *
from globalvars import *

def datasection():
    print ".data\n"
    
    # for variables in global_vars:
    #     print variables.name+":\n\t.long"+variables.value
	# f=open(AssemFile,'a')		
	# f.write(str(_varname) + ': DW 0\n')
	# f.close()
    for _var in Table.table.keys():
		_varname= Table.table[_var]['name']
		f=open(AssemFile,'a')		
		f.write(str(_varname) + ': DW 0\n')
		f.close()

def Print_Int( IRObj ):

	if IRObj.isValid()[0]:		# Int Variable printing case
		_var= IRObj.src1['name']
	else:						# Int constant printing case
		_var= IRObj.const
		# _var = "$0x"+str(int(_var,16))
	for i in ['%ecx','%edx','%ebx','%eax']:
		if RegisterStatus[i]==1:
			FreeRegister(i)
	
	f=open(AssemFile,'a')	
	f.write( "mov\t5,%edx\nmov\t" \
	+_var+"%ecx\nmov"+"\t"+"1,%ebx\nmov"+"\t"+"$0x4,eax\nint\t$0x80")
	f.close()

def Print_Str( IRObj ):

	# if IRObj.isValid()[0]:	
	# 	_str= IRObj.src1['name']
	# else:
	# 	print "Invalid Case"
	f=open(AssemFile,'a')
	
	if(IRObj.const):
		f.write( "mov\t"+len(IRObj.const)+",%edx\nmov\t"+\
		IRObj.const+"%ecx\nmov\t1,%ebx\nmov\t$0x4,eax\nint\t$0x80")
	else:
		print "Invalid Print_str"
	f.close()

def Input_Int( IRObj ):

	if IRObj.isValid()[0]:		# Int Variable Case
		_var= IRObj.src1['name']
	else:						# Int constant Case
		_const= IRObj.const

	f=open(AssemFile,'a')
	
	f.write( "mov\t5,%edx\nmov\t"+_var+"%ecx\nmov\t0x2,%ebx\nmov\t$0x3,eax\nint\t$0x80")
	f.close()

def Input_Str( IRObj ):

	if IRObj.isValid()[0]:	
		_str= IRObj.src1['name']
	else:
		print "Invalid Case"

def Jump( IRObj ):

	if IRObj.isValid()[0]:	
		print "Invalid Case"
	else:
		_target= IRObj.const

def call( IRObj ):

	if IRObj.isValid()[0]:	
		print "Invalid Case"
	else:
		_target= IRObj.const

def ret( IRObj ):

	if IRObj.isValid()[0]:	
		_target= IRObj.src1['name']
	else:
		_target= IRObj.const


def Assignment( IRObj ):

	if IRObj.isValid()[2]:

		if IRObj.isValid()[0]:
			_src= IRObj.src1['name']
			reg1= AssignRegister(_src, IRObj.lineno ,1)

		else:
			_src= IRObj.const
			reg1= _src

		_dst= IRObj.dst['name']
		reg2= AssignRegister(_dst, IRObj.lineno ,0)

		f=open(AssemFile,'a')
		f.write( "movl\t" + str(reg1) +',\t' + str(reg2)+"\n" )
		f.close()

	else:
		print "Error: Destination is not a Variable "

# def NegAssignment( IRObj ):

# 	if IRObj.isValid()[2]:

# 		if IRObj.isValid()[0]:
# 			_dst= IRObj.dst['name']
# 			_src= IRObj.src1['name']
# 		else:
# 			_dst= IRObj.dst['name']
# 			_src= IRObj.const
# 	else:
# 		print "Error: Destination is not a Variable "


def Operator1( IRObj ):			# Add, Mul, Sub, xor, or ,and
	if IRObj.isValid()[2]:
		if IRObj.isValid()[0]:
			_src1= IRObj.src1['name']
			reg1= AssignRegister( _src1, IRObj.lineno, 1 )

		else:
			_src1= IRObj.const
			reg1= _src1
		
		if IRObj.isValid()[1]:
			_src2= IRObj.src2['name']
			reg2= AssignRegister( _src2, IRObj.lineno, 1 )

		else:
			_src2= IRObj.const2
			reg2= _src2
		
		_dst= IRObj.dst['name']
		reg3 = AssignRegister( _dst, IRObj.lineno, 0)
		
		f=open(AssemFile,'a')

		if(IRObj.src2== IRObj.dst):
			reg2 = reg1
		if(IRObj.src1 != IRObj.dst and IRObj.src2 != IRObj.dst):
			f.write( "movl\t" + str(reg1) +',\t' + str(reg3)+"\n" )

		f.write( str(op2wrd[IRObj.op]) +"\t"+ str(reg2) +',\t' + str(reg3)+"\n" )
		f.close()

	else:
		print "Error: Destination is not a Variable "

def Operator2( IRObj ):			# Div, Mod

	if IRObj.isValid()[2]:

		if IRObj.op == '/':
			MainReg= '%eax'
			SecReg= '%edx'	
		
		elif IRObj.op == '%':
			MainReg= '%edx'
			SecReg= '%eax'	

		_dst= IRObj.dst["name"]
		AssignDivisionRegister( MainReg, SecReg, _dst, IRObj.lineno )

		if IRObj.isValid()[0]:
			_src1= IRObj.src1['name']
			reg1= AssignRegister( _src1, IRObj.lineno, 1 )
		else:
			_src1= IRObj.const
			reg1= _src1
		
		if IRObj.isValid()[1]:
			_src2= IRObj.src2['name']
			reg2= AssignRegister( _src2, IRObj.lineno, 1 )
			SpecialDivisor= 0
		else:
			_src2= IRObj.const2
			reg2= SpecialDivisorRegister( _src2, IRObj.lineno )
			SpecialDivisor= 1

		f=open(AssemFile,'a')

		f.write( "movl\t" + str(reg1) +',\t' + MainReg+"\n" )
		f.write( "idiv\t" + str(reg2) + "\n" )
		f.close()
			
		EndDivisionRegister( SecReg, reg2, SpecialDivisor)
		
	else:
		print "Error: Destination is not a Variable "


def AssemblyConverter():
	f = open(AssemFile,'a')
	f.write('.data\n')
	f.close()
	datasection()
	f = open(AssemFile,'a')
	f.write('\n.text\n.global _main\n_main:\n')
	f.close()
	for IRObj in statements:

		if IRObj.op == "print_int":
			Print_Int( IRObj ) 
		elif IRObj.op == "print_string":
			Print_Str( IRObj )
		elif IRObj.op == "input_int":
			Input_Int( IRObj )
		elif IRObj.op == "input_string":
			Input_Str( IRObj )

		# elif IRObj.op == "jmp":
		# 	Jump( IRObj )
		# elif IRObj.op == "call":
		# 	Call( IRObj )
		# elif IRObj.op == "ret":
		# 	Ret( IRObj )
		# elif IRObj.op == "label":
			# Label( IRObj )

		elif IRObj.op == "=":
			Assignment( IRObj )
		# elif IRObj.op == "!":
			# NegAssignment( IRObj )

		# elif IRObj.op == "ifgoto":
		# 	Conditional( IRObj )

		elif IRObj.op in ["+", "-", "*", "&", "|", "<<", ">>", "^"]:
			Operator1( IRObj )

		elif IRObj.op in ["/", "%"]:  
			Operator2( IRObj )

		# elif IRObj.op == "~":
		# 	BitNeg( IRObj )
