#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int twinArrays(int ar1_size, int* ar1, int ar2_size, int* ar2){
    int sum = 100000,temp = 0, min1_1 = 0,min1_2 = 0,min2_1 = 0,min2_2 = 0,i1 = 0, i2= 0;

    for (size_t i = 0; i < ar1_size; i++) {

        if(i == 0 ){
            min1_1 = ar1[i];
            min1_2 = ar1[i];
            min2_1 = ar2[i];
            min2_2 = ar2[i];
        }else{
            if(ar1[i] < min1_1){
                min1_2 = min1_1;
                min1_1 = ar1[i];
                i1 = i;

            }else if(ar1[i]<min1_2)
                min1_2 = ar1[i];

            if(ar2[i] < min2_1){
                min2_2 = min2_1;
                min2_1 = ar2[i];
                i2 = i;
            }
            else if(ar2[i]<min2_2)
                min2_2 = ar2[i];
        }
    }

        if(i1 != i2)
            return min1_1 + min2_1;
        else
            if(min1_1 + min2_2 >= min1_2 + min2_1)
                return min1_2 + min2_1;
            else
                return min1_1 + min2_2;

}

int main() {
    int n;
    scanf("%i", &n);
    int *ar1 = malloc(sizeof(int) * n);
    for(int ar1_i = 0; ar1_i < n; ar1_i++){
       scanf("%i",&ar1[ar1_i]);
    }
    int *ar2 = malloc(sizeof(int) * n);
    for(int ar2_i = 0; ar2_i < n; ar2_i++){
       scanf("%i",&ar2[ar2_i]);
    }
    int result = twinArrays(n,ar1, n,ar2);
    printf("%d\n", result);
    return 0;
}
