import time
import sys
from variables import имя, возраст, город
from conditions import проверить_возраст

имена = [
    {"имя": "Анна",   "возраст": 12},
    {"имя": "Максим", "возраст": 27},
    {"имя": "Света",  "возраст": 8},
    {"имя": "Денис",  "возраст": 39},
]

for человек in имена:
    sys.stdout.write("Проверяю: " + человек["имя"] + " ")
    sys.stdout.flush()

    for _ in range(5):
        time.sleep(0.4)
        sys.stdout.write(".")
        sys.stdout.flush()

    print()
    time.sleep(0.3)

    if человек["имя"] == имя:
        print("--- Найден! ---")
        print("Имя:", имя)
        print("Возраст:", возраст)
        print("Город:", город)
        проверить_возраст(возраст)
        break
