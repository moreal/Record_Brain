#include <iostream>

int arr[1000000];

int main(void) {
    int N, K;
    std::cin >> N;

    for(int i = 0; i < N; ++i)
        std::cin >> arr[i];

    std::cin >> K;

    int left = 0, right = N, mid;

    while(mid = (left+right)/2, right-left) {
        if (arr[mid] >= K) {
            right = mid;
        } else if (arr[mid] < K) {
            left = mid + 1;
        }
    }

    std::cout << mid + 1;

    return 0;
}