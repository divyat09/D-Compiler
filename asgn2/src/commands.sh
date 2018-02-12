#!/bin/bash
>AssemblyCode.S
python2 main.py $1
# gcc -c -m32 -nostdlib AssemblyCode4.S 
# gcc -m32 -nostdlib -o run AssemblyCode4.o -Wl,-melf_i386
# ./run
as --32 -g  --gstabs AssemblyCode.S -o AssemblyCode.o
ld -g -m elf_i386 AssemblyCode.o -lc  -dynamic-linker /lib/ld-linux.so.2 -o AssemblyCode
./AssemblyCode
