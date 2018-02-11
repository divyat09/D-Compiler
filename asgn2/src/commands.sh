#!/bin/bash
# >AssemblyCode1.S
# python2 main.py ../test/test3.txt
# gcc -c -m32 -nostdlib AssemblyCode1.S
# gcc -m32 -nostdlib -o run AssemblyCode1.o -Wl,-melf_i386
# ./run
as --32 -g  --gstabs AssemblyCode.S -o AssemblyCode.o
ld -g -m elf_i386 AssemblyCode.o -lc  -dynamic-linker /lib/ld-linux.so.2 -o AssemblyCode
./AssemblyCode
