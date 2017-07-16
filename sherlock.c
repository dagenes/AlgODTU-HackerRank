#include <stdio.h>
#include <math.h>

double factorial(double f)
{
    if ( f == 0 )
        return 1;
    return(f * factorial(f - 1));
}

int main(int argc, char const *argv[]) {
  int n;
  scanf("%d",&n);
  for (size_t i = 0; i < n; i++) {
    /* code */
    unsigned long x,y,sonuc;
      scanf("%ld %ld",&x,&y);
      printf("%ld %ld\n",x,y);
      sonuc = factorial(x+y-1)/ (factorial(x)*factorial(y-1));
      printf("%ld\n",sonuc);
      long deneme;
      deneme = (long)sonuc % (long)(pow(10,9)+7);
      printf("%ld\n",deneme);

  }
  return 0;
}
