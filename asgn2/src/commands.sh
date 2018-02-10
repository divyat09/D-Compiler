#!/bin/bash
>AssemblyCode1.S
python2 main.py ../test/test3.txt
gcc -c -m32 -nostdlib AssemblyCode1.S 
gcc -m32 -nostdlib -o run AssemblyCode1.o -Wl,-melf_i386
./run