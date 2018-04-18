import ply.lex as lex
import sys
import ply.yacc as yacc
from lexer import tokens
import logging

revoutput = []


def p_CompilationUnit(p):
    ''' CompilationUnit : ProgramFile
    '''
    print p.slice 

def p_ProgramFile(p):
    ''' ProgramFile : multiple_declaration
    '''
    print p.slice

def p_addExpression(p) : 
  ''' addExpression : mulExpression 
                | addExpression PLUS mulExpression 
                | addExpression MINUS mulExpression 
                | addExpression TILDE mulExpression
  '''
  print p.slice 

def p_aliasDeclaration(p): 
  ''' aliasDeclaration : ALIAS aliasInitializer comma_aliasInitializer SEMICOLON 
                       | ALIAS multiplestorageClass type declaratorIdentifierList SEMICOLON
                       | ALIAS multiplestorageClass type IDENTIFIER LPAREN parameters RPAREN multiple_memberFunctionAttribute SEMICOLON
  '''
  print p.slice 

def p_comma_aliasInitializer(p):
    ''' comma_aliasInitializer : COMMA aliasInitializer comma_aliasInitializer
                               | empty
    '''
    print p.slice 


def p_multiplestorageClass(p):
    ''' multiplestorageClass : storageClass multiplestorageClass
                             | empty
    '''
    print p.slice 

def p_aliasInitializer(p):
    ''' aliasInitializer : IDENTIFIER ASSIGN multiplestorageClass type 
                        | IDENTIFIER ASSIGN functionLiteralExpression SEMICOLON
    '''
    print p.slice 
          
def p_aliasThisDeclaration(p): 
    ''' aliasThisDeclaration : ALIAS IDENTIFIER THIS SEMICOLON
    '''
    print p.slice 
          
def p_andAndExpression(p): 
    ''' andAndExpression : orExpression 
                        | andAndExpression DOUBLE_AMPERSAND orExpression
    '''
    print p.slice 

def p_andExpression(p): 
    ''' andExpression : cmpExpression 
                     | andExpression AMPERSAND cmpExpression
    '''
    print p.slice 

def p_argumentList(p): 
    ''' argumentList : assignExpression comma_assign
    '''
    print p.slice 

def p_comma_assign(p):
    ''' comma_assign : COMMA assignExpression_question comma_assign
                      | empty
    '''
    print p.slice 

def p_assignExpression_question(p):
    ''' assignExpression_question : assignExpression 
                                  | empty

    '''
    print p.slice

def p_arguments(p): 
    ''' arguments : LPAREN argumentList_question RPAREN
    ''' 
    print p.slice 

def p_argumentList_question(p):
  ''' argumentList_question : argumentList
                | empty
  '''
  print p.slice

def p_arrayInitializer(p):
    ''' arrayInitializer : LBRACKET RBRACKET 
                         | LBRACKET arrayMemberInitialization comma_arrayMemberInitialization RBRACKET 
    '''
    print p.slice 

def p_comma_arrayMemberInitialization(p):
    ''' comma_arrayMemberInitialization : COMMA arrayMemberInitialization comma_arrayMemberInitialization
                                        | empty
    '''
    print p.slice 


def p_arrayLiteral(p):
    ''' arrayLiteral : LBRACKET argumentList_question RBRACKET
    '''
    print p.slice 
          
def p_arrayMemberInitialization(p): 
    ''' arrayMemberInitialization : assignExpression COLON nonVoidInitializer 
                                  | nonVoidInitializer
    '''
    print p.slice 

def p_assignExpression(p):
    ''' assignExpression : ternaryExpression 
                        | ternaryExpression assignOperator expression
    '''
    print p.slice 

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
    print p.slice 

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
    print p.slice 

def p_attributeDeclaration(p):
    ''' attributeDeclaration : attribute COLON
    '''
    print p.slice 

def p_autoDeclaration(p):
    ''' autoDeclaration : storageClass multiplestorageClass autoDeclarationPart comma_identifier_assign_initializer SEMICOLON
    '''
    print p.slice 

def p_autoDeclarationPart(p):
    '''
        autoDeclarationPart : IDENTIFIER ASSIGN initializer
    '''
    print p.slice

def p_comma_identifier_assign_initializer(p):
    ''' comma_identifier_assign_initializer : COMMA autoDeclarationPart comma_identifier_assign_initializer
                                           | empty
    '''
    print p.slice    

