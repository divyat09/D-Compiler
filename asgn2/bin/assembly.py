from registers import *
from globalvars import *

def datasection():
    # print ".data\n"
    # for variables in global_vars:
    #     print variables.name+":\n\t.long"+variables.value
	# f=open(AssemFile,'a')		
	# f.write(str(_varname) + ': DW 0\n')
	# f.close()

    f=open(AssemFile,'a')
    format_out = "format_out: .asciz \"%d\\n\""
    format_in = "format_in: .asciz \"%d\""
    f.write(format_out+"\n")
    f.write(format_in+"\n")
    f.close()

    # ArrayStore= {}

    for _var in Table.table.keys():
		_varname= Table.table[_var]['name']

		if Table.table[_var]['type'] == 'Array':
			f=open(AssemFile,'a')
			f.write(str(_varname) + ': .zero '+ str(4*ArraySize)+'\n')	# 1 long= 4 Bytes
			f.close()
		elif Table.table[_var]['type'] == 'Variable':
			f=open(AssemFile,'a')
			f.write(str(_varname) + ': .long 0\n')
			f.close()

		# # Printing Arrays
		# for key in ArrayStore:
		# 	f=open(AssemFile,'a')
		# 	f.write(str(key) + ': .zeros '+ str(4*ArraySize)+'\n')	# 1 long= 4 Bytes
		# 	f.close()			


def Print_Int( IRObj ):
	
	for i in ['%eax','%edx','%ecx']:
		if RegisterStatus[i]!=-1:
			FreeRegister(i)
		RegisterStatus[i] = 1

	f=open(AssemFile,'a')	
	if IRObj.isValid()[0]:		# Int Variable printing case
		_var= IRObj.src1
		# if Table.table[_var]['type']=='Array':
		# if _var in RegisterAssigned.keys():
		# print _var, RegisterAssigned[_var]
		# f.write("movl\t"+RegisterAssigned[_var]+",\t"+_var+"\n")
		# FreeRegister(RegisterAssigned[_var])
		# f.write("pushl\t"+RegisterASssigned[_var]+"\n")			
		# else:
		# if _var in RegisterAssigned.keys():
		AssignRegister(_var,IRObj.lineno,1)
		# f.write("pushl\t"+_var+"\n")		
		f.write("pushl\t"+RegisterAssigned[_var]+"\n")							

	else:						# Int constant printing case
		_var= IRObj.const
		if(isint(str(_var))):
			f.write("pushl\t$"+str(_var)+"\n")
	f.write("pushl\t"+"$format_out\n")
	f.write("call\tprintf\n")
	f.write("addl\t$8,%esp\n")
	
	for i in ['%eax','%ecx','%edx']:
		RegisterStatus[i]= -1
	# print "end ======== ",RegisterStatus["%edx"]
	
	# _var = "$0x"+str(int(_var,16))
	# length_reg = "movl\t"+"5"+",\t%edx\n" #Move 5 length of int iinto edx
	# output = "movl\t"+"("+_var+")"+",\t%ecx\n"
	# stdout = "movl\t"+"1,\t%ebx\n"
	# sys_write = "movl\t"+"$0x4"+",\t"+"%eax\n"
	# syscall = "int\t"+"$0x80\n"
	# f.write( length_reg+ output + sys_write + stdout + syscall )
	f.close()

# def Print_Str( IRObj ):

# 	# if IRObj.isValid()[0]:	
# 	# 	_str= IRObj.src1
# 	# else:
# 	# 	print "Invalid Case"
# 	f=open(AssemFile,'a')
# 	if(IRObj.const):
# 		print "hi"
# 		# length_reg = "mov"+"\t"+str(len(IRObj.const))+"%edx\n"
# 		# output = "mov\t"+IRObj.const+"%ecx\n"
# 		# stdout = "mov"+"\t"+"1,%ebx\n"
# 		# sys_write = "mov"+"\t"+"$0x4"+","+"eax\n"
# 		# syscall = "int"+"\t"+"$0x80\n"
# 		# f.write(length_reg+ output + sys_write + stdout + syscall )
# 	else:
# 		print "Invalid Print_str"
# 	f.close()

