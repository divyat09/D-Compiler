#!/home/divyat/anaconda2/bin/python
from TAC import CreateTAC
from TAC import OutputTAC
import ply.lex as lex
import sys
import ply.yacc as yacc
from lexer import tokens
import logging
import symbol_table
ST = symbol_table.SymbolTable()

Listnonterminals=[]
Rderivation=[]
Derivations=[]
RightOutput = []
s_cond=0
s_label=0
stackbegin = []
stackend = []

Gloabl_Switch_Val=0
Gloabl_Switch_Label=0

precedence = (
    ('nonassoc','CONST','IMMUTABLE','BOOL','SHORT','USHORT','INT','UINT','LONG','ULONG','CHAR','FLOAT','VOID'),
    ('nonassoc','EMPTY'),
    # ('nonassoc','IDENTIFIER'),
    ('left','RANGE'),
    ('left','COMMA'),
    ('right','EQ_PLUS','EQ_MINUS','EQ_TIMES','EQ_DIV','EQ_MODULO','EQ_LEFT','EQ_RIGHT','EQ_AND_BIT','EQ_OR_BIT','EQ_XOR_BIT'),
    ('right','QUESTION'),
    ('left','DOUBLE_PIPE'),
    ('left','DOUBLE_AMPERSAND'),
    ('nonassoc','GREATER','LESS','IS_EQ','NOT_EQ','GREATER_EQ','LESS_EQ','IS_EQ_DIFF',
    'NOT_EQ_DIFF','GREATER_DIFF','LESS_DIFF','GREATER_EQ_DIFF','LESS_EQ_DIFF'),
    ('nonassoc','PIPE'),
    ('nonassoc','CARET'),
    ('nonassoc','AMPERSAND'),
    ('nonassoc','LEFT_SHIFT'),
    ('nonassoc','RIGHT_SHIFT'),
    ('left', 'PLUS', 'MINUS','TILDE'),
    ('left', 'TIMES', 'DIV', 'MODULO'),
    ('nonassoc','PLUS_PLUS','MINUS_MINUS','UMINUS','UTIMES','UAMPERSAND','UPLUS','EXCLAMATION','CAST'),
    ('right','POWER'),
    ('right','LPAREN','LBRACKET','POST_PLUS_PLUS','POST_MINUS_MINUS','DOT'),
)
#def p_CompilationUnit(p):
 #   ''' CompilationUnit : ProgramFile
  #  '''
#    Derivations.append(p.slice) 

#def p_ProgramFile(p):
#    ''' ProgramFile : multiple_declaration
#    '''
#    Derivations.append(p.slice)

def p_Declaration_mult(p):
    ''' Declaration_mult : Declaration Declaration_mult
                         | empty
    '''
    Derivations.append(p.slice)

def p_DeclDefs(p):
    '''DeclDefs : DeclDef
                | DeclDef DeclDefs
    '''
    Derivations.append(p.slice)

def p_DeclDefs_opt(p):
    ''' DeclDefs_opt : DeclDefs
                     | empty
    '''
    Derivations.append(p.slice)

def p_DeclDef(p):
    '''DeclDef : AttributeSpecifier
    	       | Declaration
    	       | Allocator
    	       | Deallocator
    	       | AliasThis
    	       | MixinDeclaration
               | SEMICOLON
    '''
    Derivations.append(p.slice) #Postblit , | Constructor | Destructor

def p_ModuleFullyQualifiedName(p):
    ''' ModuleFullyQualifiedName : ModuleName
                                 | Packages DOT ModuleName
    '''
    Derivations.append(p.slice)

def p_ModuleName(p):
    '''
    ModuleName : IDENTIFIER
    '''
    Derivations.append(p.slice)
def p_Packages(p):
    ''' Packages : PackageName
                 | Packages DOT PackageName
    '''
    Derivations.append(p.slice)

def p_PackageName(p):
    '''PackageName : IDENTIFIER
    '''
    Derivations.append(p.slice)


def p_ImportDeclaration(p):
    '''
        ImportDeclaration : IMPORT ImportList SEMICOLON
     				      | STATIC IMPORT ImportList SEMICOLON
    '''
    Derivations.append(p.slice)
  
def p_ImportList(p):
    '''
        ImportList : Import
                   | ImportBindings
                   | Import COMMA ImportList
    '''
    Derivations.append(p.slice)

def p_Import(p):
    '''
        Import : ModuleFullyQualifiedName
               | ModuleAliasIdentifier ASSIGN ModuleFullyQualifiedName     
    '''
    Derivations.append(p.slice)


def p_ImportBindings(p):
    '''
        ImportBindings : Import COLON ImportBindList
    '''
    Derivations.append(p.slice)

def p_ImportBindList(p):
    '''
        ImportBindList : ImportBind
                       | ImportBind COMMA ImportBindList
    '''
    Derivations.append(p.slice)

def p_ImportBind(p):
    ''' 
        ImportBind : IDENTIFIER
                   | IDENTIFIER ASSIGN IDENTIFIER
    ''' 
    Derivations.append(p.slice)

def p_ModuleAliasIdentifier(p):
    '''
        ModuleAliasIdentifier : IDENTIFIER
    '''
    Derivations.append(p.slice)

def p_MixinDeclaration(p):
    '''
        MixinDeclaration : MIXIN LPAREN AssignExpression  RPAREN SEMICOLON
    '''
    Derivations.append(p.slice)

def p_Declaration(p):
    '''	Declaration : FuncDeclaration
    				| VarDeclarations 
    				| AliasDeclaration
    				| AggregateDeclaration
                    | EnumDeclaration
                    | ImportDeclaration
    '''
    Derivations.append(p.slice) 

def p_VarDeclarations(p):
    ''' VarDeclarations : StorageClasses_opt BasicType Declarators SEMICOLON
    '''
    # create symbolTable Entry with identifier p[3]['place'], type = p[2]
    # print p[2],p[3]['place']
    # print p.slice,"''''''''''''"
    # print p[2],p[3]['type']
    
    # print ST.table[p[3]['place']], "FFFFFFFFFFFFFFFFFFFFFFFFFFFFff"
    
    # print p[3]
    # if p[2]!=ST.table[p[3]['place']]['datatype']:
    #     print p[2],p[3]['type'],"error type mismatch"
    #     sys.exit(0)
    #     return
    # p[0] = {'type' : p[2]}

    Derivations.append(p.slice)

def p_Declarators(p):
    '''Declarators : DeclaratorInitializer
    		   | DeclaratorInitializer COMMA DeclaratorIdentifierList
    '''
    # print p[0],"LLLLLLLLLLLLLLLL",p.slice

    return

    Derivations.append(p.slice)

# def p_declarator_mark(p):
#     '''declarator_mark : empty
#     '''


def p_DeclaratorInitializer(p):
    '''DeclaratorInitializer : VarDeclarator
                     | VarDeclarator ASSIGN Initializer
    			     | AltDeclarator ASSIGN Initializer
    			     | AltDeclarator 
    '''
    # print p[-1],"HHHHHHHHHIIIIIIIIIIIIII",p.slice
    p[0]=p[1]
    # print p.slice
    if len(p)==4:
        # print p[0],":::::::::::"
        p[0]['type'] = p[3]['type']
        CreateTAC( '=',p[0]['place'],p[3]['place'], None )
        # print '=',p[0]['place'],p[3]['place']
        if p[1]['place'] in ST.table.keys():
            print "Redeclaration of variable not allowed",p[3]['place']
            sys.exit(0)
        if p[1]['type']!=p[3]['type']:
            print "Type error " + p[3]['type'] +" != " + p[1]['type']
            sys.exit(0)
    
        ST.addvar(p[0]['place'],p[0]['type'])
        
        return
    if len(p)==2:
        if p[0]['place'] in ST.table.keys():
            print "Redeclaration of variable not allowed",p[3]['place']
            sys.exit(0)
    
    ST.addvar(p[0]['place'],p[0]['type'])

    Derivations.append(p.slice) # rem template parameters from 2

def p_DeclaratorIdentifierList(p):	
    ''' DeclaratorIdentifierList : mark1 DeclaratorIdentifier
    				 | mark1 DeclaratorIdentifier COMMA DeclaratorIdentifierList
    '''
    # print p.slice
    # if len(p)==2:
    #     p[0]=p[1]
    
    # if len(p)==4:
    #     p[3]=[p[-3]]
        
    Derivations.append(p.slice)

