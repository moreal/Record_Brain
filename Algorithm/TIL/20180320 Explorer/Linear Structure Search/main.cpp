#include <iostream>

int arr[1000000];

int main(void) {
    int N, TO, index = -1;
    std::cin >> N;

    for(int i = 0; i < N; ++i)
        std::cin >> arr[i];

    std::cin >> TO;

    int left = 0, right = N, mid;

    while(left <= right) {
        mid = (left+right+1)/2;
        if (arr[mid] == TO) {
            index = mid;
            break;
        } else if (arr[mid] > TO) {
            right = mid;
        } else if (arr[mid] < TO) {
            left = mid;
        }
    }

    std::cout << index;

    return 0;
}