def Input_Int( IRObj ):

	# if IRObj.isValid()[0]:		# Int Variable Case
	# 	_var= IRObj.src1
	# else:						# Int constant Case
	# 	_var= IRObj.const
	f=open(AssemFile,'a')
	# # length_reg = "mov"+"\t"+"5"+"%edx\n"
	# # output = "mov\t"+_var+"%ecx\n"
	# # stdin = "mov"+"\t"+"0"+","+"%ebx\n"
	# # sys_read = "mov"+"\t"+"$0x3"+","+"eax\n"
	# # syscall = "int"+"\t"+"$0x80\n"
	# f.write( length_reg + output+ sys_read+ stdin+syscall)
	# f.close()
	if IRObj.isValid()[2]:		# Int Variable printing case
		_var= IRObj.dst
		# if Table.table[_var]['type']=='Array':
		# if _var in RegisterAssigned.keys():
		# 	f.write("movl\t"+RegisterAssigned[_var]+",\t"+_var+"\n")
		if RegisterStatus["%eax"]==1:
			FreeRegister("%eax")
		RegisterStatus["%eax"]=1
		if _var in RegisterAssigned.keys():
			FreeRegister[RegisterAssigned[_var]]
		f.write("xorl\t%eax,%eax\n")

		if '[' not in _var:		# Variable Case
			f.write("pushl\t$"+_var+"\n")
			f.write("pushl\t"+"$format_in\n")
			f.write("call\tscanf\n")
			f.write("addl\t$8,%esp\n")
		else:
			BaseName= _var.split('[')[0]
			index= _var.split('[')[1].split(']')[0]

			reg1= AssignRegister(BaseName,IRObj.lineno,0)
			f.write( 'movl\t$' + str(BaseName)+',\t'+ str(reg1) +"\n")
			
			if isint( index ):
				reg3= SpecialConstRegister( index, IRObj.lineno )
			else:
			 	reg3= AssignRegister( index, IRObj.lineno ,1 )
			
			reg2= SpecialConstRegister( 4, IRObj.lineno )
			f.write( "imul\t" + str(reg3) +',\t' + str(reg2)+"\n" )
			f.write( "addl\t" + str(reg2) +',\t' + str(reg1)+"\n" )
			f.write("pushl\t"+reg1+"\n")
			f.write("pushl\t"+"$format_in\n")
			f.write("call\tscanf\n")
			f.write("addl\t$8,%esp\n")			

	else:						# Int constant printing case
		print "Input_Int error: value must be a memory location pc"
	RegisterStatus["%eax"]=-1
	

def Input_Str( IRObj ):

	if IRObj.isValid()[0]:	
		_str= IRObj.src1
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

def Exit(IRObj):
	
	if IRObj.isValid()[0]:	
		_target= IRObj.src1
		if _target in RegisterAssigned.keys():
			_target = RegisterAssigned[_target]
	else:
		_target= '$'+IRObj.const
	
	f=open(AssemFile,'a')
	f.write("movl\t"+_target+",%ebx"+"\nmovl\t$1,%eax\nint\t$0x80\n")
	f.close()	
	return


def Ret( IRObj ):
	
	if IRObj.isValid()[0]:	
		_target= IRObj.src1
		if _target in RegisterAssigned.keys():
			_target = RegisterAssigned[_target]
	else:
		_target= '$'+IRObj.const
	
	
	f=open(AssemFile,'a')
	f.write("mov\t%ebp,\t%esp\n")
	f.write("pop\t%ebp\n")
	f.write("movl\t"+_target+",%eax"+"\nret\n")
	f.close()

