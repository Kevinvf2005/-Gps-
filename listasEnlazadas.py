class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadas:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def __iter__(self):
        auxiliar = self.primero
        while auxiliar != None:
            yield auxiliar.dato
            auxiliar = auxiliar.siguiente
    
    def vacia(self):
        return self.primero == None
    
    def recorrido(self):
        auxiliar = self.primero
        while auxiliar != None:
            print(auxiliar.dato)
            auxiliar = auxiliar.siguiente

    def contarElementos(self):
        contador = 0
        auxiliar = self.primero
        while auxiliar != None:
            contador+=1
            auxiliar = auxiliar.siguiente
        return contador
    
    def agregarInicio(self,dato):
        if self.vacia():
            self.primero = self.agregarUltimo = Nodo(dato)
        else:
            auxiliar = Nodo(dato)
            auxiliar.siguiente = self.primero
            self.primero = auxiliar
    
    def buscarPos(self, posicion):
        contador = 1
        auxiliar = self.primero
        while contador < posicion:
            auxiliar = auxiliar.siguiente
            contador+=1
        return auxiliar.dato
    
    def buscarDato(self,dato):
        auxiliar = self.primero
        while auxiliar != None:
            if auxiliar.dato == dato:
                break
            auxiliar = auxiliar.siguiente
        if auxiliar == None:
            print("Su dato No se encuentra")
        else:
            print("Su dato se encuentra")