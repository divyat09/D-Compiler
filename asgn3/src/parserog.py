import ply.lex as lex
import sys
import ply.yacc as yacc
from lexer import tokens
import logging

revoutput = []

def p_addExpression(p) : 
	'''addExpression: mulExpression 
    				| addExpression PLUS mulExpression 
					| addExpression MINUS mulExpression 
					| addExpression TILDE mulExpression;
	'''
	revoutput.append(p.slice)

def p_aliasDeclaration(p): 
	''' aliasDeclaration: ALIAS aliasInitializer comma_aliasInitializer SEMICOLON | ALIAS multiplestorageClass type identifierList SEMICOLON
	'''
	revoutput.append(p.slice)


# equivalent to (’,’ aliasInitializer)*

def p_comma_aliasInitializer(p):
	'''comma_aliasInitializer : COMMA aliasInitializer comma_aliasInitializer
							  | empty
	'''
	revouput.append(p.slice)

# multiplestorageClass is equivalent to storageClass*

def p_multiplestorageClass(p):
	''' multiplestorageClass : storageClass multiplestorageClass
							 | empty
	'''
	revouput.slice(p)

def p_aliasInitializer(p):
	'''	aliasInitializer: Identifier ASSIGN multiplestorageClass type 
						| Identifier templateParameters ASSIGN multiplestorageClass type
						| Identifier ASSIGN functionLiteralExpression SEMICOLON
						| Identifier templateParameters ASSIGN functionLiteralExpression SEMICOLON
	'''
	revoutput.append(p.slice)
          
def p_aliasThisDeclaration(p): 
	''' aliasThisDeclaration : ALIAS Identifier THIS SEMICOLON
	'''
	revoutput.append(p.slice)
          
def p_andAndExpression(p): 
	'''andAndExpression : orExpression 
						| andAndExpression DOUBLE_AMPERSAND orExpression
	'''
	revoutput.append(p.slice)
def p_andExpression(p): 
	'''andExpression : cmpExpression 
					 | andExpression AMPERSAND cmpExpression
	'''
	revoutput.append(p.slice)

def p_argumentList(p): 
	''' argumentList : assignExpression 
					| argumentList comma_assign
	'''
	revoutput.append(p.slice)

# Equivalent to ',' assignExpression
def p_comma_assign(p):
	'''comma_assign : COMMA assignExpression comma_assign
					| empty
	'''
	revoutput.append(p.slice)

def p_arguments(p): 
	''' arguments : LPAREN RPAREN
				  | LPAREN argumentList RPAREN
	'''	
	revoutput.append(p.slice)

def p_arrayInitializer(p):
	''' arrayInitializer : LBRACKET RBRACKET 
						 | LBRACKET arrayMemberInitialization comma_arrayMemberInitialization RBRACKET 
	'''
	revoutput.append(p.slice)

# equivalent to (, arrayMemberInitialization)*
def p_comma_arrayMemberInitialization(p):
	''' comma_arrayMemberInitialization : COMMA arrayMemberInitialization comma_arrayMemberInitialization
										| empty
	'''
	revouput.slice(p)

def p_arrayLiteral(p):
	''' array_Literal : LBRACKET RBRACKET 
				  	  | LBRACKET argumentList RBRACKET
	'''
	revoutput.append(p.slice)
          
def p_arrayMemberInitialization(p): 
	'''arrayMemberInitialization : assignExpression COLON nonVoidInitializer 
				  				 | nonVoidInitializer
	'''
	revoutput.append(p.slice)

def p_assignExpression(p):
	'''assignExpression : ternaryExpression 
						| ternaryExpression assignOperator expression
	'''
	revoutput.append(p.slice)

def p_assignOperator(p):
	''' assignOperator : ASSIGN 
					   | EQ_LEFT 
					   | EQ_RIGHT 
					   | EQ_PLUS 
					   | EQ_MINUS 
					   | EQ_TIMES 
					   | EQ_MODULO 
					   | EQ_AND_BIT 
					   | EQ_DIV 
					   | EQ_OR_BIT 
					   | EQ_XOR_BIT 
	'''
	revoutput.append(p.slice)

