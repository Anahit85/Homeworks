

#===================#
# Homework Task 4-5 #
# ================= #

#🔹 extend()
lst1 = [1,2]
lst2 = [3,4]
lst1.extend(lst2)
print(lst1)
#2
n = int (input("Enter a number: "))
lst1 = []
lst2 = []
for i in range(n):
    lst1.append(int(input("Enter a number: ")))
print('lst1 is done')
for i in range(n):
    lst2.append(int(input("Enter a number: ")))
print('lst2 is done')
lst1.extend(lst2)
print(lst1)



#🔹 index()
#1
lst = [2, 4, 7, 9]
numbers = lst.index(7)
print('index 7', numbers)

#2
lst = [2, 4, 7, 9]
num = int(input('Enter a number in the list: '))
print(lst.index(num))


#🔹 insert()
word = ['I','Love','Appel']
word.insert(2, 'Python')

number = int(input('Enter a number'))
position = int(input('Enter a position'))
word.insert(position, number)
i = 2
while i < len(word):
    word.insert(i, ' Python')
    i += 3

#🔹 pop()
lst = [2, 4, 7, 9]
lst.pop()
print(lst)
lst = [2, 4, 7, 9]
index = int(input('Enter a number'))
lst.pop(index)
print(lst)
while lst:
    lst.pop()
print('delete', lst.pop())
print(lst)


#🔹 remove()
fruits= ['apple', 'banana', 'orange']
fruits.remove('apple')
print(fruits)
value = input('Enter a number')
if value in fruits:
    fruits.remove(value)
a = [2,2,3,4]
i = 0
c = []
while i < len(a):
    if a[i] in c:
        a.remove(a[i])
    else:
        c.append(a[i])
        i = i + 1


#🔹 reverse()
numbers = [2, 4, 7, 9]
numbers.reverse()
print(numbers)
names = ['Anna', 'Alisia', 'Aram']
for name in names:
    names.reverse()
print(names)

#🔹 sort()
numbers = [4, 6, 8, 2]
numbers.sort()
print(numbers)
names = ['Anna', 'Mia', 'Ella']
names.sort()
print(names)
while True: # fel
    numbers = [4, 6, 8, 2]
    numbers.sort()
    for num in numbers:
        print(num, end='')
    break

#🔹 copy() + sort() համակցված
numbers = [4, 6, 8, 2]
a = numbers.copy()
a.sort()
print(numbers)
numbers = [4, 6, 8, 2]
sorted_lst = numbers.copy()
sorted_lst.sort()
if sorted_lst != numbers:
    print('not sorted')
else:
    print('sorted')

#🔹 len()
#1. Հաշվի, քանի էլեմենտ ունի լիստը
lst = [4, 6, 8, 2, 7]
cunt = len(lst)
print(lst)
#2. Օգտագործողից վերցրու անունների լիստ, եթե > 5, տպիր հաղորդագրություն
names = input('Enter 5 names'). split()
if len(names) > 5:
    print('You have got more than 5 names')
# 3.Օգտագործողից վերցրու բառեր, ավելացրու լիստին մինչեւ “stop”, հետո դասավորիր եւ տպիր։
wors_list = []
while True:
    words_list = input('Enter 5 words')
    if word.lower() == 'stop':
        break
    words_list.append(word)
words_list.sort()
print(' Sorted list ', words_list)
#4. Ստեղծիր list, պատճենիր, փոխիր մի քանի անդամ, համեմատիր՝ արդյոք նույնն են
a = [1, 2, 3, 5, 7]
b = a.copy()
b[0] = 100
b[2] = 300
print("Original list a:", a)
print("Modified copy b:", b)
if a == b:
    print("Lists are the same")
else:
    print("Lists are different")
#5. List-ին տարրեր ավելացրու եւ ցույց տուր, քանի անգամ է կրկնվում ամեն մեկը
lst = [1, 2, 2, 3, 3, 3, 4]
for item in set(lst):
    print(f"{item} occurs {lst.count(item)} times")

