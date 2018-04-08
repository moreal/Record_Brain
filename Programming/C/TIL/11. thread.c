/*
* 설명하기에 앞서
*
* 스레드는 사용자 스레드와 커널스레드로 나눌 수 있는데
* 우리가 사용할 스레드는 주로 사용자 스레드 일것이다 (일단 내 경우에는 그렇다)
*
* 좀 더 자세한 내용은 운영체제 정리하면서 적어야지..
*
* pthread..
*/

#include <pthread.h>
#include <stdio.h>

void* func(void* arg) {
	printf("%d", *(int*)arg);
}

int main(void) {
	// pthread를 사용하기 위한 구조체이다
	pthread_t p_thread[2];
	int a = 1, b =2;
	// pthread_create
	// 4개의 인자를 받는다
	// thread : 스레드 구조체 주소
	// attr : 스레드 특성 값
	// start_routine : 실행할 함수포인터
	// arg : 넘겨줄 인자
	pthread_create(&p_thread[0], NULL, func, (void*)&a);
	pthread_create(&p_thread[1], NULL, func, (void*)&b);

	return 0;
}