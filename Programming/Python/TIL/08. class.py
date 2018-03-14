# basic class
class Message:
    def __init__(self, msg, code):
        self.__msg = msg # __로 시작하는 변수는 클래스 내부에서만 다룰 수 있다.
        self.__code = code

    def get_code(self):
        return self.__code

    def get_msg(self):
        return self.__msg

    def __str__(self):
        return f"[{self.__code}] {self.__msg}"

# class extends
class NotFoundMessage(Message):
    def __init__(self):
        Message.__init__(self, "Not Found", 404)

class Forbidden(Message):
    def __init__(self):
        super(Forbidden, self).__init__("Forbidden", 403)

t, l = NotFoundMessage(), Forbidden()
print(t, l, sep="\n")

# instance, class variable
# 를래스 변수는 비유하자면 private static 같이 클래스 들끼리 공유하는 변수이다.
class Share:
    count = 0
    def __init__(self):
        Share.count += 1 # use like this
        print(f"Share.count is {Share.count}")

a, b, c = Share(), Share(), Share()

# class namespace
# 클래스는 property를 dict 형식으로 저장해 놓는다. 이것을 통하여 클래스 구조 파악이 가능할 듯 하다!
def get_variables(c):
    dic = {}
    for key, val in c.__class__.__dict__.items():
        if key[:2] != "__": dic[key] = val
    return dic

print(get_variables(a))