
"""___Homework___"""
# 30
a = int(input("Enter a number: "))
b = input("Enter a subject name: ")
if a >= 50:
    if b == 'Math':
        print('Yes it is Math')
    elif b== 'English':
        print('Yes it is English')
else:
    print("failed")

#32
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(a if a > b else b)

#33
a = int(input("Enter a price: "))
print('Sale'if a > 1000 else ' No Sale')

#35
a = int(input("Enter a temperature: "))
if a < 0:
    print('temperature is cold')
elif a <= 20:
    print('temperature is nice')
else:
    print('temperature is warm')

#36
season = int(input("1-12-1025: "))
if season in [12,1,2]:
    print('Winter')
elif season in [3,4,5]:
    print('Spring')
elif season in [6,7,8]:
    print('Summer')
elif season in [9,10,11]:
    print('Autumn')
else:
    print('wrong season')

#37
num = int(input("Enter a number: "))
num *4 if num > 0 else num
print(num)



#38
account = input("Enter a type")
a = int(input("Enter a number: "))
if account == 'savings':
    if a > 100000:
        print('High balance')
    else:
        print('Normal balance')
elif account == 'current':
    print('Business account')
else:
    print('Unknown account')

#39
exam = int(input("Enter a degrees: "))
exercise= int(input("Enter a degrees: "))
if exam >= 50 and exercise >= 50:
    print('passed')
elif exam >= 50 or exercise >= 50:
    print('provisory passed')
else:
    print('failed')

#40
a = int(input("Enter a number: "))
if a > 0:
    print('a is positive')
    if a % 2 == 0: #Rest Zahl ist 2 das bedeutet es ist eine gerade Zahl
        print('a is an even number and positive number')
    else:
        print('a is an odd number')
elif a == 0:
    print('a is zero')
else:
    print('number is negative')

#Խնդիր 1. Թվերի վերլուծություն
n = int(input("Enter a number: "))
if n > 0:
    print('n is positive')
elif n < 0:
    print('n is negative')
#elif n == 0: # Fragen ob ich auch auf dieser Weise schreiben kann.
    #print('n is zero')
else:
    print('n is zero')
if n % 2 == 0:
    print('n is an even number')
else:
    print('n is an odd number')

# Խնդիր 2. Առավելագույն և նվազագույն
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if a > b and a > c:
    print('a is greater than b and c') # darf ich auch schreiben so greatest = a?
elif b > a and b > c:
    print('b is greater than a and c')
else:
    print('c is greater than b and a')
if a < b and a < c:
    print('a is smallest than b and c')
elif b < a and b < c:
    print('b is smallest than a and c')
else:
    print('c is smallest than b and a')

#Խնդիր 3. Գնահատականների փոխակերպում
n = int(input("Enter a number: "))
if n >= 90 and n <= 100:
    print('A')
elif n >= 80 and n <= 89:
    print('B')
elif n >= 70 and n <= 79:
    print('C')
elif n >= 60 and n <= 69:
    print('D')
elif n >= 0 and n <=59:
    print('F')
else:
    print('Wrong input')

#Խնդիր 4. Թվերի միջին և մեկնաբանություն
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
sum = (a + b + c)/3
if a < 50:
    print('Low')
elif a >= 50 and a <= 80:
        print('Medium')
else:
    print('High')

#Խնդիր 5. Տարիքի կատեգորիա
age = int(input("Enter a number: "))
if age < 0:
    print('Invalid age!')
elif age <= 12:
    print('Child')
elif age >= 13 and age <= 19:
    print('Teenager')
elif age >=20 and age <= 59:
    print('Adult')
else:
    print('Senior')

# Խնդիր 6. Գումարի հաշվարկ մինչև բացասական թիվ
sum = 0
while True:
    i = int(input("Enter a number: "))
    if i < 0:
        break
    sum += i
print('sum of positive numbers')

