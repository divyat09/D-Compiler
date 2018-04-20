import std.stdio;

enum Languages { B, C, C--, C++, C#, Objective_C, D};

enum : string { 
   A = "Compilers", 
   B = "POPL", 
} 

int main() {
   
   Languages Lang;

   printf("Programming Langage: %d", Lang.C#)
   writefln("Programming Langage: %d", Languages.B)
   writefln("Programming Langage: %d", C++)

   printf("A: %s", A);
   printf("B: %s", B);

   return 0;

}