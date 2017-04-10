class automovil(object):
   def __init__(self,name,connections=None):
    self.name = name
    self.connections = {}
    if connections is not None:
       self.connections.update(connections)

automovil = [
    automovil("San Jose", {"Cartago": 25, "Monte Verde": 142, "Miravalles": 218, "Los Chiles": 194, "Santa Rosa":245, "Palo Verde": 11, "Quebrada Honda":24, "Poas":73, "Braulio Carrillo":6}),
    automovil("Cartago", {"Turrialba": 41, "Chirripo":117 , "Los Quetzales": 61}),
    automovil("Los Quetzales", {"Quepos": 127, "Uvita": 104}),
    automovil("Uvita", {"Puerto Jimenez": 150}),
    automovil("Monte Verde", {"La Fortuna": 147,'Quepos':234}),
    automovil("La Fortuna", {"Tenorio": 68,'Ls Chiles':96}),
    automovil("Miravalles", {"Rincon de la vieja": 5}),
    automovil("Braulio Carrillo", {"Puerto Viejo": 183, "Tortuguero": 63, "Sixaola":179}),
    automovil("Sixaola", {"La Amistad":20}),
    automovil("Los Chiles",{"Santa Rosa":330}),
    automovil("Rincon de la vieja",{"Quebrada Honda":97})
]
def shortest_pathAutomovil(start, end):
    P = _dijkstraAutomovil(start)
    path, node = [], end
    while not (node == start):
        if path.count(node):break
        path.append(node)
        node = P[node]
    return [start] + list(reversed(path))

def _dijkstraAutomovil(start):
    D, P = {},{}
    for knot in automovil:
        D[knot.name], P[knot.name] = float("inf"), None
    D[start] = 0
    unseen_nodes = list(automovil)
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

#print(shortest_pathAutomovil())