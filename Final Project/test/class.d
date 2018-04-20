class Box{
	int h;
	int b;
	int foo(){
		int a = h*b;
		return a;
	}
}

int main(){
	Box A;
	A.h = 2;
	A.b = 19;
	int res = A.foo();
	return 1;
}
