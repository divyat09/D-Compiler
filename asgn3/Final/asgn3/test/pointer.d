import std.stdio; 

void main () { 
   int var = 20; 
   int *ip;     
   ip = &var;     
   
   writeln("Value of var variable: ",var); 
   
   writeln("Address stored in ip variable: ",ip); 
   
   writeln("Value of *ip variable: ",*ip); 
}
