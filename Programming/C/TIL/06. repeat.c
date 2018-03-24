#include <stdio.h>
#define N 1000;

int main(void) {
    int i = 0;
    for(i = 0; i < N; ++i)
        putchar('*');

    i = 0;
    while (i < N)
        putchar('*'), ++i;
        
    return 0;
}