import std.stdio;
int main(){
    int iter;
	int x=0;
    for (iter=0; iter<= 5; iter++){
        if (iter%2){
			x=x*iter;
        }
        else{
			x=x+iter/2;
		}
    }
    return 0;
}
