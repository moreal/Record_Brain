typedef struct abc {
    int a,b;
} a;

int main(void) {
    // 위의 객체를 사용하는 방법은 아래와 같다.
    struct abc test = {0};
    a ttest = {0};

    test.a = 123; // 이렇게 각각 멤버변수에 접근 합니다.
    
    // 둘다 같은 struct abc이다. 그저 typedef로 struct abc와 a를 같은 것으로 취급하게 된 것이다.

    return 0;
}