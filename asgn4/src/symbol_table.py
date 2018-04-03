# from globalvars import *

class SymbolTable:
	def __init__(self):
		self.table = {}
		self.temp_no=0	
		self.label_no=0
		#Add variable to table 

	def get_temp(self):
		self.temp_no = self.temp_no+1
		return "tmp"+str(self.temp_no)
	
	def get_label(self):
		self.label_no = self.label_no+1
		return "label"+str(self.label_no)
		
	def addvar(self,varname,datatype):

		if '[' in varname:
			varname= varname.split('[')[0]
			self.table[varname]= {'name': varname,'type':'Array','scope':None}
		else:
			self.table[varname]={'name':varname,'type':'Variable','datatype':datatype,'scope':None}
