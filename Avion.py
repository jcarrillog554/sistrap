class avion(object):
   def __init__(self,name,connections=None):
    self.name = name
    self.connections = {}
    if connections is not None:
       self.connections.update(connections)

avion = [
    avion("San Jose", {"Liberia":210, "Puerto Jimenez":330,"Limon":160}),
    avion("Liberia", {"Puerto Jimenez": 450}),
    avion("Limon", {"Liberia": 368}),
]
def shortest_pathAvion(start, end):
    P = _dijkstraAvion(start)
    path, node = [], end
    while not (node == start):
        if path.count(node):break
        path.append(node)
        node = P[node]
    return [start] + list(reversed(path))

def _dijkstraAvion(start):
    D, P = {},{}
    for knot in avion:
        D[knot.name], P[knot.name] = float("inf"), None
    D[start] = 0
    unseen_nodes = list(avion)
    while unseen_nodes:
        shortest = min(unseen_nodes, key=lambda node:D[node.name])
        unseen_nodes.remove(shortest)
        for neighbour, distance in shortest.connections.items():
            if neighbour not in [node.name for node in unseen_nodes]:
                continue
            if D[shortest.name] + distance < D[neighbour]:
                D[neighbour] = D[shortest.name] + distance
                P[neighbour] = shortest.name
    return P

print(shortest_pathAvion("San Jose", "Liberia"))