def Assignment( IRObj ):

	if IRObj.isValid()[2]:

		
	# 	if IRObj.isValid()[0] and (IRObj.src1[0] == "*" or IRObj.src1[0] == "&"):
	# 		_src= IRObj.src1[1:]
	# 		_dst= IRObj.dst
	# 		reg2= AssignRegister(_dst, IRObj.lineno ,0)
	# 		if (IRObj.src1 == "*"):
	# 			reg1= AssignRegister(_src, IRObj.lineno ,1)
	# 			f=open(AssemFile,'a')
	# 			f.write( "movl\t[" + str(reg1) +',]\t' + str(reg2)+"\n" )
	# 			f.close()
	# 		else:
	# 			f=open(AssemFile,'a')
	# 			f.write( "lea\tbyte ptr " +_src +"," + str(reg2)+"\n" )
	# 			f.close()
	# 	else:
		if IRObj.isValid()[0]:
			_src= IRObj.src1
			reg1= AssignRegister(_src, IRObj.lineno ,1)
		else:
			_src= IRObj.const
			reg1= '$'+ _src
	# if (IRObj.dst[0]=='*'):
	# 	_dst = IRObj.dst[1:]
	# 	reg2 = AssignRegister(_dst, IRObj.lineno, 0)
	# 	f=open(AssemFile,'a')
	# 	f.write( "movl\t" + str(reg1) +',\t[' + str(reg2)+"]\n" )
	# 	f.close()
			# else:
		_dst = IRObj.dst
		reg2 = AssignRegister(_dst, IRObj.lineno, 0)
		f=open(AssemFile,'a')
		f.write( "movl\t" + str(reg1) +',\t' + str(reg2)+"\n" )
		f.close()

		if '[' in _dst:
			SaveArray( reg2, _dst )

	else:
		print "Error: Destination is not a Variable "

def BitNeg( IRObj ):

 	if IRObj.isValid()[2]:
		_dst= IRObj.dst
		reg3 = AssignRegister( _dst, IRObj.lineno, 0)
		if IRObj.isValid()[0]:	
			_src= IRObj.src1
			reg1= AssignRegister( _src, IRObj.lineno, 1 )
		else:
			_src= IRObj.const
			reg1 = SpecialConstRegister( _src, IRObj.lineno )
		f=open(AssemFile,'a')
		f.write ("movl\t"+reg1+","+reg3+"\n")
		f.write ("notl\t"+reg3+"\n")
		f.close
	else:
		print "Error: Destination is not a Variable "

def Conditional ( IRObj):
	
	flag_= 0
	if IRObj.isValid()[0]:
		_src1= IRObj.src1
		reg1= AssignRegister( _src1, IRObj.lineno, 1 )
	else:
		_src1= IRObj.const
		flag_= 1
		reg1= SpecialConstRegister( _src1, IRObj.lineno )
		RegisterStatus[reg1]= 1

	if IRObj.isValid()[1]:
		_src2= IRObj.src2
		reg2= AssignRegister( _src2, IRObj.lineno, 1 )
	else:
		_src2= IRObj.const2
		reg2= "$" + _src2
	f = open(AssemFile,'a')
	f.write( "cmpl\t"+reg2+","+reg1+"\n")
	f.write( str(op2wrd[IRObj.op])+"\t"+ IRObj.const3+"\n")
	f.close()

	if flag_:
		RegisterStatus[ reg1 ]= -1

