import ply.lex as lex
import sys
import ply.yacc as yacc
from lexer import tokens
import logging

Listnonterminals=[]
Rderivation=[]
Derivations=[]
RightOutput = []

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
    Derivations.append(p.slice)

def p_Declarators(p):
    '''Declarators : DeclaratorInitializer
    		   | DeclaratorInitializer COMMA DeclaratorIdentifierList
    '''
    Derivations.append(p.slice)

def p_DeclaratorInitializer(p):
    '''DeclaratorInitializer : VarDeclarator
                     | VarDeclarator ASSIGN Initializer
    			     | AltDeclarator ASSIGN Initializer
    			     | AltDeclarator 
    '''
    Derivations.append(p.slice) # rem template parameters from 2

def p_DeclaratorIdentifierList(p):	
    ''' DeclaratorIdentifierList : DeclaratorIdentifier
    				 | DeclaratorIdentifier COMMA DeclaratorIdentifierList
    '''
    Derivations.append(p.slice)

def p_DeclaratorIdentifier(p):
    ''' DeclaratorIdentifier : VarDeclaratorIdentifier
    			     | AltDeclaratorIdentifier
    '''
    Derivations.append(p.slice)

def p_VarDeclaratorIdentifier(p):
    ''' VarDeclaratorIdentifier : IDENTIFIER
                                | IDENTIFIER ASSIGN Initializer
    '''
    Derivations.append(p.slice) # rem template parameters from 2

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
    Derivations.append(p.slice)

def p_VarDeclarator(p):
    '''VarDeclarator : BasicType2_opt IDENTIFIER
    '''
    Derivations.append(p.slice)

def p_AltDeclarator(p):
    '''AltDeclarator : BasicType2_opt IDENTIFIER AltDeclaratorSuffixes
    		     | BasicType2_opt LPAREN AltDeclaratorX RPAREN
                 | BasicType2_opt LPAREN AltDeclaratorX RPAREN AltFuncDeclaratorSuffix
    		     | BasicType2_opt LPAREN AltDeclaratorX RPAREN AltDeclaratorSuffixes
    '''
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
    Derivations.append(p.slice)

def p_AltDeclaratorSuffixes_opt(p):
    '''AltDeclaratorSuffixes_opt : AltDeclaratorSuffixes 
				 | empty
    '''
    Derivations.append(p.slice)

def p_AltDeclaratorSuffix(p):
    '''AltDeclaratorSuffix : LBRACKET RBRACKET
    			   | LBRACKET AssignExpression RBRACKET
    			   | LBRACKET Type RBRACKET
    '''
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
    Derivations.append(p.slice)

def p_BasicType2(p):
    '''BasicType2 : BasicType2X BasicType2_opt
    '''
    Derivations.append(p.slice)

def p_BasicType2_opt(p):
    ''' BasicType2_opt : BasicType2
		       | empty
    '''
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
    Derivations.append(p.slice)

def p_NonVoidInitializer(p):
    '''NonVoidInitializer : ExpInitializer
                          | ArrayInitializer
    '''
    Derivations.append(p.slice)

def p_ExpInitializer(p):
    '''ExpInitializer : AssignExpression
    '''
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
    Derivations.append(p.slice) 

def p_CommaExpression(p):
    '''CommaExpression : AssignExpression
                       | AssignExpression COMMA CommaExpression
    '''
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
    Derivations.append(p.slice)  # add eq_power


def p_ConditionalExpression(p):
    '''ConditionalExpression : OrOrExpression
    			     | OrOrExpression QUESTION Expression COLON ConditionalExpression
    '''
    Derivations.append(p.slice) 

def p_OrOrExpression(p):
    '''OrOrExpression : AndAndExpression
    		      | OrOrExpression DOUBLE_PIPE AndAndExpression
    '''
    Derivations.append(p.slice) 

def p_AndAndExpression(p):
    '''AndAndExpression : OrExpression
    			| AndAndExpression DOUBLE_AMPERSAND OrExpression
    '''
    Derivations.append(p.slice) 

def p_OrExpression(p):
    '''OrExpression : XorExpression
    		    | OrExpression PIPE XorExpression
    '''
    Derivations.append(p.slice) 

