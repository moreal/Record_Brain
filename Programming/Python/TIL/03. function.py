# 함수를 선언함에 있어서 C나 자바와는 달리 매우 간단하게 선언이 가능하다.

def func():
    pass
name = 123

# def 이후에 함수명을 적어주고 콜론이후 블록 구간을 두어 함수의 구간임을 알린다, 이런 것은 for, if, while 에도 모두 해당 하는 내용이다.
# 그러니 "name = 123" 이라는 줄은 func() 라는 함수안의 코드가 아니다.

# 자료형을 따로 명시하지 않고 변수에 값이 담길 때 자료형이 정해지는 파이썬의 특성상 인자도 인자명만 적어주면 된다.

def gunc(a,b,c):
    return a + b + c

# 위의 gunc라는 함수는 a+b+c를 반환하는 함수이다!
# 만약 인자를 가변적으로 받고 싶다면 다음과 같이 하면 된다.

def g(*val, **dic):
    pass

# val은 튜플 형태로 값들을 받아올 것이고 dic은 딕셔너리 방식으로 값을 받아올 것이다.
# 그리고 기본값을 정해주고 싶다면 정말 간단하게도 다음과 같이 할 수 있다.

def k(val=1):
    print(val)

# 만약 우리가 아무것도 입력하지 않고 k를 호출하면 1이 출력될 것이다.

# 종류의 영어이름이다.
# Positional Arguments
# Arbitary Arguments
# Keyword Arguments
# Combination
