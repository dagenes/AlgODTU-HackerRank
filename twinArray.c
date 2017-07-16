#include "stdio.h"

int int main(int argc, char const *argv[]) {

    int n,temp,sum=100000;;
    scanf("%d\n",&n );
    int a[n],b[n];
    for (size_t i = 0; i < n; i++) {
        scanf(" %d", &temp);
        a[i]=temp;
    }
    for (size_t i = 0; i < n; i++) {
        scanf(" %d", &temp);
        b[i]=temp;
    }

    temp = 0;
    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) {
            if (i != j) {
                temp = a[i] + b[j];
                if (temp<sum) {
                    sum = temp;
                }

            }
        }
    }


    return 0;
}
