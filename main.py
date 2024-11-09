def AddAll(a,b):
    try:
        if isinstance(a(int,float)) and isinstance(b(int,float)):
            return a + b
        elif isinstance(a(str)) and isinstance(b(str)):
            return a + b
        else:
            raise TypeError
    except TypeError:
        return f'{str(a)}{str(b)}'

print(AddAll(123.456, 'строка'))
print(AddAll('яблоко', 4215))
print(AddAll(123.456, 7))