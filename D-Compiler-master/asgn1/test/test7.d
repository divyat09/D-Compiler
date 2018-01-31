import std.stdio; 
  
union Data { 
   int i; 
   float f; 
   char str[10]; 
}; 
  
int main( ) { 
   Data data; 

   data.i=2018
   data.f=9.5
   data.str="Compilers"

   pritnf("Member 1 of Union: %d", data.i )
   pritnf("Member 2 of Union: %d", data.f )
   pritnf("Member 3 of Union: %d", data.str )
   
   return 0; 
}
