
import networkx as nx
import pylab as plt


def explore(u, visited, pre, post, clock, in_degree):

    #pre
    clock += 1
    pre[u] = clock
    visited[u] = True


    for (u,v) in G.edges(u):
        in_degree[v] += 1
        if visited[v] == False:
            visited, pre, post, clock, in_degree = explore(v, visited, pre, post, clock,
                                                in_degree)

    #post
    clock +=1
    post[u] = clock

    return visited, pre, post, clock, in_degree


def valid_build_order(G):

    visited, pre, post, in_degree = {}, {}, {}, {}
    clock = 0
    sources, build_order = [], []

    for u in G.nodes():
        visited[u] = False
        in_degree[u] = 0

    for u in G.nodes():
        if not visited[u]:
            visited, pre, post, clock, in_degree = explore(u, visited, pre, post,
                                                clock, in_degree)

    for u in G.nodes():
        if in_degree[u] == 0:
            sources.append(u)

    while (len(sources)>0):
        u = sources.pop()
        build_order.append(u)
        for (u,v) in G.edges(u):
            in_degree[v] = in_degree[v] - 1

            if in_degree[v] == 0:
                sources.append(v)



    return build_order


G = nx.DiGraph()
e1 = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
G.add_edges_from(e1)
G.add_node('e')


nx.draw(G, pos=nx.shell_layout(G), with_labels = True)
plt.show()

print(valid_build_order(G))
