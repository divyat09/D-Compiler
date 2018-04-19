import ply.lex as lex
import sys
import ply.yacc as yacc
from lexer import tokens
import logging

nonterminals=[]
output=[]
countg = 0
revoutput=[]
finalout=[]

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
#    revoutput.append(p.slice) 

#def p_ProgramFile(p):
#    ''' ProgramFile : multiple_declaration
#    '''
#    revoutput.append(p.slice)

def p_Declaration_mult(p):
    ''' Declaration_mult : Declaration Declaration_mult
                         | empty
    '''
    revoutput.append(p.slice)

def p_DeclDefs(p):
    '''DeclDefs : DeclDef
                | DeclDef DeclDefs
    '''
    revoutput.append(p.slice)

def p_DeclDefs_opt(p):
    ''' DeclDefs_opt : DeclDefs
                     | empty
    '''
    revoutput.append(p.slice)

def p_DeclDef(p):
    '''DeclDef : AttributeSpecifier
    	       | Declaration
    	       | Allocator
    	       | Deallocator
    	       | AliasThis
    	       | MixinDeclaration
               | SEMICOLON
    '''
    revoutput.append(p.slice) #Postblit , | Constructor | Destructor

def p_ModuleFullyQualifiedName(p):
    ''' ModuleFullyQualifiedName : ModuleName
                                 | Packages DOT ModuleName
    '''
    revoutput.append(p.slice)

def p_ModuleName(p):
    '''
    ModuleName : IDENTIFIER
    '''
    revoutput.append(p.slice)
def p_Packages(p):
    ''' Packages : PackageName
                 | Packages DOT PackageName
    '''
    revoutput.append(p.slice)

def p_PackageName(p):
    '''PackageName : IDENTIFIER
    '''
    revoutput.append(p.slice)


def p_ImportDeclaration(p):
    '''
        ImportDeclaration : IMPORT ImportList SEMICOLON
     				      | STATIC IMPORT ImportList SEMICOLON
    '''
    revoutput.append(p.slice)
  
def p_ImportList(p):
    '''
        ImportList : Import
                   | ImportBindings
                   | Import COMMA ImportList
    '''
    revoutput.append(p.slice)

def p_Import(p):
    '''
        Import : ModuleFullyQualifiedName
               | ModuleAliasIdentifier ASSIGN ModuleFullyQualifiedName     
    '''
    revoutput.append(p.slice)






def p_ImportBindings(p):
    '''
        ImportBindings : Import COLON ImportBindList
    '''
    revoutput.append(p.slice)

def p_ImportBindList(p):
    '''
        ImportBindList : ImportBind
                       | ImportBind COMMA ImportBindList
    '''
    revoutput.append(p.slice)

def p_ImportBind(p):
    ''' 
        ImportBind : IDENTIFIER
                   | IDENTIFIER ASSIGN IDENTIFIER
    ''' 
    revoutput.append(p.slice)

def p_ModuleAliasIdentifier(p):
    '''
        ModuleAliasIdentifier : IDENTIFIER
    '''
    revoutput.append(p.slice)

def p_MixinDeclaration(p):
    '''
        MixinDeclaration : MIXIN LPAREN AssignExpression  RPAREN SEMICOLON
    '''
    revoutput.append(p.slice)

def p_Declaration(p):
    '''	Declaration : FuncDeclaration
    				| VarDeclarations 
    				| AliasDeclaration
    				| AggregateDeclaration
                    | EnumDeclaration
                    | ImportDeclaration
    '''
    revoutput.append(p.slice) 

def p_VarDeclarations(p):
    ''' VarDeclarations : StorageClasses_opt BasicType Declarators SEMICOLON
    '''
    revoutput.append(p.slice)

def p_Declarators(p):
    '''Declarators : DeclaratorInitializer
    		   | DeclaratorInitializer COMMA DeclaratorIdentifierList
    '''
    revoutput.append(p.slice)

def p_DeclaratorInitializer(p):
    '''DeclaratorInitializer : VarDeclarator
                     | VarDeclarator ASSIGN Initializer
    			     | AltDeclarator ASSIGN Initializer
    			     | AltDeclarator 
    '''
    revoutput.append(p.slice) # rem template parameters from 2

def p_DeclaratorIdentifierList(p):	
    ''' DeclaratorIdentifierList : DeclaratorIdentifier
    				 | DeclaratorIdentifier COMMA DeclaratorIdentifierList
    '''
    revoutput.append(p.slice)

def p_DeclaratorIdentifier(p):
    ''' DeclaratorIdentifier : VarDeclaratorIdentifier
    			     | AltDeclaratorIdentifier
    '''
    revoutput.append(p.slice)

def p_VarDeclaratorIdentifier(p):
    ''' VarDeclaratorIdentifier : IDENTIFIER
                                | IDENTIFIER ASSIGN Initializer
    '''
    revoutput.append(p.slice) # rem template parameters from 2

def p_AltDeclaratorIdentifier(p):
    ''' AltDeclaratorIdentifier : BasicType2 IDENTIFIER AltDeclaratorSuffixes_opt
				| BasicType2 IDENTIFIER AltDeclaratorSuffixes_opt ASSIGN Initializer
				| BasicType2_opt IDENTIFIER AltDeclaratorSuffixes
				| BasicType2_opt IDENTIFIER AltDeclaratorSuffixes ASSIGN Initializer
    '''
    revoutput.append(p.slice)

