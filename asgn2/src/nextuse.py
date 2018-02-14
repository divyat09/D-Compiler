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
		# Array Case, Store next use for A and i too in A[i]
		if '[' in IRobj.src1:
			Base= IRobj.src1.split('[')[0]
			Index= IRobj.src1.split('[')[1].split(']')[0]

	  		Global_Dict[ Base ]= IRobj.lineno
			if not isint(Index):
		 		Global_Dict[ Index]= IRobj.lineno

  		Global_Dict[ IRobj.src1 ]= IRobj.lineno
  	
	if Status[1]:
		# Array Case, Store next use for A and i too in A[i]
		if '[' in IRobj.src2:
			Base= IRobj.src2.split('[')[0]
			Index= IRobj.src2.split('[')[1].split(']')[0]

	  		Global_Dict[ Base ]= IRobj.lineno
			if not isint(Index):
		 		Global_Dict[ Index]= IRobj.lineno

		Global_Dict[ IRobj.src2 ]= IRobj.lineno

	if Status[2]:
		# Array Case, Store next use for A and i too in A[i]
		if '[' in IRobj.src1:
			Base= IRobj.dst.split('[')[0]
			Index= IRobj.ds.split('[')[1].split(']')[0]

	  		Global_Dict[ Base ]= IRobj.lineno
			if not isint(Index):
		 		Global_Dict[ Index]= IRobj.lineno

		Global_Dict[ IRobj.dst ]= int(sys.maxint)

	return Global_Dict

		
def BuildNextUseTable( bb ):
	
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
