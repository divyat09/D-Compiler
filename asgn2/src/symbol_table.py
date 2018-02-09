class SymbolTable:
    def __init__(self):
        self.table = {}
    #Add variable to table 
    def addvar(self,varname):
        self.table[varname]={'name':varname,'type':None,'scope':None}