def p_blockStatement(p):
    ''' blockStatement : LBRACE RBRACE 
                      | LBRACE declarationsAndStatements RBRACE
    ''' 
    print p.slice 

def p_bodyStatement(p):
    ''' bodyStatement : BODY blockStatement 
    '''
    print p.slice 
          
def p_breakStatement(p):
    ''' breakStatement : BREAK SEMICOLON 
                       | BREAK IDENTIFIER SEMICOLON 
    '''
    print p.slice 

def p_baseClass(p):
    ''' baseClass : type2 
    '''
    print p.slice 

def p_baseClassList(p): 
    ''' baseClassList : baseClass comma_baseclass_multiple
    '''
    print p.slice 
          
def p_comma_baseclass_multiple(p):
    ''' 
        comma_baseclass_multiple : COMMA baseClass comma_baseclass_multiple
                                 | empty
     '''
    print p.slice

def p_builtinType(p):
    ''' builtinType : BOOL 
                    | SHORT 
                    | USHORT 
                    | INT
                    | UINT 
                    | LONG 
                    | ULONG 
                    | CHAR
                    | FLOAT 
    '''
    print p.slice    

def p_caseRangeStatement(p):
    ''' caseRangeStatement : CASE assignExpression COLON ELLIPSIS CASE assignExpression COLON declarationsAndStatements
    '''
    print p.slice 

def p_caseStatement(p):
    ''' caseStatement : CASE argumentList COLON declarationsAndStatements
    '''
    print p.slice  

def p_castExpression(p):
    ''' castExpression : CAST LPAREN type_question RPAREN unaryExpression
                       | CAST LPAREN castQualifier_question RPAREN unaryExpression 
    '''
    print p.slice 
    
def p_castQualifier_question(p):
  ''' castQualifier_question : castQualifier
                   | empty
    '''
  print p.slice

def p_castQualifier(p):
    ''' castQualifier : CONST 
                      | IMMUTABLE 
    '''
    print p.slice 

def p_classDeclaration(p):
    ''' classDeclaration : CLASS IDENTIFIER SEMICOLON 
                         | CLASS IDENTIFIER COLON baseClassList structBody
                         | CLASS IDENTIFIER structBody
    '''
    print p.slice 
 
def p_cmpExpression(p):
    ''' cmpExpression : shiftExpression 
                      | equalExpression
                      | relExpression
    '''
    print p.slice 
  
def p_shiftExpression(p):
  ''' shiftExpression : addExpression
              | shiftExpression RIGHT_SHIFT addExpression
              | shiftExpression LEFT_SHIFT addExpression
  '''
  print p.slice 

def p_constraint(p):
    ''' constraint : IF LPAREN expression RPAREN
    '''
    print p.slice 

def p_constructor(p):
    ''' constructor : THIS parameters multiple_memberFunctionAttribute functionBody 
                    | THIS parameters multiple_memberFunctionAttribute SEMICOLON
                    | THIS parameters multiple_memberFunctionAttribute constraint functionBody 
                    | THIS parameters multiple_memberFunctionAttribute constraint SEMICOLON
    '''
    print p.slice 

def p_multiple_memberFunctionAttribute(p):
    ''' multiple_memberFunctionAttribute : memberFunctionAttribute multiple_memberFunctionAttribute
                                        | empty
    '''
    print p.slice 

def p_continueStatement(p):
    ''' continueStatement : CONTINUE SEMICOLON
                          | CONTINUE IDENTIFIER SEMICOLON
    '''
    print p.slice 

def p_declaration(p):
  ''' declaration : multipleattributes declaration2 
          | attribute multipleattributes LBRACE multiple_declaration RBRACE 
  '''
  print p.slice 

def p_multiple_declaration(p):
  ''' multiple_declaration : declaration multiple_declaration
               | empty
  '''
  print p.slice 

def p_multipleattributes(p):
    ''' multipleattributes : attribute multipleattributes
                           | empty
    '''
    print p.slice

def p_declaration2(p):
    ''' declaration2 : aliasDeclaration 
                     | aliasThisDeclaration 
                     | anonymousEnumDeclaration 
                     | attributeDeclaration 
                     | classDeclaration 
                     | constructor 
                     | destructor 
                     | enumDeclaration 
                     | functionDeclaration 
                     | importDeclaration 
                     | mixinDeclaration 
                     | unionDeclaration 
                     | variableDeclaration 
    '''
    print p.slice 

