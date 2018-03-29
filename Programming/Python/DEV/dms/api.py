# so simple and so dirty code

import requests,json

def login(id, pw):
    data=requests.post("http://dms.istruly.sexy/auth", data={"id":id,"pw":pw}).text
    if data[0] != "{": return False, False
    data = json.loads(data)
    return data['refresh_token'], data['access_token']

def is_right_class(class_num):
    return class_num >= 1 and class_num <= 7

def get_extensions(class_num, time=12):
    res = []
    if time == 11 or time == 12:
        datas = [list(filter(lambda x: x != 0, i)) for i in json.loads(requests.get(f"http://dms.istruly.sexy/extension/map/{time}?class_num={class_num}").text)]
        for l in datas:
            res += l
        return res
    else:
        return False

def can_select(class_num, seat_num, time=12):
    return type(get_extensions(class_num, time)[seat_num]) == int

def apply_extension(id, pw, class_num, seat_num, time=12):
    if not is_right_class(class_num):
        return False

    refresh_token, access_token = login(id, pw)
    if refresh_token == False or access_token == False: return False

    status_code = requests.post(f"http://dms.istruly.sexy/extension/{time}", 
                                headers={"Authorization":"JWT " + access_token},
                                data={"seat_num":str(seat_num), "class_num":str(class_num)}).status_code
    
    return status_code == 200