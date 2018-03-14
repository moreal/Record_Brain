# range repeat

for i in range(123):
    print(i)

# range는 __iter__ 함수와 __next__ 함수를 구현해놓은 클래스이다.

# range(N) 의 경우 0 ~ N-1
# range(A, B) 의 경우 A ~ B-1
# range(A, B, inc) 의 경우 A ~ B-1 까지 inc 만큼 키워가며.

# str repeat
# 한 글자씩 할당한다.
for c in "abcdefghijklnmopqrstuv":
    print(c)

# list repeat
# element 하나씩 할당한다.
for obj in [1,2,3,4,5]:
    print(str(obj))

# dictionary repeat
# key와 value의 튜플을 언박싱 하여 사용한다.
dic = {'name': "Moreal", "Hi": "Hello"}
for key, val in dic.items():
    print(f"key: {key} // value: {val}")

# enumerate repeate
# repeat with index
for index, data in enumerate(['a','b','c','d','e']):
    print(f"index = {index} == {data}")

# zip repeat
# 여러 리스트를 동시에 사용가능하다. 작은 리스트를 기준으로 순회한다.
for a, b in zip([1,2,3,4,5], ['a','b','c','d','e','f']):
    print(f"{str(a)} :: {b}")