def p_mark1(p):
    ''' mark1 : empty
    '''
    p[0]=p[-3]
    # print p[0],"MARK!"


def p_DeclaratorIdentifier(p):
    ''' DeclaratorIdentifier : VarDeclaratorIdentifier
    			     | AltDeclaratorIdentifier
    '''
    # print p[-1],"MARKED"
    p[0]=p[1]
    Derivations.append(p.slice)

def p_VarDeclaratorIdentifier(p):
    ''' VarDeclaratorIdentifier : IDENTIFIER
                                | IDENTIFIER ASSIGN Initializer
    '''
    # print p[-1], "MARKED AGAIN"
    Derivations.append(p.slice) # rem template parameters from 2
    if len(p)==2:
        p[0]=p[1]
        if p[1] in ST.table.keys():
            print "Redeclaration of variable not allowed",p[3]['place']
            sys.exit(0)
        else:
            ST.addvar(p[1],p[-1])
        return
    else:
        CreateTAC( '=', p[1], p[3]['place'], None )
        # print '=',p[1],p[3]['place']
        if p[3]['type'] == p[-1]:
            ST.addvar(p[1],p[-1])
    # print p[-3],"HHHHHHHHHHHHHH"

def p_AltDeclaratorIdentifier(p):
    ''' AltDeclaratorIdentifier : BasicType2 IDENTIFIER AltDeclaratorSuffixes_opt
				| BasicType2 IDENTIFIER AltDeclaratorSuffixes_opt ASSIGN Initializer
				| BasicType2_opt IDENTIFIER AltDeclaratorSuffixes
				| BasicType2_opt IDENTIFIER AltDeclaratorSuffixes ASSIGN Initializer
    '''
    Derivations.append(p.slice)

def p_Declarator(p):
    '''Declarator : VarDeclarator
		  | AltDeclarator
    '''
    p[0]=p[1]
    Derivations.append(p.slice)

def p_VarDeclarator(p):
    '''VarDeclarator : BasicType2_opt IDENTIFIER
    '''
    # print p.slice
    p[0] = {
        'place':p[2],
        'type':p[-1]
    }
    Derivations.append(p.slice)

def p_AltDeclarator(p):
    '''AltDeclarator : BasicType2_opt IDENTIFIER AltDeclaratorSuffixes
    		     | BasicType2_opt LPAREN AltDeclaratorX RPAREN
                 | BasicType2_opt LPAREN AltDeclaratorX RPAREN AltFuncDeclaratorSuffix
    		     | BasicType2_opt LPAREN AltDeclaratorX RPAREN AltDeclaratorSuffixes
    '''
    # print p[-1]
    if len(p)==4:
        p[0]={
            'place':p[2],
            'isarray':True,
            'type':p[-1]
        }
        # print p[0]
    Derivations.append(p.slice) #| BasicType2_opt LPAREN AltDeclaratorX RPAREN AltFuncDeclaratorSuffix


def p_AltDeclaratorX(p):
    '''AltDeclaratorX : BasicType2_opt IDENTIFIER
                      | BasicType2_opt IDENTIFIER AltFuncDeclaratorSuffix
		              | AltDeclarator
    '''
    Derivations.append(p.slice) # add | BasicType2_opt IDENTIFIER AltFuncDeclaratorSuffix

def p_AltDeclaratorSuffixes(p):
    '''AltDeclaratorSuffixes : AltDeclaratorSuffix
    			             | AltDeclaratorSuffix AltDeclaratorSuffixes
    '''
    if len(p)==2:
        p[0] = p[1]
        return
    Derivations.append(p.slice)

def p_AltDeclaratorSuffixes_opt(p):
    '''AltDeclaratorSuffixes_opt : AltDeclaratorSuffixes 
				 | empty
    '''
    p[0]=p[1]
    Derivations.append(p.slice)

def p_AltDeclaratorSuffix(p):
    '''AltDeclaratorSuffix : LBRACKET RBRACKET
    			   | LBRACKET AssignExpression RBRACKET
    			   | LBRACKET Type RBRACKET
    '''
    if len(p)==4:
        p[0]={}
        p[0]['index'] = p[2]
        return
    Derivations.append(p.slice)

def p_AltFuncDeclaratorSuffix(p):
    '''AltFuncDeclaratorSuffix : Parameters MemberFunctionAttributes_opt
    '''
    Derivations.append(p.slice)


def p_Type(p):
    ''' Type : BasicType BasicType2_opt
    '''
    Derivations.append(p.slice)

def p_Type_opt(p):
    ''' Type_opt : Type
                 | empty
    '''
    Derivations.append(p.slice)    


def p_BasicType(p):
    '''BasicType : BasicTypeX
    		  | DOT IdentifierList
    		  | IdentifierList
    		  | Typeof
    		  | Typeof DOT IdentifierList
    '''
    if len(p)==2:
        p[0]=p[1]
    Derivations.append(p.slice)

def p_BasicTypeX(p):
    '''BasicTypeX : BOOL 
                  | SHORT 
                  | USHORT 
                  | INT
                  | UINT 
                  | LONG 
                  | ULONG 
                  | CHAR
                  | FLOAT 
                  | VOID
    '''
    # print p.slice,p[1].upper(), "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"
    p[0] = p[1].upper()
    Derivations.append(p.slice)

def p_BasicType2(p):
    '''BasicType2 : BasicType2X BasicType2_opt
    '''
    Derivations.append(p.slice)

def p_BasicType2_opt(p):
    ''' BasicType2_opt : BasicType2
		       | empty
    '''
    p[0]=p[1]
    Derivations.append(p.slice)

def p_BasicType2X(p):
    '''BasicType2X : TIMES
    		   | LBRACKET RBRACKET
    		   | LBRACKET AssignExpression RBRACKET
    		   | LBRACKET AssignExpression RANGE AssignExpression RBRACKET
    		   | LBRACKET Type RBRACKET
               | FUNCTION Parameters
    '''
    #delegate Parameters MemberFunctionAttributesopt
    #function Parameters FunctionAttributesopt
    Derivations.append(p.slice)

def p_IdentifierList(p):
    '''IdentifierList : IDENTIFIER
    		      | IDENTIFIER DOT IdentifierList
    		      | IDENTIFIER LBRACKET AssignExpression RBRACKET DOT IdentifierList
    '''
    # print p[1], "''''''''''''''''''"
    if len(p)==2:
        p[0]=p[1]
        return
    Derivations.append(p.slice)
    #TemplateInstance
    #TemplateInstance . IdentifierList

def p_StorageClasses(p):
    '''StorageClasses : StorageClass
    		      | StorageClass StorageClasses
    '''
    Derivations.append(p.slice)


def p_StorageClass(p):
    '''StorageClass : ENUM
    		    | STATIC
    		    | EXTERN
    		    | FINAL
    		    | AUTO
    		    | CONST
    		    | IMMUTABLE
    '''
    Derivations.append(p.slice)

def p_Initializer(p):
    '''Initializer : VoidInitializer
    		   | NonVoidInitializer
    '''
    p[0]=p[1]
    Derivations.append(p.slice)

def p_NonVoidInitializer(p):
    '''NonVoidInitializer : ExpInitializer
                          | ArrayInitializer
    '''

    p[0]=p[1]
    Derivations.append(p.slice)

def p_ExpInitializer(p):
    '''ExpInitializer : AssignExpression
    '''
    p[0]=p[1]
    Derivations.append(p.slice)

def p_ArrayInitializer(p):
    '''ArrayInitializer : LBRACKET ArrayMemberInitializations_opt RBRACKET
    '''
    Derivations.append(p.slice)

def p_ArrayMemberInitializations(p):
    '''ArrayMemberInitializations : ArrayMemberInitialization
    				  | ArrayMemberInitialization COMMA
    				  | ArrayMemberInitialization COMMA ArrayMemberInitializations
    '''
    Derivations.append(p.slice)

def p_ArrayMemberInitializations_opt(p):
    '''ArrayMemberInitializations_opt : ArrayMemberInitializations
				      | empty
    '''
    Derivations.append(p.slice)


