import std.stdio; 
import std.typetuple; 
alias int myAppNumber; 
alias string myAppString;  
alias Shape.area squareArea; 

class Shape { 
   int area; 
}
class Square : Shape { 
   char p;
}
   
void main() { 
   square = new Square();  
   alias Shape.area squareArea;
   square.squareArea = 42;
   writeln(square.squareArea); 
}

