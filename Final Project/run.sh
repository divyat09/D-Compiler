python src/parser.py $1 > assm.txt
python src/main.py assm.txt
bash commands.sh
#rm AssemblyCode.S