def p_ArrayMemberInitialization(p):
    ''' ArrayMemberInitialization : NonVoidInitializer
    				 | AssignExpression COLON NonVoidInitializer
    '''
    Derivations.append(p.slice)

def p_AutoDeclaration(p):
    '''
        AutoDeclaration :  StorageClasses AutoDeclarationX SEMICOLON
    '''
    Derivations.append(p.slice)

def p_AutoDeclarationX(p):
    '''
        AutoDeclarationX : AutoDeclarationY    
                         | AutoDeclarationX COMMA AutoDeclarationY
    ''' 
    Derivations.append(p.slice)

def p_AutoDeclarationY(p):
    '''
        AutoDeclarationY : IDENTIFIER ASSIGN Initializer
    '''    
    Derivations.append(p.slice)

def p_StorageClasses_opt(p):
    '''
        StorageClasses_opt : StorageClasses
                           | empty 
    '''
    Derivations.append(p.slice)

def p_AliasDeclaration(p):
    '''
        AliasDeclaration : ALIAS StorageClasses_opt BasicType Declarators SEMICOLON 
                         | ALIAS StorageClasses_opt BasicType FuncDeclarator SEMICOLON
                         | ALIAS AliasDeclarationX  SEMICOLON
    '''
    Derivations.append(p.slice)
    print("Alias not handled currently")
    sys.exit()

def p_AliasDeclarationX(p):
    '''
        AliasDeclarationX : AliasDeclarationY
                          | AliasDeclarationX COMMA AliasDeclarationY
    '''
    Derivations.append(p.slice)

def p_AliasDeclarationY(p):
    '''
        AliasDeclarationY : IDENTIFIER ASSIGN StorageClasses_opt Type
                          | IDENTIFIER ASSIGN FunctionLiteral 
    '''
    Derivations.append(p.slice)
        

def p_Typeof(p):
    ''' Typeof : TYPEOF LPAREN Expression RPAREN
              | TYPEOF LPAREN RETURN RPAREN
    '''
    Derivations.append(p.slice)

def p_VoidInitializer(p):
    'VoidInitializer : VOID' 
    Derivations.append(p.slice)

def p_AttributeSpecifier(p):
    ''' 
        AttributeSpecifier : Attribute COLON
                           | Attribute DeclarationBlock
    '''
    Derivations.append(p.slice)

def p_Attribute(p):
    '''
        Attribute : VisibilityAttribute
    '''
    Derivations.append(p.slice)

def p_DeclarationBlock(p):
    ''' DeclarationBlock : DeclDef
                         | LBRACE DeclDefs_opt RBRACE
    '''
    Derivations.append(p.slice)  


def p_VisibilityAttribute(p):
    '''
        VisibilityAttribute : PRIVATE 
                         | PROTECTED 
                         | PUBLIC 
    '''    
    Derivations.append(p.slice)
    
def p_Expression(p):
    ''' Expression : CommaExpression
    '''
    # print p[1],"::::::::::",p.slice
    p[0]=p[1]
    # print ";;;;;;;;;",p[0],"''''''''''''''"
    Derivations.append(p.slice) 

def p_CommaExpression(p):
    '''CommaExpression : AssignExpression
                       | AssignExpression COMMA CommaExpression
    '''
    if len(p)==2:
        p[0]=p[1]
        # print p[1]
        return
    Derivations.append(p.slice) 

def p_AssignExpression(p):
    ''' AssignExpression : ConditionalExpression
                         | ConditionalExpression ASSIGN AssignExpression
                         | ConditionalExpression EQ_PLUS AssignExpression
                         | ConditionalExpression EQ_MINUS AssignExpression
                         | ConditionalExpression EQ_TIMES AssignExpression
                         | ConditionalExpression EQ_DIV AssignExpression
                         | ConditionalExpression EQ_MODULO AssignExpression
                         | ConditionalExpression EQ_AND_BIT AssignExpression
                         | ConditionalExpression EQ_OR_BIT AssignExpression
                         | ConditionalExpression EQ_XOR_BIT AssignExpression
                         | ConditionalExpression EQ_LEFT AssignExpression
                         | ConditionalExpression EQ_RIGHT AssignExpression 
    '''
    # print p.slice
    if(len(p)==2):
        p[0] = p[1]
        return
    # newPlace="t_new2"
    # p[0]={'place':newPlace, 'type':"TYPE_ERROR"}
    # p[0]['place']=p[]
    if p[2][0]=='=':
        if p[1]['type']==p[3]['type']:
            CreateTAC( '=',p[1]['place'],p[3]['place'], None )
            # print '=',p[1]['place'],p[3]['place']
            # p[1] = p[3]
            p[0]=p[1]
            # print p[1],p[3],p[2][0]
            return
        else:
            print "Type mismatch "+p[1]['type']+" != "+p[3]['type']
            sys.exit(0)
    elif p[2][0]=='<' or p[2][0]=='>':
        # print p[2][0]    
        #print p[2][0:2],p[1]['place'],p[1]['place'],p[3]['place']
        CreateTAC(p[2][0:2],p[1]['place'],p[1]['place'],p[3]['place'])
        return
    else:
        # print p[2][0],p[1]['place'],p[1]['place'],p[3]['place']
        CreateTAC(p[2][0],p[1]['place'],p[1]['place'],p[3]['place'])
        return

    
    Derivations.append(p.slice)  # add eq_power


def p_ConditionalExpression(p):
    '''ConditionalExpression : OrOrExpression
    			     | OrOrExpression QUESTION Expression COLON ConditionalExpression
    '''
    if len(p)==2:
        p[0]=p[1]
        return
    Derivations.append(p.slice) 

def p_OrOrExpression(p):
    '''OrOrExpression : AndAndExpression
    		      | OrOrExpression DOUBLE_PIPE AndAndExpression
    '''
    if len(p)==2:
        p[0]=p[1]
        return
    else:    
        newPlace = ST.get_temp()
        p[0]={
            'place':newPlace,
            'type':'undefined'
        }
        CreateTAC( p[2][0],p[1]['place'],p[3]['place'] )
        # print p[2][0],p[1]['place'],p[3]['place']
        p[0]['type'] = p[1]['type']
        return
    Derivations.append(p.slice) 

def p_AndAndExpression(p):
    '''AndAndExpression : OrExpression
    			| AndAndExpression DOUBLE_AMPERSAND OrExpression
    '''
    if len(p)==2:
        p[0]=p[1]
        return
    else:    
        newPlace = ST.get_temp()
        p[0]={
            'place':newPlace,
            'type':'undefined'
        }
        CreateTAC( p[2][0],newPlace, p[1]['place'],p[3]['place'] )
        # print p[2][0],newPlace, p[1]['place'],p[3]['place']
        p[0]['type'] = p[1]['type']
        return
    Derivations.append(p.slice) 

def p_OrExpression(p):
    '''OrExpression : XorExpression
    		    | OrExpression PIPE XorExpression
    '''
    if len(p)==2:
        p[0]=p[1]
        return
    Derivations.append(p.slice) 

def p_XorExpression(p):
    '''XorExpression : AndExpression
    		     | XorExpression CARET AndExpression
    '''
    if len(p)==2:
        p[0]=p[1]
        return
    Derivations.append(p.slice) 

def p_AndExpression(p):
    '''AndExpression : CmpExpression
    		     | AndExpression AMPERSAND CmpExpression
    '''
    if len(p)==2:
        p[0]=p[1]
        return
    Derivations.append(p.slice) 

def p_CmpExpression(p):
    '''CmpExpression : ShiftExpression
    		     | EqualExpression
		     | RelExpression
    '''
    if len(p)==2:
        p[0]=p[1]
        return
    Derivations.append(p.slice) 

def p_EqualExpression(p):
    '''EqualExpression : ShiftExpression IS_EQ ShiftExpression
    		       | ShiftExpression NOT_EQ ShiftExpression
    '''
    newPlace = ST.get_temp()
    p[0] = {
        'place':newPlace,
        'type':'TYPE_ERROR'
    }
    if p[1]['type'] == p[3]['type'] and p[1]['type']!='TYPE_ERROR': 
        CreateTAC(p[2],p[0]['place'],p[1]['place'],p[3]['place'])
        p[0]['type'] = p[1]['type']
        return
    else:
        print "Error:Type Mismatch for "+ p[2]+" Cant compare different datatypes " + p[1]['type']+"!="+p[3]['type']
        sys.exit(0)
    Derivations.append(p.slice) 

