int main(int na, char* argv[])
{
    int wflg = 0, tflg = 0;
    int dflg = 0;
    char c;
    switch(c)
    {
        case 'w':
		writeln("Hello");
		break;
        case 'W':
            wflg = 1;
            break;
        case 't':
		writeln("Bye");	
        case 'T':
            tflg = 1;
            break;
        case 'd':
            dflg = 1;
            break;
    }
    return 0;
}
