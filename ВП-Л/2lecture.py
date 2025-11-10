import random 

# първи списък
l = [1 , 2, 3, 4, 5]
print(l)

# Въвеждане на 5 числа от потребителя
l = []
for i in range(5):
    x = int(input(f"{i+1}:"))
    l.append(x) # добавя към списъка
print(l)


# Генериране на 5 случайни числа между -10 и 10
l = []
for i in range(5):
    l.append(random.randint(-10,10)) 
print(l) 

# Сумиране на елементите с използване на индекси, gives you how many elements there are (length)
sum = 0
for i in range(len(l)): 
    sum+= l[i]
print("sum =", sum)

# Сумиране на елементите директно (по стойности)
sum = 0
for x in l:
    sum += x
print("sum = ", sum)
print("min = ", min(l))
print("max = ", max(l))

ll = input("hi:").split(",")
print(ll)
ll.append([1,2,3])
print(ll)

# списък
ll = [
    [1,2,3],
    [11,12,13],
    [-1,-2,-3]
]
print(ll)

for x in ll:
    print(x)


# Печатане на всички елементи от ll, всичко на един ред, защото end=" "
for x in ll:
    for y in x:
        print(y, end=" ")
print()


# Индексиране и извличане на елементи
print(l)
print(l[1])
print(l[-1])
# print(l[10]) -> Indexerror: list index out of range
print(l[-5]) 

# slices
print(l)
print(l[1:3])
print(l[1:])
print(l[:4])
print(l[-2])
print(l[:-3])
print(l[-2:-4])
print(l[-4:-2])
print(l[:]) # prints the whole list

print(l)
l[1] = [11,12,13]
print(l)

l+= [-1,-2,-3]
print(l)
del l[0]
print(l)

del l[2:4]
print(l)

del l[:]
l.clear()
print(l)

del l 
# print (l) NameError: name 'l' is not defined.

l = []
for i in range(5):
    l.append(random.randint(-10,10)) # generates a num between -10 t0 10
print(l) 


l.remove(1)
print(l)
# l.remove(11) ValueError
if 1 in l:
    l.remove(1)

    print(8>>1)
    print(-8>>1)
    print(2<<4)