def p_RelExpression(p):
    '''RelExpression : ShiftExpression LESS ShiftExpression
                     | ShiftExpression GREATER_EQ ShiftExpression
                     | ShiftExpression GREATER ShiftExpression
                     | ShiftExpression LESS_EQ ShiftExpression
    '''
    newPlace = ST.get_temp()
    p[0] = {
        'place' : newPlace,
        'type' : 'TYPE_ERROR'
    }

    # if p[1]['place'] in ST.table.keys() and p[3]['place'] in ST.table.keys():
    if p[1]['type']=='TYPE_ERROR' or p[3]['type']=='TYPE_ERROR':
        print p[1],p[3],"TYPE_ERROR for p[1],p[3] ??"
        return

    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT' :
        # p[3] =ResolveRHSArray(p[3])
        # p[1] =ResolveRHSArray(p[1])
        # print p[2],newPlace,p[1]['place'],p[3]['place']
        CreateTAC(p[2],newPlace,p[1]['place'],p[3]['place'])
        p[0]['type'] = 'INT'

    else:
        print("Error: integer value is needed")
        sys.exit(0)
        return
    
    Derivations.append(p.slice) 

def p_ShiftExpression(p):
    ''' ShiftExpression : AddExpression
    			| ShiftExpression LEFT_SHIFT AddExpression
    			| ShiftExpression RIGHT_SHIFT AddExpression
    '''
    if len(p)==2:
        p[0]=p[1]
        return
    Derivations.append(p.slice) 

def p_AddExpression(p):
    '''AddExpression : MulExpression
    		     | AddExpression PLUS MulExpression
    		     | AddExpression MINUS MulExpression
    '''
    # print p.slice
    if len(p)==2 :
        p[0] = p[1]
        return
    # print p.slice,p[1],"'''''''''''''''''''''''''"
    newPlace = ST.get_temp()
    p[0] = {
        'place' : newPlace,
        'type' : 'TYPE_ERROR'
    }

    # if p[1]['place'] in ST.table.keys() and p[3]['place'] in ST.table.keys():
    if p[1]['type']=='TYPE_ERROR' or p[3]['type']=='TYPE_ERROR':
        print p[1],p[3],"TYPE_ERROR for p[1],p[3] ??"
        return

    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT' :
        # p[3] =ResolveRHSArray(p[3])
        # p[1] =ResolveRHSArray(p[1])
        CreateTAC( p[2],newPlace,p[1]['place'],p[3]['place'] )
        # print p[2],newPlace,p[1]['place'],p[3]['place']
        p[0]['type'] = 'INT'

    else:
        print("Error: integer value is needed")
        sys.exit(0)
        return
    # # # elif p[1]['isconst']:
    # # #     if p[3] not in ST.table.keys():

    # # if p[1]['place'] in ST.table.keys():
    # #     t1=ST.table[p[1]['place']]['datatype']
    
    # p[1]['type']    



    Derivations.append(p.slice)  # might add catexprssion

def p_MulExpression(p):
    '''MulExpression : UnaryExpression
    		     | MulExpression TIMES UnaryExpression
    		     | MulExpression DIV UnaryExpression
    		     | MulExpression MODULO UnaryExpression
    '''
    if len(p)==2 :
        p[0]=p[1]
        return
    # print p.slice, "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    if len(p)==2 :
        p[0] = p[1]
        return
    newPlace = ST.get_temp()
    p[0] = {
        'place' : newPlace,
        'type' : 'TYPE_ERROR'
    }
    if p[1]['type']=='TYPE_ERROR' or p[3]['type']=='TYPE_ERROR':
        return
    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT' :
        # p[3] =ResolveRHSArray(p[3])
        # p[1] =ResolveRHSArray(p[1])
        CreateTAC( p[2], newPlace , p[1]['place'], p[3]['place'] )         
        # print p[2],newPlace,p[1]['place'],p[3]['place']
        p[0]['type'] = 'INT'
    else:
        print("Error: integer value is needed")
    
    Derivations.append(p.slice) 

def p_UnaryExpression(p):
    '''UnaryExpression : AMPERSAND UnaryExpression %prec UAMPERSAND
    		       | PLUS_PLUS UnaryExpression 
    		       | MINUS_MINUS UnaryExpression
    		       | TIMES UnaryExpression %prec UTIMES
    		       | MINUS UnaryExpression %prec UPLUS
                   | PLUS UnaryExpression %prec UMINUS
                   | EXCLAMATION UnaryExpression
    		       | ComplementExpression
    		       | LPAREN Type RPAREN DOT IDENTIFIER
    		       | CastExpression
		           | PowExpression
    '''
    if len(p)==2 :
        p[0]=p[1]
        return
    if len(p)==3:
        if p[1]=='++' or p[1]=='--':
            if p[2]['place'] in ST.table.keys():
                if p[2]['type'] == "INT":
                    CreateTAC( p[1][0],p[2]['place'],p[2]['place'],1 )
                    # print p[1][0],p[2]['place'],p[2]['place'],1
                    p[0] = p[2]
                    return
                else:
                    "Postfix operations possible only with integer variables"
            else:
                print "Variable "+p[2]['place']+" not defined "+p.slice
                return

    # print p.slice,len(p)
    Derivations.append(p.slice)     

def p_ComplementExpression(p):
    '''ComplementExpression : TILDE UnaryExpression
    '''
    Derivations.append(p.slice)     

    
def p_NewExpression(p):
    '''NewExpression : NEW AllocatorArguments_opt Type
    		     | NewExpressionWithArgs
    '''
    Derivations.append(p.slice)  

def p_NewExpressionWithArgs(p):
    '''NewExpressionWithArgs : NEW AllocatorArguments_opt Type LBRACKET AssignExpression RBRACKET
    			     | NEW AllocatorArguments_opt Type LPAREN ArgumentList_opt RPAREN
                     | NewAnonClassExpression
    '''
    Derivations.append(p.slice) 

def p_AllocatorArguments(p): 
    '''AllocatorArguments : LPAREN ArgumentList_opt RPAREN
    '''
    Derivations.append(p.slice)  
    
def p_AllocatorArguments_opt(p):
    '''AllocatorArguments_opt : AllocatorArguments
			      | empty
    '''
    Derivations.append(p.slice) 

def p_ArgumentList_opt(p):
    '''ArgumentList_opt : ArgumentList
			| empty
    '''
    p[0] = p[1]
    Derivations.append(p.slice) 

def p_ArgumentList(p):
    '''ArgumentList : AssignExpression
    		    | AssignExpression COMMA
    		    | AssignExpression COMMA ArgumentList
    '''
    if len(p)==2:
        # print p[1], ':::::::::::'
        p[0]=p[1]
    Derivations.append(p.slice)  

def p_CastExpression(p):
    '''CastExpression : CAST LPAREN Type RPAREN UnaryExpression
    		      | CAST LPAREN RPAREN UnaryExpression
                 
    '''
    # print p.slice

    Derivations.append(p.slice)     


def p_PowExpression(p):
    '''PowExpression : PostfixExpression
                     | PostfixExpression POWER UnaryExpression
    '''
    
    Derivations.append(p.slice)   
    if len(p)==2 :
        p[0]=p[1]
        return  


def p_PostfixExpression(p):
    '''PostfixExpression : PrimaryExpression
    			         | PostfixExpression DOT IDENTIFIER
                         | PostfixExpression DOT NewExpression
                         | PostfixExpression PLUS_PLUS %prec POST_PLUS_PLUS
                         | PostfixExpression MINUS_MINUS %prec POST_MINUS_MINUS
                         | PostfixExpression LPAREN ArgumentList RPAREN
                         | BasicType LPAREN ArgumentList_opt RPAREN JmpMark                                  
    '''
    print p.slice
    Derivations.append(p.slice)    #add index expression, slice expression 
    if len(p)==2 :
        p[0]=p[1]
        return

    if len(p)==3:
        if p[1]['place'] in ST.table.keys():
            if p[1]['type'] == "INT":
                CreateTAC( p[2][0],p[1]['place'],p[1]['place'],1 )
                # print p[2][0],p[1]['place'],p[1]['place'],1
                p[0] = p[1]
                return
            else:
                "Postfix operations possible only with integer variables"
        else:
            print "Variable "+p[1]['place']+" not defined "
            return
    p[0]=p[5]
    # print p[5]    

