import queue
from collections import deque
from math import dist

class Node:
    id = -1
    pai = None
    custo = 0
    
    def __init__(self,id):
        self.id = id
    

class Grafo:
    
    matriz = [] #matriz de custo dos caminhos, alterada pelos algoritmos
    n = 0
    direcionado = False
    heuristica = []
   
    def __init__(self,n,direcionado): 
        self.n = n
        self.direcionado = direcionado
        self.heuristica = []
        for i in range(n):
            self.matriz.append([0]*n)            
    

    def custo_aresta(self, no: Node):
        return self.matriz[no.id][no.pai.id]

    def custo_no(self, no: Node):
        return no.custo

    def addAresta(self, s, t, peso=1):
        if(not self.direcionado):
            self.matriz[t][s]=peso
        self.matriz[s][t]=peso
        

    def printMatriz(self):
        print()
        print('##########')
        for i in range(self.n):
            for j in range(self.n):
                print(self.matriz[i][j],end = ' ')
            print()
        print('##########')
        print()
    

    def custo_uniforme(self, start: int, target: int, log=True):
        l = []
        expandidos = []
        
        node = Node(start)
        node.pai = Node(-1)       
        
        l.append(node)
        
        while(not (len(l) == 0)):
            aux = l.pop(0)
            expandidos.append(aux.id)
            print("expandindo ", aux.id)
            
            if(aux.id == target):
                print("expandidos: ", len(expandidos))
                return aux

            for i in range(self.n):                
                if(self.matriz[aux.id][i] >= 1 and i != aux.pai.id):
                    node = Node(i)
                    node.pai = aux
                    node.custo = self.custo_aresta(node) + aux.custo
                    l.append(node)
                    l.sort(key = self.custo_no)

            output = []
            for i in l:
                output.append({"nó": i.id, "custo": self.custo_aresta(i)})
            if log:
                print("estado atual da fila: ", output)

            print()
        return aux
 

    def a_estrela(self, start: int, target: int, log =True):
        l = []
        expandidos = 0
        
        node = Node(start)
        node.pai = Node(-1)       
        
        l.append(node)
        
        while(not (len(l) == 0)):
            aux = l.pop(0)
            expandidos += 1

            print("expandindo ", aux.id)
            
            if(aux.id == target):
                print("expandidos: ", expandidos)
                return aux

            for i in range(self.n):                
                if(self.matriz[aux.id][i] >= 1 and i != aux.pai.id ):
                    node = Node(i)
                    node.pai = aux
                    node.custo = self.heuristica[node.id] + self.custo_aresta(node) + aux.custo
                    l.append(node)
                    l.sort(key = self.custo_no)

            output = []
            for i in l:
                output.append({"nó": i.id, "custo": self.custo_aresta(i)})
            if log:
                print("estado atual da fila: ", output)

            print()
        return aux


    def melhor_escolha(self, start: int, target: int, log=True):
        l = []
        expandidos = 0
        
        node = Node(start)
        node.pai = Node(-1)       
        
        l.append(node)
        
        while(not (len(l) == 0)):
            aux = l.pop(0)
            expandidos += 1
            print("expandindo ", node.id)
            
            if(aux.id == target):
                print("expandidos: ", expandidos)
                return aux

            for i in range(self.n):                
                if(self.matriz[aux.id][i] >= 1 and i != aux.pai.id):
                    node = Node(i)
                    node.pai = aux
                    l.append(node)
                    l.sort(key = self.custo_aresta)

            output = []
            for i in l:
                output.append({"nó": i.id, "custo": self.custo_aresta(i)})
            if log:
                print("estado atual da fila: ", output)

            print()
        return aux
    

    def busca_profundidade(self, start: int, target: int):
        stack = deque()
        
        node = Node(start)
        node.pai = Node(-1)       
        expandidos = 0
        
        stack.append(node)
        
        while(not (len(stack) == 0)):
            expandidos += 1
            aux = stack.pop()
            print("expandindo {x}".format(x=aux.id))
            
            if(aux.id == target):
                print("expandidos: ", expandidos)
                return aux
            
            for i in range(self.n):                
                if(self.matriz[aux.id][i] >= 1 and i != aux.pai.id):
                    node = Node(i)
                    node.pai = aux
                    stack.append(node)
        
        return aux
 
    
    def busca_largura(self,s,t):
        q = queue.Queue()
        expandidos = 0
        
        node = Node(s)
        node.pai = Node(-1)       
        
        q.put(node)
        
        while(not q.empty()):
            aux = q.get()
            expandidos += 1
            print("expandindo {x}".format(x=aux.id))
            
            if(aux.id == t):
                print("expandidos: ", expandidos)
                return aux

            for i in range(self.n):                
                if(self.matriz[aux.id][i] >= 1 and i != aux.pai.id):
                    node = Node(i)
                    node.pai = aux
                    q.put(node)
        return aux
        

def caminho(no: Node):
    custo_caminho = 0
    print("caminho encontrado: ")
    while(no.id != -1):
        print(no.id)
        custo_caminho += g.custo_aresta(no)
        no = no.pai
    print("custo do caminho encontrado: ", custo_caminho)
    print()


g = Grafo(10,False)
g.heuristica =[
    10,
    9,
    7,
    7,
    9,
    2,
    17,
    15,
    2,
    0
]

g.addAresta(0, 2, 3)
g.addAresta(1, 3, 7)
g.addAresta(2, 3, 3)
g.addAresta(3, 5, 2)
g.addAresta(5, 4, 3)
g.addAresta(3, 6, 3)
g.addAresta(6, 9, 5)
g.addAresta(4, 7, 7)
g.addAresta(4, 8, 5)
g.addAresta(8, 9, 55)

g.addAresta(3, 7, 1)
g.addAresta(7, 4, 1)
g.addAresta(4, 2, 1)

print("BUSCA EM LARGURA")
caminho(g.busca_largura(0, 9))

print("BUSCA EM PROFUNDIDADE")
caminho(g.busca_profundidade(0, 9))

# print("BUSCA DE CUSTO UNIFORME")
# caminho(g.custo_uniforme(0, 9, True))

# print("BUSCA A*")
# caminho(g.a_estrela(0, 9, True))

print("BUSCA MELHOR ESCOLHA")
caminho(g.melhor_escolha(0, 9, False))
