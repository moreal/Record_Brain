#include <stdio.h>

int main(void) {
    /*
     * 입력을 받는 방법은 정말 여러가지 지만 일단은 기초들만 적는다.
     */

    // get a char
    char c = getchar();
    scanf("%c",&c);
    fread(&c, sizeof(char), (size_t) 1, stdin);

    // get integer
    int integer = 0;
    scanf("%d", &integer);

    // 이제 대충 알죠..?
    
    return 0;
}