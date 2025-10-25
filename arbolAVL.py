import sys 

class Node:
    def __init__(self, clave, value=None):
        self.clave = clave
        self.value = value
        self.izq = None
        self.der = None
        self.height = 1 

def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.izq) - getHeight(node.der)

def updateHeight(node):
    if node:
        node.height = 1 + max(getHeight(node.izq), getHeight(node.der))

def rotate_der(y):
    x = y.izq
    T2 = x.der

    x.der = y
    y.izq = T2

    updateHeight(y)
    updateHeight(x)

    return x

def rotate_izq(x):
    y = x.der
    T2 = y.izq

    y.izq = x
    x.der = T2

    updateHeight(x)
    updateHeight(y)

    return y

class AVLTree:
    def __init__(self):
        self.root = None

    def __iter__(self):
        yield from self.inOrdenIter(self.root)

    def inOrdenIter(self,nodo):
        if not nodo:
            return
        yield from self.inOrdenIter(nodo.izq)
        if nodo.value != None:
            yield nodo.value
        else:
            yield nodo.clave
        yield from self.inOrdenIter(nodo.der)


    def insert(self, tupla):
        if isinstance(tupla,tuple):
            clave, value = tupla

        else:
            clave, value = tupla, None
        self.root = self._insert_recursive(self.root, clave, value)

    def _insert_recursive(self, node, clave,value):
        if not node:
            return Node(clave,value)

        if clave < node.clave:
            node.izq = self._insert_recursive(node.izq, clave,value)
        elif clave > node.clave:
            node.der = self._insert_recursive(node.der, clave,value)
        else:
            return node 
        
        updateHeight(node)
        
        balance = getBalance(node)

        if balance > 1 and getBalance(node.izq) >= 0:
            node = rotate_der(node) 
        elif balance > 1 and getBalance(node.izq) < 0:
            node.izq = rotate_izq(node.izq)
            node = rotate_der(node) 
        elif balance < -1 and getBalance(node.der) <= 0:
            node = rotate_izq(node)
        elif balance < -1 and getBalance(node.der) > 0:
            node.der = rotate_der(node.der)
            node = rotate_izq(node) 
        
        return node 

    def delete(self, clave):
        self.root = self._delete_recursive(self.root, clave)

    def _delete_recursive(self, node, clave):
        if not node:
            return node
        
        if clave < node.clave:
            node.izq = self._delete_recursive(node.izq, clave)
        elif clave > node.clave:
            node.der = self._delete_recursive(node.der, clave)
        else:
            if not node.izq:
                return node.der
            
            elif not node.der:
                return node.izq
            
            temp = node.der
            while temp.izq:
                temp = temp.izq
            node.clave = temp.clave
            
            node.der = self._delete_recursive(node.der, temp.clave)

        updateHeight(node)
        balance = getBalance(node)

        if balance > 1 and getBalance(node.izq) >= 0:
            return rotate_der(node)
        if balance > 1 and getBalance(node.izq) < 0:
            node.izq = rotate_izq(node.izq)
            return rotate_der(node)
        if balance < -1 and getBalance(node.der) <= 0:
            return rotate_izq(node)
        if balance < -1 and getBalance(node.der) > 0:
            node.der = rotate_der(node.der)
            return rotate_izq(node)

        return node

    def inOrden(self,nodo,lista):
        if nodo:
            self.inOrden(nodo.izq, lista)
            if nodo.value != None:
                lista.append((nodo.value))
            else:
                lista.append((nodo.clave))
            self.inOrden(nodo.der, lista)
        return lista
    
    def obtenerLista(self):
        return self.inOrden(self.root, [])
