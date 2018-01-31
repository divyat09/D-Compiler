/*typedef struct
{
  char a;
  int b;
  char c;
  short d;
  double e;
  char name[10];
  char f;
} T;*/
class T{
  char a;
  int b;
  char c;
  short d;
  double e;
  char name[10];
  char f;
  void initialize()
  {
    a = 'a';
    b = 47114711;
    c = 'c';
    d = 1234;
    e = 3.141592897932;
    f = '*';
    name = "abc";
  }
}

/*void f (T x)
{
  x.a = 'a';
  x.b = 47114711;
  x.c = 'c';
  x.d = 1234;
  x.e = 3.141592897932;
  x.f = '*';
  x.name = "abc";
}*/

int main (){
    T k = new T();
    k.initialize();
    return 0;
}
