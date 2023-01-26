def sumNumbersDaysYear (arrayDays):
    months = 0
    function_result = 0
    while months < 12:
        i = 0
        for i in range(arrayDays[months]):
            function_result += sum(map(int, str(i + 1)))
        months += 1
    return function_result
         
infinity = 0
trust_operation = False
while infinity != 1:
    daysRegularYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = 0
    while True:
        try:
            year = int(input('Введите год: '))
            if year > 0:
                trust_operation = True
            else:
                trust_operation = False
        except:
            print('Ошибка')
        if trust_operation == True:
            break
    if year % 4 == 0:
        daysRegularYear[1] = 29
        result = sumNumbersDaysYear(daysRegularYear)
        print(f"В {year} такая сумма: {result}")
    else:
        result = sumNumbersDaysYear(daysRegularYear)
        print(f"В {year} такая сумма: {result}")
    infinity = int(input('Введите любое число, чтобы продолжить или 1, чтобы завершить программу: '))