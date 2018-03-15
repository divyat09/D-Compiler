import ply.lex as lex
import sys
import ply.yacc as yacc
from lexer import tokens
import logging

revoutput = []

def p_addExpression(p) : 
	''' addExpression : mulExpression 
    				| addExpression PLUS mulExpression 
					| addExpression MINUS mulExpression 
					| addExpression TILDE mulExpression
	'''
	revoutput.append(p.slice)

def p_aliasDeclaration(p): 
	''' aliasDeclaration : ALIAS aliasInitializer comma_aliasInitializer SEMICOLON 
						 | ALIAS multiplestorageClass type identifierList SEMICOLON
	'''
	revoutput.append(p.slice)



def p_comma_aliasInitializer(p):
    ''' comma_aliasInitializer : COMMA aliasInitializer comma_aliasInitializer
                              | empty
    '''
    revouput.append(p.slice)


def p_multiplestorageClass(p):
    ''' multiplestorageClass : storageClass multiplestorageClass
                             | empty
    '''
    revouput.slice(p)

def p_aliasInitializer(p):
    ''' aliasInitializer : Identifier ASSIGN multiplestorageClass type 
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
    ''' andAndExpression : orExpression 
                        | andAndExpression DOUBLE_AMPERSAND orExpression
    '''
    revoutput.append(p.slice)
def p_andExpression(p): 
    ''' andExpression : cmpExpression 
                     | andExpression AMPERSAND cmpExpression
    '''
    revoutput.append(p.slice)

def p_argumentList(p): 
    ''' argumentList : assignExpression 
                    | argumentList comma_assign
    '''
    revoutput.append(p.slice)

def p_comma_assign(p):
    ''' comma_assign : COMMA assignExpression comma_assign
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
    ''' arrayMemberInitialization : assignExpression COLON nonVoidInitializer 
                                 | nonVoidInitializer
    '''
    revoutput.append(p.slice)

def p_assignExpression(p):
    ''' assignExpression : ternaryExpression 
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
    ''' attribute : PRIVATE 
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

def p_comma_identifier_assign_initializer(p):
    ''' comma_identifier_assign_initializer : COMMA Identifier ASSIGN initializer comma_identifier_assign_initializer
                                           | empty
    '''
    revouput.slice(p)   

def p_blockStatement(p):
    ''' blockStatement : LBRACE RBRACE 
                      | LBRACE declarationsAndStatements RBRACE
    ''' 
    revouput.slice(p)

def p_bodyStatement(p):
    ''' bodyStatement : BODY blockStatement 
    '''
    revoutput.append(p.slice)
          
def p_breakStatement(p):
    ''' breakStatement : BREAK SEMICOLON 
                       | BREAK IDENTIFIER SEMICOLON 
    '''
    revoutput.append(p.slice)

def p_baseClass(p):
    ''' baseClass : type2 
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
    ''' castExpression : CAST LPAREN RPAREN unaryExpression
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

def p_multiple_memberFunctionAttribute(p):
    ''' multiple_memberFunctionAttribute : memberFunctionAttribute multiple_memberFunctionAttribute
                                        | empty
    '''
    revouput.slice(p)

def p_continueStatement(p):
    ''' continueStatement : CONTINUE SEMICOLON
                          | CONTINUE Identifier SEMICOLON
    '''
    revoutput.append(p.slice)

def p_declaration(p):
	''' declaration : multipleattributes declaration2 
					| attribute multipleattributes LBRACE multiple_declaration RBRACE 
	'''
	revoutput.append(p.slice)

def p_multiple_declaration(p):
	''' multiple_declaration : declaration multiple_declaration
							 | empty
	'''
	revouput.append(p.slice)

def p_multipleattributes(p):
    ''' multipleattributes : attribute multipleattributes
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
    ''' deleteExpression : DELETE unaryExpression
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

def p_comma_enumMember(p):
    ''' comma_enumMember : COMMA enumMember comma_enumMember
                        | empty
    '''
    revouput.slice(p)

def p_anonymousEnumMember(p):
    ''' anonymousEnumMember : TYPEDEF IDENTIFIER ASSIGN assignExpression 
                           | IDENTIFIER ASSIGN assignExpression 
                           | IDENTIFIER
    '''
    revoutput.append(p.slice)

