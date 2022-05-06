# Tarea 7
# Germán Jordi Arreortúa Reyes

class Group:

    def __init__(self, tabla):
        self.tabla = tabla
        self.elementos = elementos(tabla)
        self.es_grupo = es_grupo(tabla)

        if self.es_grupo is True:
            self.identidad = identidad(tabla)
            self.conmutativo = conmutative(tabla)


class Element:

    def __init__(self, elemento, group):

        if group.es_grupo is True:
            if elemento in group.elementos:
                self.elemento = elemento
                self.grupo = group
                self.inverso = inverso(elemento, group.tabla)
                self.orden = orden_del_elemento(elemento, group.tabla)

    def __str__(self):
        return self.elemento

    def __add__(self, other):
        x = self.grupo.tabla[(self.elemento, other.elemento)]
        return Element(x, self.grupo)

    def __sub__(self, other):
        x = self.grupo.tabla[(self.elemento, other.inverso)]
        return Element(x, self.grupo)


def elementos(g):  # Se obtienen los elementos a partir de g
    elements = set()
    for p in g:
        elements = elements | set(p[0]) | set(p[1])
    return elements


def es_tabla(g):  # Se comprueba que 'g' sea una tabla
    elements = elementos(g)
    n = 1
    for a in elements:
        for b in elements:
            if (a, b) not in g:
                n = 0
                break
    return n


def es_cerrado(g):  # Se comprueba que sea cerrado
    elements = elementos(g)
    for p in g:
        if g[p] not in elements:
            return False
    return True


def es_asociativo(g):  # Se comprueba que sea asociativo
    elements = elementos(g)
    for a in elements:
        for b in elements:
            for c in elements:
                if g[(a, g[(b, c)])] != g[(g[(a, b)], c)]:
                    return False
    return True


def identidad(g):  # La identidad del grupo
    elements = elementos(g)
    for a in elements:
        n = 0
        for b in elements:
            if g[(a, b)] != b or g[(b, a)] != b:
                n = 1
                break
        if n == 0:
            return a
    return 'No'


def inverso(x, g):  # El inverso de un elemento 'x' es el elemento y 'g' la tabla
    elements = elementos(g)
    e = identidad(g)

    for a in elements:
        if g[(x, a)] == e and g[(a, x)] == e:
            return a

    return 'No'


def elementos_son_invertibles(g):  # Se comprueba si todos los elementos son invertibles
    elements = elementos(g)
    for x in elements:
        if inverso(x, g) == 'No':
            return False
    return True


def es_grupo(g):  # Comprobar que sea grupo
    if g == dict():  # Se comprueba que sea diferente del vacio
        return False
    if es_tabla(g) == 0:  # Se comprueba que sea tabla
        return False
    if es_cerrado(g) is False:  # Se comprueba que sea cerrado
        return False
    if es_asociativo(g) is False:  # Se comprueba que sea asociativo
        return False
    if identidad(g) == 'No':  # Se comprueba que tenga identidad
        return False
    if elementos_son_invertibles(g) is False:  # Se comprueba que los elementos sean invertibles
        return False
    return True  # Es grupo


def conmutative(g):
    for p in g:
        if g[p] != g[(p[1], p[0])]:
            return False
    return True


def orden_del_elemento(x, g):
    e = identidad(g)
    a = x
    n = 1
    while a != e:
        a = g[(a, x)]
        n += 1
    return n


G_Klein = {('0', '0'): '0', ('0', '1'): '1', ('0', '2'): '2', ('0', '3'): '3',
           ('1', '0'): '1', ('1', '1'): '0', ('1', '2'): '3', ('1', '3'): '2',
           ('2', '0'): '2', ('2', '1'): '3', ('2', '2'): '0', ('2', '3'): '1',
           ('3', '0'): '3', ('3', '1'): '2', ('3', '2'): '1', ('3', '3'): '0'}

G_Z3 = {('0', '0'): '0', ('0', '1'): '1', ('0', '2'): '2',
        ('1', '0'): '1', ('1', '1'): '2', ('1', '2'): '0',
        ('2', '0'): '2', ('2', '1'): '0', ('2', '2'): '1'}


G = Group(G_Klein)
u = Element('1', G)
v = Element('2', G)
w = Element('3', G)

# print(G.conmutativo)
# print(G.identidad)
# print(u.orden)
print(u+v-w)

H = Group(G_Z3)
k = Element('1', H)
m = Element('2', H)

# print(H.conmutativo)
# print(H.identidad)
# print(k.orden)
print(k-m)
