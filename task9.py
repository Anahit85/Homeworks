"""#Գումար մինչեւ N
#Մուտքագրիր թիվ N, ծրագիրը պետք է հաշվի բոլոր թվերի գումարը 1-ից մինչեւ N։
user_input_N = int(input("Enter a number N:"))
total = 0
for i in range(1, user_input_N + 1):
    total += i
print('Sum =', total)

#Կենտ թվերի արտածում
#Տպիր 1-ից մինչեւ 100 միջակայքի բոլոր կենտ թվերը։
#for i in range(1, 101, 2):
    #print(i)

#Թվերի քանակը մինչեւ բացասական
#Մուտքագրիր թվեր հերթով։ Ծրագիրը հաշվի, քանի դրական թիվ է մուտքագրվել
#մինչեւ բացասական թիվը։
count = 0
while True:
    number = int(input("Enter a number:"))
    if number < 0:
        break
    count += 1
print('Print even number until an odd number =', count)

#4. Թվերի միջին արժեքը
#Մուտքագրիր N թվեր, եւ հաշվի նրանց միջին արժեքը։ (Օգտագործիր for ցիկլ եւ գումարային փոփոխական)
N = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
for num in N:
    total += num
average = total/ len(N)
print('Print average =', average)

#Բազմապատկման աղյուսակ
# Օգտագործիր for ցիկլ, որպեսզի տպես 1-ից 10 բազմապատկման աղյուսակը։

for j in range(1,11):
    for i in range(1,11):
        print(i, '*', j, '=', i * j)
print()

# 6. Թվերի գումար միայն եթե զույգ են
# Մուտքագրիր N թվեր եւ հաշվիր միայն զույգ թվերի գումարը։
N = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
for i in N:
    if i % 2 == 0:
      total += i
print('Even numbers are :', total)

#Թվերի դասակարգում
#Մուտքագրիր մի քանի թիվ, ծրագիրը պետք է տպի՝
#○ քանի թիվ է զույգ
#○ քանի թիվ է կենտ
#○ քանի թիվ է բացասական
#○ քանի թիվ է դրական
numbers = [1, 2, 3, 4, -5, 5, 6, 7, -1, 8, 9, -8]
even = 0
odd = 0
positive = 0
negative = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print("Even:", even)
print("Odd:", odd)
print("Positive:", positive)
print("Negative:", negative)


#Թվերի քառակուսիների գումար
#Տրված N-ի դեպքում հաշվիր 1-ից մինչեւ N թվերի քառակուսիների գումարը։
# 👉 Օրինակ՝ N=3 → 12+22+32=14
N = 3
total = 0

for i in range(1, N+1):
        total += i**2
print('Sum of numbers are:', total)
from task5 import result

# Գուշակիր թիվը
# Ծրագիրը պատահական ընտրում է թիվ 1-10 միջակայքում։
# Օգտագործողը փորձում է գուշակել, մինչեւ ճիշտ թիվ գրվի։ (while ցիկլ, if
# պայմանի ստուգում)
secrets = 7

while True:
    user_input = int(input("Guess a fron 1 to 10:"))
    if user_input == secrets:
        print('Correct! The number was', user_input)
        break
    else:
        print('Try again')



# 10. Փոխարկիր տառերը
# Մուտքագրիր տեքստ, ծրագիրը պետք է յուրաքանչյուր մեծատառ դարձնի
# փոքրատառ, իսկ փոքրատառ՝ մեծատառ։
# 👉 Օրինակ՝ “HeLLo” → “hEllO”

text = 'HeLLo'
result = ''
for i in text:
    if i.isupper():
        result += i.lower()
    elif i.islower():
        result += i.upper()
    else:
        result +=i
print(result)

# 11. Գումարի հաշվարկ մինչեւ 0
# Մուտքագրիր թվեր հերթով։ Ծրագիրը պետք է հաշվարկի բոլոր թվերի գումարը,
# մինչեւ մուտքագրվի 0, ապա դադարեցնի աշխատանքը։
total = 0
while True:
    num = int(input("enter a number:"))
    if num == 0:
        break
    total += num

print("The sum of the numbers is", total)

#12. Առավելագույն եւ նվազագույն արժեքներ
# Մուտքագրիր մի քանի թիվ (մինչեւ բացասական թիվ), եւ տպիր դրանցից ամենամեծն ու ամենափոքրը։
maximum = None
minimum = None
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    if maximum is None or num > maximum:
        maximum = num
    if minimum is None or num < minimum:
        minimum = num
if maximum is not None:
    print("Maximum number:", maximum)
    print("Minimum number:", minimum)
else:
    print("No non negative numbers were entered.")

#13. Թվերի դասավորում առանց sort()
# Մուտքագրիր թվերի ցուցակ եւ դասավորիր աճման կարգով՝ օգտագործելով ցիկլերեւ պայմաններ (if եւ փոխանակում)։
numbers = []
n = int(input("enter a number: "))
for i in range(len(numbers)):
    for j in range(0, len(numbers) -i -1):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
print("Numbers in ascending order:", numbers)

#14. Փոխարկիր տեքստը առանց թվերի
#Մուտքագրիր տեքստ։ Ծրագիրը պետք է նոր տեքստ վերադարձնի՝ առանց թվերի, բայց թողնելով մնացած նշանները։
#👉 Օրինակ՝ “a1b2c3” → “abc”

text = input("Enter a text: ")
new_text = ""
for char in text:
    if not char.isdigit():
        new_text += char
print("Text without numbers:", new_text)

#. Փոխադարձ բաժանելի թվեր
#Գտիր բոլոր թվերը 1-ից մինչեւ N, որոնք բաժանվում են եւ՛ 2-ի, եւ՛ 3-ի վրա, բայց ոչ 5-ի վրա։
#(Օգտագործիր and, or, not տրամաբանական օպերատորներ)

N = int(input("Enter N: "))
for num in range(1, N + 1):
    if num % 2 == 0 and num % 3 == 0 and num % 5 != 0:
        print(num, end=" ")

#Հաշվի զույգ եւ կենտ թվերի գումարները առանձին
#Մուտքագրիր մի քանի թիվ եւ հաշվի զույգերի գումարը, կենտերի գումարը առանձին։
even_sum = 0
odd_sum = 0
n = int(input("Enter a count"))
for _ in range(1, n + 1):
    num = int(input("Enter a numbers"))
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

#18. Թվերի գումարը, որոնք բաժանվում են 3-ի վրա, բայց ոչ 5-ի վրա
#Տրված միջակայքում հաշվի այն թվերի գումարը, որոնք բավարարում են պայմանը։
N = int(input("Enter a number N: "))
total = 0
for num in range(1, N + 1):
    if num % 3 == 0 and num % 5 != 0:
        total += num
print("Sum of numbers divisible by 3 but not by 5:", total)

#19.Հաշվի թվերի քառակուսիների միջին արժեքը
#Մուտքագրիր N եւ հաշվիր 1-ից մինչեւ N թվերի քառակուսիների միջինը։
n = int(input("Enter a number N: "))
total= 0
for i in range(1, n + 1):
    total += i ** 2
average = total / n
print("Average of squares from 1 to", n, "is:", average)

# 20. Գտիր ամենափոքր թիվը՝ առանց min() ֆունկցիայի
# Օգտագործիր for ցիկլ եւ if պայմանի ստուգում։
numbers = []
while True:
    user_input = int(input("Enter a number: "))
    if user_input == 0:
        break
    numbers.append(user_input)
if numbers:
    smallest = numbers[0]
    for i in numbers:
        if i < smallest:
            smallest = i
    print("The smallest number is:", smallest)
else:
    print("No numbers were entered.")

#Հաշվի բառի մեջ միայն բաղաձայն տառերը
# Տրված բառի դեպքում հաշվի միայն բաղաձայն տառերի քանակը։
word = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0
for letter in word:
    if letter.isalpha() and letter not in vowels:
        count += 1
print("Number of consonant letters:", count)

#22. Գտիր՝ քանի անգամ է տվյալ թիվը հանդիպում ցուցակում
# Օգտագործիր ցիկլ եւ պայման։

N = int(input("Enter a list length: "))
lst = []
target = int(input("Enter a number: "))
for _ in range(1, N + 1):
    user_input = int(input("Enter a number: "))
    lst.append(user_input)
print(lst.count(target)"""
from task3 import total

