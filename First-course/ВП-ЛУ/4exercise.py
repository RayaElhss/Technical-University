# 1
text = input("Enter a number separated by an interval: ")
numbers = [int(num) for num in text.split()]
opposite_numbers = [-n for n in numbers]
print(opposite_numbers)


# 2
mnojitel = int(input("mnojitel: "))
broi = int(input("broi: "))
numbers = []

for i in range(1, broi + 1):
    numbers.append(i * mnojitel)
    
print(numbers)


# 3
text = input("vuvedi chisla: ")
numbers = [int(num) for num in text.split()]

n = int(input("kolko nai-malki chisla da premahnem?: "))
sorted_numbers = sorted(numbers)

remaining = sorted_numbers[n:]

result = " ".join(str(num) for num in remaining)
print(result)


# 4
text = input("vuvedi text: ")
counts = {}

for char in text:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1
print(counts)

# 5
text = input("text: ")
key = int(input("key: "))

result = ""

for ch in text:
    if ch.isalpha():
        base = 'A' if ch.isupper() else 'a'
        result += chr((ord(ch) - ord(base) + key) % 26 + ord(base))
    else: 
        result += ch
print("Result: ", result)