 #xndir1
lst = [1,2,3,4,5,6,7,8,9,12,23,45,-4,0,-65]
s = set()
for i in lst:
    if i % 3 == 0:
        s.add(i)
print(s)
if len(s) > 5:
     print(max(s))
else:
     print("len is smaller than 5")

 #xndir2
qlow_count = 0
# digit_count = 0
# digit_values = []
#
# for char in text:
#     if char.isupper():
#         up_count += 1
#     elif char.islower():
#         low_count += 1
#     elif char.isdigit():
#         digit_count += 1
#         digit_values.append(int(char))
#
# if digit_count > up_count + low_count:
#     print(digit_values)
#
#
# print(up_count)
# print(low_count)
# print(digit_count)

# #xndir3
# lst = [1,5,7,8,9,88,55,77,54,96,52,0,-96,-85]
# avg = sum(lst)/len(lst)
# print(avg)
# i=0
# set1 = set()
#
# while i < len(lst):
#     if lst[i] > avg:
#         set1.add(lst[i])
#     i+=1
# print(set1)


# #xndir4
# text = "programming"
#
# unique_text = set(text)
# lst = list(unique_text)
# sorted_lst = sorted(lst)
# print(sorted_lst)


# #xndir5
# lst = ["john","maria","arthur","monte","levon","hovhannes","iza"]
# summary = 0
# for i in lst:
#     summary += len(i)
#
# avg = summary/len(lst)
# lst2 = []
# for i in lst:
#     if len(i) > avg:
#         lst2.append(i.capitalize())
# print(lst2)





# #xndir6
# lst = [1,5,9,7,8,55,8,9,63,41,25,41,87,96,25]
# int_lst = []
# float_lst = []
# for i in lst:
#     y = i / 2
#     if y % 1 == 0:
#         int_lst.append(int(y))
#     else:
#         float_lst.append(y)
# print(int_lst)
# print(float_lst)


# # #xndir7
# lst = ["apple", "orange", "anna", "egg", "app","fdd", "hdd","add"]
# vowels = "aeiou"
#
# for i in lst:
#     if i[0] in vowels and i[-1] == i[-2]:
#         print(i)


# # #xndir8
# lst = ["apple","orange","cat","i","ao","python","Javascript"]
#
# second_chars = []
# third_chars = []
#
# for char in lst:
#     if len(char) >= 2:
#         second_chars.append(char[1])
#     if len(char) >= 3:
#         third_chars.append(char[2])
#
# set1 = set(second_chars)
# set2 = set(third_chars)
#
# result = set1.symmetric_difference(set2)
# print(result)




# #xndir9
# x= [1,17,5,86,99,2,6,3,7,11,58,69,78,22]
#
# set1 =set()
# for i in x:
#     if i > 1:
#         count = 0
#         for j in range(2,i):
#             if i%j ==0:
#                 count += 1
#                 break
#         if count == 0:
#             set1.add(i)
# if len(set1) < 2:
#     print("Not enough primes")


#xndir11
lst = [1,5,6,8,9,2,2,5,4,7,8,9,6,2,4,11,5,6,66,44]
unique = set()
for i in lst:
    if lst.count(i) == 1:
        unique.add(i)
print(unique)

#**12. Ստեղծել ծրագիր, որը string-ի բառերը (split)հավաքում է list-ի մեջ։
# հավաքում է list-ի մեջ։
# Եթե բառի երկարությունը զույգ է → ավելացնել even_list
# Եթե կենտ է → odd_list
# Վերջում վերադարձնել union(ed) set։**
text = ('I love Python')
even_list = []
odd_list = []
text = text.split()
for i in text:
    if len(i) % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
union = set(even_list + odd_list)
print(even_list)
print(odd_list)
print(union)

#**14. Գրել ծրագիր, որը while ցիկլով շրջում է list-ը։
# Եթե հանդիպում է 0, կանգ է առնում։
# Մինչ այդ պահը հանդիպած բոլոր թվերը ավելացնում է set-ի մեջ։**

lst=[1,2,3,4,5]
s = set()
i = 0

while i < len(lst):
    if lst[i]== 0:
        break
    s.add(lst[i])
    i = i+1
print(s)

#**15. Տրված է string, որը պարունակում է սիմվոլներ եւ թվեր (օր. "a1b2c3d0e9").
# Գրել ծրագիր, որը.
# հավաքում է բոլոր տառերը մեկ list-ում
# բոլոր թվերը՝ մեկ ուրիշում
# ենթախնդիր՝ թվերից կազմել ամբողջ թիվ (1,2,3 → 123).**

a = "a1b2c3d0e9"
str_lst = []
int_lst = []

for i in a:
    if i.isalpha():        # Buchstabe
        str_lst.append(i)
    elif i.isdigit():      # Zahl
        int_lst.append(int(i))
print(str_lst)
print(int_lst)
text = ''
for i in int_lst:
    text += str(i)
print(int(text))


#**16. Տրված է list երկարություններով (օր. [3,5,2,8]).
# Ստեղծել string, որը կրկնում է * նշանը համապատասխան քանակով։
# Օրինակ → ['', '*', '', '******']
# Օգտագործել՝ for, multiplication operator.

lst = [3,5,2,8]
lst1 =[]
for i in lst:
    lst1.append('*'*i)


print(lst1)


#**18. Սահմանել list բառերով։
# Ստեղծել set, որտեղ կլինեն բառերի առաջին տառերը
# Եթե set-ը ունի ավելի քան 3 տարր, pop-ով հանել մեկ տարր։**

words = ["apple", "banana", "cherry", "avocado", "blueberry"]
first_letters = set()
for i in words:
    first_letters.add(i[0])
if len(first_letters) > 3:
    first_letters.pop()
print(first_letters)

#**20. Պարզ ժամանակաչափ։
# Օգտագործել while, որը հաշվում է 10-ից մինչեւ 0
# Տպել ամեն թիվը։
# Եթե թիվը 5 է, արտածել «Halfway».**

num = 10
while num >= 0:
    print(num)

    if num == 5:
        print('Halfway')
    num = num - 1