#23. Բառի հակառակ գրությունը՝ առանց [::-1]
# Օգտագործիր for ցիկլ եւ նոր տող ստեղծիր։
#word = input("Enter a word: ")
#reversed_word = ""
#for i in range(len(word)-1, -1, -1):
    #reversed_word += word[i]
#print("The reversed word is:", reversed_word)
word = input("Enter a word: ")
reversed_word = ""
for char in word:
    reversed_word += char


# 24. Գտիր առաջին թիվը, որը բաժանվում է եւ՛ 4-ի, եւ՛ 6-ի վրա
# Տրված միջակայքում (օր. 1-ից 100) գտիր առաջին այդպիսի թիվը։

for i in range(1, 101):
    if i % 4 == 0 and i % 6 == 0:
        print("The first number divisible by 4 and 6 is:", i)
        break


#26. Գտիր բոլոր թվերը, որոնց թվանշանների գումարը զույգ է
#Օրինակ՝ 23 → 2+3=5 (չի ընդգրկվում), 42 → 4+2=6 (ընդգրկվում է)։
lst = [86, 3, 8, 123, 567, 23]
for i in lst:
    total = 0
    for j in str(i):
        total += int(j)
    if total % 2 == 0:
        print(i)

#27. Հաշվի տեքստում բառերի քանակը
# Տրված նախադասության դեպքում հաշվի բառերի քանակը (բաժանելով ըստ բացատների)։
sentence = input("Enter a sentence:")
words = sentence.split()
word_count = len(words)
print("Number of words in the sentence:", word_count)

