def perimeter():
    print('Для вычесления периметр ')
    width = int(input('Введите ширину: '))
    length = int(input('Введите длину: '))
    
    result = (width+length)*2
    print(f'результат {result}')


def square():
    print('Для вычесления площади ')
    width = int(input('Введите ширину: '))
    length = int(input('Введите длину: '))
    
    result = width*length
    print(f'результат {result}')


from main import turn_over
turn_over()

from main import time
time(1,1,60)