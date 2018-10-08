
def dfs(G):
    visited, pre, post = {}, {}, {}
    clock = 0

    for u in G.nodes():
        visited[u] = False

    for u in G.nodes():
        if visited[u] == False:
            visited, pre, post, clock = explore(u, visited, pre, post, clock)

    return visited, pre, post, clock

visited, pre, post, clock = dfs(G)

print("visited", visited)
print("pre", pre)
print("post", post)
