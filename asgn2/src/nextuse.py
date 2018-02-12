from globalvars import *
import sys

def InitGlobalDict():
	Global_Dict={}

	for _var in Table.table.keys():
		# print int(sys.maxint)
		# print Table.table.keys()
		# print _var
		Global_Dict[Table.table[_var]['name']]= int(sys.maxint)

	return Global_Dict

def NextUse( IRobj, Global_Dict ):
  
	Status= IRobj.isValid()

	if Status[0]:
  		Global_Dict[ IRobj.src1['name'] ]= IRobj.lineno
  	
	if Status[1]:
		Global_Dict[ IRobj.src2['name'] ]= IRobj.lineno

	if Status[2]:
		Global_Dict[ IRobj.dst['name'] ]= int(sys.maxint)

	return Global_Dict

		
def BuildNextUseTable( bb ):

	# for IRobj in (statements):
	# 	Status= IRobj.isValid()
	# 	if Status[0]:
	# 		Global_Dict[ IRobj.src1 ]= -1
		
	# 	if Status[1]:
	# 		Global_Dict[ IRobj.src2 ]= -1

	# 	if Status[2]:
	# 		Global_Dict[ IRobj.dst ]= -1
	
	for _iter in range( len(bb)-1, 0, -1 ):	# Need to iterate only till the 2nd element: hence 0 and not 1
	  
	  Global_Dict= InitGlobalDict()

	  StartLine= bb[_iter -1 ] 
	  EndLine= bb[_iter] 

	for linenum in range( EndLine, StartLine-1, -1  ):
	  	# print linenum,statements	
	  	# Dont include the Ending Leader unless its the case of Ending Basic Block
	    if( _iter!= len(bb) -1 and linenum==EndLine ):
	  	    continue

	    Global_Dict= NextUse( statements[linenum -1], Global_Dict )
		# print Global_Dict
	    NextUseTable.append( Global_Dict.copy() )
		# print NextUseTable 
		# print "\n"

	NextUseTable.reverse()
	# print NextUseTable
