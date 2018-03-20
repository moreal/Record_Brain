#include <iostream>

int Narr[500000];
int main(void) {
    int N, M, tmp, cnt = 0;
    std::cin >> N;
    for(int i = 0; i < N; ++i)
        std::cin >> Narr[i];

    std::cin >> M;
    for(int i = 0; i < M; ++i) {
        std::cin >> tmp;
        cnt = 0;
        for(int& d : Narr) {
            if (d == tmp) {
                cnt++;
            }
        }
        std::cout << cnt << ' ';
    }
    return 0;
}