def p_Declarator(p):
    '''Declarator : VarDeclarator
		  | AltDeclarator
    '''
    revoutput.append(p.slice)

def p_VarDeclarator(p):
    '''VarDeclarator : BasicType2_opt IDENTIFIER
    '''
    revoutput.append(p.slice)

def p_AltDeclarator(p):
    '''AltDeclarator : BasicType2_opt IDENTIFIER AltDeclaratorSuffixes
    		     | BasicType2_opt LPAREN AltDeclaratorX RPAREN
                 | BasicType2_opt LPAREN AltDeclaratorX RPAREN AltFuncDeclaratorSuffix
    		     | BasicType2_opt LPAREN AltDeclaratorX RPAREN AltDeclaratorSuffixes
    '''
    revoutput.append(p.slice) #| BasicType2_opt LPAREN AltDeclaratorX RPAREN AltFuncDeclaratorSuffix


def p_AltDeclaratorX(p):
    '''AltDeclaratorX : BasicType2_opt IDENTIFIER
                      | BasicType2_opt IDENTIFIER AltFuncDeclaratorSuffix
		              | AltDeclarator
    '''
    revoutput.append(p.slice) # add | BasicType2_opt IDENTIFIER AltFuncDeclaratorSuffix

def p_AltDeclaratorSuffixes(p):
    '''AltDeclaratorSuffixes : AltDeclaratorSuffix
    			             | AltDeclaratorSuffix AltDeclaratorSuffixes
    '''
    revoutput.append(p.slice)

def p_AltDeclaratorSuffixes_opt(p):
    '''AltDeclaratorSuffixes_opt : AltDeclaratorSuffixes 
				 | empty
    '''
    revoutput.append(p.slice)

def p_AltDeclaratorSuffix(p):
    '''AltDeclaratorSuffix : LBRACKET RBRACKET
    			   | LBRACKET AssignExpression RBRACKET
    			   | LBRACKET Type RBRACKET
    '''
    revoutput.append(p.slice)

def p_AltFuncDeclaratorSuffix(p):
    '''AltFuncDeclaratorSuffix : Parameters MemberFunctionAttributes_opt
    '''
    revoutput.append(p.slice)


def p_Type(p):
    ''' Type : BasicType BasicType2_opt
    '''
    revoutput.append(p.slice)

def p_Type_opt(p):
    ''' Type_opt : Type
                 | empty
    '''
    revoutput.append(p.slice)    


def p_BasicType(p):
    '''BasicType : BasicTypeX
    		  | DOT IdentifierList
    		  | IdentifierList
    		  | Typeof
    		  | Typeof DOT IdentifierList
    '''
    revoutput.append(p.slice)

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
    revoutput.append(p.slice)

def p_BasicType2(p):
    '''BasicType2 : BasicType2X BasicType2_opt
    '''
    revoutput.append(p.slice)

def p_BasicType2_opt(p):
    ''' BasicType2_opt : BasicType2
		       | empty
    '''
    revoutput.append(p.slice)

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
    revoutput.append(p.slice)

def p_IdentifierList(p):
    '''IdentifierList : IDENTIFIER
    		      | IDENTIFIER DOT IdentifierList
    		      | IDENTIFIER LBRACKET AssignExpression RBRACKET DOT IdentifierList
    '''
    revoutput.append(p.slice)
#TemplateInstance
    #TemplateInstance . IdentifierList

def p_StorageClasses(p):
    '''StorageClasses : StorageClass
    		      | StorageClass StorageClasses
    '''
    revoutput.append(p.slice)


def p_StorageClass(p):
    '''StorageClass : ENUM
    		    | STATIC
    		    | EXTERN
    		    | FINAL
    		    | AUTO
    		    | CONST
    		    | IMMUTABLE
    '''
    revoutput.append(p.slice)

def p_Initializer(p):
    '''Initializer : VoidInitializer
    		   | NonVoidInitializer
    '''
    revoutput.append(p.slice)

def p_NonVoidInitializer(p):
    '''NonVoidInitializer : ExpInitializer
                          | ArrayInitializer
    '''
    revoutput.append(p.slice)

def p_ExpInitializer(p):
    '''ExpInitializer : AssignExpression
    '''
    revoutput.append(p.slice)

def p_ArrayInitializer(p):
    '''ArrayInitializer : LBRACKET ArrayMemberInitializations_opt RBRACKET
    '''
    revoutput.append(p.slice)

def p_ArrayMemberInitializations(p):
    '''ArrayMemberInitializations : ArrayMemberInitialization
    				  | ArrayMemberInitialization COMMA
    				  | ArrayMemberInitialization COMMA ArrayMemberInitializations
    '''
    revoutput.append(p.slice)

def p_ArrayMemberInitializations_opt(p):
    '''ArrayMemberInitializations_opt : ArrayMemberInitializations
				      | empty
    '''
    revoutput.append(p.slice)


def p_ArrayMemberInitialization(p):
    ''' ArrayMemberInitialization : NonVoidInitializer
    				 | AssignExpression COLON NonVoidInitializer
    '''
    revoutput.append(p.slice)

def p_AutoDeclaration(p):
    '''
        AutoDeclaration :  StorageClasses AutoDeclarationX SEMICOLON
    '''
    revoutput.append(p.slice)

def p_AutoDeclarationX(p):
    '''
        AutoDeclarationX : AutoDeclarationY    
                         | AutoDeclarationX COMMA AutoDeclarationY
    ''' 
    revoutput.append(p.slice)

