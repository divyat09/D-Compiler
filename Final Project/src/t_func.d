class foo{
    int x = 0;
}

int main(){
    int a =0;
    int b = 0;
    int res; 
    //res =  res + b;
    res = res + foo(b);
    foo c;
    res = c.x; 
    return 0;
}

