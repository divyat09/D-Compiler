# D-Compiler

### Contents
/src directory contains the code lex.py: the lexer generator

/test directory contains the test cases to be tokenised of source language D

Makefile generates the executable "lexer" for /src/lex.py in the /bin directory

### Execution

First create executable of "lex.py" using makefile and then run that executable "bin/lexer" with D Lang Source Code( Test Case ) as first command line parameter
 
1 Come to the base directory: asgn1

2 Run the command: makefile

3 Tokenise test cases: bin/lexer test/test1.d

Tokenise different test cases by passing them as input command line parameters
 	
