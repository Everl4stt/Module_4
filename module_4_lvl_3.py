graph = {'0' : set(['1', '2']),
'1' : set(['0', '3', '4']),
'2' : set(['0', '5']),
'3' : set(['1']),
'4' : set(['2', '3']),
'5' : set(['2', '6', '7']),
'6' : set(['5']),
'7' : set(['5'])}

def bfs(graph, start, queue = [], visited = []) :
    visited.append(start)
    queue.extend(graph[start])
    for v in queue:
        if v not in visited:
            visited = bfs(graph, v, queue)
    return visited

start = '0'
print(bfs(graph, start))