def anonymousEnumDeclaration(p):
    ''' anonymousEnumDeclaration : ENUM LBRACE anonymousEnumMember multipleanonymousEnumMember  RBRACE
                               | ENUM COLON type LBRACE anonymousEnumMember multipleanonymousEnumMember RBRACE
    '''
    revouput.slice(p)

def p_multipleanonymousEnumMember(p):
    ''' multipleanonymousEnumMember : anonymousEnumMember multipleanonymousEnumMember
                                   | empty
    '''
    revouput.slice(p)

def p_enumDeclaration(p):
    ''' enumDeclaration : ENUM IDENTIFIER SEMICOLON
                       | ENUM IDENTIFIER COLON TYPEDEF SEMICOLON
                       | ENUM IDENTIFIER COLON TYPEDEF enumBody
    '''
    revoutput.append(p.slice)

def p_enumMember(p):
    ''' enumMember : IDENTIFIER
                  | IDENTIFIER ASSIGN assignExpression
      '''
    revoutput.append(p.slice)
  
def p_equalExpression(p):
    ''' equalExpression : shiftExpression IS_EQ shiftExpression
                      | shiftExpression NOT_EQ shiftExpression 
    '''
    revoutput.append(p.slice)

def p_expression(p):
    ''' expression : assignExpression 
                  | expression COMMA assignExpression
    '''
    revoutput.append(p.slice)

def p_expressionStatement(p):
    ''' expressionStatement : expression SEMICOLON
    '''
    revouput.slice(p)

def p_forStatement(p):
    ''' forStatement : FOR LPAREN declaration SEMICOLON RPAREN declarationOrStatement
                    | FOR LPAREN statementNoCaseNoDefault SEMICOLON RPAREN declarationOrStatement
                    | FOR LPAREN declaration SEMICOLON expression RPAREN declarationOrStatement
                    | FOR LPAREN statementNoCaseNoDefault SEMICOLON expression RPAREN declarationOrStatement
                    | FOR LPAREN declaration expression SEMICOLON RPAREN declarationOrStatement
                    | FOR LPAREN statementNoCaseNoDefault expression SEMICOLON RPAREN declarationOrStatement
                    | FOR LPAREN declaration expression SEMICOLON expression RPAREN declarationOrStatement  
                    | FOR LPAREN statementNoCaseNoDefault expression SEMICOLON expression RPAREN declarationOrStatement                      
    '''
    revouput.slice(p)


def p_foreachStatement(p):
    ''' foreachStatement : FOREACH LPAREN foreachTypeList SEMICOLON expression RPAREN declarationOrStatement 
                         | FOREACH LPAREN foreachType SEMICOLON expression RANGE expression RBRACKET declarationOrStatement 
                         | FOREACH_REVERSE LPAREN foreachTypeList SEMICOLON expression RPAREN declarationOrStatement 
                         | FOREACH_REVERSE LPAREN foreachType SEMICOLON expression RANGE expression RPAREN declarationOrStatement 
    '''
    revouput.slice(p)

def p_foreachType(p):
  '''
      foreachType : IDENTIFIER 
	  			  | type IDENTIFIER
				  | typeConstructors IDENTIFIER
				  | typeConstructors type IDENTIFIER 
  '''
  revoutput.append(p.slice)  

def p_foreachTypeList(p):
	''' foreachTypeList : foreachType 
			  			| foreachTypeList COMMA foreachType
	'''
	revoutput.append(p.slice)

def p_functionBody(p):
    ''' functionBody : blockStatement
    '''
    revoutput.append(p.slice)

def p_functionCallExpression(p):
	''' functionCallExpression : symbol arguments unaryExpression arguments
				 			   | type arguments 
	'''
	revoutput.append(p.slice)
         