def p_attribute(p):
	'''attribute : PRIVATE 
				 | PROTECTED 
				 | PUBLIC 
				 | STATIC 
				 | EXTERN 
				 | FINAL 
				 | AUTO 
				 | CONST 
				 | IMMUTABLE 
	'''
	revoutput.append(p.slice)

def p_attributeDeclaration(p):
	''' attributeDeclaration : attribute COLON
	'''
	revoutput.append(p.slice)

def p_autoDeclaration(p):
	''' autoDeclaration : storageClass multiplestorageClass Identifier ASSIGN initializer comma_identifier_assign_initializer SEMICOLON
	'''
	revouput.slice(p)

# equivalent to (',' identifier = initializer) *
def p_comma_identifier_assign_initializer(p):
	'''comma_identifier_assign_initializer : COMMA Identifier ASSIGN initializer comma_identifier_assign_initializer
										   | empty
	'''
	revouput.slice(p)	

def p_blockStatement(p):
	'''blockStatement : LBRACE RBRACE 
					  | LBRACE declarationsAndStatements RBRACE
	''' 
	revouput.slice(p)

def p_bodyStatement(p):
	''' bodyStatement: BODY blockStatement 
	'''
	revoutput.append(p.slice)
          
def p_breakStatement(p):
	''' breakStatement : BREAK SEMICOLON 
					   | BREAK IDENTIFIER SEMICOLON 
	'''
	revoutput.append(p.slice)

def p_baseClass(p):
	'''baseClass : type2 
	'''
	revoutput.append(p.slice)

def p_baseClassList(p): 
	''' baseClassList : baseClass
 					  | baseClassList COMMA baseClass
	'''
	revoutput.append(p.slice)
          
def p_builtinType(p):
	''' builtinType : BOOL 
					| SHORT 
					| USHORT 
					| INT
					| UINT 
					| LONG 
					| ULONG 
					| CHAR
					| float 
					| d
    '''
	revoutput.append(p.slice)	

def p_caseRangeStatement(p):
	''' caseRangeStatement : CASE assignExpression COLON ELLIPSIS CASE assignExpression COLON declarationsAndStatements
	'''
	revoutput.append(p.slice)

def p_caseStatement(p):
	''' caseStatement : CASE argumentList COLON declarationsAndStatements
	'''
	revoutput.append(p.slice) 

def p_castExpression(p):
	'''castExpression : CAST LPAREN RPAREN unaryExpression
				      | CAST LPAREN type RPAREN unaryExpression
				      | CAST LPAREN castQualifier RPAREN unaryExpression 
	'''
	revoutput.append(p.slice)

def p_castQualifier(p):
	''' castQualifier : CONST 
					  | IMMUTABLE 
	'''
	revoutput.append(p.slice)

def p_classDeclaration(p):
	''' classDeclaration : CLASS Identifier SEMICOLON 
						 | CLASS Identifier COLON baseClassList structBody
						 | CLASS Identifier structBody
	'''
	revoutput.append(p.slice)
 
def p_cmpExpression(p):
	''' cmpExpression : shiftExpression 
					  | equalExpression
					  | identityExpression
 					  | relExpression
	'''
	revoutput.append(p.slice)
  
def p_constraint(p):
	''' constraint : IF LPAREN expression RPAREN
	'''
	revoutput.append(p.slice)

def p_constructor(p):
	''' constructor : THIS parameters multiple_memberFunctionAttribute functionBody 
					| THIS parameters multiple_memberFunctionAttribute SEMICOLON
					| THIS templateParameters parameters multiple_memberFunctionAttribute functionBody 
					| THIS templateParameters parameters multiple_memberFunctionAttribute SEMICOLON
					| THIS parameters multiple_memberFunctionAttribute constraint functionBody 
					| THIS parameters multiple_memberFunctionAttribute constraint SEMICOLON
					| THIS templateParameters parameters multiple_memberFunctionAttribute constraint functionBody 
					| THIS templateParameters parameters multiple_memberFunctionAttribute constraint SEMICOLON 
	'''
	revoutput.append(p.slice)

# Equivalent to memberFunctionAttribute*
def p_multiple_memberFunctionAttribute(p):
	'''multiple_memberFunctionAttribute : memberFunctionAttribute multiple_memberFunctionAttribute
										| empty
	'''
	revouput.slice(p)

