class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar1(self):
        return ("Hola, mi nombre es", self.nombre, "y tengo", self.edad, "años.")

    def saludar2(self):
        return (f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")