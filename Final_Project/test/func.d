int foo()
{	
    int x=2;
    int y=3;
    int z=4;
    return x*x+y+z;
}

int main(){
    int a = 2;
    int b = 13;
        
    int res = foo();
	writeln("%d",res);
    return 0;
}
