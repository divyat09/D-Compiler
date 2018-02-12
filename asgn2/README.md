# D-Compiler( Group-46 )

### Contents
###### /src directory 
This directory contains the python code used to generate Assembly Code form Intermediate Representation of the program

1 codegen.py
  
  	- Loads the Intermediate Representation data from testcases and iterates over each instruction
  	- Extracts out variables from each instruction and stores them in Symbol Table via symbol_table.py
  	- Uses irds.py class to generate three address code data-structure for each instruction in testcase
  	- Appends boundary lines to the basic block list by checking operator cases accordingly 
	- Uses assembly.py to generate Assembly Code(x86) from the list of three address code instructions

2 symbol_table.py

	- Conatins SymbolTable class that maps a variable to its name, type and scope

3 irds.py

	- Contains the IRDS class, its represent method takes IR instruction data and generates the 3AC( src1, src2, dst ) data-structure 
	- Handles cases of all the valid operators and assigns values to src1, src2 and dst accordingly

4 nextuse.py

	- BuildNextUseTable():Traverses each Basic Block in reverse order, calculates next use of each variable for current line and stores it
	- NextUse(): Updates the next value of varibles( src1, src2, dst ) in current instruction.

5 registers.py

	- AssignRegister(): Assigns a register to given variable. 
	  First it looks for a Free Register, it there exists a Free Regiser then its moves that variable data to register. 
	  Else it does Register Spilling to free the register to variable with largest NextUse. 

	- FreeRegister(): Loads the register value into memory, makes it a free register for allocation

	- GetFreeRegister(): Iterates over all registers to return an free or unallocated register. Returns -1 if no such register available

	- RegisterSpilling(): Removes the register assigned to max next use variable among the allocatted variables 

6 assembly.py

	- Iterates over all 3AC Instructions and generates x86 code for each instruction
	- Different methods corresponding to different types of IRObj.op

7 globalvars.py

	- Some helpful global variables

###### /test directory 
This directory contains the tests cases, txt files containing the Intermediate Representation of the program.

TestCase1: 
TestCase2: 
TestCase3: 
TestCase4: 
TestCase5: 
TestCase6: 
TestCase7: 

### Execution

1 cd to the base directory: asgn2

2 Run the command: make

3 Run test cases: bin/codegen test/test1.ir

4 Execute the generated x86 assembly code
