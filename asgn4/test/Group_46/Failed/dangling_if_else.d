int main(void){
    int i = 2;
    int a[3];
    a[0]= 0;
    a[1]= 1;
    a[2]= 2;
    if (i<=3)
        a[i]++;
    if (i>=2)
        a[i]--;
    else 
        a[i] = 1;
}
