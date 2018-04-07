import std.stdio;
int main(){
	int i=0;
	int a[10];
	while (i < 10)
	{
		a[i]=i;
		writeln(a[i]);
		i=i+1;
	}
	do{
		a[i]=i^^2;
		writeln(a[i]);
		i=i+1;
	}while(i<10);
}
