def add_everything_up(a, b):

    try:
        summa = a + b
    except(TypeError):
        return str(a) + str(b)

    if isinstance((b), int):
        c = float(a) + float(b)
        return (round(c, 4))




print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))