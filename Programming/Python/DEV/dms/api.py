# -*-coding:utf8
# so simple and so dirty code

import requests,json

def login(id, pw):
    data=requests.post("http://dms.istruly.sexy/auth", data={"id":id,"pw":pw}).text
    if data[0] != "{": return False, False
    data = json.loads(data)
    return data['refresh_token'], data['access_token']

def is_right_place(class_num, seat_num):
    if class_num >= 1 and class_num <= 4: return seat_num >= 1 and seat_num <= 20
    elif class_num == 5 or class_num == 6: return seat_num >= 1 and seat_num <= 44
    elif class_num == 7: return seat_num >= 1 and seat_num <= 49
    else: return False

def get_extension_maps(class_num, time=12):
    res = []
    if time == 11 or time == 12:
        datas = [list(filter(lambda x: x != 0, i)) for i in json.loads(requests.get(f"http://dms.istruly.sexy/extension/map/{time}?class_num={class_num}").text)]
        for l in datas:
            res += l
        return res
    else:
        return False

# def can_assign(class_num, seat_num, time=12):
    # return type(get_extension_maps(class_num, time)[seat_num]) == int

# 연장을 신청하는 메소드. class_num, seat_num 값을 필요로 합니다.
def apply_extension(id, pw, class_num, seat_num, time=12):
    if not is_right_class(class_num):
        return False

    refresh_token, access_token = login(id, pw)
    if refresh_token == False or access_token == False: return False

    if not can_assign(class_num, seat_num, time):
        print("There is already it")
        return False

    status_code = requests.post(f"http://dms.istruly.sexy/extension/{time}", 
                                headers={"Authorization":"JWT " + access_token},
                                data={"seat_num":str(seat_num), "class_num":str(class_num)}).status_code
    return status_code == 200 or status_code == 201

def get_extension_place(name, time=12):
    for class_num in range(1,8):
        maps = get_extensions(class_num, time)
        for seat_num, _name in enumerate(maps):
            if _name == name: return class_num, seat_num
    return -1, False