int main(){
    int iter;
	int x=5;
    int A[10];

    for (iter=0; iter < 10; iter++){
        if ( iter%2 == 0 ){
			A[iter]=1;
        }
        else{
			A[iter]=2;
		}    
	}

	for (iter=0; iter < 10; iter++){
		writeln("%d",A[iter]);    
	}
	return 0;
}
