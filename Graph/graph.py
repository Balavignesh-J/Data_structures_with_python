class Graph:
    def __init__(self):
        self.g={}

    def addvertex(self,v):
        if v not in self.g:
            self.g[v]=[]

    def AddEdge(self,v1,v2,directed=False):
        self.addvertex(v1)
        self.addvertex(v2)
        self.g[v1].append(v2)
        if not directed:
            self.g[v2].append(v1)
    def Display(self):
        for k,v in self.g.items():
                print(f"{k},{v}")

    def GetVertices(self):
        for k in self.g.keys():
            print(k,end=" ")

    def GetEdges(self):
        for k in self.g.keys():
            for v in self.g[k]:
                print(f"{k},{v}")

    def removevertex(self,v):
        if v in self.g:
            del self.g[v]
        for key,value in self.g.items():
            if v in value:
                value.remove(v)
    def isEdge(self,v1,v2):
        return v1 in self.g[v2] or v2 in self.g[v1]

    def RemoveEdge(self,v1,v2):
        if self.isEdge(v1,v2):
            self.g[v2].remove(v1)
            self.g[v1].remove(v2)

    def DFS(self,start,alreadyvisited=None):
        if alreadyvisited is None:
            alreadyvisited = set()
        if start not in alreadyvisited:
            alreadyvisited.add(start)
            print(start,end=" ")
            for c in self.g[start]:
                self.DFS(c,alreadyvisited)

    def BFS(self,start):
        alreadyvisited={start}
        q=[start]
        while len(q)>0:
            var=q.pop(0)
            print(var,end=" ")
            for c in self.g[var]:
                if c not in alreadyvisited:
                    q.append(c)
                    alreadyvisited.add(c)

    def shortest_path(self,v1,v2):
        alreadyvisited = {v1}
        q = [(v1,[v1])]
        while len(q) > 0:
            current,path = q.pop(0)
            for c in self.g[current]:
                if c==v2:
                    print(path+[c])
                    return
                if c not in alreadyvisited:
                    q.append((c,path+[c]))
                    alreadyvisited.add(c)
        return None

graphl = Graph()
graphl.AddEdge('A', 'B')
graphl.AddEdge('A', 'C')
graphl.AddEdge('B', 'D')
graphl.AddEdge('B', 'E')
graphl.AddEdge('C', 'F')
graphl.AddEdge('E', 'F')
graphl.AddEdge('D', 'G')
graphl.AddEdge('E', 'G')
graphl.AddEdge('F', 'H')
graphl.AddEdge('G', 'H')
graphl.Display()
graphl.GetVertices()
graphl.GetEdges()
graphl.Display()
graphl.DFS("A")
print("\n")
graphl.BFS("A")
print("\n")
graphl.shortest_path("A","H")