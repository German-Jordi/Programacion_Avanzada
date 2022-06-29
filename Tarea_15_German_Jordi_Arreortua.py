# Tarea 15
# Germán Jordi Arreortua Reyes
# Fecha de entrega: 28 de junio
# Escriba un programa recursivo que dibuje la curva de Peano
# de A(n) utilizando la biblioteca mathplotlib.

""" matplotlib """
import matplotlib.pyplot as plt


def trazar_linea(inicial_x, inicial_y, direccion):
    """
    Dibuja una linea y devuelve las coordenadas
    x e y al finalizar el trazo
    :param inicial_x: coordena inicial x en el plano
    :param inicial_y: coordena inicial y en el plano
    :param direccion: una tupla que representa en vector dirección
    :return: los valores de las coordenadas x e y al finalizar el trazo.
    """
    final_x = inicial_x + direccion[0]
    final_y = inicial_y + direccion[1]
    plt.plot([inicial_x, final_x], [inicial_y, final_y], color='darkred')
    return final_x, final_y


def curva_a(inicial_x, inicial_y, orden):
    """
    Dibuja la curva A de Hilbert de algún orden
    mayor que 0
    :param inicial_x: coordenada inicial en x
    :param inicial_y: coordenada inicial en y
    :param orden: orden de la curva
    :return:los valores de las coordenadas x e y al finalizar el trazo.
    """
    if orden == 1:
        actual_x, actual_y = trazar_linea(inicial_x, inicial_y, (-1, 0))
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (0, -1))
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (1, 0))
    else:
        actual_x, actual_y = curva_b(inicial_x, inicial_y, orden - 1)
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (-1, 0))
        actual_x, actual_y = curva_a(actual_x, actual_y, orden - 1)
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (0, -1))
        actual_x, actual_y = curva_a(actual_x, actual_y, orden - 1)
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (1, 0))
        actual_x, actual_y = curva_d(actual_x, actual_y, orden - 1)
    return actual_x, actual_y


def curva_b(inicial_x, inicial_y, orden):
    """
    Dibuja la curva B de Hilbert de algún orden
    mayor que 0
    :param inicial_x: coordenada inicial en x
    :param inicial_y: coordenada inicial en y
    :param orden: orden de la curva
    :return:los valores de las coordenadas x e y al finalizar el trazo.
    """
    if orden == 1:
        actual_x, actual_y = trazar_linea(inicial_x, inicial_y, (0, -1))
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (-1, 0))
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (0, 1))
    else:
        actual_x, actual_y = curva_a(inicial_x, inicial_y, orden - 1)
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (0, -1))
        actual_x, actual_y = curva_b(actual_x, actual_y, orden - 1)
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (-1, 0))
        actual_x, actual_y = curva_b(actual_x, actual_y, orden - 1)
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (0, 1))
        actual_x, actual_y = curva_c(actual_x, actual_y, orden - 1)
    return actual_x, actual_y


def curva_c(incial_x, inicial_y, orden):
    """
    Dibuja la curva C de Hilbert de algún orden
    mayor que 0
    :param incial_x: coordenada inicial en x
    :param inicial_y: coordenada inicial en y
    :param orden:
    :return: los valores de las coordenadas x e y al finalizar el trazo
    """
    if orden == 1:
        actual_x, actual_y = trazar_linea(incial_x, inicial_y, (1, 0))
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (0, 1))
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (-1, 0))
    else:
        actual_x, actual_y = curva_d(incial_x, inicial_y, orden - 1)
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (1, 0))
        actual_x, actual_y = curva_c(actual_x, actual_y, orden - 1)
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (0, 1))
        actual_x, actual_y = curva_c(actual_x, actual_y, orden - 1)
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (-1, 0))
        actual_x, actual_y = curva_b(actual_x, actual_y, orden - 1)
    return actual_x, actual_y


def curva_d(inicial_x, inicial_y, orden):
    """
    Dubuja la curva D de Hilbert de algún orden
    mayor que 0
    :param inicial_x: coordenada inicial en x
    :param inicial_y: coordenada inicial en y
    :param orden: orden de la curva
    :return:los valores de las coordenadas x e y al finalizar el trazo.
    """
    if orden == 1:
        actual_x, actual_y = trazar_linea(inicial_x, inicial_y, (0, 1))
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (1, 0))
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (0, -1))
    else:
        actual_x, actual_y = curva_c(inicial_x, inicial_y, orden - 1)
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (0, 1))
        actual_x, actual_y = curva_d(actual_x, actual_y, orden - 1)
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (1, 0))
        actual_x, actual_y = curva_d(actual_x, actual_y, orden - 1)
        actual_x, actual_y = trazar_linea(actual_x, actual_y, (0, -1))
        actual_x, actual_y = curva_a(actual_x, actual_y, orden - 1)
    return actual_x, actual_y


def grafica_curva_a(orden):
    """
    Grafica la curva A de Hilbert
    :param orden: orden de la curva
    """
    curva_a(0, 0, orden)
    plt.axis('equal')
    plt.axis('off')
    plt.show()


grafica_curva_a(6)
