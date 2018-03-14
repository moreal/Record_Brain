# generator 는 

def gen():
    i = 0
    while True:
        yield i
        i += 1

it = iter(gen())
#while True:
#    print(next(it))

# for문 작동방식
# in 뒤에 있는 객체의 iterator를 받아와 StopIteration이 raise 될때 까지 next를 계속 호출하며 실행한다

# 간단하게 한줄로 짜보고 싶을 때
# 리스트가 []을 사용한다면 ()을 사용하면 된다.
print(type(( i for i in range(10) if i % 5 ))) # <class 'generator'>

# generator를 사용하는 이유
# 1. 효율적인 메모리
# 그때 그때 필요한 값을 계산해서 가져오므로 리스트보다 메모리 면에서 효과적이다.
import sys
print(sys.getsizeof([i for i in range(100) if i % 2])) # 528 bytes
print(sys.getsizeof((i for i in range(100) if i % 2))) # 88 bytes

# 2. Lazy Evaluation, 게으른 계산
