all:    binary

binary: 
	mkdir -p bin/
	cp src/lexer.py bin/lexer.py
	cp src/parser.py bin/parser
	sudo chmod +x bin/parser
	sudo chmod +x bin
clean:
	find . -type f -name '*.swp' -delete; \
        find . -type f -name '*.pyc' -delete; \
        rm -rf *.o *.s *.S *.out *.html
	sudo rm -r bin


