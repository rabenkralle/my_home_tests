#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.
import sys

def salary(work_hours, rate, premium):
    return (work_hours * rate) + premium

work_hours = sys.argv[1]
rate = sys.argv[2]
premium = sys.argv[3]

print('Зарплата сотрудника {}'.format(salary(int(work_hours), int(rate), int(premium))))