def p_functionDeclaration(p):
	'''
      functionDeclaration : storageClass multiplestorageClass IDENTIFIER parameters multiple_memberFunctionAttribute SEMICOLON
	  					  | storageClass multiplestorageClass IDENTIFIER parameters multiple_memberFunctionAttribute functionBody 
	  					  | TYPEDEF IDENTIFIER parameters multiple_memberFunctionAttribute SEMICOLON 
						  | TYPEDEF IDENTIFIER parameters multiple_memberFunctionAttribute functionBody 
	  					  | storageClass multiplestorageClass IDENTIFIER templateParameters parameters multiple_memberFunctionAttribute constraint SEMICOLON
	  					  | storageClass multiplestorageClass IDENTIFIER templateParameters parameters multiple_memberFunctionAttribute SEMICOLON 							 
						  | storageClass multiplestorageClass IDENTIFIER templateParameters parameters multiple_memberFunctionAttribute constraint functionBody
						  | storageClass multiplestorageClass IDENTIFIER templateParameters parameters multiple_memberFunctionAttribute functionBody						  
						  | TYPEDEF IDENTIFIER templateParameters parameters multiple_memberFunctionAttribute constraint SEMICOLON
						  | TYPEDEF IDENTIFIER templateParameters parameters multiple_memberFunctionAttribute SEMICOLON
						  | TYPEDEF IDENTIFIER templateParameters parameters multiple_memberFunctionAttribute constraint functionBody
						  | TYPEDEF IDENTIFIER templateParameters parameters multiple_memberFunctionAttribute functionBody
	'''
	revoutput.append(p.slice)

def p_functionLiteralExpression(p):
  	'''
      functionLiteralExpression : FUNCTION parameters multiple_functionAttribute functionBody
	  							| FUNCTION functionBody
	  							| FUNCTION TYPEDEF functionBody
	  							| FUNCTION TYPEDEF parameters multiple_functionAttribute functionBody 								   
	  							| parameters multiple_functionAttribute functionBody 
	  							| functionBody 
								| IDENTIFIER assignExpression 
								| FUNCTION parameters multiple_functionAttribute assignExpression
								| FUNCTION TYPEDEF parameters multiple_functionAttribute assignExpression 
	'''
  	revoutput.append(p.slice)

def p_multiple_functionAttribute(p):
	'''
	multiple_functionAttribute : functionAttribute multiple_functionAttribute
	'''
	revouput.append(p.slice)

def p_gotoStatement(p):
    ''' gotoStatement : GOTO IDENTIFIER SEMICOLON
            | GOTO DEFAULT SEMICOLON
            | GOTO CASE SEMICOLON
            | GOTO CASE expression SEMICOLON
    '''
    revoutput.append(p.slice)

def p_identifierChain(p):
    ''' identifierChain : IDENTIFIER
              | identifierChain DOT IDENTIFIER
    '''
    revoutput.append(p.slice)

def p_identifierList(p):
    ''' identifierList : IDENTIFIER
              | identifierList COMMA IDENTIFIER
    '''
    revoutput.append(p.slice)


def p_identifierOrTemplateChain(p):
	''' identifierList : identifierOrTemplateInstance
			  | identifierOrTemplateChain DOT identifierOrTemplateInstance
	'''
	revoutput.append(p.slice)

def p_identifierOrTemplateInstance(p):
	''' identifierOrTemplateInstance : IDENTIFIER 
									 | templateInstance 
	'''
def p_identityExpression(p):
	''' identityExpression : shiftExpression IS shiftExpression
			     		   | shiftExpression EXCLAMATION IS shiftExpression
	'''
	revoutput.append(p.slice)

def p_ifStatement(p):
	''' ifStatement : IF LPAREN ifCondition RPAREN declarationOrStatement 
					| IF LPAREN ifCondition RPAREN declarationOrStatement ELSE declarationOrStatement
	'''
	revoutput.append(p.slice)

def p_ifCondition(p):
	''' ifCondition : AUTO IDENTIFIER ASSIGN expression 
		        	| TYPEDEF IDENTIFIER ASSIGN expression 
					| expression
	'''
	revoutput.append(p.slice)

def p_importBind(p):
	''' importBind : IDENTIFIER
		       	   | IDENTIFIER ASSIGN IDENTIFIER 
	'''
	revoutput.append(p.slice)

def p_importBindings(p):
	''' importBindings : singleImport COLON importBind
			   		   | singleImport COLON importBind COLON importBind
	'''
	revoutput.append(p.slice)

def p_importDeclaration(p):
	''' importDeclaration : IMPORT singleImport comma_singleImport COMMA importBindings SEMICOLON
						  | IMPORT singleImport comma_singleImport SEMICOLON
			      		  | IMPORT importBindings SEMICOLON
	'''
	revoutput.append(p.slice)

def p_comma_singleImport(p):
	''' comma_singleImport : COMMA singleImport comma_singleImport
						   | empty
	'''
	revoutput.append(p.slice)

def p_index(p):
    ''' index : assignExpression 
              | assignExpression RANGE assignExpression
    '''         
    revoutput.append(p.slice)

