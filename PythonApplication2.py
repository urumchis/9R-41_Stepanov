# -*- coding: cp1251 -*-

temperature = float(input("������� ����������� � ��������: "))

is_rainy_input = input("���� �����? (��/���): ")
 
is_rainy = (is_rainy_input == "��")

if 20 < temperature < 30:
    if is_rainy:
        print("��������, ����� � ��������")
    else:
        print("�������� � �����")

elif temperature <= 0:
    print("�������")

else:
    if is_rainy:
        is_raining_heavily_input = input("������� �� �����? (��/���): ")
        is_raining_heavily = (is_raining_heavily_input == "��")
        if is_raining_heavily:
            print("������, ��������� ������ � ����")
        else:
            print("������ � ��������")
    else:
        print("������")