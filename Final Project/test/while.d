import std.stdio;
int main(){
	int i=0;
	int a[10];
	while (i < 10)
	{
		a[i]=i;
		i=i+1;
	}
	do{
		a[i]=i*2;
		writeln("Do While");
		i=i+1;
	}while(i<10);
}
