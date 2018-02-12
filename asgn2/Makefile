all: 
  sudo mkdir bin/
  sudo cp src/globalvars.py bin/globalvars
  sudo cp src/irds.py bin/irds
  sudo cp src/main.py bin/main
  sudo cp src/nextuse bin/nextuse
  sudo cp sc/registers bin/registers
  sudo cp src/assembly bin/assembly
  sudo chmod 777 bin

clean:
  find . -type f -name '*.swp' -delete; \
  find . -type f -name '*.pyc' -delete; \
  rm *.o *.s *.out
  sudo rm -r bin
  
assembly:
  as --32 -g  --gstabs AssemblyCode4.S -o AssemblyCode4.o
  ld -g -m elf_i386 AssemblyCode4.o -lc -dynamic-linker /lib/ld-linux.so.2 -o AssemblyCode4
