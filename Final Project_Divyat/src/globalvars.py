#!/usr/bin/env python2
from Symbol_Table import *

def isint(value):
  # print "Val", value
  if (value[0]=='-'):
    value = value[1:]
    return value.isdigit()
  else:
    return value.isdigit()

#For conditionals
special_count=0

bb = [] #list for basic block
statements = [] #list of IR objects for each statement
NextUseTable= []
Table = SymbolTable()
functions = [] #stores function names
labels = {} #stores names of labels if they are line_no as labelline_no
# RegisterStatus={ '%ebx':-1, '%ecx':-1, '%esi':-1, '%edi':-1, '%eax':-1, '%edx':-1 }   
# RegisterData= {'%ebx':None, '%ecx':None, '%esi':None, '%edi':None, '%eax':None, '%edx':None }   
RegisterStatus={ '%ebx':-1, '%ecx':-1, '%eax':-1, '%edx':-1 }   
RegisterData= {'%ebx':None, '%ecx':None, '%eax':None, '%edx':None }   
RegisterAssigned= {  }

FloatRegisterStatus={ '%st0':-1, '%st1':-1, '%st2':-1, '%st3':-1, '%st4':-1, '%st5':-1, '%st6':-1, '%st7' : -1}   
FloatRegisterData= { '%st0':None, '%st1': None, '%st2': None, '%st3': None, '%st4': None, '%st5': None, '%st6': None, '%st7' : None}
FloatRegisterAssigned= { }

op2wrd= { '+': 'addl', '-': 'subl', '*': 'imul', '/': 'divl', '%': 'modl', '<<': 'shll', '>>': 'shrl', '&': 'andl', '|': 'orl', '^':'xorl',
		'ifgoto_gt':'jg', 'ifgoto_geq':'jge' , 'ifgoto_lt':'jl', 'ifgoto_leq':'jle', 'ifgoto_eq':'je', 'ifgoto_neq':'jne' }

ArraySize= 10

AssemFile='AssemblyCode.S'
