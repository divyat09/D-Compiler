union T
{
  char a;
  int b;
  char c;
  short d;
  char e;
  char name[10];
  char f;
}

void f (int x)
{
  x.a = 'a';
  x.b = 47114711;
  x.c = 'c';
  x.d = 1234;
  x.e = 3.141592897932;
  x.f = '*';
  x.name = "abc";
}

int main (){
    k = new T();
    f(k);
    return 0;
}
