import queue
from collections import deque
from math import dist

"""
A*
BCU
DFS

"""

       

class Node:
    
    id = -1
    pai = None
    coordenadas = [0, 0]
    
    def __init__(self,id):
        self.id = id
        self.coordenadas = [self.id, self.id]

    

class Grafo:
    
    matriz = []
    matriz_arestas = []
    n = 0
    direcionado = False
    heuristica = []

   
    def __init__(self,n,direcionado): 
        self.n = n
        self.direcionado = direcionado
        self.heuristica = []
        for i in range(n):
            self.matriz.append([0]*n)            
            self.matriz_arestas.append([0]*n)            
    


    def custo(self, no: Node):
        return self.matriz[no.id][no.pai.id]


    def addAresta(self, s, t, peso=1):
        if(not self.direcionado):
            self.matriz[t][s]=peso
            self.matriz_arestas[t][s]=peso
        self.matriz[s][t]=peso
        self.matriz_arestas[s][t]=peso
        

    def printMatriz(self):
        print()
        print('##########')
        for i in range(self.n):
            for j in range(self.n):
                print(self.matriz[i][j],end = ' ')
            print()
        print('##########')
        print()
    

    def bcu(self, start: int, target: int, log=True):
        l = []
        custo = 0
        expandidos = 0
        
        node = Node(start)
        node.pai = Node(-1)       
        
        l.append(node)
        
        while(not (len(l) == 0)):
            aux = l.pop(0)
            expandidos += 1
            if(aux.pai.id > -1):
                custo = self.matriz[aux.id][aux.pai.id]
            print("expandindo {x}, custo atual: {c}".format(x=aux.id, c=custo))
            
            if(aux.id == target):
                print("expandidos: ", expandidos)
                return aux

            for i in range(self.n):                
                if(self.matriz[aux.id][i] >= 1 and i != aux.pai.id):
                    node = Node(i)
                    node.pai = aux
                    self.matriz[node.id][node.pai.id] += self.custo(aux)
                    l.append(node)
                    l.sort(key = self.custo)

            # print("estado da fila: {n}".format(n=self.mostraNos(l)))
            output = []
            for i in l:
                output.append({"nó": i.id, "custo": self.custo(i)})
            if log:
                print("estado atual da fila: ", output)

            print()
        return aux
 

    def a_estrela(self, start: int, target: int, log =True):
        l = []
        # nos_buscados = []
        custo = 0
        expandidos = 0
        
        node = Node(start)
        node.pai = Node(-1)       
        
        l.append(node)
        
        while(not (len(l) == 0)):
            aux = l.pop(0)
            expandidos += 1
            if(aux.pai.id > -1):
                # self.matriz[aux.id][aux.pai.id] += self.custo(aux) + self.heuristica[aux.id]
                custo = self.custo(aux)

            print("expandindo {x}, custo atual: {c}".format(x=aux.id, c=custo))
            
            if(aux.id == target):
                # if(custo < menor_custo):
                #     menor_custo = custo
                print("expandidos: ", expandidos)
                return aux

            for i in range(self.n):                
                if(self.matriz[aux.id][i] >= 1 and i != aux.pai.id ):
                    node = Node(i)
                    node.pai = aux
                    # self.matriz[node.id][node.pai.id] += self.custo(aux) + int(dist(node.coordenadas, [target, target]))
                    self.matriz[node.id][node.pai.id] += self.custo(aux) + self.heuristica[aux.id]
                    l.append(node)

                    l.sort(key = self.custo)

            # print("estado da fila: {n}".format(n=self.mostraNos(l)))
            output = []
            for i in l:
                output.append({"nó": i.id, "custo": self.custo(i)})
            if log:
                print("estado atual da fila: ", output)

            print()
        print("o menor custo foi ", menor_custo)
        return aux

 
    def melhor_escolha(self, start: int, target: int, log=True):
        l = []
        custo = 0
        expandidos = 0
        
        node = Node(start)
        node.pai = Node(-1)       
        
        l.append(node)
        
        while(not (len(l) == 0)):
            aux = l.pop(0)
            expandidos += 1
            if(aux.pai.id > -1):
                custo = self.matriz[aux.id][aux.pai.id]
            print("expandindo {x}, custo atual: {c}".format(x=aux.id, c=custo))
            
            if(aux.id == target):
                print("expandidos: ", expandidos)
                return aux

            for i in range(self.n):                
                if(self.matriz[aux.id][i] >= 1 and i != aux.pai.id):
                    node = Node(i)
                    node.pai = aux
                    # self.matriz[node.id][node.pai.id] += self.custo(aux)
                    l.append(node)
                    l.sort(key = self.custo)

            # print("estado da fila: {n}".format(n=self.mostraNos(l)))
            output = []
            for i in l:
                output.append({"nó": i.id, "custo": self.custo(i)})
            if log:
                print("estado atual da fila: ", output)

            print()
        return aux
 

    def bp(self, start: int, target: int):
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
 
    
    def bl(self,s,t):
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
        custo_caminho += g.matriz_arestas[no.id][no.pai.id]
        no = no.pai
    print("custo do caminho encontrado: ", custo_caminho)
    print()


# g = Grafo(10,False)
g = Grafo(30,False)
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
g.addAresta(6, 9, 2)
g.addAresta(4, 7, 7)
g.addAresta(4, 8, 5)
g.addAresta(8, 9, 1)

g.addAresta(3, 7, 1)
# g.addAresta(7, 4, 1)
# g.addAresta(4, 2, 1)

# print("BUSCA EM LARGURA")
# caminho(g.bl(0, 9))

# print("BUSCA EM PROFUNDIDADE")
# caminho(g.bp(0, 9))

# print("BUSCA DE CUSTO UNIFORME")
# caminho(g.bcu(0, 9, False))

# print("BUSCA A*")
# caminho(g.a_estrela(0, 9, True))

# print("BUSCA MELHOR ESCOLHA")
# caminho(g.melhor_escolha(0, 9, False))