def p_AutoDeclarationY(p):
    '''
        AutoDeclarationY : IDENTIFIER ASSIGN Initializer
    '''    
    revoutput.append(p.slice)

def p_StorageClasses_opt(p):
    '''
        StorageClasses_opt : StorageClasses
                           | empty 
    '''
    revoutput.append(p.slice)

def p_AliasDeclaration(p):
    '''
        AliasDeclaration : ALIAS StorageClasses_opt BasicType Declarators SEMICOLON 
                         | ALIAS StorageClasses_opt BasicType FuncDeclarator SEMICOLON
                         | ALIAS AliasDeclarationX  SEMICOLON
    '''
    revoutput.append(p.slice)

def p_AliasDeclarationX(p):
    '''
        AliasDeclarationX : AliasDeclarationY
                          | AliasDeclarationX COMMA AliasDeclarationY
    '''
    revoutput.append(p.slice)

def p_AliasDeclarationY(p):
    '''
        AliasDeclarationY : IDENTIFIER ASSIGN StorageClasses_opt Type
                          | IDENTIFIER ASSIGN FunctionLiteral 
    '''
    revoutput.append(p.slice)
        

def p_Typeof(p):
    ''' Typeof : TYPEOF LPAREN Expression RPAREN
              | TYPEOF LPAREN RETURN RPAREN
    '''
    revoutput.append(p.slice)

def p_VoidInitializer(p):
    'VoidInitializer : VOID' 
    revoutput.append(p.slice)

def p_AttributeSpecifier(p):
    ''' 
        AttributeSpecifier : Attribute COLON
                           | Attribute DeclarationBlock
    '''
    revoutput.append(p.slice)

def p_Attribute(p):
    '''
        Attribute : VisibilityAttribute
    '''
    revoutput.append(p.slice)

def p_DeclarationBlock(p):
    ''' DeclarationBlock : DeclDef
                         | LBRACE DeclDefs_opt RBRACE
    '''
    revoutput.append(p.slice)  


def p_VisibilityAttribute(p):
    '''
        VisibilityAttribute : PRIVATE 
                         | PROTECTED 
                         | PUBLIC 
    '''    
    revoutput.append(p.slice)
    
def p_Expression(p):
    ''' Expression : CommaExpression
    '''
    revoutput.append(p.slice) 

def p_CommaExpression(p):
    '''CommaExpression : AssignExpression
                       | AssignExpression COMMA CommaExpression
    '''
    revoutput.append(p.slice) 

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
    revoutput.append(p.slice)  # add eq_power


def p_ConditionalExpression(p):
    '''ConditionalExpression : OrOrExpression
    			     | OrOrExpression QUESTION Expression COLON ConditionalExpression
    '''
    revoutput.append(p.slice) 

def p_OrOrExpression(p):
    '''OrOrExpression : AndAndExpression
    		      | OrOrExpression DOUBLE_PIPE AndAndExpression
    '''
    revoutput.append(p.slice) 

def p_AndAndExpression(p):
    '''AndAndExpression : OrExpression
    			| AndAndExpression DOUBLE_AMPERSAND OrExpression
    '''
    revoutput.append(p.slice) 

def p_OrExpression(p):
    '''OrExpression : XorExpression
    		    | OrExpression PIPE XorExpression
    '''
    revoutput.append(p.slice) 

def p_XorExpression(p):
    '''XorExpression : AndExpression
    		     | XorExpression CARET AndExpression
    '''
    revoutput.append(p.slice) 

def p_AndExpression(p):
    '''AndExpression : CmpExpression
    		     | AndExpression AMPERSAND CmpExpression
    '''
    revoutput.append(p.slice) 

def p_CmpExpression(p):
    '''CmpExpression : ShiftExpression
    		     | EqualExpression
		     | RelExpression
    '''
    revoutput.append(p.slice) 

def p_EqualExpression(p):
    '''EqualExpression : ShiftExpression IS_EQ ShiftExpression
    		       | ShiftExpression NOT_EQ ShiftExpression
    '''
    revoutput.append(p.slice) 

def p_RelExpression(p):
    '''RelExpression : ShiftExpression LESS ShiftExpression
                     | ShiftExpression GREATER_EQ ShiftExpression
                     | ShiftExpression GREATER ShiftExpression
                     | ShiftExpression LESS_EQ ShiftExpression
    '''
    revoutput.append(p.slice) 

def p_ShiftExpression(p):
    ''' ShiftExpression : AddExpression
    			| ShiftExpression LEFT_SHIFT AddExpression
    			| ShiftExpression RIGHT_SHIFT AddExpression
    '''
    revoutput.append(p.slice) 

def p_AddExpression(p):
    '''AddExpression : MulExpression
    		     | AddExpression PLUS MulExpression
    		     | AddExpression MINUS MulExpression
    '''
    revoutput.append(p.slice)  # might add catexprssion
def p_MulExpression(p):
    '''MulExpression : UnaryExpression
    		     | MulExpression TIMES UnaryExpression
    		     | MulExpression DIV UnaryExpression
    		     | MulExpression MODULO UnaryExpression
    '''
    revoutput.append(p.slice) 

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
    revoutput.append(p.slice)     

def p_ComplementExpression(p):
    '''ComplementExpression : TILDE UnaryExpression
    '''
    revoutput.append(p.slice)     

    
def p_NewExpression(p):
    '''NewExpression : NEW AllocatorArguments_opt Type
    		     | NewExpressionWithArgs
    '''
    revoutput.append(p.slice)  