#28. Հաշվի 1-ից մինչեւ N միջակայքում այն թվերի քանակը, որոնք բաժանվում են 3-ի կամ 7-ի վրա։
count = 0
N = int(input("Enter N "))
for i in range(1, N + 1):
    if i % 3 == 0 or i % 7 == 0:
        count += i
print("The count of numbers divisible by 3 or 7 is:", count)

# 29. Գտիր, արդյոք տեքստը պարունակում է թվեր
# Օր. “hello2” → այո, “test” → ոչ։
text = input("Enter a text: ")
for i in text:
    if i.isdigit():
        print("Yes, the text contains a number.")
        break
else:
    print("No, the text does not contain a number.")

#30. Տպիր բոլոր թվերը՝ բացի 3-ի եւ 5-ի բազմապատիկներից
# Օգտագործիր continue օպերատոր։

N = int(input("Enter N: "))
for i in range(1, N + 1):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i, end=" ")

#31. Գտիր երկու թվերից մեծագույնը՝ առանց max()
#oգտագործիր if եւ համեմատության օպերատորներ։
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
if a > b:
    print("The largest number is:",a)
elif a < b:
    print("The largest number is:",b)
else:
    print("The numbers are equal:")

#32. Հաշվի ցուցակի բոլոր տարրերի արտադրյալը
#Օգտագործիր for ցիկլ եւ բազմապատկում։
numbers = [2, 3, 4, 5]
product = 1
for i in numbers:
    product *=i
print("The product of all elements is:", product)

#33. Հաշվի տեքստում ամենաերկար բառի երկարությունը
# Օգտագործիր ցիկլ եւ պայման՝ ստուգելու ամենաերկարը։
text = input("Enter a text: ")
words = text.split()
max_length = 0
for word in words:
    if len(word) > max_length:
        max_length = len(word)
print("The length of the longest word is:", max_length)


















