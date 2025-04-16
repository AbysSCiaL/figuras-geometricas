"""Módulo para calcular áreas de figuras geométricas."""

from abc import ABC, abstractmethod

# pylint: disable=too-few-public-methods
class FiguraGeometrica(ABC):
    """Clase abstracta que define la interfaz para calcular áreas."""

    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de una figura."""


class Rectangulo(FiguraGeometrica):
    """Clase que representa un rectángulo y calcula su área."""

    def __init__(self, base, altura):
        """Inicializa un rectángulo con base y altura."""
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        return self.base * self.altura

    def descripcion(self):
        """Devuelve la descripción del rectángulo."""
        return "Figura: Rectángulo"


class Triangulo(FiguraGeometrica):
    """Clase que representa un triángulo y calcula su área."""

    def __init__(self, base, altura):
        """Inicializa un triángulo con base y altura."""
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del triángulo."""
        return (self.base * self.altura) / 2

    def descripcion(self):
        """Devuelve la descripción del triángulo."""
        return "Figura: Triángulo"


class Circulo(FiguraGeometrica):
    """Clase que representa un círculo y calcula su área."""

    def __init__(self, radio):
        """Inicializa un círculo con su radio."""
        self.pi = 3.14159
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        return self.pi * (self.radio ** 2)

    def descripcion(self):
        """Devuelve la descripción del círculo."""
        return "Figura: Círculo"


# Variables globales
BASE_RECTANGULO = 10
ALTURA_RECTANGULO = 5
BASE_TRIANGULO = 7
ALTURA_TRIANGULO = 4
RADIO_CIRCULO = 3


def main():
    """Función principal para mostrar áreas de figuras."""
    rectangulo = Rectangulo(BASE_RECTANGULO, ALTURA_RECTANGULO)
    triangulo = Triangulo(BASE_TRIANGULO, ALTURA_TRIANGULO)
    circulo = Circulo(RADIO_CIRCULO)

    print(f"Área del rectángulo: {rectangulo.calcular_area()}")
    print(f"Área del triángulo: {triangulo.calcular_area()}")
    print(f"Área del círculo: {circulo.calcular_area()}")


if __name__ == "__main__":
    main()
