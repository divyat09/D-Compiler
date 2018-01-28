import std.stdio;

int main() {
   
   long int a=10;
   a= a+1;
   uint b=50;
   float c= 34.5;
   static float d= (a+b)*c/10.0;

   printf("Value of a: %d\n", a);
   printf("Value of b: %d\n", b);
   printf("Value of c: %d\n", c);
   printf("Value of d: %d\n", d);
   
   /*
	char d= 'd'
	printf("The val of character d: %s", d)
   */

   // Here we compare the different scenarios of values of c and d

   if( c > d ){
   	printf("Floating Value  %f is greater than value %f\n", c, d);
   }
   else if( c < d ){
   	printf("Floating Value  %f is less than value %f\n", c, d);
   }
   else{
  	printf("Floating Value  %f is equal to value %f\n", c, d);
   }	

   // Here we compare the different scenarios of values of c and d using different notation of relational operators

   if( c !<= d ){
   	printf("Floating Value  %f is greater than value %f\n", c, d);
   }
   else if( c !>= d ){
   	printf("Floating Value  %f is less than value %f\n", c, d);
   }
   else{
  	printf("Floating Value  %f is equal to value %f\n", c, d);
   }	

   //Illegal name definitions for identifiers
   float 9num = 9.0;
   printf("Value is %f", 9num);

   return 0;

}
