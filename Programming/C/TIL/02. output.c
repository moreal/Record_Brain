#include <stdio.h>

int main(void) {
    
    // Format print using printf
    printf("%d",1);

    // print char array
    puts("CharArray");

    // print char to stdout
    putchar('a');

    putc('a',stdout);

    fwrite("a", sizeof(char), 1, stdout);
    
    write(0, "hello", 5);

    return 0;
}