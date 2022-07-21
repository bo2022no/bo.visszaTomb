import random


def veletlenSzam(elsoSzam, utolsoSzam):
    rnd = random.Random()
    vissza = rnd.randrange(elsoSzam, utolsoSzam)
    return vissza

def visszaFeltoltas(elsoElem):
    vissza = [0, 0, 0, 0, 0, 0]
    for i in range(6):
        vissza[i] = elsoElem
    return vissza



def tombElemek(szamok):
    vissza = [0,0,0,0,0,0]
    vissza = visszaFeltoltas(szamok[0])
    for i in szamok:
        if i < vissza[0]:
            vissza[0] = i
        if i > vissza[1]:
            vissza[1] = i
        if i % 2 == 0 and vissza[2] > i:
            vissza[2] = i
        if i % 2 == 0 and vissza[3] < i:
            vissza[3] = i
        if i % 2 != 0 and vissza[4] > i:
            vissza[4] = i
        if i % 2 != 0 and vissza[5] < i:
            vissza[5] = i
    return vissza

szamok = []



# szamok = [0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    szamok[i] = veletlenSzam(1,1000)

print(szamok)
tomb = [0,0,0,0,0,0]
tomb = tombElemek(szamok)

print("A legkisebb szam : ",tomb[0])
print("A legnagyobb szam : ",tomb[1])
print("A legkisebb páros szam : ",tomb[2])
print("A legbagyobb páros szam : ",tomb[3])
print("A legkisebb páratlan szam : ",tomb[4])
print("A legnagyobb páratlan szam : ",tomb[5])