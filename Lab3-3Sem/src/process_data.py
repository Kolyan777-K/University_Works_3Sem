import json
import sys
import os

# Добавляем путь к src для импорта модулей
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.field import field
from src.gen_random import gen_random
from src.unique import Unique
from src.print_result import print_result
from src.cm_timer import cm_timer_1

# Путь к данным
path = os.path.join(os.path.dirname(__file__), '..', 'data', 'data_light.json')

with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(list(Unique(field(arg, 'job-name'), ignore_case=True)), key=str.lower)

@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: f"{x} с опытом Python", arg))

@print_result
def f4(arg):
    salaries = list(gen_random(len(arg), 100000, 200000))
    return list(map(lambda x: f"{x[0]}, зарплата {x[1]} руб.", zip(arg, salaries)))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))