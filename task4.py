# 1️⃣capitalize()
# Գրի ծրագիր, որը մուտքագրած նախադասության առաջին տառը դարձնում է մեծատառ։
sentence = input("pyton is fun ")
print(sentence.capitalize())

# 2️⃣ count()
# Հաշվի՝ քանի անգամ է տրված տառը հանդիպում տողում։
word = input("Input word")
letter = input("Input letter")
count_1 = word.count(letter)
print("Output", count_1)

# 3️⃣ endswith()
# Ստուգիր՝ արդյոք տեքստը ավարտվում է “.com”-ով։
text = input("Input text")
result = text.endswith(".com")
print("Output", result)

# 4️⃣find()
# Գրի ծրագիր, որը գտնում է “Python” բառի առաջին դիրքը տեքստում։
word = input("Input word")
result = word.find("Python")
print("Output", result)


# 5️⃣ format()
# Տպիր նախադասություն .format() մեթոդով։
name = input("Enter your name: ")
age = input("Enter your age: ")
sentence = ("My name is {}, I am {} years old.".format(name, age))
print(sentence)

#6️⃣index()
#Գրի ծրագիր, որը վերադարձնում է առաջին “a”-ի ինդեքսը տեքստում։
word = input("Input word: ")
position = word.index("a")
print("Output", position)

#7️⃣isalnum()
#Ստուգիր՝ արդյոք տեքստը բաղկացած է միայն տառերից եւ թվերից։
text = input("Input text")
result= text.isalnum()
print('output', result)

#9️⃣isdecimal()
#Ստուգիր՝ արդյոք մուտքագրված արժեքը միայն թվանշաններ են (օր. “123”)։
txt = "123"
x = txt.isdecimal()
print(x)

#🔟 isdigit()
#Գրի ծրագիր, որը ստուգում է՝ արդյոք տեքստը թվային է։
txt = input("Input")
result = txt.isdigit()
print("Output", result)

#11isidentifier()
#Ստուգիր՝ արդյոք տեքստը կարող է լինել Python փոփոխականի անուն։
txt = input("Input: ")
result = txt.isidentifier()
print("Output:", result)

#12 islower()
#Ստուգիր՝ արդյոք բոլոր նիշերը փոքրատառ են։
word = input("Input word")
result = word.islower()
print("Output", result)

#13 isnumeric()
#Ստուգիր՝ արդյոք տեքստը բաղկացած է միայն թվային նիշերից (ներառյալ ուրիշ լեզուների թվեր)
text = input("Input word")
result = text.isnumeric()
print("Output", result)

#14️ isspace()
#Ստուգիր՝ արդյոք տեքստը բաղկացած է միայն բացատներից։
text = input("Input word")
result = text.isspace()
print("Output", result)

# 15️ istitle()
# Ստուգիր՝ արդյոք նախադասությունը գրված է վերնագրային ձեւով։
sentence = input("Input sentence")
result = sentence.istitle()
print("Output", result)

#16️ isupper()
#Ստուգիր՝ արդյոք բոլոր տառերը մեծատառ են։
letter = input("Input letter")
result = letter.isupper()
print("Output", result)

#17 join()
#Միացրու լիստի էլեմենտները մեկ տողում։
words = ["Python", "is", "fun"]
result = "-".join(words)
print("Output", result)

#18 lower()
#Գրի ծրագիր, որը տեքստը դարձնում է փոքրատառ։
text = input("Input text")
result = text.lower()
print("Output", result)

# 19️ replace()
# Փոխարինիր տեքստում բոլոր “cat”-երը “dog”-ով։
text = input("Input")
result = text.replace ('cat', 'dog')
print("Output", result)

#20️ split()
#Բաժանիր նախադասությունը բառերի լիստի։
sentence = input("Input sentence")
result = sentence.strip()
print("Output", result)

#21️ startswith()
#Ստուգիր՝ արդյոք տեքստը սկսվում է “Hello”-ով։
text = input("Input text")
result = text.startswith( 'Hello')
print("Output", result)

#22️ strip()
#Հեռացրու բացատները տողի սկզբից եւ վերջից։
text = input("Input text")
result = text.strip()
print("Output", result)

#23️ upper()
#Գրի ծրագիր, որը տեքստը դարձնում է մեծատառ։
text = input("Input text")
result = text.upper()
print("Output", result)

# ======================= #
#🧩 List Method Problems  #
# ======================= #

#🔹 append()
lst = []
for i in range(5):
    item = int(input("Enter a number "))
    lst.append(item)
print("List", lst)

#🔹 clear()
lst = [1,2,3,4,5]
lst.clear()
print("List after clear", lst)

#🔹 copy()
a = [1,2,3]
b = a.clear()
print("List a is orignal", a)
print("List b is copy", b)

#🔹 count()
lst = [3 , 5, 3, 3, 8]
count_3 = lst. count(3)
print("Count num 3", count_3, 'times')








