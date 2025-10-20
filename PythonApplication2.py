# -*- coding: cp1251 -*-

temperature = float(input("Введите температуру в градусах: "))

is_rainy_input = input("Идет дождь? (да/нет): ")
 
is_rainy = (is_rainy_input == "да")

if 20 < temperature < 30:
    if is_rainy:
        print("Футболку, шорты и дождевик")
    else:
        print("Футболку и шорты")

elif temperature <= 0:
    print("Пуховик")

else:
    if is_rainy:
        is_raining_heavily_input = input("Сильный ли дождь? (да/нет): ")
        is_raining_heavily = (is_raining_heavily_input == "да")
        if is_raining_heavily:
            print("Пальто, резиновые сапоги и зонт")
        else:
            print("Пальто и дождевик")
    else:
        print("Пальто")