def p_declarationsAndStatements(p):
    ''' declarationsAndStatements : declarationOrStatement declarationOrStatementmultiple
    '''
    print p.slice 

def p_declarationOrStatementmultiple(p):
  ''' 
      declarationOrStatementmultiple : declarationOrStatement declarationOrStatementmultiple
                                     | empty
  '''
  print p.slice

def p_declarationOrStatement(p):
    ''' declarationOrStatement : declaration 
                               | statement 
    '''
    print p.slice 

def p_declarator(p):
    ''' declarator : IDENTIFIER 
                   | IDENTIFIER ASSIGN initializer 
    '''
    print p.slice 

def p_declaratorIdentifierList(p):
    ''' 
      declaratorIdentifierList : IDENTIFIER multiple_comma_identifer
    '''
    print p.slice 

def p_multiple_comma_identifer(p):
    ''' multiple_comma_identifer : COMMA IDENTIFIER multiple_comma_identifer
                   | empty
    '''
    print p.slice

def p_defaultStatement(p):
    ''' defaultStatement : DEFAULT COLON declarationsAndStatements
    '''
    print p.slice 

def p_deleteExpression(p): 
    ''' deleteExpression : DELETE unaryExpression
    '''
    print p.slice 

def p_destructor(p):
    ''' destructor : TILDE THIS LPAREN RPAREN multiple_memberFunctionAttribute functionBody 
                   | TILDE THIS LPAREN RPAREN multiple_memberFunctionAttribute SEMICOLON
    '''
    print p.slice 

def p_doStatement(p):
    ''' doStatement : DO statementNoCaseNoDefault WHILE LPAREN expression RPAREN SEMICOLON
    '''
    print p.slice 
    
def p_enumBody(p):
    ''' enumBody : LBRACE enumMember comma_enumMember  RBRACE

    '''
    print p.slice 

def p_comma_enumMember(p):
    ''' comma_enumMember : COMMA enumMember comma_enumMember
                        | empty
    '''
    print p.slice 

def p_anonymousEnumMember(p):
    ''' anonymousEnumMember : type IDENTIFIER ASSIGN assignExpression 
                           | IDENTIFIER ASSIGN assignExpression 
                           | IDENTIFIER
    '''
    print p.slice 

def p_COMMA_TYPE_Question(p):
  '''
    COMMA_TYPE_Question : empty 
              | COLON type
  '''
  print p.slice

def p_multipleanonymousEnumMember(p):
    ''' multipleanonymousEnumMember : anonymousEnumMember multipleanonymousEnumMember
                                    | empty
    '''
    print p.slice 

def p_anonymousEnumDeclaration(p):
    ''' anonymousEnumDeclaration : ENUM COMMA_TYPE_Question LBRACE anonymousEnumMember multipleanonymousEnumMember RBRACE
    '''
    print p.slice 

def p_enumDeclaration(p):
    ''' enumDeclaration : ENUM IDENTIFIER COMMA_TYPE_Question SEMICOLON
                       | ENUM IDENTIFIER COMMA_TYPE_Question enumBody
    '''
    print p.slice 

def p_enumMember(p):
    ''' enumMember : IDENTIFIER
                  | IDENTIFIER ASSIGN assignExpression
      '''
    print p.slice 
  
def p_equalExpression(p):
    ''' equalExpression : shiftExpression IS_EQ shiftExpression
                      | shiftExpression NOT_EQ shiftExpression 
    '''
    print p.slice 

def p_expression(p):
    ''' expression : assignExpression assignExpression_multiple
    '''
    print p.slice 

def p_assignExpression_multiple(p):
    '''
        assignExpression_multiple : COMMA assignExpression assignExpression_multiple
                                  | empty
    '''
    print p.slice

def p_expressionStatement(p):
    ''' expressionStatement : expression SEMICOLON
    '''
    print p.slice 


def p_forStatement(p):
  ''' forStatement : FOR LPAREN declaration expression_question SEMICOLON expression_question RPAREN declarationOrStatement
                   | FOR LPAREN statementNoCaseNoDefault expression_question SEMICOLON expression_question RPAREN declarationOrStatement
  '''
  print p.slice