def p_XorExpression(p):
    '''XorExpression : AndExpression
    		     | XorExpression CARET AndExpression
    '''
    Derivations.append(p.slice) 

def p_AndExpression(p):
    '''AndExpression : CmpExpression
    		     | AndExpression AMPERSAND CmpExpression
    '''
    Derivations.append(p.slice) 

def p_CmpExpression(p):
    '''CmpExpression : ShiftExpression
    		     | EqualExpression
		     | RelExpression
    '''
    Derivations.append(p.slice) 

def p_EqualExpression(p):
    '''EqualExpression : ShiftExpression IS_EQ ShiftExpression
    		       | ShiftExpression NOT_EQ ShiftExpression
    '''
    Derivations.append(p.slice) 

def p_RelExpression(p):
    '''RelExpression : ShiftExpression LESS ShiftExpression
                     | ShiftExpression GREATER_EQ ShiftExpression
                     | ShiftExpression GREATER ShiftExpression
                     | ShiftExpression LESS_EQ ShiftExpression
    '''
    Derivations.append(p.slice) 

def p_ShiftExpression(p):
    ''' ShiftExpression : AddExpression
    			| ShiftExpression LEFT_SHIFT AddExpression
    			| ShiftExpression RIGHT_SHIFT AddExpression
    '''
    Derivations.append(p.slice) 

def p_AddExpression(p):
    '''AddExpression : MulExpression
    		     | AddExpression PLUS MulExpression
    		     | AddExpression MINUS MulExpression
    '''
    Derivations.append(p.slice)  # might add catexprssion
def p_MulExpression(p):
    '''MulExpression : UnaryExpression
    		     | MulExpression TIMES UnaryExpression
    		     | MulExpression DIV UnaryExpression
    		     | MulExpression MODULO UnaryExpression
    '''
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
    Derivations.append(p.slice) 

def p_ArgumentList(p):
    '''ArgumentList : AssignExpression
    		    | AssignExpression COMMA
    		    | AssignExpression COMMA ArgumentList
    '''
    Derivations.append(p.slice)  

def p_CastExpression(p):
    '''CastExpression : CAST LPAREN Type RPAREN UnaryExpression
    		      | CAST LPAREN RPAREN UnaryExpression
                 
    '''
    Derivations.append(p.slice)     


def p_PowExpression(p):
    '''PowExpression : PostfixExpression
                     | PostfixExpression POWER UnaryExpression
    '''
    Derivations.append(p.slice)     


def p_PostfixExpression(p):
    '''PostfixExpression : PrimaryExpression
    			         | PostfixExpression DOT IDENTIFIER
                         | PostfixExpression DOT NewExpression
                         | PostfixExpression PLUS_PLUS %prec POST_PLUS_PLUS
                         | PostfixExpression MINUS_MINUS %prec POST_MINUS_MINUS
                         | PostfixExpression LPAREN ArgumentList RPAREN
                         | BasicType LPAREN ArgumentList_opt RPAREN                                  
    '''
    Derivations.append(p.slice)    #add index expression, slice expression 

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
    
def p_ArrayLiteral(p):
    '''ArrayLiteral : LBRACKET ArgumentList_opt RBRACKET
                    | IDENTIFIER LBRACKET INUMBER RBRACKET
                    | IDENTIFIER LBRACKET AssignExpression RBRACKET
    '''
    Derivations.append(p.slice)

def p_FunctionLiteral(p):
    ''' FunctionLiteral : FUNCTION Type_opt ParameterAttributes_opt FunctionLiteralBody
                        | ParameterMemberAttributes FunctionLiteralBody
                        | FunctionLiteralBody
    '''
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
        IfStatement : IF LPAREN IfCondition RPAREN ThenStatement
                    | IF LPAREN IfCondition RPAREN ThenStatement ELSE ElseStatement
    '''
    Derivations.append(p.slice)

def p_IfCondition(p):
    '''
        IfCondition : Expression
                    | AUTO IDENTIFIER ASSIGN Expression
                    | BasicType Declarator ASSIGN Expression                    
    '''
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
        WhileStatement : WHILE LPAREN Expression  RPAREN ScopeStatement 
    '''
    Derivations.append(p.slice)

