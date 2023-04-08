"""
Создайте функцию напоминалку в отдельном потоке от основном программы.
Функция должна запрашивать о чем напомнить и через сколько секунд.
В основной части программы запустите поток с функцией и выполните задержку в 10 секунд.
После выполнения программа должна написать "программа завершается"
"""

import threading
import time


def potoki():
    ask = input("Что Вы бы хотели не забыть?")
    timer = int(input("Через какое количество времени (сек) Вам напонить о", ask, "?"))
    time.sleep(timer)
    print(ask)


reminder_thread = threading.Thread(target=remind)

reminder_thread.start()
time.sleep(10)
print("!0 секунд прошло! Программа завершается!")