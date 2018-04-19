from globalvars import *

class SymbolTable:
	def __init__(self):
		self.table = {}
		self.temp_no=0	
		self.label_no=0
		self.currentscope = 'main'
		self.scope_no = 0
		#Add variable to table 

	def get_temp(self):
		self.temp_no = self.temp_no+1
		return "tmp"+str(self.temp_no)
	
	def get_label(self):
		self.label_no = self.label_no+1
		return "L"+str(self.label_no)
		
	def addvar(self,varname,datatype,_type,size):
		if '[' in varname:
			varname= varname.split('[')[0]
			self.table[self.currentscope]['identifiers'][varname]= {'name': varname,'type':'Array','datatype':datatype,'scope':self.currentscope}
		else:
			self.table[self.currentscope]['identifiers'][varname]={'name':varname,'type':_type,'datatype':datatype,'scope':self.currentscope,'size':size}

	def addfunc(self,funcname,_type,datatype):
		print "Hi"
		parentscope = self.currentscope
		if funcname=='main':
			self.table[funcname]={'name':funcname,'type':_type,'datatype':datatype,'parentscope':None,'identifiers':{},'parameters':{}}
		else:	
			self.table[funcname]={'name':funcname,'type':_type,'datatype':datatype,'parentscope':parentscope,'identifiers':{},'parameters':{}}
		self.currentscope = funcname
	
	def newscope(self):
		scope = "s"+str(self.scope_no)
		self.table[scope] = {'name':scope,'type':None,'datatype':None,'parentscope':self.currentscope,'identifiers':{}}
		self.currentscope=scope
		self.scope_no+=1
	
	def endscope(self):
		self.currentscope = self.table[self.currentscope]['parentscope'] 
	
	def checkscope(self,varname):
		scope = self.currentscope
		while scope not in ['main']:
		
			if varname in self.table[scope]['identifiers']:
				return scope
		
			scope = self.table[scope]['parentscope']
		
		if varname in self.table['main']['identifiers']:
			return 'main'
		
		return None
	
	def gettype(self,scope,varname):
		return self.table[scope]['identifiers'][varname]['datatype']

	def getfunc_returntype(self,funcname):
		return self.table[funcname]['datatype']
