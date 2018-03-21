class A {
 public : 
 int *a;
 private :
 int a2;
 const int a=5; 
}
class B { int a; }


void foo()
{
    int b = new B();
    b.a = &b.a2 ;   // accesses field B.a
    b.a2 = 4;  // accesses field A.a2
    b.A.a = 5; // accesses field A.a
}
