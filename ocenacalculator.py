#oceny = [3,1,1,2,2,2,5] + [1,4,2,1,1,2,2] + [1,2]
#wagi =  [2,2,2,2,2,4,2] + [2,2,2,4,2,2,1] + [2,2]

oceny = input("Oceny > ").split()
oceny = list(map(int, oceny))
wagi = input("Wagi > ").split()
wagi = list(map(int, wagi))

combinedwaga = 0
ocenyzwaga = 0

if len(oceny) == len(wagi):
    for n in range(0,len(oceny)):
        combinedwaga += wagi[n]
        ocena =+ (oceny[n]*wagi[n])
        ocenyzwaga += ocena
        średnia = ocenyzwaga / combinedwaga

print(round(średnia, 3))