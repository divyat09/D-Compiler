#!/bin/bash
>AssemblyCode4.S
python2 main.py ../test/test4.txt
# gcc -c -m32 -nostdlib AssemblyCode4.S 
# gcc -m32 -nostdlib -o run AssemblyCode4.o -Wl,-melf_i386
# ./run
as --32 -g  --gstabs AssemblyCode4.S -o AssemblyCode4.o
ld -g -m elf_i386 AssemblyCode4.o -lc  -dynamic-linker /lib/ld-linux.so.2 -o AssemblyCode4
./AssemblyCode4
