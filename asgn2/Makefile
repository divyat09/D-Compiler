all: 
	sudo mkdir bin/
	sudo cp src/globalvars.py bin/globalvars.py
	sudo cp src/irds.py bin/irds.py
	sudo cp src/main.py bin/main.py
	sudo cp src/nextuse.py bin/nextuse.py
	sudo cp src/registers.py bin/registers.py
	sudo cp src/assembly.py bin/assembly.py
	sudo chmod 777 bin

clean:
	find . -type f -name '*.swp' -delete; \
	find . -type f -name '*.pyc' -delete; \
	sudo rm -r bin
  
assembly:
	as --32 -g  --gstabs AssemblyCode.S -o AssemblyCode.o
	ld -g -m elf_i386 AssemblyCode.o -lc -dynamic-linker /lib/ld-linux.so.2 -o AssemblyCode
