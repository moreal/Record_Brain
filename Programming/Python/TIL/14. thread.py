# python도 당연히 스레드를 지원한다.
import threading

# threading 모듈내의 Thread 클래스를 통해서 인자와 함수를 넘겨 실행한다.
def print_test():
    i = 0
    while True:
        i+=1
        print("Hello world.. ::", i)

t = threading.Thread(target=print_test, name="What") 

# start method를 통하여 thread를 동작시킨다.
t.start()

# 동기화를 위해서 threading.Lock 클래스로 acquire 과 release를 사용하여 동기화 시킬 수가 있다.
