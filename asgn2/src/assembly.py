from registers import *
from globalvars import *

def datasection():
    print ".data\n"
    # for variables in global_vars:
    #     print variables.name+":\n\t.long"+variables.value
	# f=open(AssemFile,'a')		
	# f.write(str(_varname) + ': DW 0\n')
	# f.close()
    f=open(AssemFile,'a')
    format_int = "format_int: .asciz \"%d\\n\""
    f.write(format_int+"\n")
    f.close()
    for _var in Table.table.keys():
		_varname= Table.table[_var]['name']

		if Table.table[_var]['type'] == 'Array':
			f=open(AssemFile,'a')
			f.write(str(_varname) + ': .long '+ str(4*ArraySize)+'\n')	# 1 long= 4 Bytes
			f.close()

		else:		
			f=open(AssemFile,'a')
			f.write(str(_varname) + ': .long 0\n')
			f.close()

def Print_Int( IRObj ):
	f=open(AssemFile,'a')	
	if IRObj.isValid()[0]:		# Int Variable printing case
		_var= IRObj.src1['name']
		if _var in RegisterAssigned.keys():
			f.write("pushl\t"+RegisterAssigned[_var]+"\n")
		else:
			f.write("pushl\t"+_var+"\n")			
	else:						# Int constant printing case
		_var= IRObj.const
		if(isint(str(_var))):
			f.write("pushl\t$"+str(_var))
	f.write("pushl\t"+"$format_int\n")
	f.write("call\tprintf\n")

	# _var = "$0x"+str(int(_var,16))
	# length_reg = "movl\t"+"5"+",\t%edx\n" #Move 5 length of int iinto edx
	# output = "movl\t"+"("+_var+")"+",\t%ecx\n"
	# stdout = "movl\t"+"1,\t%ebx\n"
	# sys_write = "movl\t"+"$0x4"+",\t"+"%eax\n"
	# syscall = "int\t"+"$0x80\n"
	# f.write( length_reg+ output + sys_write + stdout + syscall )
	f.close()

def Print_Str( IRObj ):

	# if IRObj.isValid()[0]:	
	# 	_str= IRObj.src1['name']
	# else:
	# 	print "Invalid Case"
	f=open(AssemFile,'a')
	if(IRObj.const):
		print "hi"
		# length_reg = "mov"+"\t"+str(len(IRObj.const))+"%edx\n"
		# output = "mov\t"+IRObj.const+"%ecx\n"
		# stdout = "mov"+"\t"+"1,%ebx\n"
		# sys_write = "mov"+"\t"+"$0x4"+","+"eax\n"
		# syscall = "int"+"\t"+"$0x80\n"
		# f.write(length_reg+ output + sys_write + stdout + syscall )
	else:
		print "Invalid Print_str"
	f.close()

def Input_Int( IRObj ):

	if IRObj.isValid()[0]:		# Int Variable Case
		_var= IRObj.src1['name']
	else:						# Int constant Case
		_var= IRObj.const
	f=open(AssemFile,'a')
	# length_reg = "mov"+"\t"+"5"+"%edx\n"
	# output = "mov\t"+_var+"%ecx\n"
	# stdin = "mov"+"\t"+"0"+","+"%ebx\n"
	# sys_read = "mov"+"\t"+"$0x3"+","+"eax\n"
	# syscall = "int"+"\t"+"$0x80\n"
	f.write( length_reg + output+ sys_read+ stdin+syscall)
	f.close()

def Input_Str( IRObj ):

	if IRObj.isValid()[0]:	
		_str= IRObj.src1['name']
	else:
		print "Invalid Case"

def Jump( IRObj ):

	if IRObj.isValid()[0]:	
		print "Invalid Case : Jump assembly.py"
	else:
		_target= IRObj.const
		jump = "JMP"+"\t"+_target+"\n"
		f = open(AssemFile,'a')
		f.write(jump)
		f.close()

def Label( IRObj ):
	if(IRObj.const in functions):
		f=open(AssemFile,'a')
		f.write("\n.type "+IRObj.const+" , @function\n")
		f.write(IRObj.const+":\n")
		f.write("push\t%ebp\n")
		f.write("mov\t%esp,\t%ebp\n")
		f.close()
		functions.remove(IRObj.const)
	else:
		f=open(AssemFile,'a')
		f.write(IRObj.const+":\n")
		f.close()		