def p_continueStatement(p):
	''' continueStatement : CONTINUE SEMICOLON
						  | CONTINUE Identifier SEMICOLON
	'''
	revoutput.append(p.slice)

def p_declaration(p):
	''' declaration : multipleattributes declaration2 | attribute multipleattributes LBRACE declaration* RBRACE 
	'''
	revoutput.append(p.slice)

# Equivalent to attribute*
def p_multipleattributes(p):
	'''multipleattributes : attribute multipleattributes
						  | empty
	'''
	revouput.slice(p)

def p_declaration2(p):
	''' declaration2 : aliasDeclaration 
					 | aliasThisDeclaration 
					 | anonymousEnumDeclaration 
					 | attributeDeclaration 
					 | classDeclaration 
					 | conditionalDeclaration 
					 | constructor 
					 | destructor 
					 | enumDeclaration 
					 | functionDeclaration 
					 | importDeclaration 
					 | mixinDeclaration 
					 | unionDeclaration 
					 | variableDeclaration 
	'''
	revoutput.append(p.slice)

def p_declarationsAndStatements(p):
	''' declarationsAndStatements : declarationOrStatement
								  | declarationOrStatement declarationsAndStatements
	'''
	revoutput.append(p.slice)

def p_declarationOrStatement(p):
	''' declarationOrStatement : declaration 
							   | statement 
	'''
	revouput.slice(p)

def p_declarator(p):
	''' declarator : Identifier 
				   | Identifier ASSIGN initializer 
				   | Identifier templateParameters ASSIGN initializer
	'''
	revoutput.append(p.slice)

def p_defaultStatement(p):
	''' defaultStatement : DEFAULT COLON declarationsAndStatements
	'''
	revoutput.append(p.slice)

def p_deleteExpression(p): 
	''' deleteExpression = DELETE unaryExpression
	'''
	revoutput.append(p.slice)

def p_destructor(p):
	''' destructor : TILDE THIS LPAREN RPAREN multiple_memberFunctionAttribute functionBody 
				   | TILDE THIS LPAREN RPAREN multiple_memberFunctionAttribute SEMICOLON
	'''
	revoutput.append(p.slice)

def p_doStatement(p):
	''' doStatement : DO statementNoCaseNoDefault WHILE LPAREN expression RPAREN SEMICOLON
	'''
	revoutput.append(p.slice)
	
def p_enumBody(p):
	''' enumBody : DOUBLE_QUOTE enumMember DOUBLE_QUOTE
				 | DOUBLE_QUOTE enumMember comma_enumMember DOUBLE_QUOTE
	'''
	revouput.slice(p)

# Equivalent to (, enumMember)*
def p_comma_enumMember(p):
	'''comma_enumMember : COMMA enumMember comma_enumMember
						| empty
	'''
	revouput.slice(p)

def p_anonymousEnumMember(p):
	'''anonymousEnumMember : TYPEDEF IDENTIFIER ASSIGN assignExpression 
						   | IDENTIFIER ASSIGN assignExpression 
						   | IDENTIFIER
	'''
	revoutput.append(p.slice)

def anonymousEnumDeclaration(p):
	'''anonymousEnumDeclaration: ENUM LBRACE anonymousEnumMember multipleanonymousEnumMember  RBRACE
							   | ENUM COLON type LBRACE anonymousEnumMember multipleanonymousEnumMember RBRACE
	'''
	revouput.slice(p)

#Equivalent to anonymousEnumMember*
def p_multipleanonymousEnumMember(p):
	'''multipleanonymousEnumMember : anonymousEnumMember multipleanonymousEnumMember
								   | empty
	'''
	revouput.slice(p)

def p_enumDeclaration(p):
	'''enumDeclaration : ENUM IDENTIFIER SEMICOLON
					   | ENUM IDENTIFIER COLON TYPEDEF SEMICOLON
					   | ENUM IDENTIFIER COLON TYPEDEF enumBody
  	'''
	revoutput.append(p.slice)

def p_enumMember(p):
	'''enumMember : IDENTIFIER
				  | IDENTIFIER ASSIGN assignExpression
	  '''
	revoutput.append(p.slice)
  
def p_equalExpression(p):
	'''equalExpression: shiftExpression IS_EQ shiftExpression
					  | shiftExpression NOT_EQ shiftExpression 
  	'''
	revoutput.append(p.slice)

