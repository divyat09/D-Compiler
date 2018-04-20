import std.stdio; 
  
int main( ) { 

   int a=10;
   int b=9;
   int _iter=0;
   float array[5]={ 1000.0, 2.0, 3.4, 17.0, 50.0 };

   for(_iter=0; _iter<5;_iter++){

      if( array[_iter] !<> 2.0 ){
         array[_iter]= -1*array[_iter];
      }

      if( array[_iter] <> 9.0 ){
         array[_iter]= -1*array[_iter];  
      }     
   }

   for(_iter=0; _iter<5;_iter++){
      printf("Element %d of Float Array is: %d", _iter, array[_iter]);
   }

   return 0; 
}
