import std.stdio;

alias int number; 
alias string sequence ;  
alias char alphabet;

int main() {
   
   number x=5;
   alphabet c='D';
   sequence s= "Compilers";

   mixin(`writeln("Compilers Project");`); 
   mixin(`writeln("%s",s);`); 
   mixin(`writeln("%d",x);`); 
   mixin(`writeln("%c",c);`); 
   
   return 0;

}