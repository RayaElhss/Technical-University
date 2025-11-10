# Hаправи сърце:
print("  **   **  ")
print(" *  * *  * ")
print("*    *    *")
print(" *       * ")
print("  *     *  ")
print("   *   *   ")
print("    * *    ")
print("     *     ")
print("     H E A R T")


# Изчисляване на възраст по година на раждане:
name = input("name: ")
currentyear = int(input("current year: "))
year = int(input("birth year: "))

age = int(currentyear - year)
print(f"Your name is {name} and you are {age} years old.")


# Пресмятане на лице на трапец:
first_base = float(input("first base: "))
second_base = float(input("second base: "))
height = float(input("height: "))

area = ((first_base + second_base) / 2) * height
print(f"The area of the trapezoid is {area}")


# Изчисляване на брутната заплата чрез час и заплащане:
hours = float(input("Your working hours: "))
rate = float(input("Your salary per hour: "))

gross_pay = hours * rate
print(f'Your gross pay is: {gross_pay}')


