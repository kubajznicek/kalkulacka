import math

vysledek = None
cislo1 = None
cislo2 = None
number  = None

def scitani(A, B):
    return A + B

def odcitani(A, B):
    return A - B

def nasobeni(A, B):
    return A * B

def deleni(A, B):
    return A / B

def umocneni(A, B):
    return A ** B

def odmocnovani(A):
    return (math.sqrt(A))

def MujInput ():
    while True:
        try:
            number = (float( input("zadejte cislo: ")))
        except ValueError:
            continue
        else:
            print(number)
            return number


#  odstrannit korba.py


print('1 sčítání')
print('2 odčítání')
print('3 násobení')
print('4 dělení')
print('5 odmocnina na 2')
print('6 umocnění')
operace = input ("zadejte operaci: ")

while True:

    if operace in "1, 2, 3, 4, 5, 6,":
        break
    else:
        print ('zadaji jste neplatný znak' )
        operace = input('znovu zadejte operaci: ')


cislo1 = MujInput()
# 9print(cislo1)

while True:
    if operace == '1':
        cislo2 = MujInput()
        vysledek = scitani(cislo1, cislo2)
        operator = "+"

    elif operace == '2':
        cislo2 = MujInput()
        vysledek = odcitani(cislo1, cislo2)
        operator = "-"

    elif operace == '3':
        cislo2 = MujInput()
        vysledek = nasobeni(cislo1, cislo2)
        operator = "*"

    elif operace == '4':
        cislo2 = MujInput()
        vysledek = deleni(cislo1, cislo2)
        operator = "/"

    elif operace == '5':
        vysledek = odmocnovani(cislo1)
        operator = "odmocneno"

    elif operace == '6':
        cislo2 = MujInput()
        vysledek = umocneni(cislo1, cislo2)
        operator = "umocneno"
    
    if cislo1 != 'nic':
        break


# print('výsledek je', vysledek)
print( )
print(cislo1, operator, cislo2, "=", vysledek)

#print(len(vysledek))