def p_expression_question(p):
  ''' expression_question : expression
              | empty
  '''
  print p.slice

def p_foreachStatement(p):
    ''' foreachStatement : FOREACH LPAREN foreachTypeList SEMICOLON expression RPAREN declarationOrStatement 
                         | FOREACH LPAREN foreachType SEMICOLON expression RANGE expression RBRACKET declarationOrStatement 
                         | FOREACH_REVERSE LPAREN foreachTypeList SEMICOLON expression RPAREN declarationOrStatement 
                         | FOREACH_REVERSE LPAREN foreachType SEMICOLON expression RANGE expression RPAREN declarationOrStatement 
    '''
    print p.slice 

def p_typeConstructorStar(p):
  ''' typeConstructorStar : typeConstructor typeConstructorStar 
                | empty
  '''
  print p.slice
  
def p_foreachType(p):
  '''
      foreachType :  typeConstructorStar type_question  IDENTIFIER 
  '''
  print p.slice   

def p_foreachTypeList(p):
  ''' foreachTypeList : foreachType foreachType_multiple
  '''
  print p.slice 

def p_foreachType_multiple(p):
  ''' 
      foreachType_multiple : COMMA foreachType foreachType_multiple
                           | empty
  '''
  print p.slice

def p_functionBody(p):
    ''' functionBody : blockStatement
    '''
    print p.slice 

def p_functionCallExpression(p):
  ''' functionCallExpression : symbol arguments 
                             | unaryExpression arguments
                             | type arguments 
  '''
  print p.slice 
         
def p_functionDeclaration(p):
  '''
      functionDeclaration : storageClass multiplestorageClass IDENTIFIER parameters multiple_memberFunctionAttribute SEMICOLON
                          | storageClass multiplestorageClass IDENTIFIER parameters multiple_memberFunctionAttribute functionBody 
                          | type IDENTIFIER parameters multiple_memberFunctionAttribute SEMICOLON 
                          | type IDENTIFIER parameters multiple_memberFunctionAttribute functionBody 
  '''
  print p.slice 

def p_functionLiteralExpression(p):
    '''
      functionLiteralExpression : FUNCTION type_question functionBody
                                | functionBody 
                                | IDENTIFIER assignExpression 
  '''
    print p.slice 

def p_gotoStatement(p):
  ''' gotoStatement : GOTO IDENTIFIER SEMICOLON
                    | GOTO DEFAULT SEMICOLON
                    | GOTO CASE expression_question SEMICOLON
  '''
  print p.slice

def p_identifierChain(p):
    ''' identifierChain : IDENTIFIER multiple_dot_identifier
    '''
    print p.slice 

def p_multiple_dot_identifier(p):
    ''' multiple_dot_identifier :  DOT IDENTIFIER multiple_dot_identifier
                                | empty
    '''
    print p.slice


def p_typeIdentifierPart(p):
    '''
        typeIdentifierPart : identifierOrTemplateInstance
                           | identifierOrTemplateInstance DOT typeIdentifierPart
                           | identifierOrTemplateInstance LBRACKET assignExpression RBRACKET DOT typeIdentifierPart
    '''
    print p.slice

def p_identifierOrTemplateChain(p):
  ''' 
      identifierOrTemplateChain : identifierOrTemplateInstance  multiple_dot_identifierOrTemplateInstance 
  '''
  print p.slice 
  
def p_multiple_dot_identifierOrTemplateInstance(p):
    ''' multiple_dot_identifierOrTemplateInstance : DOT identifierOrTemplateInstance multiple_dot_identifierOrTemplateInstance
                                                  | empty
    '''
    print p.slice

def p_identifierOrTemplateInstance(p):
  ''' identifierOrTemplateInstance : IDENTIFIER 
  '''

def p_ifStatement(p):
  ''' ifStatement : IF LPAREN ifCondition RPAREN declarationOrStatement 
                  | IF LPAREN ifCondition RPAREN declarationOrStatement ELSE declarationOrStatement
  '''
  print p.slice 
 
def p_ifCondition(p):
  ''' ifCondition : AUTO IDENTIFIER ASSIGN expression 
                  | type IDENTIFIER ASSIGN expression
                  | expression
  '''
  print p.slice 