#6. Մուտքագրիր 5 թիվ, հեռացրու ամենամեծը եւ տպիր մնացածը
my_list = []
for i in range(5):
    a = int(input('Enter a number: '))
    my_list.append(a)
    my_list.remove(max(my_list))
    print('After removing max number:', my_list)

#7. Մուտքագրիր բառերի list, ջնջիր դատարկ բառերը
name_list = input('Enter names').split()
a = []
for w in name_list:
    if w.strip() != "":
        a.append(w.strip(w))
print("List without empty words", a)


# ============================ #
# Python List եւ Tuple Խնդիրներ #
# ============================ #
# 1️⃣ Մուտքագրիր 5 թիվ եւ պահիր դրանք լիստում, հետո տպիր ամբողջ լիստը։
lst = []
for i in range(5):
    a = int(input('Enter 5 number'))
    lst.append(a)

# 2️⃣ Տպիր առաջին, վերջին եւ միջին էլեմենտները
a = [1,2,3,5,7]
print(a[0], a[-1], a[len(a)//2])

# 3️⃣ Ամենամեծ եւ ամենափոքր
a = [1,2,3,5,7]
print(max(a), 'Max', min(a), 'Min')

# 4️⃣ Լիստի երկարությունը
a = [1,2,3,5,7]
print('Length', len(a))

# 5️⃣ Ավելացրու 40
lst = [10, 20, 30]
lst.append(40)
print(lst)
# 6️⃣ Հեռացրու 20
lst.remove(20)
print(lst)

# 7️⃣ Շրջիր հակառակ
lst.reverse()
print(lst)

# 8️⃣ Միացրու լիստեր
a = [1, 2, 3]
a.extend([4, 5])
print(a)

# 9️⃣ Փոխիր երկրորդ էլեմենտը
letters = ['a', 'b', 'c']
letters[1] = 'z'
print(letters)

## 🔟 Ստուգիր՝ արդյոք 5-ը կա
print(5 in a)

#11️⃣Օգտագործողը մուտքագրում է թվեր, մինչեւ գրի “stop”։ Պահիր դրանք լիստում եւ տպիր։
numbers = input('Enter a number')
a = []
while numbers != 'Stop':
    a.append(int(numbers))
    numbers = input('Enter a number')
print(a)

#12️⃣Տրված է լիստ՝ գտիր բոլոր զույգ թվերը եւ պահիր նոր լիստում։
a = [1, 2, 3]
numbers = [x for x in a if x % 2 == 0]
print('Even numbers', a)

#13️⃣Գտիր բոլոր եզակի արժեքները լիստում (ցիկլով)։
lst = [2,4,7]
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)
print(unique)

#14️⃣Տրված է լիստ՝ հաշվիր բոլոր թվերի գումարը եւ միջինը։
value = sum(list)
average = value / len(list)
print("Sum:", value, "Average:", average)

# 15️⃣Գտիր երկրորդ ամենամեծ թիվը լիստում։
numbers = [1,4,6,2,8,9,]
second_max = sorted(set(numbers))[-2]
print(second_max)

#16️⃣Տրված է լիստ՝ հաշվիր, քանի անգամ է կրկնվում ամեն թիվ։
numbers = [1, 2, 6, 2, 8, 9,]
freq = {}   # Hier speichern wir die Häufigkeit der Zahlen.
for n in numbers:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1
print(freq)

#17️⃣Տրված է բառերի լիստ՝ տպիր ամենաերկար բառը։
words = [ " Python", " java", " CSS"]
print(max(words))

#18️⃣Լիստի բոլոր էլեմենտները բազմապատկիր 2-ով եւ պահիր նոր լիստում։
lst = [ 1,5,3,]
lst1 = lst.copy()
lst1 = [ x*2 for x in lst]
print(lst1)

#19️⃣Տրված է թվերի լիստ՝ ջնջիր բոլոր կրկնվող արժեքները՝ պահպանելով կարգը։
lst = [2,5,6,2,2] # muss noch mal gemacht werden
c = []
for i in lst:
    if i not in lst:
        lst.append(i) # fel
print(i)

#20️⃣Տրված է լիստ՝ փոխիր ամեն զույգ ինդեքսի արժեքը 0-ով։
numbers = [1,4,6,2,8,9,]
for i in range(0, len(numbers)):
    if i % 2 == 0:
        numbers[i] = 0
print(numbers)

# ================  #
# 🔹 Tuple Խնդիրներ #
# ================ #
#21️⃣Ստեղծիր tuple՝ my_tuple = (1, 2, 3, 4) եւ տպիր երկրորդ էլեմենտը։
my_tuple = (1, 2, 3, 4)
print(my_tuple[1])

#22️⃣Ստուգիր՝ արդյոք 3-ը կա թափլում։
print(3 in my_tuple)

#23️⃣Հաշվի՝ քանի անգամ է թիվ 2-ը հանդիպում (2, 5, 2, 2, 9) tuple-ում։
my_tuple = (2, 5, 2, 2, 9)
print(my_tuple.count(2))

# 25️⃣Տրված է tuple՝ (10, 20, 30)։ Փոխարկիր այն լիստի, ավելացրու 40, հետո վերածիր նորից tuple-ի։
t = (10, 20, 30)
lst = list(t)
lst.append(40)
t = tuple(lst)
print(t)

#26️⃣Միացրու երկու tuple՝ (1,2) եւ (3,4)։
t1 = (1, 2)
t2 = (3,4)
print(t1 + t2)

#27️⃣Տրված է tuple՝ (5, 10, 15)։ Հաշվի բոլոր արժեքների գումարը։
t = (5, 10, 15)
print(sum(t))

#28️⃣Ստուգիր՝ արդյոք tuple-ի բոլոր տարրերը տարբեր են։
t = (1, 2, 3)
print(len(t)==len(set(t)))

# ============= #
# Sharunakutyun #
# ============= #
#29️⃣Տրված է tuple բառերով՝ տպիր ամենաերկար բառը։
t = ('I', 'Love', 'Python')
print(max(t, key=len))

#30️⃣Գտիր ամենամեծ եւ ամենափոքր արժեքները tuple-ում։
t = (2, 5, 9, 8)
print('Min value', min(t))
print("Max value", max(t))

#31️⃣Տրված է tuple՝ փոխարկիր այն list-ի։
t = (1, 2, 3, 4)
lst = list(t)
print(lst)

#32️⃣Տրված է list՝ փոխարկիր այն tuple-ի։
lst = [1, 2, 3, 4]
t = tuple(lst)
print(t)

#33️⃣Ստեղծիր ծրագիր, որը ստանում է tuple թվերով եւ վերադարձնում է միայն զույգ թվերով list։
t = (1, 2, 3, 4)
even_numbers = []
for num in t:
    if num % 2 == 0:
        even_numbers.append(num)
    print(even_numbers)

#34 Ստեղծիր ծրագիր, որը ստանում է tuple թվերով եւ վերադարձնում է միայն զույգ թվերով list։
t = (1, [2, 3], 4)
for item in t:
    if isinstance(item, list):
        item[1] = 10
        print(t)

#35️⃣Տրված է list, որը պարունակում է tuple-ներ՝ տպիր բոլոր երկրորդ էլեմենտները։
lst = [(1, 2), (3, 4)]
for i in lst:
    print(i[1])

#36️⃣Տրված է tuple, որը պարունակում է list-ներ՝ յուրաքանչյուրի մեջ ավելացրու նոր արժեք։
t = ([1, 2], [4, 3])
for lst in t:
    lst.append(5)
    print(t)

#37️⃣Տրված է list՝ դարձիր այն set, ապա tuple, ապա նորից list։
lst = [1, 2, 3, 4]
s = set(lst)
print(s)
t = tuple(s)
print(t)

#38️⃣Տրված է tuple բառերով՝ դասավորիր այբբենական կարգով (նախ փոխիր լիստի)։
t = ('orange', 'banana', 'apple')
print(t)
lst = list(t)
lst.sort()
print(lst)

#39️⃣Ստեղծիր tuple թվերով, հետո փոխիր վերջին արժեքը՝ առանց tuple-ը փոխելու(օգտագործիր list → tuple)։
t = (7, 3, 5, 1)
lst = list(t)
lst[-1] = 10
t = tuple(lst)
print(t)

#40️⃣Տրված է tuple՝ տպիր բոլոր արժեքները մի տողով (join() օգտագործելով str(tuple) կամ list comprehension)։
t = ( 'Python', 'is', 'programming')
result = ' '.join(t)
print(result)

#41️⃣Օգտագործողից վերցրու անուններ, պահիր լիստում, եւ վերջում տպիր՝ քանի անուն է կրկնվում։
lst = []
for i in range(5):
    word = input("Enter words")
    lst.append(word)
double = 0
checked = []
for x in lst:
    if x not in checked and lst.count(x) > 1:
        double += 1
        checked.append(x)
print("Number of double words", double)

#42️⃣Տրված է list եւ tuple՝ ստեղծիր նոր list, որտեղ կլինեն միայն այն արժեքները, որոնք առկա են երկուսում։
lst = [1, 2, 3, 4]
t = (2, 6 ,3 ,4)
value = []
for num in lst:
    if num in t:
        value.append(num)
print(value)

#43️⃣Տրված է tuple թվերով՝ ստեղծիր նոր tuple, որտեղ կլինեն միայն կենտ թվերը։
t = (1, 2, 3, 4, 5)
t1 = ()
for num in t:
    if num % 2 != 0:
        t1 += num
print(t1)

#44️⃣Տրված է list բառերով՝ հաշվիր քանի բառ է սկսվում նույն տառով։
lst = ['Anna', 'Michael', 'Sarah', 'Anna']
c = []
count = 0
for words in lst:
    first_letter = words[0].upper()
    if first_letter in c:
        count += 1
    else:
        c.append(first_letter)
print('The sum of words with initial letters are', count)
from task4 import words

#45️⃣Գտիր լիստում այն էլեմենտները, որոնք հանդիպում են միայն մեկ անգամ։
lsi = [1, 1, 4, 2, 2, 3]
a = []
for i in lsi:
    if lsi.count(i) == 1:
        a.append(i)
print(a)

#46️⃣Օգտագործողից վերցրու բառերի շարք, դարձիր tuple, տպիր ամենաերկար բառը։
lst = []
for i in range(5):
    word = input("Enter words")
    lst.append(word)
t = tuple(lst)
longest = t[0]
for i in t:
    if len(i) > len(longest):
        longest = i
print('The longest word is', longest)

#47️⃣Տրված է list եւ tuple — համատեղիր դրանք մեկ ընդհանուր list-ի։
a = [1, 2, 3, 4]
t = (5, 6, 7, 8)
b = list(t)
print(a + b)

#48️⃣Տրված է tuple — ստուգիր՝ արդյոք նրա բոլոր արժեքները նույնն են։
t = (2, 4, 6, 5)
same = True # wir nehmen an die sind identisch
first = t[0] # wir vergleichen mit der ersten
for i in t:
    if i != first:
        same = False
        break
print("All elements are the same:", same)


#49️⃣Տրված է list թվերով՝ հաշվիր միջինից մեծ թվերի քանակը։
lst = [1, 2, 3, 4, 6, 9]
average = sum(lst) / len(lst)
count = 0
for i in lst:
    if i > average:
        count += 1
print("Number of elements greater than the average:", count)

# 50️⃣Ստեղծիր ծրագիր, որը վերցնում է tuple (x, y) կոորդինատներով, եւ հաշվում է դրանց հեռավորությունը սկզբնակետից։
# chgitem inch anem ?
















































