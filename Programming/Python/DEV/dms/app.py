import api, datetime
from threading import Thread
from user import *

def app():
    while True:
        now = datetime.datetime.now()
        hour, minute = now.hour, now.minute

        if hour == 5 and minute == 30:
            for user in users:
                user.extension()

def io_app():
    while True:
        get_users().append(User.valueOf(input()))

main_thread = Thread(target=app)
io_thread = Thread(target=io_app)
main_thread.start()