def p_JmpMark(p):
    '''
        JmpMark : empty
    '''
    # 'place': ST.table[p[-4]]['returnvar'],

    if p[-4] in ST.table.keys():
        # newPlace = ST.get_temp()
        p[0]={
            'place':p[-4],
            'type':ST.table[p[-4]]['datatype'] 
        }
    if( p[-4] == 'writeln'):
        CreateTAC( "print_str", p[-2]['place'], None, None )
    else:
        CreateTAC( "call", p[-4], None, None )
    # print "call ", p[-4]
    print p.slice
    print p[-2]

def p_PrimaryExpression(p):
    ''' PrimaryExpression : IDENTIFIER
                          | IdentifierList
                          | DOT IDENTIFIER  
                          | THIS 
                          | NULL 
                          | TRUE 
                          | FALSE 
                          | DOLLAR 
                          | INUMBER 
                          | DNUMBER
                          | LIT_CHAR
                          | LIT_STRPlus
                          | ArrayLiteral
                          | FunctionLiteral
                          | MixinExpression
    					  | ImportExpression
                          | NewExpressionWithArgs
                          | BasicTypeX DOT IDENTIFIER
                          | BasicTypeX LPAREN ArgumentList_opt RPAREN
                          | Typeof
                          | LPAREN Expression RPAREN 
                          | TypeidExpression                    
    '''
    # print p.slice[1].type
    Derivations.append(p.slice)
    
    if(len(p)==2):
        
        p[0] = {
        'place' : 'undefined',
        'type' : 'TYPE_ERROR'
        }
        
        #Literals
        if (p.slice[1].type =='INUMBER'):
            p[0]={
                'type':'INT',
                'place':p[1],
                'isconst':True
                }
            return
        
        if(p.slice[1].type =='DNUMBER'):
            p[0]={
                'type':'FLOAT', 
                'place':p[1],
                'isconst':True                
            }
            # print p[0],"poooooooooo"
            return
        # if str(p.slice[1])=="ArrayLiteral"

        if (p.slice[1].type =='LIT_CHAR'):
            p[0]={
                'type':'CHAR',
                'place':p[1],
                'isconst':True
                }
            return

        if (p.slice[1].type =='LIT_STRPlus'):
            print p[1],"::::::::::::::::"
            p[0]={
                'type':'STR',
                'place':p[1],
                'isconst':True
                }
            print "in here"
            return

        # Identifiers
        if type(p[1])==type({}):
            p[0]['place'] = p[1]['place']
            p[0]['type'] = p[1]['type']
            return
        if p[1] in ST.table.keys():
            p[0]['place'] = ST.table[p[1]]['name']
            p[0]['type'] = ST.table[p[1]]['datatype']
            return
        else:
            print('Error : undefined variable '+p[1]+' is used.')
            sys.exit(0)


        # if 'isconst' not in p[0].keys() and p[1] not in ST.table.keys():
        #     print p[1] + "Variable not defined"
        #     sys.exit(0)
        # p[0]=p[1]
        
def p_ArrayLiteral(p):
    '''ArrayLiteral : LBRACKET ArgumentList_opt RBRACKET
                    | IDENTIFIER LBRACKET INUMBER RBRACKET
                    | IDENTIFIER LBRACKET AssignExpression RBRACKET
    '''
    if len(p)==5:
        newPlace = ST.get_temp()
        if p[1] in ST.table.keys():
            p[0]={
                'place':newPlace,
                'type':ST.table[p[1]]['datatype']
            }
            # print '*',newPlace,p[3],sizeof(p[0]['type'])
            if type(p[3])==type({}):
                CreateTAC( '*', newPlace, p[3]['place'], '4' )
                CreateTAC( '+', newPlace, newPlace, p[1] ) 
                # print '*',newPlace,p[3]['place'],'4'
                # print '+',newPlace,newPlace,p[1]
                return
            else:
                CreateTAC( '*', newPlace, p[3], '4' )
                CreateTAC( '+', newPlace, newPlace, p[1] ) 
                # print '*',newPlace,p[3],'4'
                # print '+',newPlace,newPlace,p[1]
                return
    # print p.slice,";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"
    Derivations.append(p.slice)

def p_FunctionLiteral(p):
    ''' FunctionLiteral : FUNCTION Type_opt ParameterAttributes_opt FunctionLiteralBody
                        | ParameterMemberAttributes FunctionLiteralBody
                        | FunctionLiteralBody
    '''
    print p.slice
    Derivations.append(p.slice)

def p_ParameterAttributes(p):
    ''' ParameterAttributes : Parameters
    '''
    Derivations.append(p.slice)

def p_ParameterAttributes_opt(p):
    ''' ParameterAttributes_opt : ParameterAttributes_opt
                                | empty
    '''         
    Derivations.append(p.slice)

def p_ParameterMemberAttributes(p):
    ''' ParameterMemberAttributes : Parameters MemberFunctionAttributes_opt
    '''
    Derivations.append(p.slice) 

def p_FunctionLiteralBody(p):
    '''FunctionLiteralBody : BlockStatement
                           | BodyStatement
    '''
    Derivations.append(p.slice) # contracts 

def p_LIT_STRPlus(p):
    '''LIT_STRPlus : LIT_STR LIT_STRPlus
                   | LIT_STR
    '''
    p[0] = p[1]
    Derivations.append(p.slice) 
 
def p_MixinExpression(p):
    '''MixinExpression : MIXIN LPAREN AssignExpression RPAREN
    '''
    Derivations.append(p.slice)
       
def p_ImportExpression(p):
    '''ImportExpression : IMPORT LPAREN AssignExpression RPAREN
    '''
    Derivations.append(p.slice) 

def p_TypeidExpression(p):
    '''
        TypeidExpression : TYPEID LPAREN Type RPAREN
                          | TYPEID LPAREN Expression RPAREN
    '''
    Derivations.append(p.slice) 
    
def p_Statement(p):
    '''
        Statement : SEMICOLON
                  | NonEmptyStatement
                  | ScopeBlockStatement   
    '''
    Derivations.append(p.slice)

def p_NoScopeNonEmptyStatement(p):
    '''
        NoScopeNonEmptyStatement : NonEmptyStatement
                                 | BlockStatement   
    '''
    Derivations.append(p.slice) 
    
def p_NoScopeStatement(p):
    '''
        NoScopeStatement : SEMICOLON
                         | NonEmptyStatement    
                         | BlockStatement
    '''
    Derivations.append(p.slice) 

def p_NonEmptyOrScopeBlockStatement(p):
    '''
        NonEmptyOrScopeBlockStatement : NonEmptyStatement
                                      | ScopeBlockStatement      
    '''
    Derivations.append(p.slice) 

def p_NonEmptyStatement(p):
    '''
        NonEmptyStatement : NonEmptyStatementNoCaseNoDefault
                          | CaseStatement
                          | CaseRangeStatement    
                          | DefaultStatement
    '''
    Derivations.append(p.slice) 

def p_NonEmptyStatementNoCaseNoDefault(p):
    '''
        NonEmptyStatementNoCaseNoDefault : LabeledStatement
                                         | ExpressionStatement    
                                         | DeclarationStatement
                                         | IfStatement                                        
                                         | WhileStatement                                        
                                         | DoStatement                                        
                                         | ForStatement                                        
                                         | ForeachStatement                                        
                                         | SwitchStatement                                        
                                         | FinalSwitchStatement                                        
                                         | ContinueStatement                                        
                                         | BreakStatement                                        
                                         | ReturnStatement                                        
                                         | GotoStatement                                        
                                         | WithStatement                                        
                                         | MixinStatement                                       
                                         | ForeachRangeStatement                                        
                                         | ImportDeclaration                                        
    '''
    Derivations.append(p.slice)

