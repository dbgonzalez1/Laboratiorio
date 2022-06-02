#importar librerias para FIFO
from queue import Queue

class Grafo: #se crea aa clase grafo
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
    
    def bfs_traversal(self, nodoInicio): 
        #busqueda BFS realiza la busqueda eligiendo cada nodo para recorrer y encontrar una ruta adecuada
        visita = set() #visita y/o revisa los nodos ingresados
        cola = Queue() #se llama a la libreria que toma en cuenta una cola de datos lineal

        #Se incian los datos anteriormente iniciados visited y queue
        cola.put(nodoInicio)
        visita.add(nodoInicio)

        #mientras no esté vacia la lista realiza la busqueda
        while not cola.empty(): #empty genera una excepción de una cola vacía
            nodoActual = cola.get() #get elimina y/o devuelve un dato de la cola
            print(nodoActual, end = " ") #se imprime la cola de datos

            for (nodoSiguiente, peso) in self.m_conjuntoDato[nodoActual]: #obtiene los nodos padres
                if nodoSiguiente not in visita: #revisa el siguiente nodo y revisa si ha sido agregado o no
                    cola.put(nodoSiguiente) #put agrega a la cola el nodo obtenido
                    visita.add(nodoSiguiente) #agrega el nodo visitado

if __name__ == "__main__": 
    """Se realiza el bloque principal para determinar los datos de nuestra funcion
        Grafo por lo tanto se agregarán datos de forma manual"""

    # Al ver creado la funcion Grafo se definió el (numero de nodo y la direcion)

    ############################################
    ####               Prueba 1              ### 
    ############################################
    # Se agrega el nodo partiendo desde la longitud de 1
    print("------------------------------PRUEBA 1------------------------------")
    g = Grafo(6, directed=False) #Definicion del la longitud del grafo
    """
    Grafo tiene 5
    nodo 1: tiene el conjunto de nodos (1, 2) (1, 5) (1, 3)
    nodo #:
    recorrido del nodo 1 al 4 :  empieza 1->3->2->5->4
    """
    g.agregarNodo(1, 3)
    g.agregarNodo(1, 5)
    g.agregarNodo(1, 2)
    g.agregarNodo(2, 5)
    g.agregarNodo(2, 4)

    # añade los nodos a una lista 
    g.print_conjuntoDato()
    # imprime el grafo mostrando el indice del nodo, nodo y longitud
    print ("Visualización del recorrido del nodo"
                    " (que inicia en el vértice 1)")
    g.bfs_traversal(1)
    print()
    
    ############################################
    ####               Prueba 2              ### 
    ############################################
    print("------------------------------PRUEBA 2------------------------------")
    g2 = Grafo(7, directed=False) #Definicion del la longitud del grafo
    """
    Grafo tiene 6
    nodo 1: tiene el conjunto de nodos (6, 4)
    nodo #:
    recorrido del nodo 6:  empieza 6->4->3->5->1->2
    """
    g2.agregarNodo(6, 4)
    g2.agregarNodo(4, 3)
    g2.agregarNodo(4, 5)
    g2.agregarNodo(5, 2)
    g2.agregarNodo(5, 1)
    g2.agregarNodo(1, 2)

    # añade los nodos a una lista 
    g2.print_conjuntoDato()
    # imprime el grafo mostrando el indice del nodo, nodo y longitud
    print ("Visualización del recorrido del nodo"
                    " (que inicia en el vértice 6)")
    g2.bfs_traversal(6)
    print()

    ############################################
    ####               Prueba 3              ### 
    ############################################
    print("------------------------------PRUEBA 3------------------------------")
    g3 = Grafo(7, directed=False) #Definicion del la longitud del grafo
    """
    Grafo tiene 6
    nodo 1: tiene el conjunto de nodos (1, 2)
    nodo #:
    recorrido del nodo 1 al 4 :  empieza 1->2->3->6->5->4
    """
    g3.agregarNodo(1, 2)
    g3.agregarNodo(2, 3)
    g3.agregarNodo(2, 6)
    g3.agregarNodo(6, 5)
    g3.agregarNodo(5, 2)
    g3.agregarNodo(4, 5)
    

    # añade los nodos a una lista 
    g3.print_conjuntoDato()
    # imprime el grafo mostrando el indice del nodo, nodo y longitud
    print ("Visualización del recorrido del nodo"
                    " (que inicia en el vértice 1)")
    g3.bfs_traversal(1)
    print()

   