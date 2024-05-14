AllNumbers = {}
allstrings = []

def ltrim(s):
    i = 0
    while s[i] == ' ':
        i += 1
    return s[i:]

def rtrim(s):
    i = 1
    while s[-i] == ' ' or s[-i] == '\n':
        i += 1
    return s[:(len(s) + 1) - i]

def trim(s):
    return rtrim(ltrim(s))

def reverse_string(s):
    output = ''
    for i in range(1,  len(s) + 1):
        output += s[-i]
    return output

def atoi(s):
    output = 0
    for i in s:
        if i == ' ':
            return False
        if i == '-':
            continue
        output = (output * 10) + (ord(i) - ord('0'))
    if s[0] == '-':
        output *= -1
    return output

def itoa(i):
    output = ''
    negative = 0
    if i < 0:
        negative = 1
        i *= -1
    if i == 0:
        return '0'
    while i > 0:
        output += chr((i % 10) + ord('0'))
        i //= 10
    output = reverse_string(output)
    return ('-' * negative) + output

def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def custom_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[-1]
    left = []
    right = []
    for i in array[:-1]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    return custom_sort(left) + [pivot] + custom_sort(right)