def p_expression(p):
	'''expression : assignExpression 
				  | expression COMMA assignExpression
  	'''
	revoutput.append(p.slice)

def p_expressionStatement(p):
	'''expressionStatement : expression SEMICOLON
	'''
	revouput.slice(p)

def p_forStatement(p):
	''' forStatement: FOR LPAREN declaration SEMICOLON RPAREN declarationOrStatement
					| FOR LPAREN statementNoCaseNoDefault SEMICOLON RPAREN declarationOrStatement
					| FOR LPAREN declaration SEMICOLON expression RPAREN declarationOrStatement
					| FOR LPAREN statementNoCaseNoDefault SEMICOLON expression RPAREN declarationOrStatement
					| FOR LPAREN declaration expression SEMICOLON RPAREN declarationOrStatement
					| FOR LPAREN statementNoCaseNoDefault expression SEMICOLON RPAREN declarationOrStatement
					| FOR LPAREN declaration expression SEMICOLON expression RPAREN declarationOrStatement  
					| FOR LPAREN statementNoCaseNoDefault expression SEMICOLON expression RPAREN declarationOrStatement   					 
	'''
	revouput.slice(p)


def p_foreachStatement():
	''' foreachStatement : FOREACH LPAREN foreachTypeList SEMICOLON expression RPAREN declarationOrStatement 
						 | FOREACH LPAREN foreachType SEMICOLON expression RANGE expression RBRACKET declarationOrStatement 
						 | FOREACH_REVERSE LPAREN foreachTypeList SEMICOLON expression RPAREN declarationOrStatement 
						 | FOREACH_REVERSE LPAREN foreachType SEMICOLON expression RANGE expression RPAREN declarationOrStatement 
	'''
	revouput.slice(p)

def p_foreachType(p):
  '''
      foreachType: typeConstructors? type ? IDENTIFIER | typeConstructors? type? IDENTIFIER 
  '''
  revoutput.append(p.slice)  

def p_foreachTypeList(p):
	'''foreachTypeList: foreachType 
			  | foreachTypeList COMMA foreachType
	'''
	revoutput.append(p.slice)

def p_functionBody(p):
	'''functionBody: blockStatement
	'''
	revoutput.append(p.slice)

def p_functionCallExpression(p):
	'''functionCallExpression: symbol arguments unaryExpression arguments
				 | type arguments ;
	'''
	revoutput.append(p.slice)
         
def p_functionDeclaration(p):
  '''
      functionDeclaration: ( storageClass+ | TYPEDEF ) IDENTIFIER parameters memberFunctionAttribute* ( functionBody | SEMICOLON ) | ( storageClass+ | TYPEDEF )
      IDENTIFIER templateParameters parameters memberFunctionAttribute* constraint? ( functionBody | SEMICOLON )
  '''
  revoutput.append(p.slice)

def p_functionLiteralExpression(p):
  '''
      functionLiteralExpression: | FUNCTION TYPEDEF? (parameters functionAttribute*)? functionBody | parameters functionAttribute* functionBody |
      functionBody | IDENTIFIER assignExpression | FUNCTION TYPEDEF? parameters functionAttribute* assignExpression | parameters functionAttribute( ).....
  '''
  revoutput.append(p.slice)

def p_gotoStatement(p):
	'''gotoStatement: GOTO IDENTIFIER SEMICOLON
			| GOTO DEFAULT SEMICOLON
			| GOTO CASE SEMICOLON
			| GOTO CASE expression SEMICOLON
	'''
	revoutput.append(p.slice)

def p_identifierChain(p):
	'''identifierChain: IDENTIFIER
			  | identifierChain DOT IDENTIFIER
	'''
	revoutput.append(p.slice)

def p_identifierList(p):
	'''identifierList: IDENTIFIER
			  | identifierList COMMA IDENTIFIER
	'''
	revoutput.append(p.slice)


def p_identifierOrTemplateChain(p):
	'''identifierList: identifierOrTemplateInstance
			  | identifierOrTemplateChain DOT identifierOrTemplateInstance
	'''
	revoutput.append(p.slice)
def p_identifierOrTemplateInstance(p):
	'''identifierOrTemplateInstance: IDENTIFIER | templateInstance ;
	'''
