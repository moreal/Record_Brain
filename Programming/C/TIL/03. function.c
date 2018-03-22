#include <stdio.h>

// C에서는 위에서 선언해줘야 한다.
// 위에서 선언만 해주고 아래에서 구현하는 방법도 가능하다 (프로토타입)

void print(char* str) {
    puts(str);
}

void print_(char*);

int main(void) {
    char* str = "Hello world!";
    print(str);
    print_(str);
    return 0;
}

void print_(char* str) {
    puts(str);
}