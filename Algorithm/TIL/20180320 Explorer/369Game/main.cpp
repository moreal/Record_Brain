#include <iostream>

int main(void) {
    int N;
    std::cin >> N;
    for(int i = 1; i <= N; ++i)
        if (i % 3)
            std::cout << i << ' ';
        else
            std::cout << 'X' << ' ';
    return 0;
}