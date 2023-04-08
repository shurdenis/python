"""
Напишите функцию которая будет принимать список чисел и выводить на экран надпись "сегодня x градусов" столько раз
сколько значений в списке.
"""
def temperatureprint(temperature):
    for i in temperature:
        print("Cегодня за окном", i, "градусов")

temperature = [12, -4, 36, 50, 30]
temperatureprint(temperature)