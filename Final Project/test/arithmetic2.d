int main(){
	int a,b,c;
	int d,e,f;
	a=1;	
	b=5;
	c=5;
	a=a & b;
	b=b | c;
	c=b ^ c;
	d=b >> 2;
	e=1<<c;
	f= ~e ;
	writeln("%d %d %d %d %d %d", a,b,c,d,e,f);	
	return 0;
}