#Խնդիր 7. Թվերի միջին մինչև 0
sum = 0
count = 0
while True:
    i = int(input("Enter a numbers: "))
    if i == 0:
        break

    count += 1
    sum += i

if count > 0: # kontorlieren ob es einen Zahl eingegeben wurde
    print('sum is median =', sum / count)
else:
    print('missing number')


"""HomeWork"""
#1. Գումարել լիստի բոլոր էլեմենտները
number = [3, 7, 2, 9, 4]
total = 0
for num in number:
    total += num
print('summe ', total)

#2 Գտիր լիստի ամենամեծ թիվը
number = [3, 7, 2, 9, 4]
largest = number[0]
for num in number:
    if num > largest:
        largest = num
#3 Հաշվի, քանի անգամ է որոշ թիվ հանդիպում լիստում
numbers = [1, 3, 5, 7, 3]
target = 3
count = 0
for num in numbers:
    if num == target:
        count += 1
print(f"{target} occurs {count} times in the list")

#4 Տպիր միայն զույգ թվերը լիստից
numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if num % 2 == 0:
        print(num, 'even numbers')

# 5 Բազմապատկիր յուրաքանչյուր թիվ 2-ով եւ պահիր նոր լիստում
numbers = [1, 2, 3]
new_list = []
for num in new_list:
    new_list.append(num * 2)
print(new_list)

# 6 Հաշվի լիստի միջին արժեքը
numbers = [1, 2, 3, 4, 5, 6]
total = 0
for num in numbers:
    total += num
    count += 1
average = total / count
print(average, 'value')

#7 Ֆիլտրիր միայն դրական թվերը նոր լիստում
numbers = [-4, 5, 0, 7, -1]
new_list = []
for num in numbers:
    if num > 0:
        new_list.append(num)
print(new_list)

# 8 Փոխիր բոլոր բացասական թվերը 0-ով
numbers = [-3, 5, -1, 0, 4]
for i in numbers:
    if i < 0:
        i = 0
print(numbers)

#9 Գտիր երկրորդ ամենամեծ թիվը լիստում
numbers = [1, 2, 3, 4, 5]
for i in range (len(numbers)):

    if numbers[i] > i + 1:
        numbers[i] == 0
print(numbers)

#10 Ստուգիր՝ արդյո՞ք լիստը աճող կարգով է դասավորված
numbers = [1, 2, 3, 4, 5]
is_sorted = True
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
        break
if is_sorted:
    print("The list is sorted in ascending order.")
else:
    print("The list is NOT sorted in ascending order.")

# 11 Հաշվի, քանի տարր է կրկնվում լիստում
numbers = [[1, 2], [3, 4, 5], [6]]
flat_list = []
for sublist in numbers:
    for item in sublist:
        flat_list.append(item)
repeat_count = 0
already_counted = []
for num in flat_list:
    if num not in already_counted:
        count = 0
        for n in flat_list:
            if n == num:
                count += 1
        if count > 1:
            repeat_count += 1
        already_counted.append(num)
print("Number of repeated elements:", repeat_count)

#11. Տրված է լիստ լիստերի ձեւով (2D list), գտիր բոլոր թվերի գումարը


# 12 Հաշվի լիստի տարրերի գումարը, մինչեւ հանդիպի բացասական թիվը
numbers = [2, 4, 5, -1, 10]
total = 0
for num in numbers:
    if num < 0:
        break
    total += num
print(total, 'sum until negative number')

# 13 Ստեղծիր լիստ, որը պարունակում է միայն եզակի արժեքները
numbers = [1, 2, 2, 3, 3, 3]
new_list = []
for num in numbers:
    if num not in new_list:
        new_list.append(num)
print(new_list)


# 14 Գտիր լիստի այն երկու տարրերը, որոնց գումարը ամենամեծն է
numbers = [1, 9, 3, 7, 5]
largest_number = max(numbers)
numbers.remove(largest_number)
second_largest = max(numbers)
print('the 2 large numbers are', largest_number, second_largest)
print('numbers sum', largest_number + second_largest)



















































