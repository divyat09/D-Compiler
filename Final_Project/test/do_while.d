import std.stdio;
int main(){
	int i=0;
	int a[10];

	while (i < 10)
	{
		a[i]=i;
		writeln("%d", a[i]);		
		i=i+1;
		
	}
	i=0;
	do{
		a[i]=i*2;
		i=i+1;
		writeln("%d", a[i]);
	}while(i<10);
	
	return 0;
}
