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
arraylist = []
Listnonterminals=[]
Rderivation=[]
Derivations=[]
RightOutput = []
s_cond=0
s_label=0
stackbegin = []
stackend = []
param_list = []
Gloabl_Switch_Val=0
Gloabl_Switch_Label=0
is_class = False
flag = False
len_param = 0
FuncLabel=""
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
                        | IDENTIFIER Declarators SEMICOLON
    '''
    # print p[1],p[2], "FFFFFFFFFFF   DDDDDDDDDDDDDDDD"

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
    # print p.slice
    # p[0] = p[1]
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
    # print p.slice
    global arraylist

    global is_class
    p[0]=p[1]
    # print p[1]['place'],ST.currentscope,"::::::::::;"
    scope = ST.checkscope(p[1]['place'])
    # print scope
    currentscope = ST.currentscope
    if not is_class:
        if len(p)==4:
            # print p[0],":::::::::::"
            if "isarraylist" in p[3]:
                # print "Hi"
                # print p[3],"LLLLLLLLLLLL"
                p[0]['type'] = p[3]['type']
                if len(arraylist)>int(p[1]['size']):
                        print "Size of initializer list is greater than array size"
                        sys.exit(0)
                size = int(p[1]['size'])
                # print arraylist
                for i,j in enumerate(arraylist):
                    CreateTAC( '=',p[0]['place']+ST.currentscope+"["+ str(size-i-1) +"]",j, None )
                    # print '=',p[0]['place'],p[3]['place']
                    # scope = ST.checkscope(p[1]['place'])
                    # if p[1]['place'] in ST.table.keys():
                    if scope == currentscope:
                        print "Redeclaration of variable not allowed",p[1]['place']
                        sys.exit(0)
                    if p[1]['type']!=p[3]['type']:
                        print "Type error " + p[3]['type'] +" != " + p[1]['type']
                        sys.exit(0)
                    
                ST.addvar(p[0]['place'],p[0]['type'],"Array",p[1]['size'])
                return
            # print '=',p[0]['place'],p[3]['place']
            # scope = ST.checkscope(p[1]['place'])
            # if p[1]['place'] in ST.table.keys():
            # print p.slice, "::::::::::"

            if scope == currentscope:
                print "Redeclaration of variable not allowed",p[1]['place'], ST.table[scope]
                sys.exit(0)
            # print p[1],p[3]
            # print type(p[3])!=type({}) 

            if type(p[3])!=type({}):
                if p[1]['type']!=ST.getfunc_returntype(p[3]):
                    print "Type error " + ST.getfunc_returntype(p[3]) +" != " + p[1]['type']
                    sys.exit(0)    
                else:
                    ST.addvar(p[0]['place'],p[0]['type'],"Variable","4")
                    p[0]['type'] = ST.getfunc_returntype(p[3])
                    CreateTAC( '=',p[0]['place']+ST.currentscope,p[3], None )
                    return

            if p[1]['type']!=p[3]['type']:
                print ST.table[p[3]['place']],"KKKKKKKKKK"
                
                print "Type error " + p[3]['type'] +" != " + p[1]['type']
                sys.exit(0)
            ST.addvar(p[0]['place'],p[0]['type'],"Variable","4")
            p[0]['type'] = p[3]['type']

            if 'isconst' in p[3].keys():
                CreateTAC( '=',p[0]['place']+ST.currentscope,p[3]['place'], None )
            else:
                # print p[3],"{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{"
                if ST.checkscope(p[3]['place']):
                    CreateTAC( '=',p[0]['place']+ST.currentscope,p[3]['place']+ST.checkscope(p[3]['place']), None )
                else:
                    if 'isfunc' in p[3].keys():
                        CreateTAC( '=',p[0]['place']+ST.currentscope,p[3]['place']+".ret", None )
                        return
                    if 'scope' in p[3].keys():
                        CreateTAC( '=',p[0]['place']+ST.currentscope,p[3]['place']+p[3]['scope'], None)
                    else:
                        print p[3], " NOT DEFINED "
            return
        
        if len(p)==2:
            # if p[1]['place'] in ST.table.keys():
            if scope == currentscope:
                print "Redeclaration of variable not allowed",p[1]
                sys.exit(0)
        
        if (p[-1] in ['INT','CHAR']):
            ST.addvar(p[0]['place'],p[0]['type'],"Variable","4")
        
            # ST.addvar(p[1],p[-1],"Variable","4")
        else:
            # print ST.get_class_idlist(p[-1])
            _list = ST.get_class_idlist(p[-1])
            for ele in _list.keys():
                ST.addvar(p[1]['place']+"."+ele,_list[ele]['datatype'],"CLASS_VARIABLE","4")
                if ele in ST.table[p[-1]]['constructor'].keys():
                    CreateTAC("=",p[1]['place']+ST.currentscope+"."+ele,ST.table[p[-1]]['constructor'][ele]['value'],None)
        # return


        # print p[1],"LLLLLLLLLLLLLLLLLLL"

        if 'isarray' in p[1].keys():    
            ST.addvar(p[0]['place'],p[0]['type'],"Array",p[1]['size'])
            return
        else:
            ST.addvar(p[0]['place'],p[0]['type'],"Variable","4")
    else:
        if len(p)==4:
            if "isarraylist" in p[3]:
                p[0]['type'] = p[3]['type']
                if len(arraylist)>int(p[1]['size']):
                        print "Size of initializer list is greater than array size"
                        sys.exit(0)
                size = int(p[1]['size'])
                # print arraylist
                for i,j in enumerate(arraylist):
                    
                    # CreateTAC( '=',p[0]['place']+"["+ str(size-i-1) +"]",j, None )
                    
                    ST.addconstructor_class(is_class,p[0]['place']+"["+ str(size-i-1) +"]",j)
                    
                    # print scope, p[1]['place'],"((((((((((((((((((((((((((((("
                    if scope == currentscope:
                        print "Redeclaration of variable not allowed",p[1]['place']
                        sys.exit(0)
                    if p[1]['type']!=p[3]['type']:
                        print "Type error " + p[3]['type'] +" != " + p[1]['type']
                        sys.exit(0)
            
                ST.addvar(p[0]['place'],p[0]['type'],"Array",p[1]['size'])
                return
            # print p.slice, "::::::::::"

            if scope == currentscope:
                print "Redeclaration of variable not allowed",p[1]['place'], ST.table[scope]
                sys.exit(0)
            if type(p[3])!=type({}):
                if p[1]['type']!=ST.getfunc_returntype(p[3]):
                    print "Type error " + ST.getfunc_returntype(p[3]) +" != " + p[1]['type']
                    sys.exit(0)    
                else:
                    
                    ST.addvar(p[0]['place'],p[0]['type'],"Variable","4")
                    p[0]['type'] = ST.getfunc_returntype(p[3])
                    
                    # CreateTAC( '=',p[0]['place']+ST.currentscope,p[3], None )

                    ST.addconstructor_class(is_class,p[0]['place'],p[3])
                    
                    return
            
            if p[1]['type']!=p[3]['type']:
                print "Type error " + p[3]['type'] +" != " + p[1]['type']
                sys.exit(0)
            ST.addvar(p[0]['place'],p[0]['type'],"Variable","4")
            p[0]['type'] = p[3]['type']

            if 'isconst' in p[3].keys():

                # CreateTAC( '=',p[0]['place']+ST.currentscope,p[3]['place'], None )
                ST.addconstructor_class(is_class,p[0]['place'],p[3]['place'])
            
            else:
            
                # CreateTAC( '=',p[0]['place']+ST.currentscope,p[3]['place']+ST.currentscope, None )
                ST.addconstructor_class(is_class,p[0]['place'],p[3]['place']+"."+ST.currentscope)
            
            return
        
        if len(p)==2:
            if scope == currentscope:
                print "Redeclaration of variable not allowed",p[1]
                sys.exit(0)


        # print p[1],"LLLLLLLLLLLLLLLLLLL"

        if 'isarray' in p[1].keys():    
            ST.addvar(p[0]['place'],p[0]['type'],"Array",p[1]['size'])
            return
        else:
            ST.addvar(p[0]['place'],p[0]['type'],"Variable","4")
        # print ST.table[is_class]['constructor'],"vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"
            
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
    #     print p[3]
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
    scope = ST.checkscope(p[1])
    Derivations.append(p.slice) # rem template parameters from 2
    if len(p)==2:
        p[0]=p[1]
        # if p[1] in ST.table.keys():
        if scope==ST.currentscope:
            print "Redeclaration of variable not allowed",p[3]['place']
            sys.exit(0)
        else:
            if (p[-1] in ['INT','CHAR']):
                ST.addvar(p[1],p[-1],"Variable","4")
            else:
                # print ST.get_class_idlist(p[-1])
                _list = ST.get_class_idlist(p[-1])
                for ele in _list.keys():
                    ST.addvar(p[1]+"."+ele,_list[ele]['datatype'],"CLASS_VARIABLE","4")
                    # print ele,ST.table[p[-1]]['constructor'].keys(),"HIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII"
                    if ele in ST.table[p[-1]]['constructor'].keys():
                        CreateTAC("=",p[1]+"."+ele,ST.table[p[-1]]['constructor'][ele]['value'],None)
        return
    else:
        # print "HIIIIIIIIIIIIIIIIII"
        if "isconst" in p[3].keys():
            # print p[1], "HHHHHHHHHHHHHHHHHHHH"
            CreateTAC( '=', p[1]+ST.currentscope, p[3]['place'], None )
        else:
            CreateTAC( '=', p[1]+ST.currentscope, p[3]['place']+ST.currentscope, None )
        # print '=',p[1],p[3]['place']
        if p[3]['type'] == p[-1]:
            ST.addvar(p[1],p[-1],"Variable","4")
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
    # print p.slice
    if len(p)==4:
        p[0]={
            'place':p[2],
            'isarray':True,
            'type':p[-1],
            'size':p[3]['index']
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
    # print p.slice
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
    p[0]={}
    if len(p)==3:
        p[0]['index'] = "0"
        return
    if len(p)==4:
        p[0]['index'] = p[2]['place']
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

    if len(p)==4:
        p[0] = p[1]+"."+p[3]
        # print "HI",p[1],p[3]
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
    # print p.slice
    p[0]=p[1]
    Derivations.append(p.slice)

def p_NonVoidInitializer(p):
    '''NonVoidInitializer : ExpInitializer
                          | ArrayInitializer
    '''
    # print p.slice
    
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
    p[0] = p[2]
    # print p.slice
    
    Derivations.append(p.slice)

def p_ArrayMemberInitializations(p):
    '''ArrayMemberInitializations : ArrayMemberInitialization
    				  | ArrayMemberInitialization COMMA
    				  | ArrayMemberInitialization COMMA ArrayMemberInitializations
    '''
    p[0] = p[1]
    p[0]['isarraylist'] = True
    global arraylist
    arraylist.append(p[1]['place'])
    # print p[1],":::::::::"

    Derivations.append(p.slice)

def p_ArrayMemberInitializations_opt(p):
    '''ArrayMemberInitializations_opt : ArrayMemberInitializations
				      | empty
    '''
    p[0] = p[1]
    Derivations.append(p.slice)


def p_ArrayMemberInitialization(p):
    ''' ArrayMemberInitialization : NonVoidInitializer
    				 | AssignExpression COLON NonVoidInitializer
    '''
    p[0] = p[1]
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
    if(len(p)==2):
        p[0] = p[1]
        return
    # print "Problem is here"
    # newPlace="t_new2"
    # p[0]={'place':newPlace, 'type':"TYPE_ERROR"}
    # p[0]['place']=p[]
    if p[2][0]=='=':
        # print type(p[3]),"::::::" 
        if type(p[3])==type(""):
            if p[3] not in ST.table.keys():
                print "function not declared"+p[3]
                sys.exit(0)
            if p[1]['type'] == ST.getfunc_returntype(p[3]):
                CreateTAC( '=',p[1]['place']+ST.currentscope,p[3], None )
                p[0]=p[1]
                return
            else:
                print "type mismatch"+p[1]['type']+"!="+ST.getfunc_returntype(p[3])
                sys.exit(0)
        if p[1]['type']==p[3]['type']:
            name = p[1]['place']
            end =""
            if "[" in name:
                name = p[1]['place'].split("[")[0]
                end = "["+ p[1]['place'].split("[")[1]
            if "." in name:
                name = p[1]['place'].split(".")[0]
                end = "."+ p[1]['place'].split(".")[1]
            scope = ST.checkscope(name)
            if "isconst" in p[3].keys():
                CreateTAC( '=',name+scope+end,p[3]['place'], None )
            else:
                if '[' in p[1]['place'] or '[' in  p[3]['place']:
                    x=p[1]['place'].split("[")
                    y=p[3]['place'].split("[")
                    if len(y)==2:
                        CreateTAC( '=',x[0]+p[1]['scope']+"["+x[1],y[0]+p[3]['scope']+"["+y[1], None )
                    else:
                        CreateTAC( '=',x[0]+p[1]['scope']+"["+x[1],p[3]['place']+p[3]['scope'], None )                        
                else:                
                    CreateTAC( '=',p[1]['place']+p[1]['scope'],p[3]['place']+p[3]['scope'], None )
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
        name1 =  p[1]['place'].split("[")[0]
        end1 = ""
        if "[" in p[1]['place']:
            end1 = "["+p[1]['place'].split("[")[1]
        
        if "isconst" in p[3].keys():
            CreateTAC(p[2][0:2],name1+p[1]['scope']+end1,name1+p[1]['scope']+end1,p[3]['place'])
        else:
            name2 = p[3]['place'].split("[")[0]
            end2 = ""
            if "[" in p[3]['place']:
                end2 = "["+p[3]['place'].split("[")[1]
            CreateTAC(p[2][0:2],name1+p[1]['scope']+end1,name1+p[1]['scope']+end1,name2+p[3]['scope']+end2)
        return
    else:
        name =  p[1]['place']
        end = ""
        if "[" in p[1]['place']:
            name = p[1]['place'].split("[")[0]
            end = "["+p[1]['place'].split("[")[1]
        scope =  ST.checkscope(name)

        # print p[2][0],p[1]['place'],p[1]['place'],p[3]['place']
        if "isconst" in p[3].keys():
            CreateTAC(p[2][0],name+scope+end,name+scope+end,p[3]['place'])
        else:
            name2 = p[3]['place']
            end2 = ""
            if "[" in p[3]['place']:
                name2 = p[3]['place'].split("[")[0]
                end2 = "["+p[3]['place'].split("[")[1]
            scope2 =  ST.checkscope(name2)
            
            # print scope,scope2
            if 'scope' in p[3].keys():
                CreateTAC(p[2][0],name+scope+end,name+scope+end,name2+p[3]['scope'])
            else:
                CreateTAC(p[2][0],name+scope+end,name+scope+end,name2+scope2+end2)        
                        
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
            'type':'undefined',
            'scope':ST.currentscope
        }
        if "isconst"  in p[1].keys():
            x =  p[1]['place'] 
        else:
            if "[" not in p[1]['place']:
                x =  p[1]['place'] +  ST.currentscope
            else:
                name=p[1]['place'].split("[")[0]
                x = name + ST.checkscope(name)+"["+p[1]['place'].split("[")[1]            
        if "isconst" in p[3].keys():
            y =  p[3]['place']
            
        else:
            if "[" not in p[3]['place']:            
                y =  p[3]['place']  +  ST.currentscope 
            else:
                name=p[3]['place'].split("[")[0]
                y = name + ST.checkscope(name)+"["+p[3]['place'].split("[")[1]
        CreateTAC( p[2][0],newPlace+ ST.currentscope,x,y )
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
            'type':'undefined',
            'scope':ST.currentscope
        }
        if "isconst"  in p[1].keys():
            x =  p[1]['place'] 
        else:
            if "[" not in p[1]['place']:
                x =  p[1]['place'] +  ST.currentscope
            else:
                name=p[1]['place'].split("[")[0]
                x = name + ST.checkscope(name)+"["+p[1]['place'].split("[")[1]        
            
        if "isconst" in p[3].keys():
            y =  p[3]['place'] 
        else:
            if "[" not in p[3]['place']:            
                y =  p[3]['place']  +  ST.currentscope 
            else:
                name=p[3]['place'].split("[")[0]
                y = name + ST.checkscope(name)+"["+p[3]['place'].split("[")[1]
        CreateTAC( p[2][0],newPlace+ ST.currentscope,x,y )
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
    # print p.slice
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
        'type':'TYPE_ERROR',
        'scope':ST.currentscope
    }
    if p[1]['type'] == p[3]['type'] and p[1]['type']!='TYPE_ERROR': 
        if "isconst" in p[1].keys():
            x =  p[1]['place']  
        else:
            if "[" not in p[1]['place']:
                x =  p[1]['place'] +  ST.currentscope
            else:
                name=p[1]['place'].split("[")[0]
                x = name + ST.checkscope(name)+"["+p[1]['place'].split("[")[1]       
        if "isconst" in p[3].keys():
            y =  p[3]['place']  
        else:
            if "[" not in p[3]['place']:            
                y =  p[3]['place']  +  ST.currentscope 
            else:
                name=p[3]['place'].split("[")[0]
                y = name + ST.checkscope(name)+"["+p[3]['place'].split("[")[1]
        CreateTAC(p[2],p[0]['place']+ ST.currentscope,x,y)
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
        'type' : 'TYPE_ERROR',
        'scope': ST.currentscope
    }

    # if p[1]['place'] in ST.table.keys() and p[3]['place'] in ST.table.keys():
    if p[1]['type']=='TYPE_ERROR' or p[3]['type']=='TYPE_ERROR':
        print p[1],p[3],"TYPE_ERROR for p[1],p[3] ??"
        return

    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT' :
        # p[3] =ResolveRHSArray(p[3])
        # p[1] =ResolveRHSArray(p[1])
        # print p[2],newPlace,p[1]['place'],p[3]['place']
        if "isconst" in p[1].keys():
            x =  p[1]['place'] 
        else:
            if "[" not in p[1]['place']:
                x =  p[1]['place'] +  ST.currentscope
            else:
                name=p[1]['place'].split("[")[0]
                x = name + ST.checkscope(name)+"["+p[1]['place'].split("[")[1]

            
        if "isconst" in p[3].keys():
            y =  p[3]['place'] 
        else:
            if "[" not in p[3]['place']:            
                y =  p[3]['place']  +  ST.currentscope 
            else:
                name=p[3]['place'].split("[")[0]
                y = name + ST.checkscope(name)+"["+p[3]['place'].split("[")[1]
        CreateTAC(p[2],newPlace+ ST.currentscope,x,y)
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
    else:
        newPlace = ST.get_temp()
        p[0] = {
            'place' : newPlace,
            'type' : 'TYPE_ERROR',
            'scope': ST.currentscope
        }

        # if p[1]['place'] in ST.table.keys() and p[3]['place'] in ST.table.keys():
        if p[1]['type']=='TYPE_ERROR' or p[3]['type']=='TYPE_ERROR':
            print p[1],p[3],"TYPE_ERROR for p[1],p[3] ??"
            return

        if p[1]['type'] == 'INT' and p[3]['type'] == 'INT' :
            # p[3] =ResolveRHSArray(p[3])
            # p[1] =ResolveRHSArray(p[1])
            # print p[2],newPlace,p[1]['place'],p[3]['place']
            if "isconst" in p[1].keys():
                x =  p[1]['place'] 
            else:
                if "[" not in p[1]['place']:
                    x =  p[1]['place'] +  ST.currentscope
                else:
                    name=p[1]['place'].split("[")[0]
                    x = name + ST.checkscope(name)+"["+p[1]['place'].split("[")[1]

                
            if "isconst" in p[3].keys():
                y =  p[3]['place'] 
            else:
                if "[" not in p[3]['place']:            
                    y =  p[3]['place']  +  ST.currentscope 
                else:
                    name=p[3]['place'].split("[")[0]
                    y = name + ST.checkscope(name)+"["+p[3]['place'].split("[")[1]
            CreateTAC(p[2],newPlace+ ST.currentscope,x,y)
            p[0]['type'] = 'INT'

        else:
            print("Error: integer value is needed")
            sys.exit(0)
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
        'type' : 'TYPE_ERROR',
        'scope': ST.currentscope
    }

    # if p[1]['place'] in ST.table.keys() and p[3]['place'] in ST.table.keys():
    if p[1]['type']=='TYPE_ERROR' or p[3]['type']=='TYPE_ERROR':
        print p[1],p[3],"TYPE_ERROR for p[1],p[3] ??"
        return

    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT' :
        # p[3] =ResolveRHSArray(p[3])
        # p[1] =ResolveRHSArray(p[1])
        if "isconst" in p[1].keys():
            x =  p[1]['place'] 
        else:
            if 'isarray' in p[1].keys():
                x =  p[1]['place'].split("[")[0] + p[1]['scope'] +"["+p[1]['place'].split("[")[1] 
            else:
                x =  p[1]['place'] + p[1]['scope']                     
        if "isconst" in  p[3].keys():
            y =  p[3]['place']
        else:
            if 'isarray' in p[3].keys():
                y =  p[3]['place'].split("[")[0] + p[3]['scope'] +"["+p[3]['place'].split("[")[1]
            else:
                y =  p[3]['place'] + p[3]['scope'] 
        # print p[1],"::::::::::::;"
        CreateTAC( p[2],newPlace + ST.currentscope,x,y)
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
        # print p[0],"((((((((((((("
        return
    # print p.slice, "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    if len(p)==2 :
        p[0] = p[1]
        return
    newPlace = ST.get_temp()
    p[0] = {
        'place' : newPlace,
        'type' : 'TYPE_ERROR',
        'scope': ST.currentscope
    }
    if p[1]['type']=='TYPE_ERROR' or p[3]['type']=='TYPE_ERROR':
        return
    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT' :
        # p[3] =ResolveRHSArray(p[3])
        # p[1] =ResolveRHSArray(p[1])
        if "isconst" in p[1].keys():
            x =  p[1]['place'] 
        else:
            if 'isarray' in p[1].keys():
                x =  p[1]['place'].split("[")[0] + p[1]['scope'] +"["+p[1]['place'].split("[")[1] 
            else:
                x =  p[1]['place'] + p[1]['scope']                     
        if "isconst" in  p[3].keys():
            y =  p[3]['place']
        else:
            if 'isarray' in p[3].keys():
                y =  p[3]['place'].split("[")[0] + p[3]['scope'] +"["+p[3]['place'].split("[")[1]
            else:
                y =  p[3]['place'] + p[3]['scope'] 
        
        CreateTAC( p[2], newPlace+ ST.currentscope , x,y)         
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
    name =  p[2]['place']
    end = ""
    if "[" in p[2]['place']:
        name = p[2]['place'].split("[")[0]
        end = "["+p[2]['place'].split("[")[1]
    scope =  ST.checkscope(name)
    if len(p)==3:
        if p[1]=='++' or p[1]=='--':
            # if p[2]['place'] in ST.table.keys():
            if scope:    
                if p[2]['type'] == "INT":
                    CreateTAC( p[1][0],name+scope+end,name+scope+end,1 )
                    # print p[1][0],p[2]['place'],p[2]['place'],1
                    p[0] = p[2]
                    return
                else:
                    "Postfix operations possible only with integer variables"
            else:
                print "Variable "+p[2]['place']+" not defined "+p.slice
                return
        else:
            newplace = ST.get_temp()
            # print "HI", p[2]['scope']
            p[0] ={'place':newplace,'type':"INT",'scope':ST.currentscope}
            CreateTAC('=',newplace+ST.currentscope,p[1]+p[2]['place']+p[2]['scope'],None) 
    
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
    # print p.slice
    # print p[1], "PPPPPPPPPPPPPPPPPPPPPPPPP",p[-2]
    # if (p[1]['type'] != ST.table[p[-2]]['parameters'][p[1]['place']]['type'])

    param_list.append([p[1]['place'],p[1]['type']])
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
    
    # newPlace = ST.get_label()
    # CreateTAC()
    # p[0] = {
    #     'place':newPlace,
    #     'type':"TYPE_ERROR"
    # }
    # if len(p)==4:
    #     CreateTAC("")
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
    # print p.slice
    Derivations.append(p.slice)    #add index expression, slice expression 
    if len(p)==2 :
        p[0]=p[1]
        
        return

    if len(p)==3:
        # print "HI"
        # print p[1]['place'].strip("[")[0] , "HI"
        # if p[1]['place'] in ST.table.keys() or (p[1]["isarray"] and p[1]['place'].strip("[")[0] in ST.table.keys()):
        name =  p[1]['place']
        end = ""
        if "[" in p[1]['place']:
            name = p[1]['place'].split("[")[0]
            end = "["+p[1]['place'].split("[")[1]
        scope = ST.checkscope(name) 
        
        if (scope):
            if p[1]['type'] == "INT":
                CreateTAC( p[2][0],name+scope+end,name+scope+end,1 )
                # print p[2][0],p[1]['place'],p[1]['place'],1
                p[0] = p[1]
                return
            else:
                "Postfix operations possible only with integer variables"
        else:
            print "Variable "+p[1]['place']+" not defined "
            return
    if len(p)==6:
        u = p[1]
        if ((p[1] not in ST.table.keys()) and '.' in p[1]):
            print ST.currentscope
            objname = p[1].split(".")[0]
            scope = ST.checkscope(objname)
            # print ST.table[ST.currentscope].keys()
            u = ST.table[scope]['identifiers'][objname]['datatype']
            u = u+ '.'+p[1].split(".")[1]
            if u not in ST.table.keys():
                print "Error: function not defined"
        p[0] = {'place':u,'type':ST.getfunc_returntype(u),'isfunc':True}
    # print p[5]    

def p_JmpMark(p):
    '''
        JmpMark : empty
    '''
    # 'place': ST.table[p[-4]]['returnvar'],
    # scope = ST.checkscope(p[-4])
    scope=""
    if( p[-4] == 'writeln'):
        CreateTAC( "print_str", p[-2]['place'], None, None )
    else:
        global param_list
        # print "ajoop alien"
        # print ST.table[p[-4]]['parameters'], "oOOOOOOOOOOOOOOOOOOOOOO"
        u= p[-4]
        
        if ((p[-4] not in ST.table.keys()) and '.' in p[-4]):
            # print ST.currentscope
            objname = p[-4].split(".")[0]
            scope = ST.checkscope(objname)
            # print scope
            # print objname, ":::::::::::::"
            # print ST.table[ST.currentscope].keys()
            u = ST.table[scope]['identifiers'][objname]['datatype']
            u = u+ '.'+p[-4].split(".")[1]
            
        if u in ST.table.keys():
            # if scope:
            # newPlace = ST.get_temp()
            p[0]={
                'place':u,
                # 'type':ST.table[p[-4]]['datatype'] 
                'type':ST.table[u]['datatype']
            }

        else:
            print "FUNCTION not defined",scope
            sys.exit(0)
        i = 0
        for i,j in enumerate(param_list):
            if (len(param_list) != len(ST.table[u]['parameters'])):
                print "Number of arguments mismatch"
                sys.exit(0)
            if (ST.table[u]['parameters'][i]!= j[1]):
                print "Error type mismatch", ST.table[u]['parameters'][i],"!=" ,j[1], " in call to ",u
                sys.exit(0)
            if (j[0].isdigit()):
                CreateTAC("=",u+'_'+str(i),j[0],None)
            else:
                CreateTAC("=",u+'_'+str(i),j[0]+ST.currentscope,None)
                
        
        param_list = []
        k = i
        if "." in p[-4]:
            classname = u.split(".")[0]
            for j in ST.table[ST.table[classname]['child']]['identifiers']:
                CreateTAC("=",u+'_'+str(i+1),objname+scope+'.'+j,None)
                i = i+1
    
        CreateTAC( "call", u, None, None )
        i =k
        if "." in p[-4]:

            classname = u.split(".")[0]
            #scope = ST.checkscope(u)
            #print scope
            for j in ST.table[ST.table[classname]['child']]['identifiers']:
                CreateTAC("=",objname+scope+'.'+j,u+'_'+str(i+1),None)
                i = i+1
        

    # print "call ", p[-4]
    p[0]=p[-4]
    # print p.slice
    # print p[-2]

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
    Derivations.append(p.slice)
    
    if(len(p)==2):
        
        p[0] = {
        'place' : 'undefined',
        'type' : 'TYPE_ERROR',
        'scope':'None'
        }
        #Literals
        #if p.slice[1].type == 'FALSE' or 
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
            # print p[1],"::::::::::::::::"
            p[0]={
                'type':'STR',
                'place':p[1],
                'isconst':True
                }
            return

        # Identifiers
        
        if type(p[1])==type({}):
            if 'isarray' in p[1].keys():
                p[0] = p[1]
                return
            if 'isfunc' in p[1].keys():
                p[0] = p[1]
                return
            p[0]['place'] = p[1]['place']
            p[0]['type'] = p[1]['type']
            return
        # if p[1] in ST.table.keys():
        scope = ST.checkscope(p[1])

        if scope:
            p[0]['place'] = p[1]
            p[0]['type'] = ST.gettype(scope,p[1])
            p[0]['scope'] = scope
            # p[0]['type'] = ST.table[scope]['identifiers'][p[1]]['datatype']
            return
        
        else:

            #check parent scope if class function
            print('Error : undefined variable '+str(p[1])+' is used.')
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
        # newPlace = ST.get_temp()ArgumentList_op
        scope = ST.checkscope(p[1])
        # if p[1] in ST.table.keys():
        if scope:
            # print '*',newPlace,p[3],sizeof(p[0]['type'])
            if type(p[3])==type({}):
                p[0]={
                'place':p[1]+"["+ p[3]['place'] +"]",
                # 'type':ST.table[p[1]]['datatype'],
                'type':ST.gettype(scope,p[1]),
                'isarray':True,
                'scope':scope
                }
                # CreateTAC( '*', p[1]+"["+ p[3]['place'] +"]",None , None)
                # CreateTAC( '+', newPlace, newPlace, p[1] ) 
                # print '*',newPlace,p[3]['place'],'4'
                # print '+',newPlace,newPlace,p[1]
                return
            else:
                p[0]={
                'place':p[1]+"["+ p[3] +"]",
                # 'type':ST.table[p[1]]['datatype'],
                'type':ST.gettype(scope,p[1]),
                'isarray':True,
                'scope':scope
                }
                # CreateTAC( '*', newPlace, p[3], '4' )
                # CreateTAC( '+', newPlace, newPlace, p[1] ) 
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
    p[0] ={
        'place':p[1],
        'isfunc':True,
        'type':ST.getfunc_returntype()
    } 
    # print p.slice
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
        BlockStatement : LBRACE M_block_begin RBRACE M_block_end
                       | LBRACE M_block_begin StatementList RBRACE M_block_end
    '''
    Derivations.append(p.slice)

