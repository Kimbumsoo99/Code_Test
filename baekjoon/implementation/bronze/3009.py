import sys
input = sys.stdin.readline

graph = []
for i in range(3):
    graph.append(tuple(map(int, input().split())))

tmp = []
if graph[0][0] == graph[1][0]:
    tmp.append(graph[2][0])
elif graph[0][0] == graph[2][0]:
    tmp.append(graph[1][0])
else:
    tmp.append(graph[0][0])

if graph[0][1] == graph[1][1]:
    tmp.append(graph[2][1])
elif graph[0][1] == graph[2][1]:
    tmp.append(graph[1][1])
else:
    tmp.append(graph[0][1])


print(tmp[0], tmp[1])