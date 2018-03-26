void swap1(int a, int b) {
    int tmp = a;
    a = b;
    b = tmp;
}

void swap2(int* a, int* b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int main(void) {
    int a = 1, b = 2;
    swap1(a,b); // 아무일도 일어나지 않는다.
    swap2(&a, &b); // 실제로 값이 바뀐다!!
    // 포인터는 변수의 주소 값을 갖고 있기 때문에 인자로 넘길 때 포인터로 넘기면 값을 복사하지 않고 주소를 복사 함으로써 실제 변수 위치의 값을 수정할 수가 있는 것이다.
    return 0;
}