import std.stdio;
int main(){
    int i=6;
    for (;i<= 8 && i>= 6 && i!= 7; i++){
        if (i>=0){
            writeln("yes\n");
        }
        else 
            writeln("no\n");
    }
    return 0;
}
