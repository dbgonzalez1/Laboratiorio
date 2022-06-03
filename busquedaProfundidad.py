#importar librerias para FIFO
from queue import Queue

class Grafo:#se crea aa clase grafo
    #clase constructor -> def __init__
    def __init__(self, num_nodos, directed=True): #inicamos el metodo con los atributos
        self.m_num_nodos = num_nodos #self -> uno mismo, nodos -> ingresa datos 
        self.m_nodos = range(self.m_num_nodos) #generamos un rango de los nodo ingresados
		
        self.m_direccion = directed #atributo de direccion
		
        #nodo -> diccionatio, set ingreso de datos -> genera el conjunto de datos
        self.m_conjuntoDato = {nodo: set() for nodo in self.m_nodos}    
	
    #agregar nodos 
    def agregarNodo(self, nodo1, nodo2, peso=1): #funcion donde se declara los datos a ingresar o tomar y se incia el peso en 1
        self.m_conjuntoDato[nodo1].add((nodo2, peso)) #se asegura que los datos a ingresar serán por medio del usuario

        if not self.m_direccion: #en caso que no esté dirigido el nodo este asignará desde el nodo 2 un nuevo nodo
            self.m_conjuntoDato[nodo2].add((nodo1, peso)) #agrega nodo nuevo
    
    #se imprime el grafo
    def print_conjuntoDato(self):
        for keys in self.m_conjuntoDato.keys():
            print("nodo", keys, ": ", self.m_conjuntoDato[keys]) 
            #imprime "nodo" seguido de key que hace referencia al indice de los elementos empezando por 0

    def dfs(self, nodoInicio, objetivo, recorrido = [], visita = set()):
        recorrido.append(nodoInicio)
        visita.add(nodoInicio) #Se agrega el nodo de inicio al comienzo de nuestra ruta transversal y lo marcamos como visitado
        if nodoInicio == objetivo:
            return recorrido 
        for (nodoVecino, peso) in self.m_conjuntoDato[nodoInicio]:
            if nodoVecino not in visita: 
                """se tçatraviesa los vecinos del nodo de inicio que aún no han sido 
                    visitados y se llama a la función recursivamente para cada uno de ellos"""
                resultadoNodo = self.dfs(nodoVecino, objetivo, recorrido, visita)
                if resultadoNodo is not None:
                    return resultadoNodo
        recorrido.pop()
        return None


if __name__ == "__main__":
    """Se realiza el bloque principal para determinar los datos de nuestra funcion
            Grafo por lo tanto se agregarán datos de forma manual"""

    # Al ver creado la funcion Grafo se definió el (numero de nodo y la direcion)

    ############################################
    ####               Prueba 1              ### 
    ############################################
    # Se agrega el nodo partiendo desde la longitud de 1
    print("------------------------------PRUEBA 1------------------------------")
    g = Grafo(6, directed=False) # Gráfico no dirigido que representa con 5 nodos
    """
    Grafo tiene 5
    nodo 1: tiene el conjunto de nodos (1, 2) (1, 5) (1, 3)
    nodo #:
    recorrido del nodo 1 al 5 :  empieza 1->2->5
    """
    # Se agrega todos los bordes del grafo
    g.agregarNodo(1, 3)
    g.agregarNodo(1, 5)
    g.agregarNodo(1, 2)
    g.agregarNodo(2, 5)
    g.agregarNodo(2, 4)
    # Imprime la lista tomando en cuenta el nodo, peso
    g.print_conjuntoDato()

    listaRuta = []
    listaRuta = g.dfs(1, 5) # Encontrar una ruta de nodo 1 a nodo 5
    print(f"La ruta transversal del nodo 1 al nodo 5 es: {listaRuta}") # Imprime la lista del recorrido
    

    ############################################
    ####               Prueba 2              ### 
    ############################################
    # Se agrega el nodo partiendo desde la longitud de 1
    print("------------------------------PRUEBA 2------------------------------")
    g2 = Grafo(6, directed=False) #Definicion del la longitud del grafo
    """
    Grafo tiene 6
    nodo 1: tiene el conjunto de nodos (3, 1) (4, 1) (2, 1)
    nodo #:
    recorrido del nodo 6:  empieza 1->4
    """
    g2.agregarNodo(1, 3)
    g2.agregarNodo(1, 4)
    g2.agregarNodo(1, 2)
    g2.agregarNodo(2, 1)
    g2.agregarNodo(2, 4)
    g2.agregarNodo(3, 1)
    g2.agregarNodo(3, 1)
    g2.agregarNodo(4, 1)
    g2.agregarNodo(4, 2)
    
    g2.print_conjuntoDato()

    listaRuta = []
    listaRuta = g2.dfs(1, 4) # Encontrar una ruta de nodo 1 a nodo 4
    print(f"La ruta transversal del nodo 1 al nodo 4 es: {listaRuta}") # Imprime la lista del recorrido

    ############################################
    ####               Prueba 3              ### 
    ############################################
    print("------------------------------PRUEBA 3------------------------------")
    g3 = Grafo(7, directed=False) #Definicion del la longitud del grafo
    """
    Grafo tiene 6
    nodo 1: tiene el conjunto de nodos (2, 1)
    nodo #:
    recorrido del nodo 1 al 3 :  empieza 1->2->3
    """
    g3.agregarNodo(1, 2)
    g3.agregarNodo(2, 3)
    g3.agregarNodo(2, 6)
    g3.agregarNodo(6, 5)
    g3.agregarNodo(5, 2)
    g3.agregarNodo(4, 5)

    g3.print_conjuntoDato()

    listaRuta = []
    listaRuta = g3.dfs(1, 3) # Encontrar una ruta de nodo 1 a nodo 3
    print(f"La ruta transversal del nodo 1 al nodo 3 es: {listaRuta}") # Imprime la lista del recorrido
    
