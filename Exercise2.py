class graph:
    def __init__(self):
        self.x = [[" "," "],[" "," "]]
        self.firsttime = 0
    def create_edge(self,input):
        if self.firsttime == 0:
            self.x = [["-",input],[input,"0"]]
            self.firsttime = 1
        else:
            for i in range (len(self.x)):
                self.x[i].append("0")
            self.x.append([])
            for i in range (len(self.x[0])):
                self.x[-1].append("0")
            self.x[0][-1] = input
            self.x[-1][0] = input
    def connect(self,NodeA,NodeB):
        if NodeA in self.x[0] and NodeB in self.x[0] :
            NodeAIndex,NodeBIndex = 0,0
            for i in range(len(self.x)):
                if NodeA == self.x[0][i]:
                    NodeAIndex = i
                elif NodeB == self.x[0][i]:
                    NodeBIndex = i
            self.x[NodeAIndex][NodeBIndex] = "1"
            self.x[NodeBIndex][NodeAIndex] = "1"
        else:
            print ("Not")

TableA = graph()
TableA.create_edge("A")
TableA.create_edge("B")
TableA.create_edge("C")
TableA.create_edge("D")
TableA.create_edge("E")
TableA.create_edge("F")
TableA.connect("A","B")
TableA.connect("A","C")
TableA.connect("C","D")
TableA.connect("C","F")
TableA.connect("E","F")