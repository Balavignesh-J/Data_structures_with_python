class Graph:
    def __init__(self):
        self.g={}

    def addvertex(self,v):
        if v not in self.g:
            self.g[v]={}

    def AddEdge(self,v1,v2,w,directed=False):
        self.addvertex(v1)
        self.addvertex(v2)
        self.g[v1][v2]=w
        if not directed:
            self.g[v2][v1]=w

    def Display(self):
        for k,v in self.g.items():
                print(f"{k},{v}")

    def GetVertices(self):
        for k in self.g.keys():
            print(k,end=" ")
        print()

    def GetEdges(self):
        for k in self.g.keys():
            for v in self.g[k]:
                print(f"{k},{v},{self.g[k][v]}")

    def removevertex(self,v):
        if v in self.g:
            del self.g[v]
        for key,value in self.g.items():
            if v in value:
                del self.g[key][v]

    def isEdge(self,v1,v2):
        return v1 in self.g.get(v2,{}) or v2 in self.g.get(v1,{})

    def RemoveEdge(self,v1,v2):
        if self.isEdge(v1,v2):
            del self.g[v1][v2]
            del self.g[v2][v1]

graphl = Graph()
graphl.AddEdge('A', 'B',10)
graphl.AddEdge('B', 'C',20)
graphl.AddEdge('B', 'D',30)
graphl.AddEdge('D', 'A',40)
graphl.Display()
print("After vertex remove")
graphl.removevertex("D")
graphl.Display()
graphl.RemoveEdge("A","B")
print("After edge remove")
graphl.Display()
graphl.GetVertices()
graphl.GetEdges()
