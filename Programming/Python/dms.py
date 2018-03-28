# so simple code

import requests,json

cookies = {}

def login(id, pw):
    data=requests.post("http://dms.istruly.sexy/auth", data={"id":id,"pw":pw}).text
    if data[0] != "{": return False
    data = json.loads(data)
    cookies['JWT'] = data['refresh_token']

def is_right_class(class_num):
    return class_num >= 1 and class_num <= 7

def get_extensions(time, class_num):
    res = []
    if time == 11 or time == 12:
        datas = [list(filter(lambda x: x != 0, i)) for i in json.loads(requests.get(f"http://dms.istruly.sexy/extension/map/{time}?class_num={class_num}").text)]
        for l in datas:
            res += l
        return res
    else:
        return False

def can_select(time, class_num, seat_num):
    maps = get_extensions(time, class_num)
    return type(maps[seat_num]) == int

def apply_extension(id, pw, class_num, seat_num):
    if not is_right_class(class_num):
        return False
    login(id, pw)
    maps = get_extensions(12, class_num)
    print(maps)