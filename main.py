import math

eps = 0.000001
print("Лабораторная работа №3. Черников Никита, ИС-02")
print("Программа для подсчета натурального логарифма ln((x + 1) / x).")
x = float(input("Введите значение переменной x: "))
if x < -1 or x > 1:
    number = 1
    sum = 0
    while True:
        element = (-1) ** (number + 1) / (x ** (number) * number)
        sum += element
        print(number, "й элемент ряда: ", '{:>11}'.format(str(format(element, '.6f'))), sep="")
        number += 1
        if math.fabs(element) < eps:
            break
    print("Сумма ряда ln(({0} + 1) / {0}) =".format(x), format(sum, '.6f'))
else:
    print("Ошибка: введено некорректное значение.")
