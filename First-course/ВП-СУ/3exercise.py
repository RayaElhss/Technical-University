# 1
n = int(input("vuvedi broi chisla: "))
numbers = []

for i in range(n):
    num = int(input(f"vuvedti element {i + 1}: "))
    numbers.append(num)
    
print("\nvuvedeniq spisuk e: ", numbers)

  
# dali sushtestvuva
x = int(input("vuvedi chislo dali e v spisuka: "))
if x in numbers:
    print(f"chisloto {x} e v spisuka.")
else:
    print(f"chisloto {x} ne e v spisuka.")


# sortiram spisuka
numbers.sort()
print("sortiran spisuk: ", numbers)

# max element
max_element = max(numbers)
print("max element e: ", max_element)

# iztrivane na element po index
index_to_delete = int(input("Koi index da iztriem?: "))
if 0 <= index_to_delete < len(numbers):
    deleted = numbers.pop(index_to_delete)
    print(f"Iztrit e elementat: {deleted}")
else:
    print("Nevaliden index za iztrivane.")

# promenq stoinostta na element
index_to_change = int(input("Koi index da promenim?: "))
if 0 <= index_to_change < len(numbers):
    new_value = int(input("Vavedete nova stoinost: "))
    numbers[index_to_change] = new_value
    print(numbers)
else:
    print("Nevaliden index za promqna.")


# 2
n = int(input("vuvedi broi nizove: "))
nizove = []

for i in range(n):
    s = input("vuvedi niz: ")
    nizove.append(s)
    
print("vuvedeniq spisuk e: ", nizove)

# nai dulug niz
longest = nizove[0]
for s in nizove:
    if len(s) > len(longest):
        longest = s

print("nai dulgiq niz e: ", longest)

# zamenqme niz s drug
old_str = input("vuvedi niz koito iskash da iztriesh: ")
if old_str in nizove:
    new_str = input("vuvedi nov niz: ")
    index = nizove.index(old_str)
    nizove[index] = new_str
    print("promeneniq spisuk e: ", nizove)
else:
    print("nqma takuv niz")
    
# iztrivame niz
to_delete = input("\nvuvedi niz koito iskash da iztriem: ")
if to_delete in nizove:
    nizove.remove(to_delete)
    
    print("sled iztrivane spisuka e: ", nizove)
else:
    print("nqma takuv niz v spisuka")
    
# vmukvane na nov niz na izbrana poziciq
new_insert = input("vuvedi nov niz za vmukvane: ")
position = int(input("izberi index poziciq na element v niza: "))
if 0 <= position <= len(nizove):
    nizove.insert(position, new_insert)
else:
    print("nevaliden index")
    
print("okonchatelen index: ", nizove)


# 3
n = int(input("vuedi broi kluchove: "))
m = int(input("vuvedi broi stoinosti: "))

data = {}

# vuvejdane na kluchove i stoinosti:
for i in range(min(n,m)):
    key = input(f"vuvedi kluch {i + 1}: ")
    value = input(f"vuvedi stoinost {i + 1}: ")
    data[key] = value
    
print("purvonachalen rechnik: ", data)

# tursim izbran kluch v rechnika (data)
search_key = input("vuvedi kluch za tursene: ")
if search_key in data:
    print(f"{search_key} sushtestvuva v rechnika")
else:
    print(f"{search_key} ne sushtestvuva v rechnika")

# promqna na stoinost po kluch
change_key = input("vuvedi kluch chiqto stoinost iskate da promenite: ")
if search_key in data:
    new_value = input("vuvedi nova stoinost: ")
    data[change_key] = new_value
    print("rechnika sled promqa: ", data)
else:
    print("takuv kluch nqma v rechnika.")
    
# iztriva element ot rechnika po kluch
delete_key = input("vuvedi kluch za iztrivane: ")
if delete_key in data:
    del data[delete_key]
    print("rechnik sled iztrivane: ", data)
else: 
    print("nqma takuv kluch.")
    
# izvejdane na vsichki kluchove i stoinosti ot rechnika
print("\nkluchove v rechnika: ", list(data.keys()))
print("\nstoinosti v rechnika: ", list(data.values()))

# sortira rechnika po kluchove
sorted_data = dict(sorted(data.items()))
print("rechnika sortiran po kluchove: ", sorted_data)

