import std.stdio;

alias int number; 
alias string sequence ;  
alias char alphabet;

int main() {
   
   number x=5;
   alphabet c='D';
   sequence s= "Compilers";

   mixin(`writefln("Compilers Project");`); 
   mixin(`writefln("%s",s);`); 
   mixin(`writefln("%d",x);`); 
   mixin(`writefln("%c",c);`); 
   
   return 0;

}