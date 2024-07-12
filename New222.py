first = input("Введите число 123:")
second = input("Введите число 456:")
third = input("Введите число 789:")
if first == second and first == third and second == third:
    print(3)
elif first == second or third == first or second == third:
    print(2)
else:
    print(0)