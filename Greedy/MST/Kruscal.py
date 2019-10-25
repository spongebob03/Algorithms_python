#kruscal
parent = {}
rank = {}

# 정점 집합
def make_set(v):
    parent[v] = v
    rank[v] = 0

# 해당 정점의 최상위 정점을 찾는다.
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])

    return parent[v]

# 두 정점을 연결
def union(v, u):
    root1 = find(v)
    root2 = find(u)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2

            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal(graph):
    totalWeight=0
    for v in graph['vertices']:
        make_set(v)

    mst = []

    edges = graph['edges']
    edges.sort()

    for edge in edges:
        weight, v, u = edge

        if find(v) != find(u):
            union(v, u)
            mst.append(edge)
            totalWeight+=weight
    print("totalWeight=",totalWeight)
    return mst
#연결리스트로 그래프 표현
graph = {
    'vertices': ['1', '2', '3', '4', '5', '6', '7','8'],
    'edges': [
        (6, '1', '2'),
        (4, '1', '3'),
        (6, '2', '1'),
        (3, '2', '6'),
        (10, '2', '8'),
        (7, '2', '5'),
        (7, '5', '2'),
        (1, '5', '8'),
        (1, '8', '5'),
        (10, '8', '2'),
        (8, '8', '6'),
        (8, '6', '8'),
        (3, '6', '2'),
        (2, '6', '3'),
        (4, '3', '1'),
        (2, '3', '6'),
        (5, '3', '4'),
        (9, '6', '4'),
        (9, '4', '6'),
        (5, '4', '3'),
        (11, '4', '7'),
        (11, '7', '4'),
    ]
}

print(kruskal(graph))