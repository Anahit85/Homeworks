
#Ֆունկցիաներ եւ տվյալների տիպեր#
#____________(1–40)__________#

"""1.
Գրել square_numbers(nums) → վերադարձնել list, որտեղ բոլոր թվերը քառակուսի են։"""
from unicodedata import digit


def square_numbers(nums):
    return [i**2 for i in nums]

"""2.
Գրել count_even(nums) → հաշվել զույգ թվերի քանակը։"""

def count_even(nums):
    lst1 = [i % 2 == 0 for i in nums]
    return len(lst1)


"""3.
Գրել reverse_string(text) → վերադարձնել շրջված տող։"""
def reverse_string(text):
    return text[::-1]

"""4.
Գրել remove_negatives(nums) → վերադարձնել list առանց բացասական թվերի։"""
def remove_negatives(nums):
    return [i for i in nums if i>=0]

"""5.
Գրել sum_strings(data) → գումարել միայն այն տարրերը, որոնք string են եւ կարելի է
վերածել int-ի։"""
def sum_strings(data):
    total = 0
    for i in data:
        if isinstance(i, str):
            try:
                # Versuchen, den String in int umzuwandeln
                number = int(i)
                total += number
            except ValueError:
                pass
            # Falls Umwandlung nicht möglich is
            # wird das Element ignoriert
    return total

"""6.
Գրել find_longest_word(text)։?"""
def find_longest_word(text):
    longest_word = ""
    for word in text.split():
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


"""7.
Գրել merge_lists(a, b) → միավորել երկու list առանց կրկնությունների։"""
def merge_lists(a, b):
    return list(set(a + b))

"""8.
Գրել count_vowels(text)։"""
def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for i in text:
        if i in vowels:
            count += 1
    return count

"""9.Գրել multiply_all(nums) → վերադարձնել բոլոր թվերի արտադրյալը։"""
def multiply_all(nums):
    product = 1
    for n in nums:
        product *= n
    return product

"""10.
Գրել get_initials(full_name) → "John Smith" → "JS"։"""
def get_initials(full_name):
    text = full_name.strip()
    initials = ""
    for char in text:
        initials += char [0]
    return initials.upper()

print(get_initials("John Smith"))

"""11.
Գրել dict_values_sum(d) → գումարել միայն թվային value-ները։"""
def dict_values_sum(d):
    total = 0
    for value in d.values():
        if isinstance(value, (int, float)):
            total += value
    return total

"""12.
Գրել filter_short_words(words, n) → պահել միայն այն բառերը, որոնց
երկարությունը > n։"""

def filter_short_words(words, n):
    lst =[]
    for word in words:
        if len(word) >= n:
            lst.append(word)
    return lst

    #return list(filter(lambda word: len(word) >= n, words))
    #filter nur Wörter mit >n

print(filter_short_words(["John", "Banana", 'dog'], 3))

"""13.
Գրել unique_elements(data) → վերադարձնել list առանց կրկնությունների։"""
def unique_elements(data):

    seen = set()
    unique = []
    for item in data:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique

"""14.
Գրել count_char(text, ch) → հաշվել տեքստում նշված սիմվոլը։"""
def count_char(text, ch):
    count = 0
    for char in text:
        if char == ch:
            count += 1
    return count

"""15.
Գրել double_if_number(data) → եթե թիվ է → կրկնապատկել, եթե str → երկարություն
վերադարձնել։"""
def double_if_number(data):
    if isinstance(data, (int, float)):
        return data * 2
    elif isinstance(data, str):
        return len(data)
    else:
        return None

"""16.
Գրել max_in_dict(d) → վերադարձնել ամենամեծ թվային value-ն։"""
def max_in_dict(d):
    max_value = 0
    for value in d.values():
        if isinstance(value, dict):  # Rekursiver Fall
            max_value = max(max_value, max_in_dict(value))
        elif isinstance(value, (int, float)) and not isinstance(value, bool):
            max_value = max(max_value, value)
    return max_value

"""17.
Գրել min_max(nums) → վերադարձնել (min, max) tuple։"""
def min_max(nums):
    return (min(nums), max(nums))

"""18.
Գրել replace_spaces(text) → բացատները փոխարինել _-ով։"""
def replace_spaces(text):
    return text.replace(' ', '_')

"""19.
Գրել is_palindrome(text)։"""
def is_palindrome(text):
    return text[::-1] == text #Detta vänder texten baklänges.

"""20"""
def flatten_once(data):
    result = []
    for item in data:
        if isinstance(item, list): #om elementet är en lista.
            result += item
        else:
            result.append(item)
    return result
"""21.
Գրել remove_duplicates(text) → տողից հանել կրկնվող սիմվոլները։"""
def remove_duplicates(text):
    result = ""
    for ch in text:
        if ch not in result:
            result += ch
    return result

"""22.
Գրել sum_digits(number)։"""
def sum_digits(number):
    sum = 0
    for digit in number:
        sum += int(digit)
    return sum

"""23.
Գրել split_even_odd(nums) → վերադարձնել dict՝ { "even": [], "odd": [] }"""
def split_even_odd(nums):
    even = []
    odd = []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return {"even": even, "odd": odd }


"""24.
Գրել average_dict_values(d)։"""
def average_dict_values(d):
    total = 0
    for value in d.values():
        total += value
    return total / len(d)

