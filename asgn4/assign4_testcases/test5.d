int c=1;
int d=2;
int e=2;

void main() { 
	if (c > 0 && d > 0 )
	    d++;
	else if (d > 0 && e >0) // bitwise and
	    e++;
	else
	    d--;
}

