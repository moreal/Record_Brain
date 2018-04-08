#include <stdio.h>
#include <stdlib.h>

// heap은 stack, code, data로 이루어진 메모리 구조중 한 부분이다.
// 사용자가 운영체제에 일정한 메모리량을 요구하면 할당해주는 영역이다.
// 필요한 만큼 메모리를 사용 가능하다는게 이점이고 그에서 생기는 오버헤드로 인해 느리다는 점이다.  

int main(void) {
    // malloc은 void*를 반환한다. 어떤 타입의 포인터가 될 수 있는 정말 신기한 친구이다. (포인터의 크기가 일정하기 때문이다)
    char* cp = (char*) malloc(sizeof(char) * 20);
    
    // 할당을 해제해주고자 한다면 free 함수를 사용하면 된다.
    free(cp);

    // calloc은 일정한 값으로 초기화가 가능한 함수이고 realloc은 다시 할당해주는 것이다.
    
    return 0;
}