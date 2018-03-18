class A { int a; int a2;}
class B : A { int a; }

void foo(B b)
{
    b.a = 3;   // accesses field B.a
    b.a2 = 4;  // accesses field A.a2
    b.A.a = 5; // accesses field A.a
}