# obhojdane i izvajdane na elementi po kluch
for key in sorted_data:
    print(f"{key} => {sorted_data[key]}")


# 4
# purvo mnojestvo
n = int(input("vuvedi broi elementi za purvoto mnojestvo: "))
set1 = set()
for i in range(n):
    num = int(input(f"vuvedi element {i + 1} za purvoto mnojestvo: "))
    set1.add(num)
    
# vtoro mnojestvo
m = int(input("vuvedi broi elementi za vtoroto mnojestvo: "))
set2 = set()
for i in range(m):
    num = int(input(f"vuvedi element {i + 1} za vtoroto mnojestvo: "))
    set2.add(num)
    
print("purvo mnojestvo: ", set1)
print("vtorto mnojestvo: ", set2)

# opredelqne na razmera
print("\nrazmer na purvo mnojestvo: ", len(set1))
print("\nrazmer na vtorto mnojestvo: ", len(set2))

# obedinenie
union_set = set1.union(set2)
print("obedinenie na mnojestvata: ", union_set)

# razlika
difference_set = set1.difference(set2)
print("razlikata e: ", difference_set)

# presichane
intersection_set = set1.intersection(set2)
print("presichane na mnojestvata: ", intersection_set)

# premahvane na izbran element ot purvo mnojestvo
element = int(input("vuvedi element za premahvane"))
if element in set1:
    set1.remove(element)
    print("sled premahvane na elementa: ", set1)
else:
    print("nqma takuv element")

# izchitsvane na mnojestvata
set1.clear()
set2.clear()
print("\npurvo mnojestvo: ", set1)
print("\nvtoro mnojestvo: ", set2)


# 5
data = {}

for i in range(7):
    key = input(f"vuvedi kluch {i + 1}: ")
    value = input(f"vuvedi stoinost za {key}: ")
    data[key] = value
    
print("purvonachalen rechnik: ", data)

# zamqna na stoinost po izbran kluch
change_key = input("vuvedi kluch koito iskash da zamenish: ")
if change_key in data:
    new_value = input("vuvedi novata stoinost ")
    data[change_key] = new_value
    print("rechnika sled promqna: ", data)
else:
    print("nqma takuv kluch v rechnika")
    
# iztrivane na element po kluch
delete_key = input("koi kluch iskash da iztriesh?: ")
if delete_key in data:
    del data[delete_key]
    print("rechnika sled iztrivane: ", data)   
else:
    print("nqma takuv kluch v rechnika")
    
# dobavqne na nova dvoika kluch stoinost:
new_key = input("vuvedi nov kluch za dobavqne: ") 
new_value = input("vuvedi nova stoinost za dobavqne: ")
data[new_key] = new_value

print("okonchatelen rechnik: ", data)

# 6
n = int(input("vuvedi broi gradove: "))
cities = []

for i in range(n):
    city = input(f"vuvedi grad {i + 1}: ")
    cities.append(city)
    
print("spisuk s gradove: ", cities)

# dobavqne na nov grad
new_city = input("vuvedi ime na grad za dobavqne: ")
cities.append(new_city)
print("sled dobavqne: ", cities)

# iztrivane na grad
delete_city = input("\nvuvedi ime na grad za iztrivane: ")
if delete_city in cities:
    cities.remove(delete_city)
    print("sled iztrivane: ", cities)
else:
    print("nqma takuv grad  spisuka.")
    
# izvejdane na spisuk
print("\nGradove v spisuka: ")
for c in cities:
    print("-", c)
    
# sortirane na spisuk
cities.sort()
print("\nsortiran spisuk s gradove: ")
print(cities)

# tursene na element
search_city = input("\nvuvedi ime na grad za tursene: ")
if search_city in cities:
    print("\ngradut e v spisuka.")
else:
    print("nqma takuv grad v spisuka.")
    
# konkatenirane na spisuci
m = int(input("vuvedi broi gradove za noviq spisuk: "))
new_list = []
for i in range(m):
    new_city = input(f"vuvedi nov grad {i+1}: ")
    new_list.append(new_city)
    
# obedinqvane
cities = cities + new_list
print("\nsled konkatenirane dvata spisuka sa: ")
print(cities)