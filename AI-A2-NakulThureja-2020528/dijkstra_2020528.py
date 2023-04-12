import sys
import pandas as pd
from queue import PriorityQueue

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.edges = [[-1 for i in range(vertices)] for j in range(vertices)]
        self.visited = []
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
    def clear(self):
        self.visited = []

def dijkstra(graph, source):
    Dict = {v:10000000000000 for v in range(graph.v)}
    Dict[source] = 0

    pq = PriorityQueue()
    pq.put((0, source))

    while(pq.qsize()!=0):
        (dist, current) = pq.get()
        graph.visited.append(current)

        for neighbor in range(graph.v):
            if graph.edges[current][neighbor] != -1:
                distance = graph.edges[current][neighbor]
                if neighbor not in graph.visited:
                    min_cost = min(Dict[neighbor], Dict[current] + distance)
                    if(min_cost<Dict[neighbor]):
                        pq.put((min_cost, neighbor))
                        Dict[neighbor] = min_cost
    
    graph.clear()
    return Dict


if __name__ == '__main__':
    Cities = ['AGARTALA','AGRA','AHMEDABAD','ALLAHABAD','AMRITSAR','ASANSOL','BANGALORE','BARODA','BHOPAL','BHUBANESHWAR','BOMBAY','CALCUTTA','CALICUT','CHANDIGARH','COCHIN','COIMBATORE','DELHI','GWALIOR','HUBLI','HYDERABAD','IMPHAL','INDORE','JABALPUR','JAIPUR','JAMSHEDPUR','JULLUNDUR','KANPUR','KOLHAPUR','LUCKNOW','LUDHIANA','MADRAS','MADURAI','MEERUT','NAGPUR','NASIK','PANJIM','PATNA','PONDICHERRY','PUNE','RANCHI','SHILLONG','SHIMLA','SURAT','TRIVANDRUM','VARANASI','VIJAYAWADA','VISHAKAPATNAM']
    dict1={}
    dict2={}
    j = 0
    length = 47
    b = [0]
    b = b*length
    a=[b]
    a=a*length
    for i in Cities:
        dict1[j] = i
        dict2[i] = j
        j+=1
    
    df = pd.read_csv('capitalroaddistance.csv')

    list = df.T.reset_index().values.T.tolist()
    data = []
    city1 = list[0]
    list = list[1:]
    g = Graph(length)
    
    for j in list:
        for k in range(20):
            c1 = j[0]
            c2 = city1[k+1]
            cost = j[k+1]
            n1 = dict2[c1]
            n2 = dict2[c2]
            g.add_edge(n1,n2,cost)
    
    for i in range(length):
        dict = dijkstra(g, i)
        for j in range(length):
            datatemp = [dict1[i],dict1[j],dict[j]]
            data.append(datatemp)
              
    df = pd.DataFrame(data)
    df.to_csv('heuristics.csv', index=False, header=False)
