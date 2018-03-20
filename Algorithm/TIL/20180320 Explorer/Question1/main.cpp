#include <iostream>

int Narr[100000];
int main(void) {
    int N, M, tmp; bool isIn = false;
    std::cin >> N;
    for(int i = 0; i < N; ++i)
        std::cin >> Narr[i];

    std::cin >> M;
    for(int i = 0; i < M; ++i) {
        std::cin >> tmp;
        isIn = false;
        for(auto& d : Narr) {
            if (d == tmp) {
                isIn = true;
                break;
            }
        }
        std::cout << isIn << '\n';
    }
    return 0;
}