def p_NewExpressionWithArgs(p):
    '''NewExpressionWithArgs : NEW AllocatorArguments_opt Type LBRACKET AssignExpression RBRACKET
    			     | NEW AllocatorArguments_opt Type LPAREN ArgumentList_opt RPAREN
                     | NewAnonClassExpression
    '''
    revoutput.append(p.slice) 

def p_AllocatorArguments(p): 
    '''AllocatorArguments : LPAREN ArgumentList_opt RPAREN
    '''
    revoutput.append(p.slice)  
    
def p_AllocatorArguments_opt(p):
    '''AllocatorArguments_opt : AllocatorArguments
			      | empty
    '''
    revoutput.append(p.slice) 

def p_ArgumentList_opt(p):
    '''ArgumentList_opt : ArgumentList
			| empty
    '''
    revoutput.append(p.slice) 

def p_ArgumentList(p):
    '''ArgumentList : AssignExpression
    		    | AssignExpression COMMA
    		    | AssignExpression COMMA ArgumentList
    '''
    revoutput.append(p.slice)  

def p_CastExpression(p):
    '''CastExpression : CAST LPAREN Type RPAREN UnaryExpression
    		      | CAST LPAREN RPAREN UnaryExpression
                 
    '''
    revoutput.append(p.slice)     


def p_PowExpression(p):
    '''PowExpression : PostfixExpression
                     | PostfixExpression POWER UnaryExpression
    '''
    revoutput.append(p.slice)     


def p_PostfixExpression(p):
    '''PostfixExpression : PrimaryExpression
    			         | PostfixExpression DOT IDENTIFIER
                         | PostfixExpression DOT NewExpression
                         | PostfixExpression PLUS_PLUS %prec POST_PLUS_PLUS
                         | PostfixExpression MINUS_MINUS %prec POST_MINUS_MINUS
                         | PostfixExpression LPAREN ArgumentList RPAREN
                         | BasicType LPAREN ArgumentList_opt RPAREN                                  
    '''
    revoutput.append(p.slice)    #add index expression, slice expression 

