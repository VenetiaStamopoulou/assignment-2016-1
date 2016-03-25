import argparse

parser = argparse.ArgumentParser()

parser.add_argument("filename", help="name of graph")
parser.add_argument("k", help="size of truss",
                    type=int)

args = parser.parse_args()

f = open(args.filename)

g = []
e = []
s = []

for line in f:

    x = line.split()
    x = [int(i) for i in x]
    g.append(x)

f.close()

y = 0
n = len(g)
for i in range (0, n):

    if y < max(g[i]):
        y = max(g[i])

graph = {}
e = []
s = []

for i in g:
   e.append(i[0])
   s.append(i[1])

for i in range(0,y):
    neighbours = []
    for j in range(0,n):

        if i == e[j]:
            neighbours.append(s[j])
        elif i == s[j]:
            neighbours.append(e[j])
        graph[i] = neighbours

edge = []
for i in range(0, y):
    a = graph[i]
    b = graph[i + 1]
    u = set.intersection(a,b)
    if (size(intersection(a, b)) < (k - 2)):
        graph.remove(edge)
print (edge)