def p_indexExpression(p):
	''' indexExpression : unaryExpression LBRACKET RBRACKET 
					    | unaryExpression LBRACKET index comma_index RBRACKET
	'''
	revoutput.append(p.slice)

def p_comma_index(p):
	''' comma_index : COMMA index comma_index
					| empty
	'''
	revouput.append(p.slice)

def p_initializer(p):
	''' initializer : VOID 
					| nonVoidInitializer 
	'''
	revoutput.append(p.slice)

def p_isExpression(p):
	''' isExpression : IS LPAREN type RPAREN
					 | IS LPAREN type identifier RPAREN
					 | IS LPAREN type COLON typeSpecialization RPAREN
					 | IS LPAREN type identifier COLON typeSpecialization RPAREN 					  
					 | IS LPAREN type ASSIGN typeSpecialization RPAREN
					 | IS LPAREN type identifier ASSIGN typeSpecialization RPAREN 					  
					 | IS LPAREN type COLON typeSpecialization COMMA templateParameterList RPAREN
					 | IS LPAREN type identifier COLON typeSpecialization COMMA templateParameterList RPAREN 					  
					 | IS LPAREN type ASSIGN typeSpecialization COMMA templateParameterList RPAREN
					 | IS LPAREN type identifier ASSIGN typeSpecialization COMMA templateParameterList RPAREN 					  
	'''
	revoutput.append(p.slice)

def p_labeledStatement(p):
    ''' labeledStatement : Identifier COLON 
                         |  Identifier COLON declarationOrStatement
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

def p_newAnonClassExpression(p):
    ''' newAnonClassExpression : NEW CLASS arguments baseClassList structBody
							   | NEW CLASS arguments structBody
							   | NEW CLASS baseClassList structBody
							   | NEW CLASS structBody 							    
							   | NEW arguments CLASS structBody
							   | NEW arguments CLASS arguments structBody
							   | NEW arguments CLASS baseClassList structBody
							   | NEW arguments CLASS arguments baseClassList structBody
    '''
    revoutput.append(p.slice)

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
    ''' 
        orOrExpression : andAndExpression
                       | orOrExpression DOUBLE_PIPE andAndExpression
    '''
    revoutput.append(p.slice)

def p_parameterAttributeStar(p):
    '''
        parameterAttributeStar : parameterAttribute parameterAttributeStar
                               | empty
    '''
    revoutput.append(p.slice)

def p_parameter(p):
    ''' 
        parameter : parameterAttributeStar type parameterAttributeStar type Identifier ELLIPSIS parameterAttributeStar type Identifier ASSIGN assignExpression
                  | parameterAttributeStar type parameterAttributeStar type Identifier ELLIPSIS parameterAttributeStar type Identifier
                  | parameterAttributeStar type parameterAttributeStar type Identifier ELLIPSIS parameterAttributeStar type ASSIGN assignExpression
                  | parameterAttributeStar type parameterAttributeStar type Identifier ELLIPSIS parameterAttributeStar type 
                  | parameterAttributeStar type parameterAttributeStar type ELLIPSIS parameterAttributeStar type Identifier ASSIGN assignExpression
                  | parameterAttributeStar type parameterAttributeStar type ELLIPSIS parameterAttributeStar type Identifier
                  | parameterAttributeStar type parameterAttributeStar type ELLIPSIS parameterAttributeStar type ASSIGN assignExpression
                  | parameterAttributeStar type parameterAttributeStar type ELLIPSIS parameterAttributeStar type 
    '''
    revoutput.append(p.slice)

def p_parameterAttribute(p):
    ''' 
        parameterAttribute : typeConstructor 
                           | FINAL 
                           | OUT 
                           | AUTO 
                           | RETURN
    '''
    revoutput.append(p.slice)

def CommaParameterStar(p):
  ''' 
        CommaParameterStar : COMMA parameter CommaParameterStar
                           | empty      
  '''
  revoutput.append(p.slice)


def p_parameters(p):
    ''' 
        parameters : LPAREN parameter CommaParameterStar COMMA ELLIPSIS RPAREN 
                   | LPAREN parameter CommaParameterStar RPAREN   
                   | LPAREN ELLIPSIS RPAREN 
                   | LPAREN RPAREN
    '''
    revoutput.append(p.slice)

def p_postblit(p):
    ''' 
        postblit : THIS LPAREN THIS RPAREN multiple_memberFunctionAttribute functionBody
                 | THIS LPAREN THIS RPAREN multiple_memberFunctionAttribute SEMICOLON
    '''
    revoutput.append(p.slice)

def p_powExpression(p):
    ''' 
      powExpression : unaryExpression 
                      | powExpression DOUBLEXOR unaryExpression 
    '''
    revoutput.append(p.slice)

def StringLiteralPlus(p):
  '''
      StringLiteralPlus: StringLiteral StringLiteralPlus | StringLiteral
  '''
  revoutput.append(p.slice)

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
                          | StringLiteralPlus
                          | CharacterLiteral
    '''
    revoutput.append(p.slice)