def p_ScopeStatement(p):
    '''
        ScopeStatement : NonEmptyStatement
                       | BlockStatement
    '''
    Derivations.append(p.slice)

def p_ScopeBlockStatement(p):
    '''
        ScopeBlockStatement : BlockStatement
    '''
    Derivations.append(p.slice)

def p_LabeledStatement(p):
    '''
        LabeledStatement : IDENTIFIER COLON
                         | IDENTIFIER COLON NoScopeStatement
                         | IDENTIFIER COLON Statement
    '''
    Derivations.append(p.slice)

def p_BlockStatement(p):
    '''
        BlockStatement : LBRACE RBRACE
                       | LBRACE StatementList RBRACE
    '''
    Derivations.append(p.slice)

def p_StatementList(p):
    '''
        StatementList : Statement
                      | Statement StatementList
    '''
    Derivations.append(p.slice)

def p_ExpressionStatement(p):
    '''
        ExpressionStatement : Expression SEMICOLON
    '''
    Derivations.append(p.slice)

def p_DeclarationStatement(p):
    '''
        DeclarationStatement : Declaration
                             | StorageClasses Declaration
    '''
    Derivations.append(p.slice)

def p_IfStatement(p):
    '''
        IfStatement : IF LPAREN IfCondition RPAREN ifmark1 ThenStatement ifmark2 
                    | IF LPAREN IfCondition RPAREN ifmark1 ThenStatement ifmark3 ELSE ElseStatement ifmark4
    '''
    # print p.slice
    
    Derivations.append(p.slice)

def p_ifmark4(p):
    '''
        ifmark4 : empty 
    '''
    CreateTAC( "label", p[-5][0], None, None  )
    # print "label",p[-5][0]

def p_ifmark3(p):
    '''
        ifmark3 : empty 
    '''
    CreateTAC("jmp", p[-2][0], None, None )
    CreateTAC("label", p[-2][1], None, None )   
    # print "jmp",p[-2][0]    
    # print "label",p[-2][1]

def p_ifmark2(p):
    '''
        ifmark2 : empty 
    '''
    CreateTAC( "label", p[-2][1], None, None )
    # print "label",p[-2][1]

def p_ifmark1(p):
    ''' ifmark1 : empty
    '''
    After_Label = ST.get_label()
    Else_Label = ST.get_label()

    CreateTAC( "ifgoto_eq", Else_Label, p[-2]['place'], '0' )
    # print "ifgoto_eq", p[-2]['place'],'1', Else_Label
    p[0] = [After_Label, Else_Label]


def p_IfCondition(p):
    '''
        IfCondition : Expression
                    | AUTO IDENTIFIER ASSIGN Expression
                    | BasicType Declarator ASSIGN Expression                    
    '''
    
    if len(p)==2:
        # print p[1]
        p[0] = p[1]
    Derivations.append(p.slice)

def p_ThenStatement(p):
    '''
        ThenStatement : ScopeStatement
    '''
    Derivations.append(p.slice)

def p_ElseStatement(p):
    '''
        ElseStatement : ScopeStatement
    '''
    Derivations.append(p.slice)

def p_WhileStatement(p):
    '''
        WhileStatement : WHILE LPAREN Expression RPAREN while_M1 ScopeStatement while_M2
    '''
    Derivations.append(p.slice)

def p_while_M1(p):
    '''
        while_M1 : 
    '''
    Repeat_Label =  ST.get_label()
    After_Label =  ST.get_label()

    CreateTAC( "label", Repeat_Label, None, None )
    CreateTAC( "ifgoto_eq", After_Label, p[-2]['place'], 0 )
    global stackbegin
    global stackend
    stackend.append(After_Label)
    stackbegin.append(Repeat_Label)
    # print "label", Repeat_Label
    # print "ifgoto_eq", p[-2]['place'], "0", After_Label
    p[0]= [Repeat_Label, After_Label]
    
def p_while_M2(p):
    '''
        while_M2 : 
    '''
    CreateTAC( "jmp", p[-2][0], None, None )
    CreateTAC( "label", p[-2][1], None, None )
    global stackbegin
    global stackend
    stackend.pop()
    stackbegin.pop()
    # print "jmp", p[-2][0]
    # print "label", p[-2][1]

def p_DoStatement(p):
    '''
        DoStatement : DO Dowhile_M1 ScopeStatement WHILE LPAREN Expression  RPAREN Dowhile_M2 
    '''
    Derivations.append(p.slice)

def p_Dowhile_M1(p):
    '''
        Dowhile_M1 : empty
    '''
    Repeat_Label= ST.get_label()
    After_Label = ST.get_label()
    CreateTAC( "label", Repeat_Label, None, None )
    global stackbegin
    global stackend
    stackend.append(After_Label)
    stackbegin.append(Repeat_Label)
    # print "label", Repeat_Label
    p[0]=[ Repeat_Label,After_Label ]

def p_Dowhile_M2(p):
    '''
        Dowhile_M2 : empty
    '''
    CreateTAC( "ifgoto_eq", p[-6][0], p[-2]['place'], 0)
    CreateTAC("label",p[-6][1],None,None)
    global stackbegin
    global stackend
    stackend.pop()
    stackbegin.pop()
    # print "ifgoto_eq", p[-2]['place'], "0", p[-6][0]

def p_ForStatement(p):
    '''
        ForStatement : FOR LPAREN Initialize Test_opt SEMICOLON for_M1 Increment_opt RPAREN for_M2 ScopeStatement for_M3
    '''
    # print p.slice
    Derivations.append(p.slice)

def p_for_M1(p):
    '''
        for_M1 :
    '''
    IncrLabel = ST.get_label()
    StatementLabel = ST.get_label()
    EndLabel = ST.get_label()

    if 'place' in p[-2].keys():
        CreateTAC( "ifgoto_eq", EndLabel, p[-2]['place'] ,0 )
        CreateTAC( "jmp", StatementLabel, None, None )
        CreateTAC( "label", IncrLabel, None, None )
        # print "ifgoto_eq", p[-2]['place'] ,'0', label3
        # print "jmp", label2
        # print "label", label1
    global stackbegin
    global stackend
    stackend.append(EndLabel)
    stackbegin.append(IncrLabel)
    p[0]=[IncrLabel, StatementLabel, EndLabel]
    Derivations.append(p.slice)

def p_for_M2(p):
    '''
        for_M2 :
    '''

    CreateTAC( "ifgoto_eq", p[-3][2] , p[-5]['place'], 0  )
    CreateTAC( "label", p[-3][1], None, None )
    # print "ifgoto_eq", p[-5]['place'] ,'0', p[-3][2]
    # print "label", p[-3][1]

def p_for_M3(p):
    '''
        for_M3 :
    '''
    CreateTAC( "jmp", p[-5][0], None, None )
    CreateTAC( "label", p[-5][2], None, None )
    global stackbegin
    global stackend
    stackend.pop()
    stackbegin.pop()
    # print "jmp", p[-5][0]
    # print "label", p[-5][2]

def p_Initialize(p):
    '''
        Initialize : SEMICOLON
                   | NoScopeNonEmptyStatement
    '''
    Derivations.append(p.slice)

def p_Test(p):
    ''' 
        Test : Expression
    '''
    p[0]=p[1]
    Derivations.append(p.slice)

def p_Test_opt(p):
    ''' 
        Test_opt : Test
                 | empty
    '''
    p[0]=p[1]
    Derivations.append(p.slice)


def p_Increment(p):
    '''
        Increment : Expression
    '''
    Derivations.append(p.slice)

def p_Increment_opt(p):
    '''
        Increment_opt : Increment
                      | empty
    '''
    Derivations.append(p.slice)


def p_AggregateForeach(p):
    '''
        AggregateForeach : Foreach LPAREN ForeachTypeList SEMICOLON ForeachAggregate RPAREN
    '''
    Derivations.append(p.slice)

def p_ForeachStatement(p):
    '''
        ForeachStatement : AggregateForeach NoScopeNonEmptyStatement
    '''
    Derivations.append(p.slice)

def p_Foreach(p):
    '''
        Foreach : FOREACH 
                | FOREACH_REVERSE
    '''
    Derivations.append(p.slice)