def p_DoStatement(p):
    '''
        DoStatement : DO ScopeStatement WHILE LPAREN Expression  RPAREN 
    '''
    Derivations.append(p.slice)

def p_ForStatement(p):
    '''
        ForStatement : FOR LPAREN Initialize Test_opt SEMICOLON Increment_opt RPAREN ScopeStatement 
    '''
    Derivations.append(p.slice)

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
    Derivations.append(p.slice)

def p_Test_opt(p):
    ''' 
        Test_opt : Test
                 | empty
    '''
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
        SwitchStatement : SWITCH LPAREN Expression RPAREN ScopeStatement
    '''
    Derivations.append(p.slice)

def p_CaseStatement(p):
    '''
        CaseStatement : CASE ArgumentList COLON ScopeStatementList
    '''
    Derivations.append(p.slice)

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
    Derivations.append(p.slice)

def p_StatementListNoCaseNoDefault(p):
    '''
        StatementListNoCaseNoDefault : StatementNoCaseNoDefault
                                     | StatementNoCaseNoDefault StatementListNoCaseNoDefault
    '''
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
    Derivations.append(p.slice)

def p_ContinueStatement(p):
    '''
        ContinueStatement : CONTINUE IDENTIFIER_opt SEMICOLON
    '''
    Derivations.append(p.slice)

def p_BreakStatement(p):
    '''
        BreakStatement : BREAK IDENTIFIER_opt SEMICOLON
    '''
    Derivations.append(p.slice)

def p_ReturnStatement(p):
    '''
        ReturnStatement : RETURN Expression_opt SEMICOLON
    '''
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
    Derivations.append(p.slice) 

def p_UnionDeclaration(p):
    '''UnionDeclaration : UNION IDENTIFIER SEMICOLON
    			| UNION IDENTIFIER AggregateBody
    			| AnonUnionDeclaration
    '''
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
    '''FuncDeclaration : StorageClasses_opt BasicType FuncDeclarator FunctionBody
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

def p_empty(p):
    'empty : %prec EMPTY'
    pass

yacc.yacc(debug=True,start='Declaration_mult')
a=open(sys.argv[1],'r')
a=a.read()
data = ""
a+="\n"
yacc.parse(a, debug=False)


File=sys.argv[1]
File= File.split('/')[-1][:-2] + ".html"
sys.stdout = open(str(File), 'w')

def ExpandTerminal():
    for i in range( 0, len(RightOutput),1 ):
        for j in range(0, len(RightOutput[i]),1 ):
            if RightOutput[i][j] not in Listnonterminals:
                RightOutput[i][j]= RightOutput[i][j].value

def TransformRight( ):
    CurrString=[]
    CurrString.append( Rderivation[0][0] )

    for index in range( 0, len(Rderivation),1 ):
        CurrDerv= Rderivation[index]
        CurrNonT= CurrDerv[0]

        UpdatedString=[]
        for iter_ in range( len(CurrString)-1,-1,-1 ):
            if CurrNonT == CurrString[ iter_ ]:
                
                for i in range( 0, iter_, 1 ):
                    UpdatedString.append( CurrString[i] )

                for item in CurrDerv[1:]:
                    UpdatedString.append( item )

                for i in range( iter_+1, len(CurrString), 1 ):
                    UpdatedString.append( CurrString[i] )
                
                RightOutput.append( UpdatedString )
                break

        CurrString= UpdatedString


for i in range(len(Derivations)):
    Listnonterminals.append(Derivations[i][0])

for i in range(len(Derivations)-1,-1,-1):
    Rderivation.append(Derivations[i])


TransformRight()
ExpandTerminal()

print "<html> <head> <title> Derivation </title> </head> <body>"
print "<h3> Rightmost Derivation of the code</h3>"
print  "<b> "+ str(Rderivation[0][0])+"</b> "+ "</br>"

for index in range(0,len(RightOutput)):
    CurrString = RightOutput[index]
    flag=0
    
    for index2 in range(0, len(CurrString),1 ):
        if CurrString[index2] in Listnonterminals:
            flag = index2
    
    for index2 in range(0, len(CurrString),1 ):
        symbol= CurrString[ index2 ]
        if index2==flag:
            print "<b>" + str(symbol) + "</b>"
        else:
            print str(symbol)       
    print "</br>"

print "</body></html>"

