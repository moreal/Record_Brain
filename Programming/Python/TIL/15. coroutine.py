# 다른 언어들과 비슷하게 yield을 사용한다
# 코루틴을 가진 제네레이터는 __next__와 send method를 지닌다.
# send는 값을 밀어 넣어주고 next는 다음 블로킹(yield) 로 넘긴다.
# 종료시에는 close로 종료한다.

def coroutine_test():
    while True:
        print("before yield")
        i = yield
        print(i)

c = coroutine_test()
next(c) # yield까지 실행 이동합니다.
c.send(6)
print("Hello world!")
c.send(7)
c.close()

"""
출력결과

before yield
6
before yield
Hello world!
7
before yield
"""

# 알수있는것: yield를 만나면 제어권을 main에게 넘긴다.