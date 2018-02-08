def NextUse( IRobj, Global_Dict ):
  
	Status= IRobj.isValid()

 	if Status[0]:
  		Global_Dict[ IRobj.src1 ]= IRobj.lineno
  	
	if Status[1]:
		Global_Dict[ IRobj.src2 ]= IRobj.lineno

	if Status[2]:
		Global_Dict[ IRobj.dst ]= -1

  	return Global_Dict


def BuildNextUseTable( bb ):

	for _iter in range( len(bb)-1, 0, -1 ):	# Need to iterate only till the 2nd element: hence 0 and not 1
	  
	  Global_Dict= {}

	  # Start and End here are in the opposite sense from English
	  # They represent the start and end of basic block as per the NextUse Algo sense i.e. starting from bottom
	  Start= bb[_iter]
	  End= bb[_iter +1 ]  # Not doing +1 here as the range func of python would take care of it

	  for linenum in range( Start, End  ):
	  	Global_Dict= NextUse( statements[linenum -1], Global_Dict )
	    NextUseTable.append( Global_Dict )