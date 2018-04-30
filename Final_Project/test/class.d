class Box{
	int h;
	int b;
	int foo(){
		int a = h*b;
		return a;
	}
    int hello(){
		writeln("%d %d",h,b);
	    return 1;
	}
}

int main(){
	Box A;
	A.h = 2;
	A.b = 19;
	int res = A.foo();
	writeln("%d",  res);
	writeln("%d %d",A.h, A.b);
	A.hello();
	
	return 1;
}