def p_PrimaryExpression(p):
    ''' PrimaryExpression : IDENTIFIER
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
    revoutput.append(p.slice) 
    
def p_ArrayLiteral(p):
    '''ArrayLiteral : LBRACKET ArgumentList_opt RBRACKET
                    | IDENTIFIER LBRACKET INUMBER RBRACKET
                    | IDENTIFIER LBRACKET AssignExpression RBRACKET
    '''
    revoutput.append(p.slice)

def p_FunctionLiteral(p):
    ''' FunctionLiteral : FUNCTION Type_opt ParameterAttributes_opt FunctionLiteralBody
                        | ParameterMemberAttributes FunctionLiteralBody
                        | FunctionLiteralBody
    '''
    revoutput.append(p.slice)

def p_ParameterAttributes(p):
    ''' ParameterAttributes : Parameters
    '''
    revoutput.append(p.slice)

def p_ParameterAttributes_opt(p):
    ''' ParameterAttributes_opt : ParameterAttributes_opt
                                | empty
    '''         
    revoutput.append(p.slice)

def p_ParameterMemberAttributes(p):
    ''' ParameterMemberAttributes : Parameters MemberFunctionAttributes_opt
    '''
    revoutput.append(p.slice) 

def p_FunctionLiteralBody(p):
    '''FunctionLiteralBody : BlockStatement
                           | BodyStatement
    '''
    revoutput.append(p.slice) # contracts 

def p_LIT_STRPlus(p):
    '''LIT_STRPlus : LIT_STR LIT_STRPlus
                   | LIT_STR
    '''
    revoutput.append(p.slice) 
 
def p_MixinExpression(p):
    '''MixinExpression : MIXIN LPAREN AssignExpression RPAREN
    '''
    revoutput.append(p.slice)
       
def p_ImportExpression(p):
    '''ImportExpression : IMPORT LPAREN AssignExpression RPAREN
    '''
    revoutput.append(p.slice) 

def p_TypeidExpression(p):
    '''
        TypeidExpression : TYPEID LPAREN Type RPAREN
                          | TYPEID LPAREN Expression RPAREN
    '''
    revoutput.append(p.slice) 
    
def p_Statement(p):
    '''
        Statement : SEMICOLON
                  | NonEmptyStatement
                  | ScopeBlockStatement   
    '''
    revoutput.append(p.slice)

def p_NoScopeNonEmptyStatement(p):
    '''
        NoScopeNonEmptyStatement : NonEmptyStatement
                                 | BlockStatement   
    '''
    revoutput.append(p.slice) 
    
def p_NoScopeStatement(p):
    '''
        NoScopeStatement : SEMICOLON
                         | NonEmptyStatement    
                         | BlockStatement
    '''
    revoutput.append(p.slice) 

def p_NonEmptyOrScopeBlockStatement(p):
    '''
        NonEmptyOrScopeBlockStatement : NonEmptyStatement
                                      | ScopeBlockStatement      
    '''
    revoutput.append(p.slice) 

def p_NonEmptyStatement(p):
    '''
        NonEmptyStatement : NonEmptyStatementNoCaseNoDefault
                          | CaseStatement
                          | CaseRangeStatement    
                          | DefaultStatement
    '''
    revoutput.append(p.slice) 

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
    revoutput.append(p.slice)

def p_ScopeStatement(p):
    '''
        ScopeStatement : NonEmptyStatement
                       | BlockStatement
    '''
    revoutput.append(p.slice)

def p_ScopeBlockStatement(p):
    '''
        ScopeBlockStatement : BlockStatement
    '''
    revoutput.append(p.slice)

def p_LabeledStatement(p):
    '''
        LabeledStatement : IDENTIFIER COLON
                         | IDENTIFIER COLON NoScopeStatement
                         | IDENTIFIER COLON Statement
    '''
    revoutput.append(p.slice)

def p_BlockStatement(p):
    '''
        BlockStatement : LBRACE RBRACE
                       | LBRACE StatementList RBRACE
    '''
    revoutput.append(p.slice)

def p_StatementList(p):
    '''
        StatementList : Statement
                      | Statement StatementList
    '''
    revoutput.append(p.slice)

def p_ExpressionStatement(p):
    '''
        ExpressionStatement : Expression SEMICOLON
    '''
    revoutput.append(p.slice)

def p_DeclarationStatement(p):
    '''
        DeclarationStatement : Declaration
                             | StorageClasses Declaration
    '''
    revoutput.append(p.slice)

def p_IfStatement(p):
    '''
        IfStatement : IF LPAREN IfCondition RPAREN ThenStatement
                    | IF LPAREN IfCondition RPAREN ThenStatement ELSE ElseStatement
    '''
    revoutput.append(p.slice)

def p_IfCondition(p):
    '''
        IfCondition : Expression
                    | AUTO IDENTIFIER ASSIGN Expression
                    | BasicType Declarator ASSIGN Expression                    
    '''
    revoutput.append(p.slice)

def p_ThenStatement(p):
    '''
        ThenStatement : ScopeStatement
    '''
    revoutput.append(p.slice)

def p_ElseStatement(p):
    '''
        ElseStatement : ScopeStatement
    '''
    revoutput.append(p.slice)

def p_WhileStatement(p):
    '''
        WhileStatement : WHILE LPAREN Expression  RPAREN ScopeStatement 
    '''
    revoutput.append(p.slice)

def p_DoStatement(p):
    '''
        DoStatement : DO ScopeStatement WHILE LPAREN Expression  RPAREN 
    '''
    revoutput.append(p.slice)

def p_ForStatement(p):
    '''
        ForStatement : FOR LPAREN Initialize Test_opt SEMICOLON Increment_opt RPAREN ScopeStatement 
    '''
    revoutput.append(p.slice)

def p_Initialize(p):
    '''
        Initialize : SEMICOLON
                   | NoScopeNonEmptyStatement
    '''
    revoutput.append(p.slice)

def p_Test(p):
    ''' 
        Test : Expression
    '''
    revoutput.append(p.slice)

def p_Test_opt(p):
    ''' 
        Test_opt : Test
                 | empty
    '''
    revoutput.append(p.slice)


def p_Increment(p):
    '''
        Increment : Expression
    '''
    revoutput.append(p.slice)

def p_Increment_opt(p):
    '''
        Increment_opt : Increment
                      | empty
    '''
    revoutput.append(p.slice)


def p_AggregateForeach(p):
    '''
        AggregateForeach : Foreach LPAREN ForeachTypeList SEMICOLON ForeachAggregate RPAREN
    '''
    revoutput.append(p.slice)

def p_ForeachStatement(p):
    '''
        ForeachStatement : AggregateForeach NoScopeNonEmptyStatement
    '''
    revoutput.append(p.slice)

def p_Foreach(p):
    '''
        Foreach : FOREACH 
                | FOREACH_REVERSE
    '''
    revoutput.append(p.slice)

def p_ForeachTypeList(p):
    '''
        ForeachTypeList : ForeachType
                        | ForeachType COMMA ForeachTypeList
    '''
    revoutput.append(p.slice)

def p_ForeachType(p):
    '''
        ForeachType : ForeachTypeAttributes_opt BasicType Declarator
                    | ForeachTypeAttributes_opt IDENTIFIER
                    | ForeachTypeAttributes_opt ALIAS IDENTIFIER 
    '''
    revoutput.append(p.slice)

def p_ForeachTypeAttributes_opt(p):
    '''
        ForeachTypeAttributes_opt : ForeachTypeAttributes 
                                  | empty
    '''
    revoutput.append(p.slice)
  
def p_ForeachTypeAttributes(p):
    '''
        ForeachTypeAttributes : ForeachTypeAttribute
                             | ForeachTypeAttribute ForeachTypeAttributes_opt
    '''
    revoutput.append(p.slice)

def p_ForeachTypeAttribute(p):
    '''
        ForeachTypeAttribute : ENUM
    '''
    revoutput.append(p.slice)


def p_ForeachAggregate(p):
    '''
        ForeachAggregate : Expression
    '''
    revoutput.append(p.slice)

def p_RangeForeach(p):
    '''
        RangeForeach : LPAREN  ForeachType SEMICOLON LwrExpression RANGE UprExpression RPAREN
    '''
    revoutput.append(p.slice)

def p_LwrExpression(p):
    '''
        LwrExpression : Expression
    '''
    revoutput.append(p.slice)

def p_UprExpression(p):
    '''
        UprExpression : Expression
    '''
    revoutput.append(p.slice)

def p_ForeachRangeStatement(p):
    '''
        ForeachRangeStatement : RangeForeach ScopeStatement
    '''
    revoutput.append(p.slice)

def p_SwitchStatement(p):
    '''
        SwitchStatement : SWITCH LPAREN Expression RPAREN ScopeStatement
    '''
    revoutput.append(p.slice)

def p_CaseStatement(p):
    '''
        CaseStatement : CASE ArgumentList COLON ScopeStatementList
    '''
    revoutput.append(p.slice)

def p_CaseRangeStatement(p):
    '''
        CaseRangeStatement : CASE FirstExp COLON RANGE LastExp COLON ScopeStatementList
    '''
    revoutput.append(p.slice)

def p_FirstExp(p):
    '''
        FirstExp : AssignExpression
    '''
    revoutput.append(p.slice)

def p_LastExp(p):
    '''
        LastExp : AssignExpression
    '''
    revoutput.append(p.slice)

def p_DefaultStatement(p):
    '''
        DefaultStatement : DEFAULT COLON ScopeStatementList
    '''
    revoutput.append(p.slice)

def p_ScopeStatementList(p):
    '''
        ScopeStatementList : StatementListNoCaseNoDefault
    '''
    revoutput.append(p.slice)

def p_StatementListNoCaseNoDefault(p):
    '''
        StatementListNoCaseNoDefault : StatementNoCaseNoDefault
                                     | StatementNoCaseNoDefault StatementListNoCaseNoDefault
    '''
    revoutput.append(p.slice)

def p_StatementNoCaseNoDefault(p):
    ''' 
        StatementNoCaseNoDefault : SEMICOLON
                                 | NonEmptyStatementNoCaseNoDefault
                                 | ScopeBlockStatement
    '''
    revoutput.append(p.slice)

def p_FinalSwitchStatement(p):
    '''
        FinalSwitchStatement : FINAL SWITCH LPAREN Expression RPAREN ScopeStatement
    '''
    revoutput.append(p.slice)

def p_IDENTIFIER_opt(p):
    '''
        IDENTIFIER_opt : IDENTIFIER
                       | empty
    '''
    revoutput.append(p.slice)

def p_Expression_opt(p):
    '''
        Expression_opt : Expression
                       | empty
    '''
    revoutput.append(p.slice)

def p_ContinueStatement(p):
    '''
        ContinueStatement : CONTINUE IDENTIFIER_opt SEMICOLON
    '''
    revoutput.append(p.slice)

def p_BreakStatement(p):
    '''
        BreakStatement : BREAK IDENTIFIER_opt SEMICOLON
    '''
    revoutput.append(p.slice)

def p_ReturnStatement(p):
    '''
        ReturnStatement : RETURN Expression_opt SEMICOLON
    '''
    revoutput.append(p.slice)

def p_GotoStatement(p):
    '''
        GotoStatement : GOTO IDENTIFIER SEMICOLON
                      | GOTO DEFAULT SEMICOLON
                      | GOTO CASE SEMICOLON
                      | GOTO CASE Expression SEMICOLON
    '''
    revoutput.append(p.slice)
    
def p_WithStatement(p):
    '''
        WithStatement : WITH LPAREN Expression RPAREN ScopeStatement
                      | WITH LPAREN Symbol RPAREN ScopeStatement

    '''
    revoutput.append(p.slice) # | WITH LPAREN TemplateInstance RPAREN ScopeStatement   

def p_MixinStatement(p):
    '''
        MixinStatement : MIXIN LPAREN AssignExpression RPAREN SEMICOLON
    ''' 
    revoutput.append(p.slice)

def p_AggregateDeclaration(p):
    '''AggregateDeclaration : ClassDeclaration
    			    | UnionDeclaration
    '''
    revoutput.append(p.slice) 

def p_UnionDeclaration(p):
    '''UnionDeclaration : UNION IDENTIFIER SEMICOLON
    			| UNION IDENTIFIER AggregateBody
    			| AnonUnionDeclaration
    '''
    revoutput.append(p.slice) 

def p_AnonUnionDeclaration(p):
    ''' AnonUnionDeclaration : UNION AggregateBody
    '''
    revoutput.append(p.slice) 

def p_AggregateBody(p):
    ''' AggregateBody : LBRACE DeclDefs_opt RBRACE
    '''
    revoutput.append(p.slice) # might add Postblit                  
    
def p_ClassDeclaration(p):
    '''ClassDeclaration : CLASS IDENTIFIER SEMICOLON
                        | CLASS IDENTIFIER BaseClassList_opt AggregateBody
    '''
    revoutput.append(p.slice)

def p_BaseClassList(p):
    '''BaseClassList : COLON SuperClass
	             | COLON SuperClass COMMA Interfaces
    		     | COLON Interfaces
    '''
    revoutput.append(p.slice)

def p_BaseClassList_opt(p):
    '''BaseClassList_opt : BaseClassList
                         | empty
    '''
    revoutput.append(p.slice)

def p_SuperClass(p):
    '''SuperClass : BasicType
    '''
    revoutput.append(p.slice)

def p_Interfaces(p):
    '''Interfaces : Interface
    		  | Interface COMMA Interfaces
    '''
    revoutput.append(p.slice)

def p_Interface(p):
    'Interface : BasicType'
    revoutput.append(p.slice)



def p_Allocator(p):
    '''Allocator : NEW Parameters SEMICOLON
    		 | NEW Parameters FunctionBody
    '''
    revoutput.append(p.slice)

def p_Deallocator(p):
    '''Deallocator : DELETE Parameters SEMICOLON
    		   | DELETE Parameters FunctionBody
    '''
    revoutput.append(p.slice)

def p_AliasThis(p):
    '''AliasThis : ALIAS IDENTIFIER THIS SEMICOLON
    '''
    revoutput.append(p.slice)

def p_NewAnonClassExpression(p):
    '''NewAnonClassExpression : NEW AllocatorArguments_opt CLASS ClassArguments_opt SuperClass_opt Interfaces_opt AggregateBody
    '''
    revoutput.append(p.slice)

def p_ClassArguments(p):
    '''ClassArguments : LPAREN ArgumentList_opt RPAREN
    '''
    revoutput.append(p.slice)

def p_ClassArguments_opt(p):
    '''ClassArguments_opt : ClassArguments
		          | empty
    '''
    revoutput.append(p.slice)

def p_SuperClass_opt(p):
    '''SuperClass_opt : SuperClass 
		              | empty
    '''
    revoutput.append(p.slice)

def p_Interfaces_opt(p):
    '''Interfaces_opt : Interfaces
		      | empty
    '''
    revoutput.append(p.slice)

def p_EnumDeclaration(p):
    '''
        EnumDeclaration : ENUM IDENTIFIER EnumBody
                        | ENUM IDENTIFIER COLON EnumBaseType EnumBody
                        | AnonymousEnumDeclaration
    '''
    revoutput.append(p.slice)

def p_EnumBaseType(p):
    '''
        EnumBaseType : Type
    '''
    revoutput.append(p.slice)

def p_EnumBody(p):
    ''' 
        EnumBody : LBRACE EnumMembers RBRACE
                 | SEMICOLON
    ''' 
    revoutput.append(p.slice)

def p_EnumMembers(p):
    '''
        EnumMembers : EnumMember 
                    | EnumMember COMMA 
                    | EnumMember COMMA EnumMembers
    '''
    revoutput.append(p.slice)

def p_EnumMember(p):
    '''
        EnumMember : IDENTIFIER 
                   | IDENTIFIER ASSIGN AssignExpression
    '''
    revoutput.append(p.slice)

def p_AnonymousEnumDeclaration(p):
    '''
        AnonymousEnumDeclaration : ENUM COLON EnumBaseType LBRACE EnumMembers RBRACE 
                                 | ENUM LBRACE EnumMembers RBRACE
                                 | ENUM LBRACE AnonymousEnumMembers RBRACE   
    '''
    revoutput.append(p.slice)

def p_AnonymousEnumMembers(p):
    '''
        AnonymousEnumMembers : AnonymousEnumMember
                             | AnonymousEnumMember COMMA 
                             | AnonymousEnumMember COMMA AnonymousEnumMembers
    '''
    revoutput.append(p.slice)

def p_AnonymousEnumMember(p):
    '''
        AnonymousEnumMember : EnumMember 
                            | Type IDENTIFIER ASSIGN AssignExpression
    '''    
    revoutput.append(p.slice)
    
def p_FuncDeclaration(p):
    '''FuncDeclaration : StorageClasses_opt BasicType FuncDeclarator FunctionBody
                        | StorageClasses_opt BasicType FuncDeclarator SEMICOLON
    		            | AutoFuncDeclaration
    '''
    revoutput.append(p.slice)

def p_AutoFuncDeclaration(p):
    '''AutoFuncDeclaration : StorageClasses IDENTIFIER FuncDeclaratorSuffix FunctionBody
    '''
    revoutput.append(p.slice)

def p_FuncDeclarator(p):
    '''FuncDeclarator : BasicType2_opt IDENTIFIER FuncDeclaratorSuffix
    '''
    revoutput.append(p.slice)

def p_FuncDeclaratorSuffix(p):
    '''FuncDeclaratorSuffix : Parameters MemberFunctionAttributes_opt
    '''
    revoutput.append(p.slice)

def p_Parameters(p):
    '''Parameters : LPAREN ParameterList_opt RPAREN
    '''
    revoutput.append(p.slice)

def p_ParameterList(p):
    '''ParameterList : Parameter
    		     | Parameter COMMA ParameterList
    		     | ELLIPSIS
    '''
    revoutput.append(p.slice)


def p_ParameterList_opt(p):
    '''ParameterList_opt : ParameterList
            		     | empty
    '''
    revoutput.append(p.slice)

def p_Parameter(p):
    '''Parameter : InOut_opt BasicType Declarator
    		 | InOut_opt BasicType Declarator ELLIPSIS
    		 | InOut_opt BasicType Declarator ASSIGN AssignExpression
    		 | InOut_opt Type
    		 | InOut_opt Type ELLIPSIS
    '''
    revoutput.append(p.slice)

def p_InOut(p):
    '''InOut : InOutX
    	     | InOut InOutX
    '''
    revoutput.append(p.slice)

def p_InOutX(p):
    '''InOutX : AUTO
    	      | FINAL
    	      | SCOPE
    '''
    revoutput.append(p.slice)

def p_InOut_opt(p):
    '''InOut_opt : InOut
	  	 | empty
    '''
    revoutput.append(p.slice)


def p_MemberFunctionAttributes(p):
    '''MemberFunctionAttributes : MemberFunctionAttribute
    				| MemberFunctionAttribute MemberFunctionAttributes
    '''
    revoutput.append(p.slice)

def p_MemberFunctionAttributes_opt(p):
    '''MemberFunctionAttributes_opt : MemberFunctionAttributes
                                    | empty
    '''
    revoutput.append(p.slice)



def p_MemberFunctionAttribute(p):
    '''MemberFunctionAttribute : CONST
    		               | IMMUTABLE
    			       | RETURN
    '''
    revoutput.append(p.slice)
    
    

def p_FunctionBody(p):
    '''FunctionBody : BlockStatement
                    | BodyStatement
    '''
    revoutput.append(p.slice)
    

def p_BodyStatement(p):
    '''BodyStatement : BODY BlockStatement
    '''
    revoutput.append(p.slice)


def p_Symbol(p):
    ''' Symbol : SymbolTail
               | DOT SymbolTail
    '''
    revoutput.append(p.slice)

def p_SymbolTail(p):
    '''SymbolTail : IDENTIFIER
                  | IDENTIFIER DOT SymbolTail
    '''
    revoutput.append(p.slice)

def p_error(p):
    if p == None:
        print str(sys.argv[1])+" :: You missed something at the end"
    else:
	print str(sys.argv[1])+" :: Syntax error in line no " + str(p.lineno)

def p_empty(p):
    'empty : %prec EMPTY'
    pass

def rightderivation(prefx,sufx):
    global finalout
    global countg
    lcount=countg
    count=0
    last=[]
    for i in range(1,len(output[lcount])):
        if not (output[lcount][i] in nonterminals):
            count+=1
        else:
            last.append(i)
    pre=" "
    for i in range(1,len(output[lcount])):
        if(last != [] and i==last[-1]):
            pre=pre+" <b> "+str(valuate(lcount,i))  +" </b> "
        else:
            pre=pre+str(valuate(lcount,i)) +  " "
    if(count==len(output[lcount])-1):
        countg+=1
        return pre
    del last[-1]
    finalout.append(computestr(prefx)+" " + pre+" " +sufx)
    suf=" "
    for x in range(len(output[lcount])-1,0,-1):
        if not (output[lcount][x] in nonterminals):
            suf = valuate(lcount,x)+suf
            continue
        las =-1
        if(numnonterminals(countg+1)==0 and last==[]):
            for i in range(len(prefx)-1,-1,-1):
                if prefx[i] in nonterminals:
                    las=i
                    break
            pre=" "
            for i in range(len(prefx)):
                if(i==las):
                    pre=pre+" <b> "+str(prefx[i])  +" </b> "
                elif prefx[i] in nonterminals:
                    pre=pre+str(prefx[i]) +  " "
                else:
                    pre=pre+str(prefx[i].value)+  " "
            flag=0
        else:
            pre=computestr(prefx)
            flag=1
        for i in range(1,x):
            if(flag ==1 and last != [] and i==last[-1] ): 
                pre=pre+" <b> "+str(valuate(lcount,i))  +" </b> "
            else:
                pre=pre+str(valuate(lcount,i))+" "
        countg+=1
        suf = str(rightderivation(prefx+output[lcount][1:x],suf+sufx)) +" " + suf
        countg-=1
        finalout.append(pre+" " +suf+" " +sufx)
        if (last != []):
            del last[-1]
    countg+=1
    return suf

def computestr(lis):
    stri=" "
    for i in range(len(lis)):
        if lis[i] in nonterminals:
            stri=stri+str(lis[i]) +  " "
        else:
            stri=stri+str(lis[i].value)+  " "
    return stri

def valuate(line,x):
    if output[line][x] in nonterminals:
        return output[line][x]
    else:
        return output[line][x].value

def numnonterminals(line):
    # print output[line]
    count=0
    for i in range(1,len(output[line])):
        if output[line][i] in nonterminals:
            count+=1
    # print count
    return count

def truncfinal():
    global finalout
    i=0
    while i < len(finalout)-1:
        if(removeempty(finalout[i].split(' '))==removeempty(finalout[i+1].split(' '))):
            del finalout[i+1]
        else:
            # print "truncfinal"
            # print finalout[i]
            # print finalout[i+1]
            i+=1


def removeempty(lis):
    i=0
    while i < len(lis):
        if(lis[i]=='' or lis[i]=='<b>' or lis[i]=='</b>'):
            del lis[i]
        else:
            i+=1
    return lis



yacc.yacc(debug=True,start='Declaration_mult')
a=open(sys.argv[1],'r')
a=a.read()
data = ""
a+="\n"
yacc.parse(a, debug=True)
# for item in revoutput:
#   print item
filename=sys.argv[1]
fnstart=0
fnend=0
for j in range(len(filename)):
    if filename[j]=='/':
        fnstart=j
    if filename[j]=='.':
        fnend=j
filename=filename[fnstart+1:fnend]
sys.stdout = open(str(filename)+".html", 'w')

# a=a.split('\n')
# for s in a:
#     if not (s == ''): 
#         # data += " " +s
#         yacc.parse(s)

for i in range(len(revoutput)):
    nonterminals.append(revoutput[i][0])
for i in range(len(revoutput)-1,-1,-1):
    output.append(revoutput[i])
# for i in output:
#     print i
print "<html> <head> <title> Rightmost derivation </title> </head> <body bgcolor='#E6E6FA'>"
print "<h2> Rightmost Derivation of the code</h2>"
print  "<b style = color:red> "+ str(output[0][0])+"</b> "+ "</br>"
rightderivation([],"")
truncfinal()
for i in finalout:
    sp=i.split(' ')
    st=""
    for j in range(len(sp)):
        if sp[j]=='':
            continue
        if sp[j]=='<b>':
            st+="<b style = color:red> "
        else:
            st+=sp[j]+ " "
    print st + "</br>"
print "</body></html>"

