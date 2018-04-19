import std.stdio;
int main(){
    int iter;
    int A[10];
    for (iter=0; iter< 10; iter++){
        if (iter%2){
	    A[iter]= A[iter] + 1;
        }
        else
	    A[iter]= A[iter] + 1; 
    }
}
