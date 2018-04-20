int main(){
	float a,b,c;
	float D[3];
	float d;
	b=5.0;
	c=5.0;
	b=b/c;
	a=b+c;
	c=b-a;
	a=b*c;
	D[0] = a%c/d;
	D[1] += D[0];
  	D[2] = a*b+c/D[0]%D[1];
	return 0;
}
