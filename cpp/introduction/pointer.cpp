#include <stdio.h>
#include <iostream>

using namespace std;
void update(int *a,int *b) {
    int c = *a;
    *a= *a + *b;
    *b= c - *b;
    cout << "a->" << *a << "b->" << *b<< endl;
    if(*b<0)
    {
      cout << "girdi"<< endl;
        *b *=-1;

    }
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
