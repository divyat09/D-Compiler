int main(){
    int i = 0;
    int a[3]=[1,2,3];

    if (a[1]<=a[2])
        a[1]++;
    else if (a[1]>=a[2])
        a[1]--;
    else 
        a[1] = a[2];

	writeln("%d %d %d", a[0], a[1], a[2]);

	return 0;
}