def p_importBind(p):
  ''' importBind : IDENTIFIER
                 | IDENTIFIER ASSIGN IDENTIFIER 
  '''
  print p.slice 

def p_importBindings(p):
  ''' importBindings : singleImport COLON importBind importBindstr
  '''
  print p.slice 

def p_importBindstr(p):
  ''' importBindstr : COMMA importBind importBindstr
                    | empty
  '''
  print p.slice
  
def p_importDeclaration(p):
  ''' importDeclaration : IMPORT singleImport comma_singleImport COMMA importBindings SEMICOLON
                        | IMPORT singleImport comma_singleImport SEMICOLON
                        | IMPORT importBindings SEMICOLON
  '''
  print p.slice 

def p_comma_singleImport(p):
  ''' comma_singleImport : COMMA singleImport comma_singleImport
               | empty
  '''
  print p.slice 

def p_importExpression(p):
  '''   
     importExpression : IMPORT LBRACKET assignExpression RBRACKET
  '''   
  print p.slice 

def p_index(p):
    ''' index : assignExpression RANGE assignExpression
              | assignExpression 
    '''         
    print p.slice 

def p_indexExpression(p):
  ''' indexExpression : unaryExpression LBRACKET RBRACKET 
              | unaryExpression LBRACKET index comma_index RBRACKET
  '''
  print p.slice 

def p_comma_index(p):
  ''' comma_index : COMMA index comma_index
                  | empty
  '''
  print p.slice 

def p_initializer(p):
  ''' initializer : VOID 
                  | nonVoidInitializer 
  '''
  print p.slice 

def p_labeledStatement(p):
    ''' labeledStatement : IDENTIFIER COLON declarationOrStatement_question
    '''
    print p.slice 

def p_declarationOrStatement_question(p):
    ''' declarationOrStatement_question :  declarationOrStatement 
                                        | empty
    ''' 
    print p.slice

def p_memberFunctionAttribute(p):
    ''' memberFunctionAttribute : IMMUTABLE 
                                | CONST 
                                | RETURN
    '''
    print p.slice 

def p_mixinDeclaration(p):
    ''' mixinDeclaration : mixinExpression SEMICOLON 
    '''
    print p.slice 
    
def p_mixinExpression(p):
    ''' mixinExpression : MIXIN LPAREN assignExpression RPAREN 
    '''
    print p.slice 


def p_mulExpression(p):
    ''' mulExpression : powExpression 
                      | mulExpression TIMES powExpression
                      | mulExpression DIV powExpression
                      | mulExpression MODULO powExpression
    '''
    print p.slice 

def p_newAnonClassExpression(p):
    ''' newAnonClassExpression : NEW arguments_question CLASS arguments_question baseClassList_question structBody
    '''
    print p.slice 

def p_arguments_question(p):
    ''' arguments_question : arguments 
                           | empty 
    '''
    print p.slice 
    
def p_baseClassList_question(p):
    ''' baseClassList_question : baseClassList 
                               | empty
    '''
    print p.slice
    
def p_newExpression(p):
    ''' newExpression : NEW type 
                      | NEW type LBRACKET assignExpression RBRACKET 
                      | NEW type arguments
                      | newAnonClassExpression
    '''
    print p.slice 

def p_nonVoidInitializer(p):
    ''' nonVoidInitializer : assignExpression 
                           | arrayInitializer
    '''
    print p.slice 

def p_orExpression(p):
    ''' orExpression : xorExpression 
                     | orExpression PIPE xorExpression 
    '''
    print p.slice 

def p_orOrExpression(p):
    ''' 
        orOrExpression : andAndExpression
                       | orOrExpression DOUBLE_PIPE andAndExpression
    '''
    print p.slice 

def p_parameterAttributeStar(p):
    '''
        parameterAttributeStar : parameterAttribute parameterAttributeStar
                               | empty
    '''
    print p.slice 

def p_parameter(p):
    ''' 
        parameter : parameterAttributeStar type Identifier_question ELLIPSIS 
                  | parameterAttributeStar type Identifier_question 
                  | parameterAttributeStar type Identifier_question ASSIGN assignExpression
    '''
    print p.slice 

def  p_Identifier_question(p):
  ''' Identifier_question : IDENTIFIER 
                          | empty
  '''
  print p.slice

