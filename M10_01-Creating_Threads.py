import time
from threading import Thread

numbers_ = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
letters_ = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')


def numbers_thread():
    for i in numbers_:
        time.sleep(1)
        print(i)


def letters_thread():
    for j in letters_:
        time.sleep(1.01)
        print(j)


thread_1 = Thread(target=numbers_thread)
thread_2 = Thread(target=letters_thread)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
