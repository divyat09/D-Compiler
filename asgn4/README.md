# D-Compiler( Group-46 )

### Contents
###### /src directory 
This directory contains the python code used to generate Assembly Code form Intermediate Representation of the program

1 lexer.py
  
  	Generates lexer for the grammar using ply's lexical analysis tool ply.lex

2 parser.py

	Generates LALR(1) parser for the Grammar using ply's syntactic analysis tool ply.yacc. Although the grammar is not yaccable we have made sincere attempts to make a sensible parser, there are some shift-reduce, reduce-reduce conflicts but the preferred rules and choices in case of conflict are correct. So, in terms of correctness, the parser works fine. 

	The semantic actions corresponding to production rules have been added to the parser. Markers have been used for semantic actions of inherited attributes.

3 symbol_table.py
	

4 TAC.py
	
	Stores the three address code for each statement in the program in the form of a list. It has a method OutputTAC()" that iterates over the list of three address codes and outputs the Intermediate Code for the source code.

###### /test directory 
This directory contains the tests cases, txt files containing the Intermediate Representation of the program.

TestCase1: alias.d : Declare alias names for some variables and class object variables

TestCase2: arithmetic.d: Contains variables, arrays and some computations on them 

TestCase3: class.d: Declared classes and initialised class objects

TestCase4: class_inheritance.d : Declared a base class ,a derived class and initialised class objects

TestCase5: dangling_if_else.d : a nested if_else statement 

TestCase6: enum.d : Created an enumeration list

TestCase7: for.d: A for loop that print yes on odd and no on even number of iterations

TestCase8: func.d : Call to function foo passing 3 parameters with different data types

TestCase9: nested_for.d : A nested for loop that increments a variable

TestCase10: pointer.d : Declared and initialised pointers 

TestCase11: switch.d : Implemented a switch case statement

TestCase12: union.d : Created a union and initialised the variables in the union

TestCase13: while.d : Tests while loop and dowhile implementation

TestCase14: keywords.d : Tests implementation of special keywords in our grammar
### Execution

1 cd to the base directory: asgn4

2 Run the command: make

3 Run test cases: bin/irgen test/test1.d
