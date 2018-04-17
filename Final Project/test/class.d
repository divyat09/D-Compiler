extern int d;
int q;
extern float v;
class Box{
	public:
		int h;
		float b;
		char p;
	private:
		void foo();
	protected:
		char foo1();
}

int main(){
	
	A=new Box();
	A.h = 12;
	A.b = 12.89;
	A.p = 'k';
}