def Call( IRObj ):

	for i in ['%eax','%ecx','%edx']:
		if RegisterStatus[i]==1:
			FreeRegister(i)
			
	f=open(AssemFile,'a')
	f.write("call\t"+IRObj.const+"\n")
	f.close()

def Ret( IRObj, flag_exit ):
	
	if IRObj.isValid()[0]:	
		_target= IRObj.src1['name']
		if _target in RegisterAssigned.keys():
			_target = RegisterAssigned[_target]
	else:
		_target= '$'+IRObj.const
	
	if flag_exit==0:
		f=open(AssemFile,'a')
		f.write("movl\t"+_target+",%ebx"+"\nmovl\t$1,%eax\nint\t$0x80\n")
		f.close()	
		return
	
	f=open(AssemFile,'a')
	f.write("mov\t%ebp,\t%esp\n")
	f.write("pop\t%ebp\n")
	f.write("movl\t"+_target+",%eax"+"\nret\n")
	f.close()

def Assignment( IRObj ):

	if IRObj.isValid()[2]:

		
		if IRObj.isValid()[0] and (IRObj.src1['name'][0] == "*" or IRObj.src1['name'][0] == "&"):
			_src= IRObj.src1['name'][1:]
			_dst= IRObj.dst['name']
			reg2= AssignRegister(_dst, IRObj.lineno ,0)
			if (IRObj.src1 == "*"):
				reg1= AssignRegister(_src, IRObj.lineno ,1)
				f=open(AssemFile,'a')
				f.write( "movl\t[" + str(reg1) +',]\t' + str(reg2)+"\n" )
				f.close()
			else:
				f=open(AssemFile,'a')
				f.write( "lea\tbyte ptr " +_src +"," + str(reg2)+"\n" )
				f.close()
		else:
			if IRObj.isValid()[0]:
				_src= IRObj.src1['name']
				reg1= AssignRegister(_src, IRObj.lineno ,1)
			else:
				_src= IRObj.const
				reg1= '$'+ _src
			if (IRObj.dst['name'][0]=='*'):
				_dst = IRObj.dst['name'][1:]
				reg2 = AssignRegister(_dst, IRObj.lineno, 0)
				f=open(AssemFile,'a')
				f.write( "movl\t" + str(reg1) +',\t[' + str(reg2)+"]\n" )
				f.close()
			else:
				_dst = IRObj.dst['name']
				reg2 = AssignRegister(_dst, IRObj.lineno, 0)
				f=open(AssemFile,'a')
				f.write( "movl\t" + str(reg1) +',\t' + str(reg2)+"\n" )
				f.close()
	else:
		print "Error: Destination is not a Variable "

def BitNeg( IRObj ):

 	if IRObj.isValid()[2]:
		_dst= IRObj.dst['name']
		reg3 = AssignRegister( _dst, IRObj.lineno, 0)
		if IRObj.isValid()[0]:	
			_src= IRObj.src1['name']
			reg1= AssignRegister( _src, IRObj.lineno, 1 )
		else:
			_src= IRObj.const
			reg1 = '$'+ _src
		f.open(AssemFile,'a')
		f.write ("not\t"+reg3+","+reg2)
		f.close
	else:
		print "Error: Destination is not a Variable "

def Conditional ( IRObj):

	if IRObj.isValid()[0]:
		_src1= IRObj.src1['name']
		reg1= AssignRegister( _src1, IRObj.lineno, 1 )
	else:
		_src1= IRObj.const
		reg1= SpecialConstRegister( _src1, IRObj.lineno )
	
	if IRObj.isValid()[1]:
		_src2= IRObj.src2['name']
		reg2= AssignRegister( _src2, IRObj.lineno, 1 )
	else:
		_src2= IRObj.const2
		reg2= "$" + _src2
	f = open(AssemFile,'a')
	f.write( "cmpl\t"+reg2+","+reg1+"\n")
	f.write( str(op2wrd[IRObj.op])+"\t"+ labels[IRObj.const3]+"\n")
	f.close()

