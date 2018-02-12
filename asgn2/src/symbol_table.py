from globalvars import *

class SymbolTable:
    def __init__(self):
        self.table = {}
    #Add variable to table 
    def addvar(self,varname):

		if '[' in varname:
			self.table[varname]= {'name': varname,'type':'Array','scope':None}
		else:
			self.table[varname]={'name':varname,'type':'Variable','scope':None}