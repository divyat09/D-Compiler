#!/usr/bin/env python2
from symbol_table import *

def isint(value):
  if (value[0]=='-'):
    value = value[1:]
    return value.isdigit()
  else:
    return value.isdigit()

bb = [] #list for basic block
statements = [] #list of IR objects for each statement
NextUseTable= []
Table = SymbolTable()

RegisterStatus={ '%ebx':-1, '%ecx':-1, '%esi':-1, '%edi':-1, '%eax':-1, '%edx':-1 }   
RegisterData= {'%ebx':None, '%ecx':None, '%esi':None, '%edi':None, '%eax':None, '%edx':None }   
RegisterAssigned= {  }

op2wrd= { '+': 'addl', '-': 'subl', '*': 'imul', '/': 'divl', '%': 'modl', '<<': 'shll', '>>': 'shrl', '&': 'andl', '|': 'orl', '^':'xorl',
		'ifgoto_gt':'jg', 'ifgoto_geq':'jge' , 'ifgoto_lt':'jl', 'ifgoto_leq':'jle', 'ifgoto_eq':'je', 'ifgoto_neq':'jne' }

AssemFile='AssemblyCode1.S'