def p_identityExpression(p):
	'''identityExpression: shiftExpression IS shiftExpression
			     | shiftExpression EXCLAMATION IS shiftExpression
	'''
	revoutput.append(p.slice)
def p_ifStatement(p):
	'''ifStatement: IF LPAREN ifCondition RPAREN declarationOrStatement 
			| IF LPAREN ifCondition RPAREN declarationOrStatement ELSE declarationOrStatement
	'''
	revoutput.append(p.slice)

def p_ifCondition(p):
	'''ifCondition: AUTO IDENTIFIER ASSIGN expression 
		        | TYPEDEF IDENTIFIER ASSIGN expression 
			| expression
	'''
	revoutput.append(p.slice)
def p_importBind(p):
	'''importBind: IDENTIFIER
		       | IDENTIFIER ASSIGN IDENTIFIER 
	'''
	revoutput.append(p.slice)
def p_importBindings(p):
	'''importBindings: singleImport COLON importBind
			   | singleImport COLON importBind COLON importBind
	'''
	revoutput.append(p.slice)

def p_importDeclaration(p):
	'''importDeclaration: IMPORT singleImport (’,’ singleImport)* (’,’ importBindings)? SEMICOLON
			      | IMPORT importBindings SEMICOLON
	'''
	revoutput.append(p.slice)


def p_index(p):
	''' index : assignExpression 
			  |	assignExpression RANGE assignExpression
	'''			
	revoutput.append(p.slice)

#############################################
def p_indexExpression(p):
	''' indexExpression : unaryExpression LBRACKET RBRACKET 
					    | unaryExpression LBRACKET index (’,’index)* RBRACKET
	'''
	revoutput.append(p.slice)
#############################################

def p_initializer(p):
	''' initializer : VOID 
					| nonVoidInitializer ; ;
	'''
	revoutput.append(p.slice)

#####################################################
def p_isExpression(p):
	''' isExpression : IS LPAREN type identifier? RPAREN IS LPAREN type identifier? COLON typeSpecialization RPAREN IS LPAREN type identifier? 		ASSIGN typeSpecialization RPAREN IS LPAREN type identifier? COLON typeSpecialization COMMA templateParameterList RPAREN IS LPAREN type 			identifier? ASSIGN typeSpecialization COMMA templateParameterList RPAREN 
	'''
	revoutput.append(p.slice)
#####################################################

def p_labeledStatement(p):
	''' labeledStatement : Identifier COLON 
						 |	Identifier COLON declarationOrStatement
	'''
	revouput.slice(p)

def p_memberFunctionAttribute(p):
	''' memberFunctionAttribute : functionAttribute 
								| IMMUTABLE 
								| CONST 
								| RETURN
	'''
	revoutput.append(p.slice)

def p_mixinDeclaration(p):
	''' mixinDeclaration : mixinExpression SEMICOLON 
						 | templateMixinExpression SEMICOLON
	'''
	revoutput.append(p.slice)
	
def p_mixinExpression(p):
	''' mixinExpression : MIXIN LPAREN assignExpression RPAREN 
	'''
	revouput.slice(p)


def p_mulExpression(p):
	''' mulExpression : powExpression 
					  | mulExpression TIMES 
					  | mulExpression DIV 
					  | mulExpression MODULO
	'''
	revoutput.append(p.slice)

##########################################
def p_newAnonClassExpression(p):
	''' newAnonClassExpression : NEW arguments? CLASS arguments? baseClassList? structBody 
	'''
	revoutput.append(p.slice)
###########################################
def p_newExpression(p):
	''' newExpression : NEW type 
					  | NEW type LBRACKET assignExpression RBRACKET 
					  | NEW type arguments
					  | newAnonClassExpression
	'''
	revoutput.append(p.slice)

def p_nonVoidInitializer(p):
	''' nonVoidInitializer : assignExpression 
						   | arrayInitializer
						   | structInitializer
	'''
	revoutput.append(p.slice)

def p_orExpression(p):
	''' orExpression : xorExpression 
					 | orExpression PIPE xorExpression 
	'''
	revoutput.append(p.slice)

def p_orOrExpression(p):
	''' orOrExpression : andAndExpression
					   | orOrExpression DOUBLE_PIPE andAndExpression
	'''
	revoutput.append(p.slice)