def p_M_block_begin(p):
    '''
        M_block_begin : 
    '''
    ST.newscope()
    global param_list,FuncLabel
    i = 0
    if len(param_list):
        for i,j in enumerate(param_list):
            CreateTAC( "=", j[0]+ST.currentscope, FuncLabel+'_'+str(i), None )
            # print i
            ST.addvar(j[0],j[1],"Variable","4")
    #print FuncLabel
    classname = FuncLabel.split(".")[0]
    global len_param
    len_param = i
    if "." in FuncLabel:
        for j in ST.table[ST.table[classname]['child']]['identifiers']:
            scope = ST.checkscope(j)
            #print j,scope,"::::::::::::"
            CreateTAC("=",j+scope,FuncLabel+'_'+str(i+1),None)
            i = i+1
    param_list = []
    
    Derivations.append(p.slice)


def p_M_block_end(p):
    '''
        M_block_end : empty
    '''
    # print FuncLabel,"hi"
    # classname = FuncLabel.split(".")[0]
    # i = p[-3]
    # if "." in FuncLabel:
    #     for j in ST.table[ST.table[classname]['child']]['identifiers']:
    #         scope = ST.checkscope(j)            
    #         CreateTAC("=",FuncLabel+'_'+str(i+1),j+scope,None)
    #         i = i+1
    
    ST.endscope()
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
    
    scope = ST.checkscope(p[-2]['place'])
    print p[-2],"HOOOOOOOOOOOOo"

    CreateTAC( "ifgoto_eq", Else_Label, p[-2]['place']+p[-2]['scope'], '0' )
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
        WhileStatement : WHILE LPAREN while_M0 Expression RPAREN while_M1 ScopeStatement while_M2
    '''
    Derivations.append(p.slice)

def p_while_M0(p):
    '''while_M0 : empty
    '''
    Repeat_Label =  ST.get_label()
    After_Label =  ST.get_label()

    CreateTAC( "label", Repeat_Label, None, None )
    global stackbegin
    global stackend
    stackend.append(After_Label)
    stackbegin.append(Repeat_Label)
    # print "label", Repeat_Label
    # print "ifgoto_eq", p[-2]['place'], "0", After_Label
    p[0]= [Repeat_Label, After_Label]
    
def p_while_M1(p):
    '''
        while_M1 : 
    '''
    CreateTAC( "ifgoto_eq", p[-3][1], p[-2]['place']+p[-2]['scope'], 0 )
    
def p_while_M2(p):
    '''
        while_M2 : 
    '''
    CreateTAC( "jmp", p[-5][0], None, None )
    CreateTAC( "label", p[-5][1], None, None )
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
    CreateTAC( "ifgoto_eq", p[-6][0], p[-2]['place']+p[-2]['scope'], 0)
    CreateTAC("label",p[-6][1],None,None)
    global stackbegin
    global stackend
    stackend.pop()
    stackbegin.pop()
    # print "ifgoto_eq", p[-2]['place'], "0", p[-6][0]

def p_ForStatement(p):
    '''
        ForStatement : FOR LPAREN Initialize for_test_mark Test_opt SEMICOLON for_M1 Increment_opt RPAREN for_M2 ScopeStatement for_M3
    '''
    # print p.slice
    Derivations.append(p.slice)

def p_for_test_mark(p):
    '''
        for_test_mark : empty
    '''
    TestLabel = ST.get_label()
    CreateTAC('label',TestLabel,None,None)
    p[0] = [TestLabel]

def p_for_M1(p):
    '''
        for_M1 :
    '''
    print p[-3]
    IncrLabel = ST.get_label()
    StatementLabel = ST.get_label()
    EndLabel = ST.get_label()

    if 'place' in p[-2].keys():
        CreateTAC( "ifgoto_eq", EndLabel, p[-2]['place']+p[-2]['scope'] ,0 )
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
    CreateTAC("jmp",p[-6][0],None,None)
    # CreateTAC( "ifgoto_eq", p[-3][2] , p[-5]['place'], 0  )
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

    # print FuncLabel+".ret"
    classname = FuncLabel.split(".")[0]
    print FuncLabel
    global len_param
    i = len_param
    if "." in FuncLabel:
        for j in ST.table[ST.table[classname]['child']]['identifiers']:
            scope = ST.checkscope(j)
            # print j,scope            
            CreateTAC("=",FuncLabel+'_'+str(i+1),j+scope,None)
            i = i+1
    CreateTAC("=",FuncLabel+".ret",p[2]['place']+p[2]['scope'],None)
    CreateTAC( 'ret', p[2]['place']+p[2]['scope'], None, None )    
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

    # print("Classes not handeld currently")
    # sys.exit(0)

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
    ''' AggregateBody : LBRACE AggBody_m1 DeclDefs_opt RBRACE AggBody_m2
    '''
    Derivations.append(p.slice) # might add Postblit                  

def p_AggBody_m1(p):
    '''AggBody_m1 : empty
    '''
    ST.newscope()
    # print "HI"
    
def p_AggBody_m2(p):
    '''AggBody_m2 : empty
    '''
    ST.endscope()
    
    # print "HI"

def p_ClassDeclaration(p):
    '''ClassDeclaration : CLASS IDENTIFIER SEMICOLON
                        | CLASS IDENTIFIER BaseClassList_opt class_m1 AggregateBody class_m2
    '''
    Derivations.append(p.slice)

def p_class_m1(p):
    '''class_m1 : empty
    '''
    global is_class
    is_class = p[-2]
    ST.addclass(is_class,"Class")

def p_class_m2(p):
    '''class_m2 : empty
    '''
    global is_class
    is_class = False


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
    '''FuncDeclaration  : StorageClasses_opt BasicType FuncDeclarator func_m1 FunctionBody func_m4 
                        | StorageClasses_opt BasicType FuncDeclarator func_m2 SEMICOLON 
    		            | AutoFuncDeclaration
    '''
    Derivations.append(p.slice)

def p_func_m1(p):
    '''func_m1 : empty
    '''
    # print p[-1]
    global is_class
    global FuncLabel
    if is_class != False:
        #FuncLabel = is_class+"."+ p[-1][0] # pass aprameters too
        #ST.addfunc_class(is_class,FuncLabel,p[-2],"class_func")
        #print ST.table[FuncLabel],">>>>>>>>>>>>>"
        global flag
        flag=is_class
        FuncLabel = is_class+'.'+p[-1][0]
        is_class = False

    else:
        FuncLabel = p[-1][0]
    #ST.addfunc(FuncLabel,"function",p[-2])
    CreateTAC( "label", FuncLabel, None, None )
    
    # global param_list
    # # print param_list, ".............."
    # for i,j in enumerate(param_list):
    #     CreateTAC( "=", j[0], FuncLabel+'_'+str(i), None )
    
    # param_list = []


def p_func_m4(p):
    '''func_m4 : empty
    '''
    global flag
    if (flag):
        global is_class
        is_class = flag
        flag = False


def p_func_m2(p):
    '''func_m2 : empty
    '''
    global param_list
    param_list = []

def p_AutoFuncDeclaration(p):
    '''AutoFuncDeclaration : StorageClasses IDENTIFIER FuncDeclaratorSuffix FunctionBody
    '''
    Derivations.append(p.slice)

def p_FuncDeclarator(p):
    '''FuncDeclarator : BasicType2_opt IDENTIFIER func_m3 FuncDeclaratorSuffix
    '''
    Derivations.append(p.slice)

    FuncLabel= p[2]
    # ST.addfunc(FuncLabel,"function",p[-1])
    # CreateTAC( "label", FuncLabel, None, None )
    # # print "label ", FuncLabel
    # p[0] = p[2]
    p[0] = [p[2]]


def p_func_m3(p):
    '''func_m3 : empty
    '''
    # print p[-1],">>>>>>>>>>>>>>>>>>>>"
    global is_class
    if (is_class):
        ST.addfunc_class(is_class,is_class+'.'+p[-1],p[-3],"class_func")
        ST.addfunc(is_class+'.'+p[-1],"class_func",p[-3],is_class)
        ST.currentscope = is_class+"."+p[-1]
    else:
        ST.addfunc(p[-1],"function",p[-3],None)
        ST.currentscope = p[-1]

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
    # param_list.append(p[1])
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
    # print p.slice
    global param_list
    param_list.append([p[3]['place'],p[2]])
    # print param_list,":::::::::::::::::"

    # p[0] = p[3]['place']
    # print p[-3],"jk"
    # ST.addvar(p[3]['place'],p[2],'variable','4')
    # print ST.currentscope,"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
    ST.table[ST.currentscope]['parameters'].append(p[2]) 
    # ST.table[ST.currentscope]['parameters']p[3]['place']['type'] = p[2] 

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
# for i in ST.table:
#     print ST.table[i]['name'],ST.table[i]['parentscope']
    # if 'parameters' in ST.table[i].keys(): 
    #     print ST.table[i]['identifiers'],"}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}"

    # for j in ST.table[i]['identifiers']:
    #     print ST.table[i]['identifiers'][j]
# print ""
# print ""

# Print the IR Code generated
OutputTAC()
