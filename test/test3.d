import std.stdio;

int factorial(int num);

int factorial( int num ){

   int _iter=1;
   long int fact= 1;
   for( _iter=1; _iter<=num; _iter++ ){
      fact= fact*_iter;
   }

   return fact;
}

int main() {

   int _Val= 10;
   int _Result= factorial(_Val);

   printf("Factorial of %d has the value: %d", _Val, _Result);
   return 0;

}