"""1. Տիպերից կախված վարք
Խնդիր
Գրել process(value) ֆունկցիա, որը.
● եթե int կամ float → վերադարձնի քառակուսին
● եթե str → վերադարձնի տողի երկարությունը
● եթե list կամ tuple → վերադարձնի թվային տարրերի գումարը
● եթե dict → վերադարձնի բանալիների քանակը
● այլ դեպքում → "Unsupported type" """



def process(value):
    if isinstance(value, (int, float)):
        return value
    elif isinstance(value, str):
        return value
    elif isinstance(value, (list,tuple)):
        lst=[]
        for item in value:
            if isinstance(item, (int, float)) and not isinstance(item, bool):
                lst.append(item)
        return sum(lst)
    elif isinstance(value, dict):
        return len(value)
    else:
        return "Unsupported type"

"""2. Mixed list վերլուծություն
Խնդիր
Գրել analyze_list(data) ֆունկցիա, որը ընդունում է տարբեր տիպերի list եւ
վերադարձնում է dictionary.
{
"numbers": [1, 3.5, 7],
"strings": ["hi", "ok"],
"others": [[], {}]
}
Պահանջներ.
● պահպանել սկզբնական հերթականությունը
● չօգտագործել collections"""
def analyze_list(data):
    result ={
        "numbers": [],
        "strings": [],
        "others": []
    }
    for item in data:
        if isinstance(item, (int, float)):
            result["numbers"].append(item)
        if isinstance(item, str):
            result["strings"].append(item)
        else:
            result["others"].append(item)
        return result

lst = ["sss", 1, [1, 2, 3], {"a": 45}, 15, 78, "str", True, False]
print(analyze_list(lst))

"""3. Dict արժեքների ֆիլտրում
Խնդիր
Գրել filter_dict(d) ֆունկցիա, որը վերադարձնում է նոր dict՝
● միայն այն զույգերը, որոնց value-ն int կամ float է
● եւ value > 10"""
def filter_dict(d):
    filtered_dict = {}
    for key, value in d.items():
        if isinstance(value, (int, float)):
            filtered_dict[key] = value
        return dict
dct = {"a": 5, "b": 27, "c": 5, "d": 25, "e": "anfkjhnf"}
print(filter_dict(dct))

"""4. Տվյալների normalize ֆունկցիա
Խնդիր
Գրել normalize(data) ֆունկցիա։
Եթե data-ն.
● list է → վերադարձնել list, որտեղ բոլոր թվերը float են
● tuple է → վերադարձնել tuple նույն ձեւով
● set է → վերադարձնել set, միայն թվային արժեքներով
● dict է → վերադարձնել dict, որտեղ միայն թվային value-ներն են եւ float տիպով

📌 Չթույլատրել type change (list → tuple, tuple →list)"""

def normalize(data):

    if isinstance(data, list):
        # return [float(i) for i in data if isinstance(i, (int, float))]

        lst = []
        for i in data:
            if isinstance(i, (int, float)):
                lst.append(float(i))
        return lst
    elif isinstance(data, tuple):
        return data
    elif isinstance(data, set):
        return {i for i in data if isinstance(i, (int, float))}
    elif isinstance(data, dict):
        return {k: float(v) for k, v in data.items()
                if isinstance(v, (int, float))}
    else:
        return "Unsupported type"

"""5. String parsing + type conversion
Խնդիր
Գրել parse_values(text) ֆունկցիա։
Մուտք.
"text = '10, 3.14, hello, 7, world'"
Ելք.
{
"int": [10, 7],
"float": [3.14],
"str": ["hello", "world"]
}
📌 Չօգտագործել regex"""

def parse_values(text):
    result = {
        "int": [10, 7],
        "float": [3.14],
        "str": ["hello", "world"]
    }
    parts = [i.strip() for i in text.split(",")]

    for item in parts:
        if item.isdigit():
            result['int'].append(int(item))
        elif item.count(".") == 1 and item.replace(".", "").isdigit():
            result['float'].append(float(item))
        else:
            result["str"].append(item)

    return result
text = '14, 3.5, hi, 5, python, [1,2,5."funny"]'
print(parse_values(text))

#6
def sum_nested(data):
    # Falls data eine Zahl ist, geben wir sie direkt zurück.
    # Das ist der Basisfall der Rekursion.
    if isinstance(data, (int, float)):
        return data

    # Wir initialisieren die Summe mit 0.
    total = 0

    # Falls data eine Liste oder ein Tuple ist,
    # gehen wir rekursiv jedes Element durch.
    if isinstance(data, (list, tuple)):
        for item in data:
            total += sum_nested(item)

    # Falls data ein Dictionary ist,
    # iterieren wir über die Werte (nicht über die Keys!).
    elif isinstance(data, dict):
        for item in data.values():
            total += sum_nested(item)

    # Falls es weder Zahl noch Container is (z.B. String),
    # wird es ignoriert und 0 zurückgegeben.
    return total


print(sum_nested([1, "string", [2, (3, 4, [1, 2, 3])], {"a": 5,"b":[1,2,3,[4,5,6,[7,8,9]]]}]))


"""7. Տիպերի validation
Խնդիր
Գրել validate_types(*args) ֆունկցիա, որը վերադարձնում է True, եթե
● բոլոր args-ը նույն տիպի են
● հակառակ դեպքում False
Բացառել bool (չհամարել որպես int)"""
def validate_types(*args):
    if not args:
        return True

    t = type(args[0])
    if t is bool:
        return True
    for x in args:
        if type(x) != t:
            return False
    return True

