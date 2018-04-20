all:    binary

binary: 
	mkdir -p bin/
	cp src/lexer.py bin/lexer.py
	cp src/symbol_table.py bin/symbol_table.py
	cp src/TAC.py bin/TAC.py
	cp src/parser.py bin/irgen
	cp src/globalvars.py bin/globalvars.py
	cp src/irds.py bin/irds.py
	cp src/nextuse.py bin/nextuse.py
	cp src/registers.py bin/registers.py
	cp src/assembly.py bin/assembly.py
	cp src/Symbol_Table.py bin/Symbol_Table.py	
	cp src/main.py bin/codegen
	cp run.sh bin/compile
	sudo chmod +x bin/irgen
	sudo chmod +x bin/codegen
	sudo chmod +x bin/compile
	sudo chmod +x bin
clean:
	find . -type f -name '*.swp' -delete; \
        find . -type f -name '*.pyc' -delete; \
        rm -rf *.o *.s *.S *.out *.html
	sudo rm -r bin

assembly:
	as --32 -g  --gstabs AssemblyCode.S -o AssemblyCode.o
	ld -g -m elf_i386 AssemblyCode.o -lc -dynamic-linker /lib/ld-linux.so.2 -o AssemblyCode4

