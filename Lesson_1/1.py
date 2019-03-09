# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
num = int(input("Введите число:\n"))

num1 = num//100
num2 = num//10%10
num3 = num%10

sum = num1 + num2 + num3
mul = num1 * num2 * num3

print('Сумма:', sum)
print('Произведение:', mul)