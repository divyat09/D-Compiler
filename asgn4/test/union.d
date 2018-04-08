import std.stdio;

union Data { 
   int i; 
   float f; 
   char str[13]; 
}
void main() { 
   data = new Data(); 
   writeln("sizd of: ", data.size()); 
   
   data.i = 10; 
   writeln( "data.i : ", data.i); 
   
   data.f = 220.5; 
   writeln( "data.f : ", data.f);  
   
   data.str = "D Programming".dup; 
   writeln( "data.str : ", data.str); 
}
