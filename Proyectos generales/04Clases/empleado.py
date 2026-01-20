from persona import Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, puesto, salario):
        super().__init__(nombre, edad)
        self.puesto = puesto
        self.salario = salario

    def mostrar_datos(self):
        return f"""
            Nombre: {self.nombre}, 
            Edad: {self.edad}, 
            Puesto: {self.puesto}, 
            Salario: {self.salario}"
        """
