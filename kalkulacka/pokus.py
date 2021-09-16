import math
#import

#ahoj more

vysledek = 'nic'
cislo1 = 'nic'
cislo2 = 'nic2'

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

print('1 sčítání')
print('2 odčítání')
print('3 násobení')
print('4 dělení')
print('5 odmocnina na 2')
print('6 umocnění')
operace = input ("zadejte operaci ")


while True:
    if operace == '1':
        cislo1 = float( input("prvni cislo "))
        cislo2 = float( input("druhe cislo "))
        vysledek = scitani(cislo1, cislo2)

    elif operace == '2':
        cislo1 = float( input("prvni cislo "))
        cislo2 = float( input("druhe cislo "))
        vysledek = odcitani(cislo1, cislo2)

    elif operace == '3':
        cislo1 = float( input("prvni cislo "))
        cislo2 = float( input("druhe cislo "))
        vysledek = nasobeni(cislo1, cislo2)

    elif operace == '4':
        cislo1 = float( input("prvni cislo "))
        cislo2 = float( input("druhe cislo "))
        vysledek = deleni(cislo1, cislo2)

    elif operace == '5':
        cislo1 = float(input('cislo'))
        vysledek = (math.sqrt(cislo1))

    elif operace == '6':
        cislo1 = float( input("prvni cislo "))
        cislo2 = float( input("druhe cislo "))
        vysledek = umocneni(cislo1, cislo2)

    else:
        print ('zadaji jste neplatný znak' )
        operace = input('znovu zadejte operaci ')
    
    if cislo1 != 'nic':
        break


print('výsledek je', vysledek)

#print(len(vysledek))


