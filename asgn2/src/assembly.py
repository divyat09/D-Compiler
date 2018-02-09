def datasection():
    print ".data\n"
    for variables in global_vars:
        print variables.name+":\n\t.long"+variables.value

def Print_Int( IRObj ):

	if IRObj.isValid()[0]:		# Int Variable printing case
		_var= IRObj.src1['name']
	else:						# Int constant printing case
		_const= IRObj.const

def Print_Str( IRObj ):

	if IRObj.isValid()[0]:	
		_str= IRObj.src1['name']
	else:
		print "Invalid Case"

def Input_Int( IRObj ):

	if IRObj.isValid()[0]:		# Int Variable Case
		_var= IRObj.src1['name']
	else:						# Int constant Case
		_const= IRObj.const

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
			_dst= IRObj.dst['name']
			_src= IRObj.src1['name']
		else:
			_dst= IRObj.dst['name']
			_src= IRObj.const
	else:
		print "Error: Destination is not a Variable "

def NegAssignment( IRObj ):

	if IRObj.isValid()[2]:

		if IRObj.isValid()[0]:
			_dst= IRObj.dst['name']
			_src= IRObj.src1['name']
		else:
			_dst= IRObj.dst['name']
			_src= IRObj.const
	else:
		print "Error: Destination is not a Variable "


def Operator1( IRObj ):			# Add, Mul, Sub

	if IRObj.isValid()[2]:

		if IRObj.isValid()[0]:
			_src1= IRObj.src1['name']
			reg1= AssignRegister( _src1, IRObj.lineno )
		else
			_src1= IRObj.const
			reg1= _src1

		if IRObj.isValid()[1]:
			_src2= IRObj.src2['name']
			reg2= AssignRegister( _src2, IRObj.lineno )
		else
			_src2= IRObj.const2
			reg2= _src2

		_dst= IRObj.dst["name"]
		reg3= AssignRegister( _dst, IRObj.lineno )

	else:
		print "Error: Destination is not a Variable "

def Operator2( IRObj ):			# Div, Mod

	if IRObj.isValid()[2]:

		if IRObj.isValid()[0]:
			_src1= IRObj.src1['name']
		else
			_src1= IRObj.const

		if IRObj.isValid()[1]:
			_src1= IRObj.src2['name']
		else
			_src1= IRObj.const2

		_dst= IRObj.dst["name"]

	else:
		print "Error: Destination is not a Variable "


def Divide( IRObj ):

def Mod(IRObj):

def AssemblyConverter():

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
			Ret( IRObj )
		elif IRObj.op == "label":
			Label( IRObj )

		elif IRObj.op == "=":
			Assignment( IRObj )
		elif IRObj.op == "!":
			NegAssignment( IRObj )

		elif IRObj.op == "ifgoto":
			Conditional( IRObj )

		elif IRObj.op == "+" || IRObj.op == "-" || IRObj.op == "*" :
			Operator1( IRObj )

		elif IRObj.op == "/" || IRObj.op == "%":  
			Operator2( IRObj )
		
		elif IRObj.op == "&" || IRObj.op == "|":
			BitOperator1( IRObj )

		elif IRObj.op == "~":
			BitNeg( IRObj )
		elif IRObj.op == "<<":
			LeftShift( IRObj )
		elif IRObj.op == ">>":
			RightShift( IRObj )
