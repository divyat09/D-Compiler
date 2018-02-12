from globalvars import *

class SymbolTable:
    def __init__(self):
        self.table = {}
    #Add variable to table 
    def addvar(self,varname):

		if '[' in varname:
			_name= varname.split('[')[0]
			self.table[_name]= {'name':varname,'type':'Array','scope':None}
		else:
 	       self.table[varname]={'name':varname,'type':'Variable','scope':None}