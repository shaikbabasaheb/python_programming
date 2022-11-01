#undirected graph function to add a node using adjacency matrix 
def add_node(value):
    global node_count
    if value in nodes:
        print(value,'is already exits')
    else:
        node_count+=1
        nodes.append(value)
        for i in graph:
            i.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,'is not in nodes')
    elif v2 not in nodes:
        print(v2,'is not in nodes')
    else:
        idx1=nodes.index(v1)
        idx2=nodes.index(v2)
        graph[idx1][idx2]=1
        graph[idx2][idx1]=1

def add_edge_cost(v1,v2,cost):
    if v1 not in nodes:
        print(v1,'is not in nodes')
    elif v2 not in nodes:
        print(v2,'is not in nodes')
    else:
        idx1=nodes.index(v1)
        idx2=nodes.index(v2)
        graph[idx1][idx2]=cost
        graph[idx2][idx1]=cost

def delete_node(value):
    global node_count
    if value not in nodes:
        print(value,'is not in nodes')
    else:
        idx=nodes.index(value)
        node_count-=1
        nodes.remove(value)
        graph.pop(idx)
        for i in graph:
            i.pop(idx)

def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1,'not in nodes')
    elif v2 not in nodes:
        print(v2,'not in nodes')
    else:
        idx1=nodes.index(v1)
        idx2=nodes.index(v2)
        graph[idx1][idx2]=0
        graph[idx2][idx1]=0

def add_cost_directed(v1,v2,cost):
    if v1 not in nodes:
        print(v1,'not in graph')
    elif v2 not in nodes:
        print(v2,'not in graph')
    else:
        idx1=nodes.index(v1)
        idx2=nodes.index(v2)
        graph[idx1][idx2]=cost

def print_graph_data():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],'<4'),end=' ')
        print()

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=' ')
        print()

nodes=[]
graph=[]
node_count=0
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')
print('Nodes added in graph:')
print(nodes)
print_graph()

print('Edges added between two nodes in a graph')
add_edge('A','B')
add_edge('D','E')
print_graph()

print('Adding cost between two nodes')
add_edge_cost('A','B',10)
add_edge_cost('A','E',20)
print_graph_data()

print('Deleting operation')
delete_node('C')
print(nodes)
print_graph_data()

print('Deleting edge')
delete_edge('A','B')
print(nodes)
print_graph_data()
