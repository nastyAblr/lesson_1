"""
Задание 1.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0

Обязательно решите с применением f-строк
"""
a = float(input('введите размер выручки: '))
b = float(input('Введите размер издержек: '))
if a - b > 0:
    print(f'Прибыль равна:{a - b}')
    c = (a - b) / a
    print(f'Рентабельность составляет: {c}')
    d = int(input('Количество сотрудников: '))
    j = (a - b)/d
    print(f'Прибыль в расчте на одного сотрудника составляет: {j}')
else:
    print('Убыток')