def Operator1( IRObj ):			# Add, Mul, Sub, xor, or ,and
	if IRObj.isValid()[2]:
		if IRObj.isValid()[0]:
			_src1= IRObj.src1
			reg1= AssignRegister( _src1, IRObj.lineno, 1 )

		else:
			_src1= IRObj.const
			reg1= '$'+ _src1
		
		if IRObj.isValid()[1]:
			_src2= IRObj.src2
			reg2= AssignRegister( _src2, IRObj.lineno, 1 )

		else:
			_src2= IRObj.const2
			reg2= '$'+ _src2
		
		_dst= IRObj.dst
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

		if '[' in _dst:
			SaveArray( reg3, _dst )

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
		_dst= IRObj.dst
		AssignDivisionRegister( MainReg, SecReg, _dst, IRObj.lineno )

		if IRObj.isValid()[0]:
			_src1= IRObj.src1
			reg1= AssignRegister( _src1, IRObj.lineno, 1 )
		else:
			_src1= IRObj.const
			reg1= '$'+_src1
		
		if IRObj.isValid()[1]:
			_src2= IRObj.src2
			reg2= AssignRegister( _src2, IRObj.lineno, 1 )
		else:
			# A special Syntax Case. You cant write "idiv 4". Need to assing 4 to some register first
			_src2= IRObj.const2
			reg2= SpecialConstRegister( _src2, IRObj.lineno )

		f=open(AssemFile,'a')

		f.write( "movl\t" + str(reg1) +',\t' + "%eax"+"\n" )
		f.write("cdq\n")
		f.write( "idiv\t" + str(reg2) + "\n" )
		f.close()
		
		# To free the Second Register containg the value of Modulo/Quotient which we dont need 	
		EndDivisionRegister( MainReg, SecReg, _dst, IRObj.lineno  )
		
	else:
		print "Error: Destination is not a Variable "

def Operator3( IRObj ):			# left and right shift
	flag = 0
	if IRObj.isValid()[2]:
		_dst= IRObj.dst
		reg3 = AssignRegister( _dst, IRObj.lineno, 0)
		
		f=open(AssemFile,'a')
		if IRObj.isValid()[1]:
			_src2= IRObj.src2
			reg2= AssignRegister( _src2, IRObj.lineno, 1 )
			if str(reg2) == "%ecx":
				flag = 1
			elif RegisterStatus["%ecx"] == 1 and str(reg2) != "%ecx" :
				FreeRegister("%ecx")
				f.write("movl\t"+str(reg2)+",%ecx\n")
			elif RegisterStatus["%ecx"] == -1:
				f.write("movl\t"+str(reg2)+",%ecx\n")
			reg2 = "%cl"
		else:
			_src2= IRObj.const2
			reg2= '$'+ _src2
		RegisterStatus["%ecx"] = 1
		if IRObj.isValid()[0]:
			_src1= IRObj.src1
			reg1= AssignRegister( _src1, IRObj.lineno, 1 )
		else:
			_src1= IRObj.const
			reg1= '$'+ _src1
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
		if (flag == 0):
			RegisterStatus["%ecx"] = -1
		
	else:
		print "Error: Destination is not a Variable "
	


def SaveContext( lineno ):
	# Save Context Information
	if lineno in bb:
		for register in RegisterStatus : 		
			if RegisterStatus[register]==1:
				varname= RegisterData[register]
				FreeRegister(register)

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
		# elif IRObj.op == "print_string":
		# 	Print_Str( IRObj )
		elif IRObj.op == "input_int":
			Input_Int( IRObj )
		elif IRObj.op == "input_string":
			Input_Str( IRObj )

		elif IRObj.op == "jmp":
			SaveContext( IRObj.lineno + 1 )
			Jump( IRObj )

		elif IRObj.op == "call":
			Call( IRObj )    
		elif IRObj.op == "ret":
			Ret( IRObj)
		elif IRObj.op == "exit":
			Exit( IRObj )
		elif IRObj.op == "label":
			if IRObj.lineno in bb:
				SaveContext( IRObj.lineno )
			Label( IRObj )
		elif IRObj.op == "=":
			Assignment( IRObj )

		elif IRObj.op[0] == "i":
			SaveContext( IRObj.lineno + 1 )
		 	Conditional( IRObj )

		elif IRObj.op in ["+", "-", "*", "&", "|",  "^"]:
			Operator1( IRObj )

		elif IRObj.op in [">>","<<"]:
			Operator3(IRObj)

		elif IRObj.op in ["/", "%"]:  
			Operator2( IRObj )

		elif IRObj.op == "~":
			BitNeg( IRObj )

		# if str(IRObj.lineno-1) in labels.keys():
		# 	f=open(AssemFile,'a')
		# 	f.write(labels[str(IRObj.lineno)]+":\n")
		# 	f.close()			

		
	# Program End Context Save Case
	# SaveContext( IRObj.lineno )