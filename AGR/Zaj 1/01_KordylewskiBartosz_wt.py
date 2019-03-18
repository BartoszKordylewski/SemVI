
with open('graf.txt') as textFile:                                                                              #Otwieranie pliku z zapisana macierza przyleglosci
    lines = [line.split() for line in textFile]
    Array = [list(map(int, i)) for i in lines]

print(" ")
print("a) Wypisuje stopnie kolejnych wierzcholkow")
maxEdges=0
index=1
for v in Array:
    d=0
    for e in v:
        if e == 1:
            d+=1
        if maxEdges < d:
            maxEdges = d
    print("Stopien wierzcholka "+str(index)+": " + str(d))
    index+=1

print(" ")
print ("b) wypisuje wierzcholki przylegle do wierzcholka o najwiekszym stopniu")
index_2=1
for v in Array:
    aVertives=[]
    aVertex=0
    degree =0
    for e in v:
        if e == 1:
            degree += 1
            aVertives.append(aVertex)
        aVertex +=1
    if degree == maxEdges:
        print ("Przylegle wierzcholki wierzcholka o numerze " + str(index_2)+ ": " + str(aVertives))
    index_2+=1

print(" ")
print("c) Wypisuje wszystkie krawedzie grafu")
index_3=1
e=[]
for v in Array:
    index_3_1 = 1
    for m in v:
        eAr = []
        if m == 1:
            eAr.append(index_3)
            eAr.append(index_3_1)
        if eAr:
            e.append(eAr)
        index_3_1 += 1
    eAr = []
    index_3 += 1

p = set()
q = []
for n in e:
    sd = tuple(sorted(n))
    if sd not in p:
            q.append(n)
            p.add(sd)
n = q
print('Wszystkie krawedzie wystepujace w grafie')
print(n)

print("")
print("d) wypisuje macierz incydencji")
Array_2 = []
index_4 = 0
for v in Array:
    i_Array = []
    for e in n:
        if e[0] == index_4 or e[1] == index_4:
            i_Array.append(1)
        else:
            i_Array.append(0)
    Array_2.append(i_Array)
    index_4 += 1
print("Macierz incydencji")
for o in Array_2:
    print(o)

print("")
print("e) wypisuje liste nastepnikow")
index_5 = 0
for v in Array:
    aVs = []
    aVx = 0
    d = 0
    for e in v:
        if e == 1:
            d += 1
            aVs.append(aVx)
        aVx += 1
    print("Nastepniki wierzcholka " + str(index_5) + ': ' + str(aVs))
    index_5 += 1;