def p_ForeachTypeList(p):
    '''
        ForeachTypeList : ForeachType
                        | ForeachType COMMA ForeachTypeList
    '''
    Derivations.append(p.slice)

def p_ForeachType(p):
    '''
        ForeachType : ForeachTypeAttributes_opt BasicType Declarator
                    | ForeachTypeAttributes_opt IDENTIFIER
                    | ForeachTypeAttributes_opt ALIAS IDENTIFIER 
    '''
    Derivations.append(p.slice)

def p_ForeachTypeAttributes_opt(p):
    '''
        ForeachTypeAttributes_opt : ForeachTypeAttributes 
                                  | empty
    '''
    Derivations.append(p.slice)
  
def p_ForeachTypeAttributes(p):
    '''
        ForeachTypeAttributes : ForeachTypeAttribute
                             | ForeachTypeAttribute ForeachTypeAttributes_opt
    '''
    Derivations.append(p.slice)

def p_ForeachTypeAttribute(p):
    '''
        ForeachTypeAttribute : ENUM
    '''
    Derivations.append(p.slice)


def p_ForeachAggregate(p):
    '''
        ForeachAggregate : Expression
    '''
    Derivations.append(p.slice)

def p_RangeForeach(p):
    '''
        RangeForeach : LPAREN  ForeachType SEMICOLON LwrExpression RANGE UprExpression RPAREN
    '''
    Derivations.append(p.slice)

def p_LwrExpression(p):
    '''
        LwrExpression : Expression
    '''
    Derivations.append(p.slice)

def p_UprExpression(p):
    '''
        UprExpression : Expression
    '''
    Derivations.append(p.slice)

def p_ForeachRangeStatement(p):
    '''
        ForeachRangeStatement : RangeForeach ScopeStatement
    '''
    Derivations.append(p.slice)

def p_SwitchStatement(p):
    '''
        SwitchStatement : SWITCH LPAREN Expression RPAREN switch_M1 ScopeStatement switch_M2
    '''
    Derivations.append(p.slice)
def p_switch_M1(p):
    '''
        switch_M1 : empty
    '''
    # print p[-2],"::::::::"
    global s_cond
    global s_label
    
    s_cond = p[-2]['place']
    s_label = ST.get_label()
    global stackend
    stackend.append(s_label)
    # print s_cond,s_label

def p_switch_M2(p):
    '''
        switch_M2 : empty
    '''
    global s_label
    CreateTAC("label", s_label, None, None)
    global stackend
    stackend.pop()
    # print "label", s_label


# def p_Switch_Mark1(p):
#     '''
#         Switch_Mark1 : empty
#     '''
#     Gloabl_Switch_Val= p[-2]['place']
#     Gloabl_Switch_Label= ST.get_label()  

# def p_Switch_Mark2(p):
#     '''
#         Switch_Mark2 : empty
#     '''
#     CreateTAC( "label", Gloabl_Switch_Label, None, None )
#     # print "label ", Gloabl_Switch_Label

def p_CaseStatement(p):
    '''
        CaseStatement : CASE ArgumentList COLON c_m1 ScopeStatementList c_m2
    '''
    # print p.slice
    Derivations.append(p.slice)

def p_c_m1(p):
    '''
        c_m1 : empty
    ''' 
    global s_cond
    global s_label
    label = ST.get_label()
    CreateTAC( "ifgoto_neq", label , s_cond, p[-2]['place']  )
    # print "ifgoto_neq", s_cond, p[-2]['place'], label
    p[0] = [label]

def p_c_m2(p):
    '''
        c_m2 : empty
    ''' 
    global s_l
    CreateTAC( "jmp", s_label, None, None )
    CreateTAC( "label", p[-2][0], None, None )
    # print "jmp", s_label
    # print "label" , p[-2][0]

def p_CaseRangeStatement(p):
    '''
        CaseRangeStatement : CASE FirstExp COLON RANGE LastExp COLON ScopeStatementList
    '''
    Derivations.append(p.slice)

def p_FirstExp(p):
    '''
        FirstExp : AssignExpression
    '''
    Derivations.append(p.slice)

def p_LastExp(p):
    '''
        LastExp : AssignExpression
    '''
    Derivations.append(p.slice)

def p_DefaultStatement(p):
    '''
        DefaultStatement : DEFAULT COLON ScopeStatementList
    '''
    Derivations.append(p.slice)


def p_ScopeStatementList(p):
    '''
        ScopeStatementList : StatementListNoCaseNoDefault
    '''
    p[0] = p[1]
    Derivations.append(p.slice)

def p_StatementListNoCaseNoDefault(p):
    '''
        StatementListNoCaseNoDefault : StatementNoCaseNoDefault
                                     | StatementNoCaseNoDefault StatementListNoCaseNoDefault
    '''
    p[0]=p[1]
    Derivations.append(p.slice)

def p_StatementNoCaseNoDefault(p):
    ''' 
        StatementNoCaseNoDefault : SEMICOLON
                                 | NonEmptyStatementNoCaseNoDefault
                                 | ScopeBlockStatement
    '''
    Derivations.append(p.slice)

def p_FinalSwitchStatement(p):
    '''
        FinalSwitchStatement : FINAL SWITCH LPAREN Expression RPAREN ScopeStatement
    '''
    Derivations.append(p.slice)

def p_IDENTIFIER_opt(p):
    '''
        IDENTIFIER_opt : IDENTIFIER
                       | empty
    '''
    Derivations.append(p.slice)

def p_Expression_opt(p):
    '''
        Expression_opt : Expression
                       | empty
    '''
    p[0] = p[1]
    Derivations.append(p.slice)

def p_ContinueStatement(p):
    '''
        ContinueStatement : CONTINUE IDENTIFIER_opt SEMICOLON
    '''
    label = stackbegin[-1]
    CreateTAC("jmp",label,None,None)
    Derivations.append(p.slice)

def p_BreakStatement(p):
    '''
        BreakStatement : BREAK IDENTIFIER_opt SEMICOLON
    '''
    label = stackend[-1]
    CreateTAC("jmp",label,None,None)
    Derivations.append(p.slice)

def p_ReturnStatement(p):
    '''
        ReturnStatement : RETURN Expression_opt SEMICOLON
    '''
    # print 'ret',p[2]['place']
    CreateTAC( 'ret', p[2]['place'], None, None )    

    Derivations.append(p.slice)

def p_GotoStatement(p):
    '''
        GotoStatement : GOTO IDENTIFIER SEMICOLON
                      | GOTO DEFAULT SEMICOLON
                      | GOTO CASE SEMICOLON
                      | GOTO CASE Expression SEMICOLON
    '''
    Derivations.append(p.slice)
    
def p_WithStatement(p):
    '''
        WithStatement : WITH LPAREN Expression RPAREN ScopeStatement
                      | WITH LPAREN Symbol RPAREN ScopeStatement

    '''
    Derivations.append(p.slice) # | WITH LPAREN TemplateInstance RPAREN ScopeStatement   

def p_MixinStatement(p):
    '''
        MixinStatement : MIXIN LPAREN AssignExpression RPAREN SEMICOLON
    ''' 
    Derivations.append(p.slice)

def p_AggregateDeclaration(p):
    '''AggregateDeclaration : ClassDeclaration
    			    | UnionDeclaration
    '''
    print("Classes not handeld currently")
    sys.exit(0)

    Derivations.append(p.slice) 

def p_UnionDeclaration(p):
    '''UnionDeclaration : UNION IDENTIFIER SEMICOLON
    			| UNION IDENTIFIER AggregateBody
    			| AnonUnionDeclaration
    '''
    print("Unions not handeld currently")
    sys.exit(0)

    Derivations.append(p.slice) 

def p_AnonUnionDeclaration(p):
    ''' AnonUnionDeclaration : UNION AggregateBody
    '''
    Derivations.append(p.slice) 

def p_AggregateBody(p):
    ''' AggregateBody : LBRACE DeclDefs_opt RBRACE
    '''
    Derivations.append(p.slice) # might add Postblit                  
    
def p_ClassDeclaration(p):
    '''ClassDeclaration : CLASS IDENTIFIER SEMICOLON
                        | CLASS IDENTIFIER BaseClassList_opt AggregateBody
    '''
    Derivations.append(p.slice)

