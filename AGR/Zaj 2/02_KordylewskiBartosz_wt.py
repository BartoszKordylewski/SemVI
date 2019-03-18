
matrix = []
f=open("matrixDFS.txt", "r")
with open('matrixDFS.txt') as textFile:                                 #Otwieranie pliku z zapisana macierza przyleglosci dla jednego lub kilku grafow
    lines = [line.split() for line in textFile]
    matrix = [list(map(int, i)) for i in lines]
matrixgraph = {}
index = 0
for v in matrix:
    adjacenVertices = []
    adjacentVertex = 0
    degree = 0
    for edge in v:
        if edge == 1:
            degree += 1
            adjacenVertices.append(adjacentVertex)
        adjacentVertex += 1
    v = {index: set(adjacenVertices)}
    matrixgraph.update(v)
    index += 1;

def dfs(matrixgraph, s):                                # Implementacja DFS
    path = []                                           # sciezka
    c = []
    vertices = []
    for v in matrixgraph:
        vertices.append(v)
    visited = set()                                     # ustawienie juz odwiedzonych wierzcholkow w tablicy aby juz ich nie odwiedzic
    stack = [s]
    while stack:
        v = stack.pop()
        if v not in visited:
            c.append(v)
            visited.add(v)
            vertices.remove(v)
            stack.extend(matrixgraph[v] - visited)
        if not stack and vertices:
            path.append(c)
            c = []
            stack.append(vertices[0])
        if not stack and not vertices:
            path.append(c)
    return path

Components = dfs(matrixgraph, 0)                        # Wstawienie do tablicy skladowych spojnosci

nextVertices = []
for c in Components:
    for v in c:
        nextVertices.append(v)


print("Wierzcholki w kolejnosci ich rozpatrzenia:")
print(nextVertices)



print("Liczba skladowych spojnosci rowna jest " + str(len(Components)))



print("Kolejne skladowe spojnosci:")
for c in Components:
    print(c)