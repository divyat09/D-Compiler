templateParameterList

conditionalStatement

functionAttribute

def p_multiple_functionAttribute(p):
  '''
  multiple_functionAttribute : functionAttribute multiple_functionAttribute
  '''
  revouput.append(p.slice)


				DOUBT  DOUBT DOUBT DOUBT DOUBT DOUBT DOUBT DOUBT DOUBT DOUBT 

  def p_identityExpression(p):
  ''' identityExpression : shiftExpression IS shiftExpression
                 | shiftExpression EXCLAMATION IS shiftExpression
  '''
  revoutput.append(p.slice)


def p_isExpression(p):
  ''' isExpression : IS LPAREN type RPAREN
           | IS LPAREN type IDENTIFIER RPAREN
           | IS LPAREN type COLON typeSpecialization RPAREN
           | IS LPAREN type IDENTIFIER COLON typeSpecialization RPAREN            
           | IS LPAREN type ASSIGN typeSpecialization RPAREN
           | IS LPAREN type IDENTIFIER ASSIGN typeSpecialization RPAREN             
           | IS LPAREN type COLON typeSpecialization COMMA templateParameterList RPAREN
           | IS LPAREN type IDENTIFIER COLON typeSpecialization COMMA templateParameterList RPAREN            
           | IS LPAREN type ASSIGN typeSpecialization COMMA templateParameterList RPAREN
           | IS LPAREN type IDENTIFIER ASSIGN typeSpecialization COMMA templateParameterList RPAREN             
  '''
  revoutput.append(p.slice)

def p_cmpExpression(p):
    ''' cmpExpression : shiftExpression 
                      | equalExpression
                      | identityExpression
                      | relExpression
    '''
    revoutput.append(p.slice)

IMPORTANT

DOUBLE XOR: Replaced with CARET currently
basicType: Replaced with type currently

def p_powExpression(p):
    ''' 
      powExpression : unaryExpression 
                      | powExpression CARET unaryExpression 
    '''
    revoutput.append(p.slice)

def p_primaryExpression(p):
    ''' primaryExpression : identifierOrTemplateInstance 
                          | DOT identifierOrTemplateInstance 
                          | typeConstructor LPAREN basicType RPAREN DOT IDENTIFIER 
                          | basicType DOT IDENTIFIER 
                          | basicType arguments 
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
    revoutput.append(p.slice)

