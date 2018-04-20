int main(int na, char* argv[])
{
    int b = 1;
    int i= 5;

    switch(b)
    {
      case i<5:
		b= b+2;
      case i==5:
		{
					b=b+3;
					writeln("%d",b);
		}
	  default: 
		b=b+1;
    }
	writeln("%d",b);
    return 0;
}
