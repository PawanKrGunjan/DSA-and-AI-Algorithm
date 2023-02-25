import math

def A_star(Graph_nodes, start, end):
    open_list = []
    closed_list = set()
    path = []
    g_score = {node: math.inf for node in Graph_nodes}
    g_score[start] = 0
    f_score = {node: math.inf for node in Graph_nodes}
    f_score[start] = g_score[start] + H[start]

    open_list.append(start)

    while open_list:
        current = None
        current_f_score = math.inf
        for node in open_list:
            if f_score[node] < current_f_score:
                current_f_score = f_score[node]
                current = node

        if current == end:
            current_path = [end]
            while current != start:
                for node, cost in Graph_nodes[current]:
                    if g_score[node] == g_score[current] - cost:
                        current_path.insert(0, node)
                        current = node
                        break
            return g_score[end], current_path

        open_list.remove(current)
        closed_list.add(current)

        for neighbor, cost in Graph_nodes[current]:
            if neighbor in closed_list:
                continue

            tentative_g_score = g_score[current] + cost

            if neighbor not in open_list:
                open_list.append(neighbor)
            elif tentative_g_score >= g_score[neighbor]:
                continue

            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = g_score[neighbor] + H[neighbor]

    return float('inf'), []

H = {'A':-1,'B':6,'C':5,'D':1,'E':7,'F':3,'G':0,'H':3,'I':1,'J':8,'K':13,'L':14,'M':15,'N':16,'O':7,'P':8}
H = {
    'A': -1,
    'B': 6,
    'C': 5,
    'D': 1,
    'E': 7,
    'F': 3,
    'G': 0,
    'H': 3,
    'I': 1,
    'J': 2,
    'K': 3,
    'L': 4,
    'M': 5,
    'N': 6,
    'O': 7,
    'P': 8
}


Graph_nodes = {
    'A': [('B', 2), ('C', 3), ('D', 4)],
    'B': [('E', 1), ('F', 9)],
    'C': [('G', 1), ('H', 9)],
    'D': [('I', 6)],
    'E': [('J', 2), ('K', 3), ('L', 4)],
    # 'F':None,
    # 'J':None,
    # 'K':None,
    # 'L':None,
    'G': [('P', 7)],
    # 'P':None,
    'I': [('M', 2), ('N', 3), ('O', 4)],
    # 'M':None,
    # 'N':None,
    # 'O':None,
}


cost, path = A_star(Graph_nodes, 'A', 'P')
print("Shortest Path :",Path)
print('Minimum Cost :',cost)