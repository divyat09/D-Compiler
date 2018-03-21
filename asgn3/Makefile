all:    binary

binary: 
	sudo mkdir -p bin/
	sudo cp src/lexer.py bin/lexer
	sudo cp src/parser.py bin/parser
	sudo chmod +x bin/parser
clean:
	find . -type f -name '*.swp' -delete; \
        find . -type f -name '*.pyc' -delete; \
        rm -rf *.o *.s *.S *.out
	sudo rm -r bin


