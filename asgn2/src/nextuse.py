def NextUse( IRobj ):
  
	Status= IRobj.isValid()

 	if Status[0]:
  		Global_Dict[ IRobj.src1 ]= IRobj.lineno
  	
	if Status[1]:
		Global_Dict[ IRobj.src2 ]= IRobj.lineno

	if Status[2]:
		Global_Dict[ IRobj.dst ]= -1

  	return Global_Dict