#include <iostream>

int main(void) {
    int A = -1, B = -1;
    while(true) {
	    std::cin >> A >> B;
	    if(!A && !B)
		    break;
	    std::cout << A + B << '\n';
    }
    return 0;
}