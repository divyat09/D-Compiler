#!/usr/bin/env python2
from symbol_table import *

bb = [] #list for basic block
statements = [] #list of IR objects for each statement
NextUseTable= []
Table = SymbolTable()

RegisterStatus={ '%ebx':-1, '%esx':-1, '%esi':-1, '%edi':-1, '%eax':-1, '%edx':-1 }   
RegisterData= {'%ebx':None, '%esx':None, '%esi':None, '%edi':None, '%eax':None, '%edx':None }   
RegisterAssigned= {  }

op2wrd= { '+': 'addl', '-': 'subl', '*': 'mull', '/': 'divl', '%': 'modl', '<<': 'shll', '>>': 'shrl', '&': 'andl', '|': 'orl', '^':'xorl' }

AssemFile='AssemblyCode.asm'