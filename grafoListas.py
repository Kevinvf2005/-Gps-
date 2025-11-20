class Nodo:
    def __init__(self, nombre, data=None):
        self.nombre = nombre
        self.data = data
        self.vecinos = set()


class Grafo:
    def __init__(self):
        self.nodos = {}

    def __iter__(self):
        return iter(self.nodos.values())

    def insertar(self, nombre, data=None):
        if nombre not in self.nodos:
            self.nodos[nombre] = Nodo(nombre, data)
        else:
            self.nodos[nombre].data = data

    def conectar(self, a, b):
        if a in self.nodos and b in self.nodos:
            self.nodos[a].vecinos.add(b)
            self.nodos[b].vecinos.add(a)

    def eliminar(self, nombre):
        if nombre in self.nodos:
            for nodo in self.nodos.values():
                nodo.vecinos.discard(nombre)

            del self.nodos[nombre]

    def buscar(self, nombre):
        return self.nodos.get(nombre, None)

    def lista(self):
        return list(self.nodos.values())

    def nombres(self):
        return list(self.nodos.keys())
