all:    binary

binary: 
        sudo mkdir -p bin/
        sudo cp src/globalvars.py bin/globalvars.py
        sudo cp src/irds.py bin/irds.py
        sudo cp src/main.py bin/codegen
        sudo cp src/nextuse.py bin/nextuse.py
        sudo cp src/registers.py bin/registers.py
        sudo cp src/assembly.py bin/assembly.py
        sudo cp src/symbol_table.py bin/symbol_table.py
        sudo chmod +x bin/codegen
clean:
        find . -type f -name '*.swp' -delete; \
        find . -type f -name '*.pyc' -delete; \
        rm -rf *.o *.s *.S *.out
        sudo rm -r bin

assembly:
        as --32 -g  --gstabs AssemblyCode.S -o AssemblyCode.o
        ld -g -m elf_i386 AssemblyCode.o -lc -dynamic-linker /lib/ld-linux.so.2 -o AssemblyCode4
