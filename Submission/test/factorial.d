int fact( int n )
{		
	int i=0;
	int out_=1;
	for(i=2;i<=n;i++){
		out_= out_*i; 
	}
	return out_;
}

int main(){
    int n;
	scanf("%d",n);
    int ans = fact(n);
	writeln("%d", ans);
    return 0;
}