###############################################################################
def p_parameter(p):
	''' parameter : parameterAttribute* type parameterAttribute* type Identifier? ’...’ parameterAttribute* type Identifier? (’=’assignExpression)?;
	'''
	revoutput.append(p.slice)
###############################################################################
def p_parameterAttribute(p):
	''' parameterAttribute : typeConstructor 
						   | FINAL 
						   | OUT 
						   | AUTO 
						   | RETURN
	'''
	revoutput.append(p.slice)

############################
def p_parameters(p):
	''' parameters : LPAREN parameter (’,’ parameter)* (’,’ ’...’)? ’)’ | ’(’ ’...’ ’)’ | ’(’ ’)’
	'''
	revoutput.append(p.slice)
############################
###############################################
def p_postblit(p):
	''' postblit : THIS LPAREN THIS RPAREN multiple_memberFunctionAttribute functionBody
				 | THIS LPAREN THIS RPAREN multiple_memberFunctionAttribute SEMICOLON
	'''
	revoutput.append(p.slice)
################################################

def p_powExpression(p):
	''' powExpression : unaryExpression 
					  | powExpression ’ˆitemˆ’ unaryExpression 
	'''
	revoutput.append(p.slice)
################################################

def p_primaryExpression(p):
	''' primaryExpression : identifierOrTemplateInstance 
						  | DOT identifierOrTemplateInstance 
						  | typeConstructor LPAREN basicType RPAREN DOT Identifier 
						  | basicType DOT Identifier 
						  | basicType arguments 
						  | arrayLiteral 
						  | LPAREN expression RPAREN 
						  | functionLiteralExpression 
						  | traitsExpression 
						  | mixinExpression 
						  | importExpression 
						  | DOLLAR 
						  | THIS 
						  | NULL 
						  | TRUE 
						  | FALSE 
						  | IntegerLiteral 
						  | FloatLiteral
#######################################################################
						  | StringLiteral+ 
##################################################################
						  | CharacterLiteral
	'''
	revoutput.append(p.slice)

def p_register(p):
	''' register : Identifier 
				 | Identifier LPAREN IntegerLiteral RPAREN 
	'''
	revoutput.append(p.slice)
  
def p_relExpression():
  '''
      relExpression: shiftExpression | relExpression relOperator shiftExpression

  '''
  revoutput.append(p.slice)  

def p_relOperator():
  '''
      relOperator: LESS | LESSEQ | GREATER | GREATER_EQ | IS_EQ_DIFF | NOT_EQ_DIFF | LESS_EQ_DIFF
      | LESS_DIFF | GREATER_EQ__DIFF |  GREATER_DIFF

  '''
  revoutput.append(p.slice)

def returnStatement():
  '''
      returnStatement: RETURN expression? SEMICOLON
  '''
  revoutput.append(p.slice)

def shiftExpression():
  ''' 
      shiftExpression: addExpression | shiftExpression ( LEFTSHIFT | RIGHTSHIFT ) addExpression
  '''
  revoutput.append(p.slice)

def p_singleImport():
  '''
      singleImport: ( IDENTIFIER ASSIGN )? identifierChain
  '''
  revoutput.append(p.slice)

def p_statement():
  '''
      statement: statementNoCaseNoDefault | caseStatement | caseRangeStatment | defaultStatement
  '''
  revoutput.append(p.slice)
  
def statementNoCaseNoDefault():
  '''
      statementNoCaseNoDefault: labeledStatement | blockStatement | ifStatement | whileStatement | doStatement | forStatement | foreachStatement | switchStatement | finalSwitchStatement | continueStatement | breakStatement | returnStatement | gotoStatement | withStatement | conditionalStatement | expressionStatement
  '''
  revoutput.append(p.slice)
  
def p_storageClass(p):
    ''' storageClass : typeConstructor | ’AUTO’ | ’ENUM’ | ’EXTERN’ | ’FINAL’ | ’STATIC’
    '''
    revoutput.append(p.slice)
 

def p_statement():
  '''
      statement: statementNoCaseNoDefault | caseStatement | caseRangeStatment | defaultStatement
  '''
  revoutput.append(p.slice)
  
