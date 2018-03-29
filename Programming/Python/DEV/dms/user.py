import api

__users = []

class PlaceError(Exception):
    pass

def add_user(name, id, pw, class_num=1, seat_num=1)
    try:
        user = User(name, id, pw, class_num, seat_num)
        users.append(user)
    except Exception as exc:
        pass

def get_users():
    return __users

def can_assign(class_num, seat_num):
    if not api.is_right_place(class_num, seat_num): return False
    
    for user in get_users():
        if user.seat_num == seat_num and user.class_num == class_num: return False

    return True

class User():
    def __init__(self, name, id, pw, class_num, seat_num):
        self.name, self.id, self.pw = name, id, pw

        if not can_assign(class_num, seat_num):
            raise PlaceError()

        self.class_num, self.seat_num = class_num, seat_num

    def __str__(self):
        return f"{self.name}:{self.id}:{self.pw}:{self.class_num}:{self.seat_num}"

    def set_seat(self, class_num, seat_num):
        self.class_num, self.seat_num = class_num, seat_num

    def extension(self):
        api.apply_extension(self.id, self.pw, self.class_num, self.seat_num)

    def valueOf(data):
        name, id, pw, class_num, seat_num = data.split(":")
        return User(name, id, pw, int(class_num), int(seat_num))