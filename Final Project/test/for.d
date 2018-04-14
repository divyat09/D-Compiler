import std.stdio;
int main(){
    int iter;
    for (iter=0; iter<= 5; iter++){
        if (iter%2){
            writeln("yes\n");
        }
        else 
            writeln("no\n");
    }
    return 0;
}
