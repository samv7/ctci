
import networkx as nx
import pylab as plt


def explore(u, visited, pre, post, clock):

    #pre
    clock += 1
    pre[u] = clock
    visited[u] = True

    for (u,v) in G.edges(u):
        if visited[v] == False:
            visited, pre, post, clock = explore(v, visited, pre, post, clock)

    #post
    clock +=1
    post[u] = clock

    return visited, pre, post, clock


def is_there_a_path(G,s,t):

    visited, pre, post = {}, {}, {}
    clock = 0

    for u in G.nodes():
        visited[u] = False

    visited, pre, post, clock = explore(s, visited, pre, post, clock)

    return visited[t]

def path_between(G, s, t):

    visited = {}
    Q = Queue()

    for u in G.nodes():
        visited[u] = False

    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for (u,v) in G.edges(u):
            if visited[v] == False:
                visited[v] = True
                Q.put(v)


    return visited[t]

G = nx.DiGraph()
e1 = [('A', 'C'), ('C', 'E'), ('C', 'F'), ('B', 'A'), ('B', 'D')]
G.add_edges_from(e1)
G.add_edge('D', 'C')


nx.draw(G, pos=nx.shell_layout(G), with_labels = True)
plt.show()



print(is_there_a_path(G, 'B', 'C')) #true

print(is_there_a_path(G, 'C', 'A')) #false


print(is_there_a_path(G, 'D', 'A')) #false



print(path_between(G, 'B', 'C')) #true

print(path_between(G, 'C', 'A')) #false


print(path_between(G, 'D', 'A')) #false
