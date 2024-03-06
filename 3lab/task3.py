ones = {1: "один ", 2: "два ", 3: "три ", 4: "четыре ", 5: "пять ", 6: "шесть ", 7: "семь ", 8: "восемь ", 9: "девять "}
special = {11: "одиннадцать ", 12: "двенадцать ", 13: "тринадцать ", 14: "четырнадцать ", 15: "пятнадцать ", 16: "шестнадцать ", 17: "семнадцать ", 18: "восемнадцать ", 19: "девятнадцать "}
tens = {2: "двадцать ", 3: "тридцать ", 4: "сорок ", 5: "пятьдесят ", 6: "шестьдесят ", 7: "семьдесят ", 8: "восемьдесят ", 9: "девяносто "}
hundreds = {1: "сто ", 2: "двести ", 3: "триста ", 4: "четыреста ", 5: "пятьсот ", 6: "шестьсот ", 7: "семьсот ", 8: "восемьсот ", 9: "девятьсот "}
thousand = "Тысяча"
number = int(input("Please enter number: "))
if number < 0 or number > 1000:
    print("Ошибка! ")
if number == 1000:
    print(thousand)
elif number // 100 and number % 100 // 10 == 1:
    sotni = number // 100
    osobye = number % 100
    print(hundreds[sotni], special[osobye])
elif number // 100 and number % 100 // 10 != 1:
    sotni = number // 100
    desyatki = number % 100 // 10
    edinitsy = number % 10
    print(hundreds[sotni], tens[desyatki], ones[edinitsy])
elif number // 10 and number // 10 != 1:
    desyatki = number // 10
    edinitsy = number % 10
    print(tens[desyatki], ones[edinitsy])
elif number // 10 == 1:
    print(special[number])
elif number > 0:
    print(ones[number])
else:
    print("ноль ")
