# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2 and num1 < num3:
    print('1 число')
elif num1 < num2 and num1 > num3:
    print('1 число')
elif num2 > num1 and num2 < num3:
    print('2 число')
elif num2 < num1 and num2 > num3:
    print('2 число')
elif num3 > num1 and num3 < num2:
    print('3 число')
elif num3 < num1 and num3 > num2:
    print('3 число')

