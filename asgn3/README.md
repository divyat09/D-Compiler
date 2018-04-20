# D-Compiler( Group-46 )

### Contents
###### /src directory 
This directory contains the python code used to generate Assembly Code form Intermediate Representation of the program

1 lexer.py
  
  	-

2 parser.py

	- 

###### /test directory 
This directory contains the tests cases, txt files containing the Intermediate Representation of the program.

TestCase1: cmp_3_num.d: Compares 3 numbers and returns smallest

TestCase2: inp_arr.d: Scans an array of 10 elements and prints it 

TestCase3: operators1.d: Functionality of all arithematic operators

TestCase4: operators2.d: Functionality of all Bitwise Operators

TestCase5: func_fact.d: Computes factorial of the entered number

TestCase6: VarSpiller.d: Checks of correct Regiser Spilling as per Next Use in Variables

TestCase7: ArrSpiller.d: Checks for correct Register Spilling as per Next Use in Arrray

TestCase8: conditional.d: All the conditional operators 

### Execution

1 cd to the base directory: asgn3

2 Run the command: make

3 Run test cases: bin/parser test/test1.d

4 firefox test1.html
