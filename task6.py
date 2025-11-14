# ========== #
# Homework 6 #
# ========== #
#1. Թվային լիստի վիճակագրություն
a = [12, 7, 9, 21, 14, 18]
average = sum(a) / len(a)
maximum = max(a)
minimum = min(a)
count_above_avg = sum(1 for x in a if x > average)
print(f"average={average}, max={maximum}, min={minimum}, count_above_avg={count_above_avg}")

#🧩 2. չգրել֊֊֊֊Հաշվել բառերի հաճախականությունը Տրված է տեքստ, հաշվել յուրաքանչյուր բառի հանդիպման քանակը։ (օգտագործիր split() եւ dictionary)
text = "python is fun and python is easy"
words_count = {}
words = text.split()
for word in words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
print(words_count)

#🧩 3. Լիստում գտնիր ամենաշատ կրկնվող տարրը
nums = [1, 2, 3, 4, 3, 2, 1]
max_num = []
max_count = 0
for i in nums:
    a = nums.count(i)
    if a > max_count:
        max_count = a
        max_num = [i]
    elif a == max_count and i not in max_num:
        max_num.append(i)
print("The most frequent elements are", max_num )

# 🧩 4. Անունների ֆիլտրավորում
# Տրված է անունների լիստ։
# Հեռացրու բոլոր այն անունները, որոնք չեն սկսվում մեծատառով եւ պահիր մնացածը։
names = ["anna", "Bob", "john", "Alice"]
sorted_names = []
for i in names:
    if i[0].isupper():
     sorted_names.append(i)
print(sorted_names)

#🧩 5. Թվերի համեմատություն առանց max()/min()
#Գրի ծրագիր, որը գտնում է ամենամեծ թիվը լիստում առանց max() օգտագործելու։
nums = [5, 8, 12, 3, 9]
max_num = []
for i in nums:
    if i > nums[-1]:
        max_num.append(i)
print(max_num)

#🧩 6. Գրի ծրագիր, որը ստանում է թվերի tuple եւ վերադարձնում
#նոր tuple՝ առանց կրկնվող տարրերի։
t = (1, 2, 2, 3, 4, 4, 5)
unique_numbers = []
for i in t:
    if i not in unique_numbers:
        unique_numbers.append(i)
unique_numbers = sorted(unique_numbers)
print(unique_numbers)


#🧩 7. Գտիր string-ի մեջ ամենաերկար բառը եւ դրա երկարությունը
text = "Python programming is really powerful"
words = text.split()
longest = words[0]
for word in text:
    if len(word) > len (longest):
        longest = word
print('The longest word is', longest, len(longest))
#? Warum schreibt es 'python is fun'?

#🧩 8. Լիստում փոխարինիր բոլոր բացասական թվերը 0-ով
nums = [5, -3, 7, -1, 0, 9]
lst = []
for i in nums:
    if i > 0:
        lst.append(0)
    else:
        lst.append(i)
print(lst)

#🧩 9. Գտիր բոլոր թվերը, որոնք բաժանվում են 3-ի եւ 5-ի
nums = [3, 5, 15, 30, 7, 45, 8]
lst = []
for i in nums:
    if i % 3 == 0 and i % 5 == 0:
        lst.append(i)
print(lst)

#🧩 10. Գրի ծրագիր, որը ստուգում է՝ արդյոք լիստի տարրերը դասավորված են աճման կարգով
#(առանց sort() օգտագործելու)
nums = [3, 5, 15, 30, 7, 45, 8]
is_sorted = True
for i in range(len(nums)):
    if nums[i] > nums[i +1]:
        is_sorted = False
        break
if is_sorted:
    print( 'The list is sorted')
else:
    print( 'The list is unsorted')
# Was mache ich falsch?

#🧩 11. Գրի ծրագիր, որը ստանում է string-երի լիստ եւ  վերադարձնում է միայն այն բառերը, որոնք ունեն ավելի քան 3 տառ եւ պարունակում են “a” տառը։
words = ["cat", "apple", "dog", "banana", "sky"]
lst =[]
for i in words:
    if len(i) > 3 and 'a' in i:
        lst.append(i)
print(lst)

#🧩 12. Տրված է թիվ, ստուգիր՝ արդյոք դա պալինդրոմ է (օր.՝ 1221)
# Ich verstehe nicht.

#🧩 13. Բառերի դասավորում ըստ երկարության
# Տրված է բառերի լիստ։ Վերադարձրու բառերը ըստ երկարության աճման կարգով։
words = ["python", "is", "awesome", "fun"]
lst =[]
longest = words[0]
for word in words:
    if len(word) > len (longest):
        longest = word
print('Ihe words in lentgh is', longest)
# Ich brauche hilfe

#🧩 14. Միացրու երկու լիստ, բայց առանց կրկնվող տարրերի
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c = a + b
for i in c:
    unique_numbers = []
    for i in c:
        if i not in unique_numbers:
            unique_numbers.append(i)
print(unique_numbers)

#🧩 15. Գրի ծրագիր, որը կհաշվի՝ քանի բառ է սկսվում մեծատառով եւ քանի փոքրատառով
words = ["Apple", "banana", "Orange", "grape", "Pear"]
uppercase = []
lowercase = []
for word in words:
    if word[0].isupper():
     uppercase.append(word)
    else:
     lowercase.append(word)
print('Uppercase', len(uppercase))
print('Lowercase', len(lowercase))

#🧩 16. Բարդ string վերլուծություն
#Տրված է նախադասություն. Գրի ծրագիր, որը վերադարձնում է՝
#● բառերի քանակը,
#● տառերի քանակը (առանց բացատների),
#● ամենաերկար բառը։
text = "Python makes data analysis simple and powerful"
words = text.split()
word_count = len(words)
letter_count = 0
for char in text:
    if char != " ":
        letter_count += 1
longest_word = words[0]
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("Word count", word_count)
print("Letter count (without spaces)", letter_count)
print("Longest word", longest_word)

# 🧩 17. Գրի ծրագիր, որը թվերի լիստում գտնում է բոլոր զույգ թվերի գումարը եւ կենտ թվերի միջինը
nums = [10, 5, 8, 3, 6, 11]
even_sum = 0
odd_numbers = []
for num in nums:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_numbers.append(num)
if odd_numbers:
    odd_avg = sum(odd_numbers) / len(odd_numbers)
else:
    odd_avg = 0
print("even_sum =", even_sum)
print("odd_avg =", round(odd_avg, 2))

#🧩 18. Տրված է բառերի լիստ, վերադարձրու նոր լիստ՝ առանց կրկնվող բառերի, պահպանելով սկզբնական հերթականությունը
words = ["dog", "cat", "dog", "bird", "cat"]
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)
print(unique_words)

#🧩 19. Գրի ծրագիր, որը հաշվում է՝ քանի անգամ է յուրաքանչյուր տառ հանդիպում տեքստում (բացի բացատներից)
text = 'Hello world'
char_count = {}
for char in text:
    if char != " ":
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
print(char_count)

#🧩 20. Գրի ծրագիր, որը ստուգում է՝ արդյոք բոլոր լիստի տարրերը նույնն են
nums = [3, 3, 3, 3]
same_numbers = True
for i in range(1, len(nums)):
    if nums[i] != nums[0]:
        same_numbers = False
        break
print('All numbers are same', same_numbers)