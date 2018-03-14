# iterator 는 __iter__ 그리고 __next__를 구현함으로써 만들어진다.

class Iterator:
    def __init__(self):
        self.num = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        return self.num

it = iter(Iterator())
for i in it:
    print(i)

# 근데 사실 __next__ 만 구현이 되어있다면 작동한다.