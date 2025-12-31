birth_year = int(input("Enter your birth year: "))
current_year = 2025

age = current_year - birth_year
print("Your age is:", age)

#

n = int(input("Enter a number: "))

total = 0
for i in range(1, n + 1):
    total += i

print("Sum from 1 to", n, "is:", total)


#

for i in range(1, 13):
    print("12 x", i, "=", 12 * i)

#
text = input("Enter a string: ")

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

#
num = int(input("Enter a number: "))

print("Square:", num * num)
print("Cube:", num * num * num)
