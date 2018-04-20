int c=1;
int d=2;
int e=2;

void main() { 
	if (c && d)
	    d++;
	else if (d & e) // bitwise and
	    e++;
	else
	    d--;
}

