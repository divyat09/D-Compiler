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

	for _iter in range( 0, len(bb)-1 ):	# Need to iterate only till the 2nd last element
	  
	  Global_Dict= {}
	  Start= bb[_iter]
	  End= bb[_iter +1 ]  # Not doing -1 here as the range func of python would take care of it

	  for linenum in range( Start, End  ):
	  	Global_Dict= NextUse( statements[linenum -1], Global_Dict )
	    NextUseTable.append( Global_Dict )