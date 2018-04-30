# D-Compiler( Group-46 )

### Contents
###### /src directory 
This directory contains the python code used to generate Assembly Code form Source Code of the program

####### Source Code to Intermediate Representation

1 lexer.py
  
  	Generates lexer for the grammar using ply's lexical analysis tool ply.lex

2 parser.py

	Generates LALR(1) parser for the Grammar using ply's syntactic analysis tool ply.yacc. Although the grammar is not yaccable we have made sincere attempts to make a sensible parser, there are some shift-reduce, reduce-reduce conflicts but the preferred rules and choices in case of conflict are correct. So, in terms of correctness, the parser works fine. 

	The semantic actions corresponding to production rules have been added to the parser. Markers have been used for semantic actions of inherited attributes.

3 symbol_table.py

	Stores the name, scope, type, datatype, size, place of a varible. It gets called from the parser.py when a variable is declared. 
	
4 TAC.py
	
	Stores the three address code for each statement in the program in the form of a list. It has a method OutputTAC()" that iterates over the list of three address codes and outputs the Intermediate Representation Code for the source code.

####### Intermediate Representation to Assembly Code

1 codegen.py
  
  	- Loads the Intermediate Representation data from testcases and iterates over each instruction
  	- Extracts out variables from each instruction and stores them in Symbol Table via symbol_table.py
  	- Uses irds.py class to generate three address code data-structure for each instruction in testcase
  	- Appends boundary lines to the basic block list by checking operator cases accordingly 
	- Uses assembly.py to generate Assembly Code(x86) from the list of three address code instructions

2 Symbol_Table.py

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

TestCase1: arithmetic1.d : Contains variables, arrays and some computations on them 

TestCase2: arithmetic2.d: Bit Wise Operations 

TestCase3: array1.d : Arrays and Loops

TestCase4: array2.d : Basic Array Implementation Example

TestCase5: class.d: Declared classes and initialised class objects

TestCase6: factorial.d : A function that computes factorial of a number

TestCase7: func.d : Call to function foo passing 3 parameters with different data types

TestCase8: for.d: Execution of a for loop statement

TestCase9: dangling_if_else.d : A nested if_else statement 

TestCase10: do_while.d : Execution of a do_while statement 

TestCase11: switch.d : Implementation a switch case statement

TestCase12: while.d : Tests a  basic while loop implementation

TestCase13: input.d : Takes an input as number and outputs the square of the number

### Execution

1 cd to the base directory: FinalProject

2 Run the command: make

3 Run test cases: bin/compile test/test1.d