def p_BaseClassList(p):
    '''BaseClassList : COLON SuperClass
	             | COLON SuperClass COMMA Interfaces
    		     | COLON Interfaces
    '''
    Derivations.append(p.slice)

def p_BaseClassList_opt(p):
    '''BaseClassList_opt : BaseClassList
                         | empty
    '''
    Derivations.append(p.slice)

def p_SuperClass(p):
    '''SuperClass : BasicType
    '''
    Derivations.append(p.slice)

def p_Interfaces(p):
    '''Interfaces : Interface
    		  | Interface COMMA Interfaces
    '''
    Derivations.append(p.slice)

def p_Interface(p):
    'Interface : BasicType'
    Derivations.append(p.slice)



def p_Allocator(p):
    '''Allocator : NEW Parameters SEMICOLON
    		 | NEW Parameters FunctionBody
    '''
    Derivations.append(p.slice)

def p_Deallocator(p):
    '''Deallocator : DELETE Parameters SEMICOLON
    		   | DELETE Parameters FunctionBody
    '''
    Derivations.append(p.slice)

def p_AliasThis(p):
    '''AliasThis : ALIAS IDENTIFIER THIS SEMICOLON
    '''
    Derivations.append(p.slice)

def p_NewAnonClassExpression(p):
    '''NewAnonClassExpression : NEW AllocatorArguments_opt CLASS ClassArguments_opt SuperClass_opt Interfaces_opt AggregateBody
    '''
    Derivations.append(p.slice)

def p_ClassArguments(p):
    '''ClassArguments : LPAREN ArgumentList_opt RPAREN
    '''
    Derivations.append(p.slice)

def p_ClassArguments_opt(p):
    '''ClassArguments_opt : ClassArguments
		          | empty
    '''
    Derivations.append(p.slice)

def p_SuperClass_opt(p):
    '''SuperClass_opt : SuperClass 
		              | empty
    '''
    Derivations.append(p.slice)

def p_Interfaces_opt(p):
    '''Interfaces_opt : Interfaces
		      | empty
    '''
    Derivations.append(p.slice)

def p_EnumDeclaration(p):
    '''
        EnumDeclaration : ENUM IDENTIFIER EnumBody
                        | ENUM IDENTIFIER COLON EnumBaseType EnumBody
                        | AnonymousEnumDeclaration
    '''
    Derivations.append(p.slice)

    print("Enum not handled currently")
    sys.exit(0)

def p_EnumBaseType(p):
    '''
        EnumBaseType : Type
    '''
    Derivations.append(p.slice)

def p_EnumBody(p):
    ''' 
        EnumBody : LBRACE EnumMembers RBRACE
                 | SEMICOLON
    ''' 
    Derivations.append(p.slice)

def p_EnumMembers(p):
    '''
        EnumMembers : EnumMember 
                    | EnumMember COMMA 
                    | EnumMember COMMA EnumMembers
    '''
    Derivations.append(p.slice)

def p_EnumMember(p):
    '''
        EnumMember : IDENTIFIER 
                   | IDENTIFIER ASSIGN AssignExpression
    '''
    Derivations.append(p.slice)

def p_AnonymousEnumDeclaration(p):
    '''
        AnonymousEnumDeclaration : ENUM COLON EnumBaseType LBRACE EnumMembers RBRACE 
                                 | ENUM LBRACE EnumMembers RBRACE
                                 | ENUM LBRACE AnonymousEnumMembers RBRACE   
    '''
    Derivations.append(p.slice)

def p_AnonymousEnumMembers(p):
    '''
        AnonymousEnumMembers : AnonymousEnumMember
                             | AnonymousEnumMember COMMA 
                             | AnonymousEnumMember COMMA AnonymousEnumMembers
    '''
    Derivations.append(p.slice)

def p_AnonymousEnumMember(p):
    '''
        AnonymousEnumMember : EnumMember 
                            | Type IDENTIFIER ASSIGN AssignExpression
    '''    
    Derivations.append(p.slice)
    
def p_FuncDeclaration(p):
    '''FuncDeclaration  : StorageClasses_opt BasicType FuncDeclarator FunctionBody
                        | StorageClasses_opt BasicType FuncDeclarator SEMICOLON
    		            | AutoFuncDeclaration
    '''
    Derivations.append(p.slice)


def p_AutoFuncDeclaration(p):
    '''AutoFuncDeclaration : StorageClasses IDENTIFIER FuncDeclaratorSuffix FunctionBody
    '''
    Derivations.append(p.slice)

def p_FuncDeclarator(p):
    '''FuncDeclarator : BasicType2_opt IDENTIFIER FuncDeclaratorSuffix
    '''
    Derivations.append(p.slice)

    FuncLabel= p[2]
    ST.addfunc(FuncLabel,"function",p[-1])
    CreateTAC( "label", FuncLabel, None, None )
    # print "label ", FuncLabel
    p[0] = p[2]


def p_FuncDeclaratorSuffix(p):
    '''FuncDeclaratorSuffix : Parameters MemberFunctionAttributes_opt
    '''
    Derivations.append(p.slice)

def p_Parameters(p):
    '''Parameters : LPAREN ParameterList_opt RPAREN
    '''
    Derivations.append(p.slice)

def p_ParameterList(p):
    '''ParameterList : Parameter
    		     | Parameter COMMA ParameterList
    		     | ELLIPSIS
    '''
    Derivations.append(p.slice)


def p_ParameterList_opt(p):
    '''ParameterList_opt : ParameterList
            		     | empty
    '''
    Derivations.append(p.slice)

def p_Parameter(p):
    '''Parameter : InOut_opt BasicType Declarator
    		 | InOut_opt BasicType Declarator ELLIPSIS
    		 | InOut_opt BasicType Declarator ASSIGN AssignExpression
    		 | InOut_opt Type
    		 | InOut_opt Type ELLIPSIS
    '''
    Derivations.append(p.slice)

def p_InOut(p):
    '''InOut : InOutX
    	     | InOut InOutX
    '''
    Derivations.append(p.slice)

def p_InOutX(p):
    '''InOutX : AUTO
    	      | FINAL
    	      | SCOPE
    '''
    Derivations.append(p.slice)

def p_InOut_opt(p):
    '''InOut_opt : InOut
	  	 | empty
    '''
    Derivations.append(p.slice)


def p_MemberFunctionAttributes(p):
    '''MemberFunctionAttributes : MemberFunctionAttribute
    				| MemberFunctionAttribute MemberFunctionAttributes
    '''
    Derivations.append(p.slice)

def p_MemberFunctionAttributes_opt(p):
    '''MemberFunctionAttributes_opt : MemberFunctionAttributes
                                    | empty
    '''
    Derivations.append(p.slice)



def p_MemberFunctionAttribute(p):
    '''MemberFunctionAttribute : CONST
    		               | IMMUTABLE
    			       | RETURN
    '''
    Derivations.append(p.slice)
    
    

def p_FunctionBody(p):
    '''FunctionBody : BlockStatement
                    | BodyStatement
    '''
    Derivations.append(p.slice)
    

def p_BodyStatement(p):
    '''BodyStatement : BODY BlockStatement
    '''
    Derivations.append(p.slice)


def p_Symbol(p):
    ''' Symbol : SymbolTail
               | DOT SymbolTail
    '''
    Derivations.append(p.slice)

def p_SymbolTail(p):
    '''SymbolTail : IDENTIFIER
                  | IDENTIFIER DOT SymbolTail
    '''
    Derivations.append(p.slice)

def p_error(p):
    if p == None:
        print str(sys.argv[1])+" :: You missed something at the end"
    else:
    	print str(sys.argv[1])+" :: Syntax error in line no " + str(p.lineno)
        # Exit in case of error: Dont generate IR Code
        sys.exit(0)

def p_empty(p):
    'empty : %prec EMPTY'
    pass

# Build the abstract syntax parse tree
yacc.yacc(debug=True,start='Declaration_mult')
a=open(sys.argv[1],'r')
a=a.read()
data = ""
a+="\n"
yacc.parse(a)#, debug=True)

# Printing the identifiers stored in Symbol Table
for i in ST.table:
    print ST.table[i]
print ""
print ""

# Print the IR Code generated
OutputTAC()