"""25.
Գրել capitalize_words(text)։"""
def capitalize_words(text):
    return text.capitalize()

"""Գրել count_words(text)։"""
def count_words(text):
    return len(text.split())

"""27.
Գրել zip_lists(a, b) → վերադարձնել list of tuples։"""
def zip_lists(a, b):
    return list(zip(a, b))

"""28.
Գրել sort_numbers(nums) առանց օգտագործելու .sort()։"""
"""Ինչպես է աշխատում
Անցնում ենք ցուցակով (for ցիկլերով)։
Համեմատում ենք հարևան թվերը։
Եթե ձախ թիվը մեծ է աջից՝ փոխում ենք տեղերը։
Ամեն անցումից հետո ամենամեծ թիվը գնում է վերջ։"""
def sort_numbers(nums):
    n = len(nums)

    for i in range(n):
        for j in range(0, n - i - 1): #Այս ցիկլը անցնում է ցուցակի հարևան թվերով և համեմատում է դրանք։
            if nums[j] > nums[j + 1]: # Սա ստուգում է՝արդյոք ձախ թիվը մեծ է աջից։
                nums[j], nums[j + 1] = nums[j + 1], nums[j] #Եթե ձախ թիվը մեծ է, նրանք փոխում են տեղերը։

    return nums

"""29.
Գրել remove_empty_strings(data)։"""
def remove_empty_strings(data):
        for item in data:
            if item == "":
                data.remove(item)
        return data
"""30.
Գրել find_index(data, value) → եթե չկա → -1։"""
def find_index(data, value):
    for index, item in enumerate(data): #ger både index och värde från listan.
        if value == item:
            return index
    return -1

"""31.
Գրել group_by_length(words) → վերադարձնել dict ըստ երկարության։"""
def group_by_length(words):
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = [word]
        else:
            result[length].append(word)

        return result


"""32.
Գրել multiply_dict_values(d, n)։"""
def multiply_dict_values(d, n):
    result = {}
    for key, value in d.items():
        result[key] = value * n
    return result

"""33 Գրել count_uppercase(text)։"""
def count_uppercase(text):
    count = 0
    for char in text:
        if char.isupper():
            count += 1

    return count

"""34.
Գրել all_positive(nums) → վերադարձնել True եթե բոլորը դրական են։"""
def all_positive(nums):
    for num in nums:
        if num <= 0:
            return False
    return True
    #return False not in [num >0 for num in nums]


"""35.
Գրել dict_keys_to_list(d)։"""
def dict_keys_to_list(d):
    return list(d.keys())

"""36.
Գրել reverse_list(data) առանց [::-1]։"""
def reverse_list(data):
    return "". join(reversed(data))

"""37.
Գրել common_elements(a, b)։"""
def common_elements(a, b):
    return list(set(a) & set(b)) #intersection

"""38.
Գրել remove_value(data, value)։"""
def remove_value(data, value):
    return data.pop(value)

"""39.
Գրել string_to_list(text) → բաժանել ըստ բացատի։"""
def string_to_list(text):
    return text.split()

"""40.
Գրել is_sorted(nums)։"""
def is_sorted(nums):
    return sorted(nums) == nums


#### Ֆունկցիաներ + Exception Handling (41–50)####
"""41.
Գրել safe_divide(a, b)
Եթե բաժանումը հնարավոր չէ → վերադարձնել "Cannot divide"։"""
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Cannot divide'

"""42 Գրել safe_int(value) → եթե չի վերածվում int-ի → վերադարձնել None։"""
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None

"""43.
Գրել safe_get(d, key) → եթե key չկա → վերադարձնել "Key not found"։"""
def safe_get(d, key):
    try:
        return d.get(key)
    except KeyError:
        return 'Key not found'

"""44.
Գրել safe_list_access(lst, index)։"""
def safe_list_access(lst, index):
    try:
        return lst[index]
    except IndexError:
        return 'Index out of range'


"""45.
Գրել parse_number(text) → եթե թիվ չէ → raise ValueError։"""
def parse_number(text):
    try:
        return int(text)
    except ValueError:
        raise ValueError("Not a number")

"""46.
Գրել calculate_average(nums) → եթե list-ը դատարկ է → raise Exception։"""
def calculate_average(nums):
    try:
        return sum(nums) / len(nums)
    except ZeroDivisionError:
        return 'Cannot divide'

"""47.
Գրել validate_age(age) → եթե < 0 → raise ValueError։"""
def validate_age(age):
        age = int(age)
        if age < 0:
            raise ValueError('age cannot be negative')


"""48.
Գրել read_file_content(filename) → եթե file չկա → վերադարձնել "File not
found"։"""
def read_file_content(filename):
    try:
        with open(filename, "r") as file: # versucht es zu läsen
            return file.read()
    except FileNotFoundError:
        return 'File not found'

"""49.
Գրել safe_pop(lst) → եթե դատարկ է → վերադարձնել None։"""
def safe_pop(lst):
    try:
        return lst.pop()
    except IndexError:
        return None

"""50.
Գրել custom_division(a, b) →
Եթե b == 0 → raise ZeroDivisionError
Եթե ոչ թիվ են → raise TypeError"""
def custom_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Cannot divide'
    except TypeError:
        return 'Cannot divide'



