def statementNoCaseNoDefault():
    '''
        statementNoCaseNoDefault: labeledStatement | blockStatement | ifStatement | whileStatement | doStatement | forStatement | foreachStatement | switchStatement | finalSwitchStatement | continueStatement | breakStatement | returnStatement | gotoStatement | withStatement | conditionalStatement | expressionStatement
    '''
    revoutput.append(p.slice)
    
def p_storageClass(p):
    ''' 
        storageClass : typeConstructor | ’AUTO’ | ’ENUM’ | ’EXTERN’ | ’FINAL’ | ’STATIC’
    '''
    revoutput.append(p.slice)
 
def p_structBody():
    '''
	structBody: LBRACE declaration* RBRACE
    '''
    revouput.append(p.slice)
def p_switchStatement():
    '''
        switchStatement: SWITCH LBRACKET expression RBRACKET statement ......
    '''
    revoutput.append(p.slice)

def p_ternaryExpression():
    '''
        ternaryExpression: orOrExpression ( '?' expression COLON ternaryExpression )? 
    '''
    revoutput.append(p.slice)


def p_type():
    '''
        type : typeConstructors? type2 typeSuffix*
    '''
    revoutput.append(p.slice)    

def p_type2():
    '''
        type2 : builtinType | symbol | typeofExpression ( DOT identifierOrTemplateChain )? | typeConstructor LBRACKET TYPEDEF RBRACKET 
    '''
    revoutput.append(p.slice)    


def p_typeConstructor():
    '''
        typeConstructor : 'CONST' | 'IMMUTABLE'
    '''
    revoutput.append(p.slice)    

def p_typeConstructors():
    '''       
        typeConstructors : typeConstructor | typeConstructor typeConstructors
    '''
    revoutput.append(p.slice)    

def p_typeSpecialization():
    ''' typeSpecialization : type | ’UNION’ | ’CLASS’ | ’ENUM’ | ’FUNCTION’ | ’CONST’ | ’IMMUTABLE’ | ’RETURN’ | ’TYPEDEF’
    '''
    revoutput.append(p.slice)    

def p_typeSuffix():
    '''       
        typeSuffix : '*' | LBRACKET type? RBRACKET | LBRACKET assignExpression RBRACKET | LBRACKET assignExpression RANGE assignExpression RBRACKET |
        ( DELEGATE | FUNCTION ) parameters multiple_memberFunctionAttribute SEMICOLON typeidExpression COLON TYPEID LBRACKET ( TYPEDEF | expression ) RBRACKET 
        SEMICOLON typeofExpression COLON TYPEOF LBRACKET ( expression | RETURN ) RBRACKET 
    '''
    revoutput.append(p.slice)    

def p_unaryExpression():
    '''       
        unaryExpression: primaryExpression | AMPERSAND unaryExpression | '!' unaryExpression | TIMES unaryExpression | PLUS unaryExpression | 
        MINUS unaryExpression | . |  PLUS_PLUS unaryExpression  | ... | newExpression | deleteExpression | castExpression | functionCallExpression |
        indexExpression } LBRACKET TYPEDEF RBRACKET DOT identifierOrTemplateInstance | unaryExpression DOT newExpression | unaryExpression DOT 
        identifierOrTemplateInstance | .. | unaryExpression PLUS_PLUS

    '''
    revoutput.append(p.slice)    

def p_unionDeclaration():
    '''
        unionDeclaration: UNION Idefntifier templateParameters constraint? structBody | UNION IDENTIFIER ( structBody | SEMICOLON ) | UNION structBody 
    '''
    revoutput.append(p.slice)    

def p_variableDeclaration():
    '''
	variableDeclaration: multiplestorageClass TYPEDEF declarator ( COMMA declarator )* SEMICOLON | multiplestorageClass TYPEDEF IDENTIFIER ASSIGN functionBody SEMICOLOON 
	| autoDeclaration
    '''
    revoutput.append(p.slice)    

def p_whileStatement():
	'''
	whileStatement: WHILE LBRACKET expression RBRACKET declarationOrStatement
  	'''
	revouput.append(p.slice)  
def p_withStatement():
	'''
	withStatement: WITH LBRACKET expression RBRACKET statementNoCaseNoDefault
	'''
	revouput.slice(p)

def xorExpression():
	''' storageClass :andExpression | <xorExpression> ’ˆ’ <andExpression>
	'''
	revoutput.append(p.slice)

yacc.yacc()
    