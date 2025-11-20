# ========================= #
#      SET  ՀԵՇՏ ԽՆԴԻՐՆԵՐ    #
#      Task 7               #
# ========================= #

# 1 Ստեղծիր դատարկ set և ավելացրու դրա մեջ 3 տարր add()-ով։
set1 = set()
set1.add(1)
set1.add(2)
set1.add(3)
print(set1)

#2  Ստեղծիր set թվերով 1-ից 5-ը և օգտատիրոջից վերցրած թիվը ավելացրու set-ին։
set1 = {1,2,3,4,5}
x = int(input("Enter a number: "))
set1.add(x)
print(set1)

#3 Տրված է set: {"red", "green"}

set1 = {"red", "green"}
set1.update(["blue", "yellow", "black"])
print(set1)

#4 Սահմանիր set և տպիր առաջին (պատահական) pop() եղած արժեքը։

set1 = {10,20,30}
x = set1.pop()
print(x)
print(set1)


#5 . Ստեղծիր set և հեռացրու նրանից կոնկրետ արժեք remove()-ով այնպես, որ սխալ չտա։
s = {1,2,3,4,5,6,7,8,9}
x = int(input("Enter a number: "))
if x in s:
    s.remove(x)
    print(f'{x} is removed from the set')
else:
    print("X is not in the set")
print(s)

#6  Ստեղծիր set և այնպես հեռացրու գոյություն չունեցող տարր, որ սխալ չլինի (discard())։
set1 = {1,2,3,4,5,6,7,8,9}
set1.discard(10)
print(set1)

#7 Ստուգիր՝ արդյոք տվյալ տարրը կա set-ի մեջ՝ օգտագործելով in։
set1 = {1,2,3,4,5,6,7,8,9}
x = int(input("Enter a number: "))
if x in set1:
    print("Exists")
else:
    print("Not Exists")

#8  Գրիր ծրագիր, որը ամբողջ set-ը կմաքրի clear()-ով։
s = {1,5,6,7,9}
s.clear()
print(s)

# ======================= #
# UPDATE / UNION ԽՆԴԻՐՆԵՐ #
# ====================== #

#9  Ստեղծիր երկու set և միավորիր դրանք update() օգտագործելով։
s1 = {1,2,3}
s2 = {4,5,6}

s1.update(s2)
print(s1)


#10 Տրված է երկու set. Գրի՛ր ծրագիր, որը կստեղծի նոր set նրանց միավորումով, օգտագործելով union()։
s1 = {"A","B","C"}
s2 = {"D","E","F"}

s3 = s1.union(s2)
print(s3)

# ============================ #
# INTERSECTION /               #
# INTERSECTION_UPDATE ԽՆԴԻՐՆԵՐ  #
# ============================ #

#11 Գտիր երկու set-երի intersection-ը՝ intersection() ֆունկցիայով։
s1 = {"a","b","c"}
s2 = {"a","v","g",}

s3 = s1.intersection(s2)
print(s3)



#12  Տրված է set A և B. Գրի՛ր ծրագիր, որը A-ի վրա կիրառում է intersection_update() այնպես, որ A-ում մնան միայն ընդհանուր տարրերը։
A = {1,2,4}
B = {2,3,4}

A.intersection_update(B)
print(A)



#13  Գրիր ծրագիր, որը ստուգում է՝ երկու set-երը ընդհանուր տարր ունեն թե ոչ։ (Օգտագործել intersection())
s1 = {1,2,3}
s2 ={3,4,5}
if s1.intersection(s2):
    print("Uni krknvox element")
else:
    print("Chuni krknvox element")


#14 Ստեղծիր երկու set և գտիր տարրերը, որոնք կան միայն մեկում՝ symmetric_difference() միջոցով։
s1 = {1,2,3,4,5,6,7,8,9}
s2 = {9,10}

s3 = s1.symmetric_difference(s2)
print(s3)




#15 Տրված է set A և B. Կատարիր symmetric_difference_update(), որպեսզի A-ը պահի միայն այն տարրերը, որոնք B-ում չկան։

A = {"a","b","c"}
B = {"a","d","f"}

A.symmetric_difference_update(B)
print(A)



#16 Ստուգիր՝ արդյոք symmetric difference-ի չափը մեծ է 3-ից։
s1 = {1,2,3,4,5,6,7,8,9}
s2 = {10,8}

s3 = s1.symmetric_difference(s2)
if len(s3) > 3:
    print(True)
else:
    print(False)

# ======================= #
# POP / REMOVE / DISCARD  #
# ԽՆԴԻՐՆԵՐ                 #
# ======================= #

#17  Ստեղծիր set և pop-ով հեռացրու բոլոր տարրերը (մինչև դատարկ դառնա)։
s1 = {1,2,3,4,5,6,7,8,9}

while s1:
    s1.pop()

print(s1)

# ====================== #
# FROZENSET ԽՆԴԻՐՆԵՐ      #
# ====================== #

#19 Ստեղծիր frozen set և փորձիր դրա մեջ տարր ավելացնել (տես, թե ինչ սխալ է տալիս)։
fs = frozenset([1,2,3])

fs.add(4)
print(fs)


#20  Տրված է list. Վերածիր այն frozen set-ի, ապա ստուգիր՝ արդյոք frozen set-ը կարող է լինել dictionary key։
lst = [1,2,3]
fs = frozenset(lst)
d = {fs:lst}
print(d)

#21 Ստեղծիր frozen set և ստուգիր դրա երկարությունը, միջին արժեքը և ամենամեծը։
fs = frozenset([1,2,3,4,5,6,7])

print(len(fs))
print(sum(fs)/len(fs))
print(max(fs))


#22 Ստեղծիր երկու frozen set և գտիր նրանց intersection-ը և symmetric difference-ը։
fs1 = frozenset([1,2,3])
fs2 = frozenset([4,5,6])

print(fs1.intersection(fs2))
print(fs1.symmetric_difference(fs2))

# ======== #
# ԽՈՐԱՑՎԱԾ  #
# ======== #

#23  Տրված է set և frozen set: Գրի՛ր ծրագիր, որը համեմատում է, թե որում կան ավել տարրեր։**
s1 = {1,2,4}
fs1 = frozenset([1,2,3,4])
if len(s1) > len(fs1):
    print("SET")
elif len(s1) < len(fs1):
    print("FROZENSET")
else:
    print("Equal")


#25 Ստեղծիր set և հեռացրու նրանից բոլոր տարրերը for-loop + pop() համադրությամբ։

set1 = {1,2,4,5,9,10}

for _ in range(len(set1)):
    set1.pop()
print(set1)

#26 Գրի՛ր ծրագիր, որը երկու set-երից ստանում է նոր set, որը բաղկացած է միայն եզակի (ոչ կրկնվող) տարրերից՝ օգտագործելով symmetric difference։
A = {1,2,3}
B = {3,4,5}

C = A.symmetric_difference(B)
print(C)

#27 Ստեղծիր set անուններով և update() կիրառիր list-ի, tuple-ի և մյուս set-ի վրա (սովորիր տարբերությունները)։
s = {"apple"}

s.update(["banana", "orange"])
s.update(("mango", "grape"))
s.update({"kiwi","watermelon"})

print(s)

