#include <iostream>

int main(void) {
    int arr[9], index = 0;
    
    for(int i = 0; i < 9; ++i)
        std::cin >> arr[i];

    for(int i = 1; i < 9; ++i)
        if(arr[index] < arr[i])
            index = i;

    std::cout << arr[index] << '\n' << index;
    
    return 0;
}