def p_register(p):
    ''' register : Identifier 
                 | Identifier LPAREN IntegerLiteral RPAREN 
    '''
    revoutput.append(p.slice)
  
def p_relExpression(p):
  '''
      relExpression : shiftExpression 
                    | relExpression relOperator shiftExpression

  '''
  revoutput.append(p.slice)  

def p_relOperator(p):
  '''
      relOperator : LESS 
                  | LESSEQ 
                  | GREATER 
                  | GREATER_EQ 
                  | IS_EQ_DIFF 
                  | NOT_EQ_DIFF 
                  | LESS_EQ_DIFF
                  | LESS_DIFF 
                  | GREATER_EQ__DIFF 
                  | GREATER_DIFF

  '''
  revoutput.append(p.slice)

def returnStatement(p):
  '''
      returnStatement : RETURN expression? SEMICOLON
  '''
  revoutput.append(p.slice)

def shiftExpression(p):
  ''' 
      shiftExpression : addExpression | shiftExpression ( LEFTSHIFT | RIGHTSHIFT ) addExpression
  '''
  revoutput.append(p.slice)

def p_singleImport(p):
  '''
      singleImport : IDENTIFIER ASSIGN identifierChain
                   | identifierChain
  '''
  revoutput.append(p.slice)
  
def statementNoCaseNoDefault(p):
  '''
      statementNoCaseNoDefault : labeledStatement | blockStatement | ifStatement | whileStatement | doStatement | forStatement | foreachStatement | switchStatement | finalSwitchStatement | continueStatement | breakStatement | returnStatement | gotoStatement | withStatement | conditionalStatement | expressionStatement
  '''
  revoutput.append(p.slice)

def p_statement(p):
  '''
      statement : statementNoCaseNoDefault 
                | caseStatement 
                | caseRangeStatment 
                | defaultStatement
  '''
  revoutput.append(p.slice)
  
def statementNoCaseNoDefault(p):
    '''
        statementNoCaseNoDefault : labeledStatement | blockStatement | ifStatement | whileStatement | doStatement | forStatement | foreachStatement | switchStatement | finalSwitchStatement | continueStatement | breakStatement | returnStatement | gotoStatement | withStatement | conditionalStatement | expressionStatement
    '''
    revoutput.append(p.slice)
    
def p_storageClass(p):
    ''' 
        storageClass : typeConstructor 
                     | AUTO 
                     | ENUM 
                     | EXTERN 
                     | FINAL 
                     | STATIC
    '''
    revoutput.append(p.slice)

def p_declarationStar(p):
    '''
        declarationStar : declaration declarationStar
                        | empty 
    '''
    revoutput.append(p.slice)
 
def p_structBody(p):
    '''
    structBody : LBRACE declarationStar RBRACE
    '''
    revouput.append(p.slice)
def p_switchStatement(p):
    '''
        switchStatement : SWITCH LBRACKET expression RBRACKET statement
    '''
    revoutput.append(p.slice)

def p_symbol(p):
    '''
        symbol : DOT identifierOrTemplateChain
              | identifierOrTemplateChain
    '''
    revoutput.append(p.slice)

def p_ternaryExpression(p):
    '''
        ternaryExpression : orOrExpression QUESTION expression COLON ternaryExpression
                          | orOrExpression
    '''
    revoutput.append(p.slice)

def p_typeSuffixStar(p):
    '''
        typeSuffixStar : typeSuffix typeSuffixStar 
        | empty 
    '''
    revoutput.append(p);

def p_type(p):
    '''
        type : typeConstructors type2 typeSuffixStar
             | type2 typeSuffixStar
    '''
    revoutput.append(p.slice)    