def Operator1( IRObj ):			# Add, Mul, Sub, xor, or ,and
	if IRObj.isValid()[2]:
		if IRObj.isValid()[0]:
			_src1= IRObj.src1['name']
			reg1= AssignRegister( _src1, IRObj.lineno, 1 )

		else:
			_src1= IRObj.const
			reg1= '$'+ _src1
		
		if IRObj.isValid()[1]:
			_src2= IRObj.src2['name']
			reg2= AssignRegister( _src2, IRObj.lineno, 1 )

		else:
			_src2= IRObj.const2
			reg2= '$'+ _src2
		
		_dst= IRObj.dst['name']
		reg3 = AssignRegister( _dst, IRObj.lineno, 0)
		
		f=open(AssemFile,'a')
		
		# Need to create a temporary register for the cases of type: a= b op a		
		if(IRObj.src2== IRObj.dst):
			reg0= GetFreeRegister()	
			if reg0 == -1:
				reg0= RegisterSpilling( IRObj.lineno )	
			f.write( "movl\t" + str(reg1) +',\t' + str(reg0)+"\n" )
			f.write( str(op2wrd[IRObj.op]) +"\t"+ str(reg2) +',\t' + str(reg0)+"\n" )
			f.write( "movl\t" + str(reg0) +',\t' + str(reg3)+"\n" )		

		# a= a op b case
		elif(IRObj.src1== IRObj.dst): 
			f.write( str(op2wrd[IRObj.op]) +"\t"+ str(reg2) +',\t' + str(reg3)+"\n" )
		
		# a= b op c	 case
		else:
			f.write( "movl\t" + str(reg1) +',\t' + str(reg3)+"\n" )
			f.write( str(op2wrd[IRObj.op]) +"\t"+ str(reg2) +',\t' + str(reg3)+"\n" )
	
		f.close()

	else:
		print "Error: Destination is not a Variable "


def Operator2( IRObj ):			# Div, Mod

	if IRObj.isValid()[2]:

		# Main Register stores the result we need. 
		# In any case, eax stores quotient and edx stores remainder
		# Hence, according to operator the MainReg changes from eax to edx
		if IRObj.op == '/':
			MainReg= '%eax'
			SecReg= '%edx'	
		
		elif IRObj.op == '%':
			MainReg= '%edx'
			SecReg= '%eax'	

		# We explicitly need to store _dst in the Main Register
		# Hence, a special Resiter Allocation Function for this case
		_dst= IRObj.dst["name"]
		AssignDivisionRegister( MainReg, SecReg, _dst, IRObj.lineno )

		if IRObj.isValid()[0]:
			_src1= IRObj.src1['name']
			reg1= AssignRegister( _src1, IRObj.lineno, 1 )
		else:
			_src1= IRObj.const
			reg1= '$'+_src1
		
		if IRObj.isValid()[1]:
			_src2= IRObj.src2['name']
			reg2= AssignRegister( _src2, IRObj.lineno, 1 )
		else:
			# A special Syntax Case. You cant write "idiv 4". Need to assing 4 to some register first
			_src2= IRObj.const2
			reg2= SpecialConstRegister( _src2, IRObj.lineno )

		f=open(AssemFile,'a')

		f.write( "movl\t" + str(reg1) +',\t' + MainReg+"\n" )
		f.write( "idiv\t" + str(reg2) + "\n" )
		f.close()
		
		# To free the Second Register containg the value of Modulo/Quotient which we dont need 	
		EndDivisionRegister( SecReg )
		
	else:
		print "Error: Destination is not a Variable "

def AssemblyConverter():

	flag_exit=0

	f = open(AssemFile,'a')
	f.write('.data\n')
	f.close()
	datasection()
	f=open(AssemFile,'a')
	f.write('\n.text\n.globl _start\n_start:\n')
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

		elif IRObj.op == "jmp":
			Jump( IRObj )
		elif IRObj.op == "call":
			Call( IRObj )    
		elif IRObj.op == "ret":
			Ret( IRObj, flag_exit )
			flag_exit=1

		elif IRObj.op == "label":
			Label( IRObj )

		elif IRObj.op == "=":
			Assignment( IRObj )

		elif IRObj.op[0] == "i":
		 	Conditional( IRObj )

		elif IRObj.op in ["+", "-", "*", "&", "|", "<<", ">>", "^"]:
			Operator1( IRObj )

		elif IRObj.op in ["/", "%"]:  
			Operator2( IRObj )

		elif IRObj.op == "~":
			BitNeg( IRObj )
		# Save Context Information
		if IRObj.lineno-1 in bb and IRObj.lineno-1 != bb[-1] :
			print IRObj.lineno
			for register in RegisterStatus:
				if RegisterStatus[register]==1:
					FreeRegister(register)
		if str(IRObj.lineno) in labels.keys():
			f=open(AssemFile,'a')
			f.write(labels[str(IRObj.lineno)]+":\n")
			f.close()			
		
