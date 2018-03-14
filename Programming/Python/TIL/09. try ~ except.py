# java의 try catch 문 같은 역할이다.
try:
    int("ZZ",16)
except Exception as e:
    print(e)
    pass

# throw 대신 raise를 사용한다.
try:
    raise Exception()
except Exception as e:
    print("is right?")

# 자신만의 예외를 만들고 싶다면 다음과 같이 하면 된다.
class MyException(Exception):
    pass

try:
    raise MyException()
except MyException as e:
    print("my custom exception!!")