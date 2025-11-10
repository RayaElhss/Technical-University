numbers = []
n = int(input("enter a number: "))

for i in range(n):
    num = int(input(f"enter number {i+1}: "))
    numbers.append(num)
print("the list is: ", numbers)

# tursim indexa na nai malkoto otricatelno chislo
negatives = [x for x in numbers if x < 0]
min_negative = min(negatives)
index_min = numbers.index(min_negative)  

max_negative = max(negatives)
index_max = numbers.index(max_negative)  

print(f"Най-малкото отрицателно число е: {min_negative}, index: {index_min}")  
print(f"Най-голямото отрицателно число е: {max_negative}, index: {index_max}")  


# tursim sumata na dqsnoto chislo 
sum_tens = 0

for num in numbers:
    s = str(num)

    if "-" in s:
        s = s[1:]  # махаме минуса

    if len(s) >= 2:
        tens = int(s[-2])
    else:
        tens = 0

    if tens % 2 == 0:
        sum_tens += num

print(f"Сумата е: {sum_tens}")

