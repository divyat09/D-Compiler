#!/bin/bash
as --32 -g  --gstabs AssemblyCode.S -o AssemblyCode.o
ld -g -m elf_i386 AssemblyCode.o -lc  -dynamic-linker /lib/ld-linux.so.2 -o AssemblyCode
./AssemblyCode
#>AssemblyCode.S
