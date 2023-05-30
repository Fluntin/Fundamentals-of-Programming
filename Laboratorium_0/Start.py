def hypotenusa(a,b):
    # dubbla gångertecken används som operator för potensräkning
    return ((a**2 + b**2)**0.5)

a = float(input('Ange längd på katet a: '))
b = float(input('Ange längd på katet b: '))
c = hypotenusa(a,b)

print('Hypotenusan blir ', c)