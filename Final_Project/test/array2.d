int main(){
    int A[3] =[1,2,3];
    A[2]=A[0]*A[1];
    A[1]=A[0]+A[2];
    A[0]=A[1]+A[2];
	writeln("%d %d %d", A[0], A[1], A[2] );
	return 1;
}
