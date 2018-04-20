# from globalvars import *

class SymbolTable:
	def __init__(self):
		self.table = {}
		self.temp_no=0	
		self.label_no=0
		self.currentscope = None
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

	def addfunc(self,funcname,_type,datatype,parentscope):
		# print "Hi"
		if not parentscope:
			parentscope = self.currentscope
			# if funcname=='main':
			# 	self.table[funcname]={'name':funcname,'type':_type,'datatype':datatype,'parentscope':None,'identifiers':{},'parameters':[]}
			# else:	
			# 	self.table[funcname]={'name':funcname,'type':_type,'datatype':datatype,'parentscope':None,'identifiers':{},'parameters':[]}
			self.table[funcname]={'name':funcname,'type':_type,'datatype':datatype,'parentscope':None,'identifiers':{},'parameters':[]}
		else:
			self.table[funcname]={'name':funcname,'type':_type,'datatype':datatype,'parentscope':self.table[parentscope]['child'],'identifiers':{},'parameters':[]}

		self.currentscope = funcname
	
	def addclass(self,classname,_type):
		self.table[classname]={'name':classname,'type':_type,'datatype':None,'parentscope':None,'identifiers':{},'member_functions':{},'child':'s'+str(self.scope_no),'constructor':{}}
		self.currentscope = classname


	def addvar_class(self,varname,datatype,_type,size):
		if '[' in varname:
			varname= varname.split('[')[0]
			self.table[self.currentscope]['identifiers'][varname]= {'name': varname,'type':'Array','datatype':datatype,'scope':self.currentscope}
		else:
			self.table[self.currentscope]['identifiers'][varname]={'name':varname,'type':_type,'datatype':datatype,'scope':self.currentscope,'size':size}

	def addconstructor_class(self,classname,varname,value):
		self.table[classname]['constructor'][varname]={'name':varname+"."+self.currentscope,'value':value}

	
	def addfunc_class(self,classname,funcname,datatype,_type):
		#print self.table[classname]['child'], "KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
		self.table[classname]['member_functions'][funcname]={'name':funcname,'type':_type,'datatype':datatype,'parentscope':self.table[classname]['child'],'identifiers':{},'parameters':[]}
		self.currentscope = funcname
		#print self.table[classname]['member_functions'][funcname]['parentscope']

	def get_class_idlist(self,classname):
		return self.table[self.table[classname]['child']]['identifiers']

	def newscope(self):
		scope = "s"+str(self.scope_no)
		self.table[scope] = {'name':scope,'type':None,'datatype':None,'parentscope':self.currentscope,'identifiers':{}}
		self.currentscope=scope
		self.scope_no+=1
	
	def endscope(self):
		self.currentscope = self.table[self.currentscope]['parentscope'] 
	
	def checkscope(self,varname):
		scope = self.currentscope
		# print scope, varname , self.table[scope]#['identifiers']
		while scope not in [None]:
			# print not self.table[scope]['identifiers'],"GGGGGGGGGGGG"
			if bool(self.table[scope]['identifiers']) and (varname in self.table[scope]['identifiers']):
				return scope
		
			scope = self.table[scope]['parentscope']
		

		if 'main' in self.table.keys():
			if varname in self.table['main']['identifiers']:
				return 'main'
		
		return None
	
	def gettype(self,scope,varname):
		return self.table[scope]['identifiers'][varname]['datatype']

	def getfunc_returntype(self,funcname):
		return self.table[funcname]['datatype']
