import std.stdio;
int main(){
    int i;
    for (i=0;i<= 3 && i>= 1 && i!= 2; i++){
        if (i>=2){
            writeln("yes\n");
        }
        else 
            writeln("no\n");
    }
    return 0;
}
