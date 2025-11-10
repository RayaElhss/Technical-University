# vocabulary:
.split();
.random();
.min();
.max();
.append();
.clear();
.count();
.int(); # преобразува към цяло число
.float();

# Python bitwise operators:
& -> (and) -> x & y
| -> (or) -> x | y
^ -> (xor) -> x ^ y
~ -> (not) -> ~x
<< -> (zero fill left shift) -> x << 2
>> -> (signed right shift) -> x >> 2


# неизменяеми типове данни: са такива, чиито стойности не могат да се променят след създаването им.
int, float, list, tuple, str, bool

# компилатор / интерпретатор (разлика)
интерпретатор - превежда и изпълнява ред по ред кода, директно се изпълнява. 
компилатор - превежда целия програмен код наведнъж в машинен език

# idle: е вградената среда за писане и изпълнение на Python код.

# овновни математически оператори:
+ , - , * , / , // (целочислено деление), %

# in - проверка за наличие (case-sensitive)
пример: 
'h' in hello
output: true

-----
# Логически изрази:
== оператор за равенство
!= различие
<, <=
>, >=

not - обръща стойността на даден логически израз 
hey = true, not hey -> hey = false

and
or

# if else conditionals:
if <логически израз>:
   <код, който се изпълнява, когато логическия израз е true>
else:
   <код, който се изпълнява, когато логическия израз е false>


# while и for цикъл:
# for range
range (<начало>, <край>, <стъпка>)
range(5) => 0,1,2,3,4

ord() -> priema simvul i vrushta simvol kod
chr()-> ...

while <логически израз>:
    <тяло на цикъл>

break and continue

# izvlichane na secheiie ot spisuk
# metodi
.reverse()
.append()
.insert()
.remove()
.pop()
del
.sort(reverse=True)
.tuple()

# dictionary:
d1 = {'name':'ivan', 'last_name':'Petrov', 'age': 20}
d2 = dict(name = 'ivan', last_name = 'Petrov')
d3 = dict([('name','ivan'), ('last name', 'Petrov')])

d4 = {}
d4['name'] = 'ivan'

#obhojdane 
for

for key in d1.keys():
  print(key, d1[key])

dkeys = list(d1.keys())
dkeys.sort()

# dobavqne
d1['city'] = 'Plovdiv'
# iztrivane
del d1['city]

# mnojestvo (set)
s1 = set([1,3,5,1,4,3]) => {1,3,5,4}
s2 = {1,3,5,4}

# obhojdame
for el in s2:
  print(el)

# operatori
obedinenie |
s1 = {1,2,3,4}
s2 = {2,4,5,7}
s3 = s1 | s2
output: {1,2,3,4,5,7} ne trqbva da ima povtarqshi

razlika - 
s4 = s1 - s2
output: {1,3}

presichane na mnojestvo &
s5 = s1 & s2
output: {2,4}










