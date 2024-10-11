try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter b: "))

except ValueError:
    print('a or b or c = int')
    
D = b**2 - 4 * a * c
x1 = ( -b + D**0.5) / ( 2*a)
x2 = ( -b - D**0.5) / (2*a)
print(x1)
print(x2)


