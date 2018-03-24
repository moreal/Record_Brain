#include <stdio.h>

int arr[1024];

int main(void) {
    FILE* f = fopen("file-path.txt","rb+");
    
    /*
     * 파일 모드
     * r - read
     * w - write (처음부터 쓴다)
     * a - append (뒤에 추가한다)
     * r+ - read + write
     * w+ - read + write
     * a+ - read + append
     * rb - binary로 읽기
     * wb - binary로 쓰기
     * ab - binary 추가 쓰기
     */

    fread(arr, sizeof(int), 8, f); // 4byte(int size) 만큼 8개의 요소를 f포인터로 부터 arr에 담아옵니다.
    fwrite("develpment", sizeof(char), 10, f);
    fclose(f);
    // 실행 ㄴ, 물론 Visual에서만..
    return 0;
}