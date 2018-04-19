all: 
	chmod +x src/lex.py
	sudo mkdir bin/
	sudo cp src/lex.py bin/lexer
	sudo chmod 777 bin

clean:
	find . -type f -name '*.swp' -delete; \
	find . -type f -name '*.pyc' -delete; \
	sudo rm -r bin
