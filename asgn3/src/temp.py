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
    print p.slice 


def p_structBody(p):
    '''
    structBody : LBRACE multiple_declaration RBRACE
    '''
    print p.slice 

def p_baseClassList(p): 
    ''' baseClassList : baseClass
                      | baseClassList COMMA baseClass
    '''
    print p.slice 
          

def p_newExpression(p):
    ''' newExpression : NEW type 
                      | NEW type LBRACKET assignExpression RBRACKET 
                      | NEW type arguments
                      | newAnonClassExpression
    '''
    print p.slice 

def p_typeSuffix(p):
    '''       
        typeSuffix : TIMES 
                   | LBRACKET type RBRACKET
                   | LBRACKET RBRACKET 
                   | LBRACKET assignExpression RBRACKET 
                   | LBRACKET assignExpression RANGE assignExpression RBRACKET
                   | DELEGATE parameters multiple_memberFunctionAttribute SEMICOLON typeidExpression COLON TYPEID LBRACKET type RBRACKET
                   | DELEGATE parameters multiple_memberFunctionAttribute SEMICOLON typeidExpression COLON TYPEID LBRACKET expression RBRACKET
                   | FUNCTION  parameters multiple_memberFunctionAttribute SEMICOLON typeidExpression COLON TYPEID LBRACKET type RBRACKET
                   | FUNCTION  parameters multiple_memberFunctionAttribute SEMICOLON typeidExpression COLON TYPEID LBRACKET expression RBRACKET
                   | SEMICOLON typeofExpression COLON TYPEOF LBRACKET expression RBRACKET 
                   | SEMICOLON typeofExpression COLON TYPEOF LBRACKET RETURN RBRACKET 
    '''   
    print p.slice     


def p_functionBody(p):
    ''' functionBody : blockStatement
           | bodyStatement
           | empty
    '''
    print p.slice 