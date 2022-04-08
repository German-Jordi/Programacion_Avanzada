# Tarea 6: Escribir un programa donde se definan sus propias excepciones y las apliquen.
# Germán Jordi Arreortúa Reyes.
# Programación Avanzada.
# 7 de abril de 2022.
# El siguiente programa calcula el área de un triágulo a partir de sus lados.

# Excepción para errores al ingresar longitudes que no formen un triángulo.
class ErrorNoFormanunTriangulo(Exception):

    def __init__(self, lados, message="Los lados no forman un triángulo"):
        self.lados = lados
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.lados} -> {self.message}'


# Se ingresan las longitudes de los lados del triángulo (enteros).
print("Calcular área de un triángulo")
print("Ingresar las longitudes de los lados del triángulo")
a = int(input("Ingresar primer lado: "))
b = int(input("Ingresar segundo lado: "))
c = int(input("Ingresar tercer lado: "))

lados = (a, b, c)
# Se comprueba si los tres lados no forman triángulo.
if c >= a+b or b >= a+c or a >= b+c:
    raise ErrorNoFormanunTriangulo(lados)

# Puesto que los lados forman un triángulo entoncese obtiene el semiperimetro.
s = (a+b+c)/2
# Se obtiene el área con la formula de Herón.
area = ((s*(s-a)*(s-b)*(s-c))**0.5)
# Se imprime el área
print("El área es: ", area)