def p_type2(p):
    '''
        type2 : builtinType 
              | symbol 
              | typeofExpression DOT identifierOrTemplateChain
              | typeofExpression   
              | typeConstructor LBRACKET TYPEDEF RBRACKET 
    '''
    revoutput.append(p.slice)    


def p_typeConstructor(p):
    '''
        typeConstructor : CONST 
                        | IMMUTABLE
    '''
    revoutput.append(p.slice)    

def p_typeConstructors(p):
    '''       
        typeConstructors : typeConstructor 
                         | typeConstructor typeConstructors
    '''
    revoutput.append(p.slice)    

def p_typeSpecialization(p):
    ''' typeSpecialization : type 
                           | UNION 
                           | CLASS 
                           | ENUM 
                           | FUNCTION 
                           | CONST 
                           | IMMUTABLE 
                           | RETURN 
                           | TYPEDEF
    '''
    revoutput.append(p.slice)    

def p_typeSuffix(p):
    '''       
        typeSuffix : TIMES 
                   | LBRACKET type RBRACKET
                   | LBRACKET RBRACKET 
                   | LBRACKET assignExpression RBRACKET 
                   | LBRACKET assignExpression RANGE assignExpression RBRACKET
                   | DELEGATE parameters multiple_memberFunctionAttribute SEMICOLON typeidExpression COLON TYPEID LBRACKET TYPEDEF RBRACKET
                   | DELEGATE parameters multiple_memberFunctionAttribute SEMICOLON typeidExpression COLON TYPEID LBRACKET expression RBRACKET
                   | FUNCTION  parameters multiple_memberFunctionAttribute SEMICOLON typeidExpression COLON TYPEID LBRACKET TYPEDEF RBRACKET
                   | FUNCTION  parameters multiple_memberFunctionAttribute SEMICOLON typeidExpression COLON TYPEID LBRACKET expression RBRACKET
                   | SEMICOLON typeofExpression COLON TYPEOF LBRACKET expression RBRACKET 
                   | SEMICOLON typeofExpression COLON TYPEOF LBRACKET RETURN RBRACKET 
    '''   
    revoutput.append(p.slice)    

def p_unaryExpression(p):
    '''       
        unaryExpression : primaryExpression 
                        | AMPERSAND unaryExpression 
                        | EXCLAMATION unaryExpression 
                        | TIMES unaryExpression 
                        | PLUS unaryExpression
                        | MINUS unaryExpression 
                        | DOT 
                        | PLUS_PLUS unaryExpression  
                        | ELIPSIS 
                        | newExpression 
                        | deleteExpression 
                        | castExpression 
                        | functionCallExpression 
                        | indexExpression 
                        | LBRACKET TYPEDEF RBRACKET DOT identifierOrTemplateInstance 
                        | unaryExpression DOT newExpression 
                        | unaryExpression DOT 
                        | identifierOrTemplateInstance 
                        | RANGE 
                        | unaryExpression PLUS_PLUS

    '''
    revoutput.append(p.slice)    



def p_unionDeclaration(p):
    '''
        unionDeclaration : UNION Idefntifier templateParameters structBody 
                         | UNION Idefntifier templateParameters constraint structBody 
                         | UNION IDENTIFIER structBody 
                         | UNION IDENTIFIER SEMICOLON 
                         | UNION structBody 
    '''
    revoutput.append(p.slice)    

def p_CommaDeclarator(p):
    '''
        CommaDeclarator : COMMA declarator CommaDeclarator 
                        | empty
    '''
    revoutput.append(p.slice)

def p_variableDeclaration(p):
    '''
    variableDeclaration : multiplestorageClass TYPEDEF declarator CommaDeclarator SEMICOLON 
                        | multiplestorageClass TYPEDEF IDENTIFIER ASSIGN functionBody SEMICOLOON 
                        | autoDeclaration
    '''
    revoutput.append(p.slice)    

def p_whileStatement(p):
    '''
    whileStatement : WHILE LBRACKET expression RBRACKET declarationOrStatement
    '''
    revouput.append(p.slice)  
def p_withStatement(p):
    '''
    withStatement : WITH LBRACKET expression RBRACKET statementNoCaseNoDefault
    '''
    revouput.slice(p)

def xorExpression(p):
    ''' storageClass :andExpression | xorExpression CARET andExpression
    '''
    revoutput.append(p.slice)

def p_empty(p):
    'empty :'
    pass

yacc.yacc()
