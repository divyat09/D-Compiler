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
  print p.slice 

def p_mulExpression(p):
    ''' mulExpression : powExpression 
                      | mulExpression TIMES powExpression
                      | mulExpression DIV powExpression
                      | mulExpression MODULO powExpression
    '''
    print p.slice 

def p_powExpression(p):
    ''' 
      powExpression : unaryExpression 
                      | powExpression CARET unaryExpression 
    '''
    print p.slice 

def p_unaryExpression(p):
    '''       
        unaryExpression : primaryExpression 
                        | AMPERSAND unaryExpression 
                        | EXCLAMATION unaryExpression 
                        | TIMES unaryExpression 
                        | PLUS unaryExpression
                        | MINUS unaryExpression 
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

def p_primaryExpression(p):
    ''' primaryExpression : identifierOrTemplateInstance 
                          | DOT identifierOrTemplateInstance 
                          | typeConstructor LPAREN type RPAREN DOT IDENTIFIER 
                          | type DOT IDENTIFIER 
                          | type arguments 
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

def p_newExpression(p):
    ''' newExpression : NEW type 
                      | NEW type LBRACKET assignExpression RBRACKET 
                      | NEW type arguments
    '''
    print p.slice 


def p_deleteExpression(p): 
    ''' deleteExpression : DELETE unaryExpression
    '''
    print p.slice 


def p_castExpression(p):
    ''' castExpression : CAST LPAREN RPAREN unaryExpression
                      | CAST LPAREN type RPAREN unaryExpression
                      | CAST LPAREN castQualifier RPAREN unaryExpression 
    '''
    print p.slice 

def p_castQualifier(p):
    ''' castQualifier : CONST 
                      | IMMUTABLE 
    '''
    print p.slice 

def p_functionCallExpression(p):
  ''' functionCallExpression : symbol arguments unaryExpression arguments
                 | type arguments 
  '''
  print p.slice


def p_symbol(p):
    '''
        symbol : DOT identifierOrTemplateChain
              | identifierOrTemplateChain
    '''
    print p.slice 

def p_identifierOrTemplateChain(p):
  ''' 
      identifierOrTemplateChain : identifierOrTemplateInstance
                     | identifierOrTemplateChain DOT identifierOrTemplateInstance
  '''
  print p.slice 

def p_identifierOrTemplateInstance(p):
  ''' identifierOrTemplateInstance : IDENTIFIER 
  '''     

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


def p_index(p):
    ''' index : assignExpression 
              | assignExpression RANGE assignExpression
    '''         
    print p.slice 

def p_type(p):
    '''
        type : typeConstructors type2 typeSuffixStar
             | type2 typeSuffixStar
    '''
    print p.slice     

def p_typeSuffix(p):
    '''       
        typeSuffix : 
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


def p_typeSuffixStar(p):
    '''
        typeSuffixStar : typeSuffix typeSuffixStar 
        | empty 
    '''
    print p.slice 

def p_type2(p):
    '''
        type2 : builtinType 
              | symbol 
              | typeofExpression DOT identifierOrTemplateChain
              | typeofExpression   
              | typeConstructor LBRACKET type RBRACKET 
    '''
    print p.slice 

def p_typeofExpression(p):
  ''' 
        typeofExpression : TYPEOF LBRACKET expression RBRACKET  
                         | TYPEOF LBRACKET RETURN RBRACKET  
  '''
  print p.slice 
def p_typeConstructors(p):
    '''       
        typeConstructors : typeConstructor 
                         | typeConstructor typeConstructors
    '''
    print p.slice     

def p_typeConstructor(p):
    '''
        typeConstructor : CONST 
                        | IMMUTABLE
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

def p_argumentList(p): 
    ''' argumentList : assignExpression 
                    | argumentList comma_assign
    '''
    print p.slice 


def p_comma_assign(p):
    ''' comma_assign : COMMA assignExpression comma_assign
                    | empty
    '''
    print p.slice 


def p_functionBody(p):
    ''' functionBody : empty
    '''
    print p.slice 

def p_arrayLiteral(p):
    ''' arrayLiteral : LBRACKET argumentList_question RBRACKET
    '''
    print p.slice 

def p_expression(p):
    ''' expression : assignExpression 
                  | expression COMMA assignExpression
    '''
    print p.slice 

def p_functionLiteralExpression(p):
    '''
      functionLiteralExpression : FUNCTION functionBody
                                | FUNCTION type functionBody
                                | functionBody 
                                | IDENTIFIER assignExpression 
  '''
    print p.slice 

def p_mixinExpression(p):
    ''' mixinExpression : MIXIN LPAREN assignExpression RPAREN 
    '''
    print p.slice 


def p_importExpression(p):
  '''   
     importExpression : IMPORT LBRACKET assignExpression RBRACKET
  '''   
  print p.slice 

def p_LIT_STRPlus(p):
  '''
      LIT_STRPlus : LIT_STR LIT_STRPlus
                        | LIT_STR
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

def p_ternaryExpression(p):
    '''
        ternaryExpression : orOrExpression QUESTION expression COLON ternaryExpression
                          | orOrExpression
    '''
    print p.slice 

def p_orOrExpression(p):
    ''' 
        orOrExpression : andAndExpression
                       | orOrExpression DOUBLE_PIPE andAndExpression
    '''
    print p.slice 

def p_andAndExpression(p): 
    ''' andAndExpression : orExpression 
                        | andAndExpression DOUBLE_AMPERSAND orExpression
    '''
    print p.slice 


def p_orExpression(p):
    ''' orExpression : xorExpression 
                     | orExpression PIPE xorExpression 
    '''
    print p.slice 

def p_xorExpression(p):
    ''' xorExpression : andExpression 
                      | xorExpression CARET andExpression
    '''
    print p.slice 

def p_andExpression(p): 
    ''' andExpression : cmpExpression 
                     | andExpression AMPERSAND cmpExpression
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

def p_equalExpression(p):
    ''' equalExpression : shiftExpression IS_EQ shiftExpression
                      | shiftExpression NOT_EQ shiftExpression 
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

def p_error(p):
    if p == None:
        print str(sys.argv[1])+" :: You missed something at the end"
    else:
        print str(sys.argv[1])+" :: Syntax error in line no " + str(p.lineno)

def p_empty(p):
    'empty :'
    pass


yacc.yacc(debug=True)
a=open(sys.argv[1],'r')
a=a.read()
data = ""
a+="\n"
yacc.parse(a, debug=True)
# for item in revoutput:
#   print item