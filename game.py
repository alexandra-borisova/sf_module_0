import numpy as np
number = np.random.randint(1,100)    # загадали число
print ("Загадано число от 1 до 99")
a = 1
b = 100
for count in range(1,100): 
    predict = np.random.randint(a, b) # предполагаемое число
    if number > predict:
        print ('Загаданное число больше чем', predict)
        a = predict+1 # ограничиваем диапазон поиска и исключаем числоб которое уже проверяли        
    elif number < predict:
        print ('Загаданное число меньше чем', predict)
        b = predict # ограничиваем диапазон поиска, -1 не требуется, так как b всегда меньше на 1
    elif number == predict:
        print ('Вы угадали число', number)
        break
        
print ('Вы угадали число', number, 'за', count, 'попыток.')