def p_parameterAttribute(p):
    ''' 
        parameterAttribute : typeConstructor 
                           | FINAL 
                           | AUTO 
                           | RETURN
    '''
    print p.slice 

def p_CommaParameterStar(p):
  ''' 
        CommaParameterStar : COMMA parameter CommaParameterStar
                           | empty      
  '''
  print p.slice 


def p_parameters(p):
    ''' 
        parameters : LPAREN parameter CommaParameterStar COMMA ELLIPSIS RPAREN 
                   | LPAREN parameter CommaParameterStar RPAREN   
                   | LPAREN ELLIPSIS RPAREN 
                   | LPAREN RPAREN
    '''
    print p.slice 


def p_powExpression(p):
    ''' 
      powExpression : unaryExpression 
                    | powExpression POWER unaryExpression 
    '''
    print p.slice 

def p_LIT_STRPlus(p):
  '''
      LIT_STRPlus : LIT_STR LIT_STRPlus
                  | LIT_STR
  '''
  print p.slice 


def p_primaryExpression(p):
    ''' primaryExpression : identifierOrTemplateInstance 
                          | DOT identifierOrTemplateInstance 
                          | typeConstructor LPAREN builtinType RPAREN DOT IDENTIFIER 
                          | builtinType DOT IDENTIFIER 
                          | builtinType arguments 
                          | arrayLiteral 
                          | LPAREN expression RPAREN 
                          | functionLiteralExpression 
                          | mixinExpression 
                          | importExpression 
                          | DOLLAR 
                          | THIS 
                          | NULL 
                          | TRUE 
                          | FALSE 
                          | INUMBER 
                          | DNUMBER
                          | LIT_STRPlus
                          | LIT_CHAR
    '''
    print p.slice 

  
def p_relExpression(p):
  '''
      relExpression : shiftExpression 
                    | relExpression relOperator shiftExpression

  '''
  print p.slice   

def p_relOperator(p):
  '''
      relOperator : LESS 
                  | LESS_EQ 
                  | GREATER 
                  | GREATER_EQ 
                  | IS_EQ_DIFF 
                  | NOT_EQ_DIFF 
                  | LESS_EQ_DIFF
                  | LESS_DIFF 
                  | GREATER_EQ_DIFF 
                  | GREATER_DIFF

  '''
  print p.slice 

def p_returnStatement(p):
  '''
      returnStatement : RETURN expression_question SEMICOLON
  '''
  print p.slice 

def p_singleImport(p):
  '''
      singleImport : IDENTIFIER ASSIGN identifierChain
                   | identifierChain
  '''
  print p.slice 
  
def p_statement(p):
  '''
      statement : statementNoCaseNoDefault 
                | caseStatement 
                | caseRangeStatement 
                | defaultStatement
  '''
  print p.slice 

def p_statementNoCaseNoDefault(p):
  '''
      statementNoCaseNoDefault : labeledStatement 
                              | blockStatement 
                              | ifStatement 
                              | whileStatement 
                              | doStatement 
                              | forStatement 
                              | foreachStatement 
                              | switchStatement 
                              | continueStatement 
                              | breakStatement 
                              | returnStatement 
                              | gotoStatement 
                              | withStatement 
                              | expressionStatement
  '''
  print p.slice   
    
def p_storageClass(p):
    ''' 
        storageClass : typeConstructor 
                     | AUTO 
                     | ENUM 
                     | EXTERN 
                     | FINAL 
                     | STATIC
    '''
    print p.slice 

def p_structBody(p):
    '''
    structBody : LBRACE multiple_declaration RBRACE
    '''
    print p.slice 

def p_switchStatement(p):
    '''
        switchStatement : SWITCH LPAREN expression RPAREN statement
    '''
    print p.slice 

def p_symbol(p):
    '''
        symbol : DOT identifierOrTemplateChain
              | identifierOrTemplateChain
    '''
    print p.slice 

def p_ternaryExpression(p):
    '''
        ternaryExpression : orOrExpression QUESTION expression COLON ternaryExpression
                          | orOrExpression
    '''
    print p.slice 

def p_typeSuffixStar(p):
    '''
        typeSuffixStar : typeSuffix typeSuffixStar 
        | empty 
    '''
    print p.slice 
    
def p_type(p):
    '''
        type : typeConstructors_quetsion type2 typeSuffixStar
    '''
    print p.slice     

