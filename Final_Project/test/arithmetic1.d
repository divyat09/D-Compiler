int main(){
	int a,b,c;
	int D[3];
	int d;
	b=-5;
	c=5;
	b=b/c;
	a=b+c;
	c=b-a;
	a=b*c;
    d=2;
	D[0] = a%c/d;
	D[1] += D[0]*b+c;
  	D[2] = a*b+c;
	writeln("%d %d %d",a,b,c,D[0],D[1],D[2]);
	return 0;
}