print(validate_types(1.0, 2.0))


def aggregate(data):
    """ Wir erstellen ein leeres Dictionary,
    # in dem wir die aufsummierten Werte speichern.
    # Format wird später z.B. {"A": 17, "B": 5} sein."""
    result = {}

    """ Wir gehen jedes Element der Liste "data" durch.
    Jedes Element soll ein Dictionary sein. """
    for item in data:

        """Sicherheitsprüfung:
        1. Ist das Element überhaupt ein Dictionary?
        2. Enthält es den Key "type"?
        3. Enthält es den Key "value"?
        Falls eine dieser Bedingungen nicht erfüllt ist,
        wird das Element ignoriert (wie in der Aufgabe gefordert)."""
        if isinstance(item, dict) and "type" in item and "value" in item:

            """ Wir speichern den Wert von "type" in der Variable t.
            # Beispiel: t = 'A'"""
            t = item["type"]

            """Wir speichern den Wert von "value" in der Variable v.
            # Beispiel: v = 10"""
            v = item["value"]

            """Wir prüfen, ob der Wert numerisch ist (int oder float).
            # Falls nicht (z.B. String), wird er ignoriert."""
            if isinstance(v, (int, float)):

                """Hier passiert die Aggregation (Summierung):
                # result.get(t, 0) bedeutet:
                # - Falls t schon im Dictionary existiert → nimm den aktuellen Wert
                # - Falls nicht → nimm 0 als Startwert
                
                # Danach addieren wir den neuen Wert v dazu."""
                result[t] = result.get(t, 0) + v

    """ Am Ende geben wir das fertige aggregierte Dictionary zurück."""
    return result


# Testdaten
data = [
    {"type": "A", "value": 10},
    {"type": "B", "value": 5},
    {"type": "A", "value": 7},
    {"a": "A", "b": 7},  # Wird ignoriert, da "type" und "value" fehlen
]

# Funktionsaufruf + Ausgabe
print(aggregate(data))


"""9. Flexible comparison function
Խնդիր
Գրել compare(a, b) ֆունկցիա։
● եթե նույն տիպի են → վերադարձնել a == b
● եթե տարբեր տիպի են, բայց թվային → համեմատել որպես float
● այլ դեպքում → False"""

def compare(a,b):
    if type(a) == type(b):
        return a==b
    if isinstance(a,(int,float)) and isinstance(b,(int,float)):
        return float(a) == float(b)
    return False

print(compare(3, 3.4))

"""10. Safe getter
Խնդիր
Գրել safe_get(data, path) ֆունկցիա։
data = {"a": {"b": [10, 20]}}
safe_get(data, ["a", "b", 1]) # 20
safe_get(data, ["a", "c"]) # None
📌 Աշխատում է dict + list խառն տվյալների վրա"""
def safe_get(data, path):
    current = data

    for key in path:
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, list) and isinstance(key, int) and key < len(current):
            current = current[key]
        else:
            return current

"""11. Թվերի եւ տեքստերի հաշվարկ
Խնդիր
Գրել count_types(data) ֆունկցիա, որը list-ից հաշվում է՝
{
"numbers": ?,
"strings": ?
}
📌 Թվեր = int + float
📌 Մնացածը անտեսել"""
def count_types(data):
    nums = 0
    strs = 0

    for i in data:
        if isinstance(i, (int, float)):
            nums += 1
        elif isinstance(i, str):
            strs += 1
    return {"numbers": nums, "strings": strs}

data = [1, 2, 3, "shfkh", "fhhdf", 5]
print(count_types(data))

"""12. Բառերի երկարություն
Խնդիր
Գրել word_lengths(text) ֆունկցիա։
"python is fun"
→ [6, 2, 3]
📌 Բաժանել բացատներով"""

def word_lenghts(text):
    words = text.split()
    lens = []
    for word in words:
        lens.append(len(word))
        return lens

print(word_lenghts("python is fun"))

"""13. Ամենամեծ թիվը list-ում
Խնդիր
Գրել max_number(data) ֆունկցիա, որը վերադարձնում է ամենամեծ թիվը list-ում։
📌 Եթե թվեր չկան → վերադարձնել None"""

def max_number(data):
    nums = [i for i in data if isinstance(i, (int,float))]

    if nums:
        return max(nums)
    return None

data = [1,2,3,4,5,("dfsfsdf"),6,"fasfsafasas7,8,9,10",34,432,543,["fsdfas"]]
print(max_number(data))

"""14. Տողի մեջ թվերի քանակ

Խնդիր
Գրել count_digits(text) ֆունկցիա։
"abc123x5"
→ 4
📌 Օգտագործել isdigit()"""

def count_digits(text):
    count = 0
    for ch in text:
        if ch.isdigit():
            count += 1
    return count

text = "hfhffklfdj"
print(count_digits(text))

"""15. List → Dict փոխակերպում
Խնդիր
Գրել list_to_dict(words) ֆունկցիա։
["hi", "python"]
→ {"hi": 2, "python": 6}
📌 value = բառի երկարություն"""
def list_to_dict(words):
    result ={}
    for i in words:
        result[i] = len(i)
    return result

print(list_to_dict(["hi", "python","1","fdasfsdgfsdg"]))







