#include <stdio.h>

int main(void) {
    char c = getchar();
    // if else-if else
    if (c == 'A')
        puts("A를 입력했군!");
    else if (c == 'B')
        puts("B를 입력하다니ㅣ...");
    else
        puts("뭘 입력한..");

    // switch
    switch(c) {
        case 'A':
            puts("A를 입력했군요!");
            break; // 만약 break 를 해주지 않으면 A일 경우 아래 코드들도 모두 실행된다.
        case 'B':
            puts("B를 입력했다");
            break;
        default:
            puts("뭘 입력한거야..");
    }

    // 3항연산자 : 위험..
    c == 'A' ? puts("A를 입력했군요") : c == 'B' ? puts("B를 입력해") : puts("그렇군요..");

    return 0;
}