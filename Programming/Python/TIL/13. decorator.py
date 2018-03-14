# Flask 같은 Opensource들을 보면은 @을 사용한 데코레이터를 많이 볼 수 있다.
# 간단한 decorator 사용법에 대해 정리한 파일이다.

# function decorator
def decorator_test(func):
    def decorate():
        print("before called")
        func()
        print("after called")

    return decorate

@decorator_test
def test():
    print("Hello")

test() # 이 경우 test는 before called, Hello, after called를 출력하는 함수가 된 것이다.

# function decorator with args
def decorater_with_args(func):
    def decorate(*args, **kwargs): # kwargs = keywordarguments
        return func(*args,**kwargs)
    return decorate

@decorater_with_args
def test_1(*args, **kwargs):
    for key, val in kwargs.items():
        print(f"{key} :: {val}")
    print(list(args))

test_1(1,2,3,4)

# class decoration
class decorate_as_class:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print("Class Decoration TEST")
        self.func(*args,**kwargs)

class A:
    @decorate_as_class
    def test():
        test_1(1,2,3,4)

A.test()

# 이번 정리는 참 더럽다..