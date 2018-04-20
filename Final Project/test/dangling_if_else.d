int main(){
    int i = 0;
    int a[3]=[1,2,3];
    int z = a[1] || a[2];
    a[1] = a[2]+ a[3];
    a[1] <<= a[2];
    if (a[1]<=a[3])
        a[1]++;
    else if (a[2]>=a[3])
        a[1]--;
    else 
        a[1] = a[3];
    int x = a[1]<<a[2];
    x >>=2;
}
