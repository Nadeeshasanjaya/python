import math


try:
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)

except ZeroDivisionError:
    print("can't Division by zero")



try:
    temp = int(input("Enter the temperature : "))
    fahrenheit = temp * 9 / 5 + 32
    print(fahrenheit)
except ValueError:
    print("can't cant enter letters")



try:
    radius = int(input("Enter the radius : "))
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    print(area)
    print(circumference)
except ValueError:
    print("can't cant enter letters")



try:
    num = int(input("Enter the number : "))
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
except ValueError:
    print("can't cant enter letters")



sentence = input("Enter the sentence : ")
count = len(sentence)
print(count)