def p_typeConstructors_quetsion(p):
    ''' typeConstructors_quetsion : typeConstructors 
                  | empty
    '''
    print p.slice


def p_type2(p):
    '''
        type2 : builtinType 
              | typeIdentifierPart 
              | THIS DOT typeIdentifierPart
              | typeofExpression typeIdentifierPart_question
              | typeConstructor LPAREN type RPAREN 
    '''
    print p.slice     

def p_typeIdentifierPart_question(p):
  '''
        typeIdentifierPart_question : DOT typeIdentifierPart
                                    | empty
  '''
  print p.slice 

def p_typeConstructor(p):
    '''
        typeConstructor : CONST 
                        | IMMUTABLE
    '''
    print p.slice

def p_typeConstructors(p):
    '''       
        typeConstructors : typeConstructor multiple_typeConstructors
    '''
    print p.slice     

def p_multiple_typeConstructors(p):
    '''
         multiple_typeConstructors : typeConstructor multiple_typeConstructors
                                   | empty 
    '''
    print p.slice

def p_typeSuffix(p):
    '''       
        typeSuffix : TIMES 
                   | LBRACKET type_question RBRACKET  
                   | LBRACKET assignExpression RBRACKET 
                   | LBRACKET assignExpression RANGE assignExpression RBRACKET
                   | DELEGATE parameters multiple_memberFunctionAttribute 
                   | FUNCTION  parameters multiple_memberFunctionAttribute
    '''   
    print p.slice 
    
def p_type_question(p):
  ''' type_question : type 
            | empty
  '''
  print p.slice 

def p_typeidExpression(p):
  ''' typeidExpression : TYPEID LPAREN type RPAREN
             | TYPEID LPAREN expression RPAREN
  '''
  print p.slice 

def p_typeofExpression(p):
  ''' typeofExpression : TYPEOF LPAREN expression RPAREN
             | TYPEOF LPAREN RETURN RPAREN
  '''
  print p.slice


def p_unaryExpression(p):
    '''       
        unaryExpression : primaryExpression 
                        | UAMPERSAND unaryExpression 
                        | EXCLAMATION unaryExpression 
                        | UTIMES unaryExpression 
                        | UPLUS unaryExpression
                        | UMINUS unaryExpression 
                        | PLUS_PLUS unaryExpression
                        | MINUS_MINUS unaryExpression  
                        | newExpression 
                        | deleteExpression 
                        | castExpression 
                        | functionCallExpression 
                        | indexExpression 
                        | LPAREN type RPAREN DOT identifierOrTemplateInstance 
                        | unaryExpression DOT newExpression 
                        | unaryExpression DOT  identifierOrTemplateInstance  
                        | unaryExpression PLUS_PLUS
            | unaryExpression MINUS_MINUS

    '''
    print p.slice     


def p_unionDeclaration(p):
    '''
        unionDeclaration : UNION IDENTIFIER structBody 
                         | UNION IDENTIFIER SEMICOLON 
                         | UNION structBody 
    '''
    print p.slice     

def p_CommaDeclarator(p):
    '''
        CommaDeclarator : COMMA declarator CommaDeclarator 
                        | empty
    '''
    print p.slice 

def p_variableDeclaration(p):
    '''
    variableDeclaration : multiplestorageClass type declarator CommaDeclarator SEMICOLON 
                        | multiplestorageClass type IDENTIFIER ASSIGN functionBody SEMICOLON 
                        | autoDeclaration
    '''
    print p.slice     

def p_whileStatement(p):
    '''
         whileStatement : WHILE LPAREN expression RPAREN declarationOrStatement
    '''
    print p.slice   

def p_withStatement(p):
    '''
         withStatement : WITH LPAREN expression RPAREN statementNoCaseNoDefault
    '''
    print p.slice 

def p_xorExpression(p):
    ''' xorExpression : andExpression 
                      | xorExpression CARET andExpression
    '''
    print p.slice 

def p_error(p):
    if p == None:
        print str(sys.argv[1])+" :: You missed something at the end"
    else:
        print str(sys.argv[1])+" :: Syntax error in line no " + str(p.lineno)

def p_empty(p):
    'empty :'
    pass


yacc.yacc()
a=open(sys.argv[1],'r')
a=a.read()
data = ""
a+="\n"
yacc.parse(a, debug=1)
# for item in revoutput:
#   print item