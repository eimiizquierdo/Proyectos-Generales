# Diccionarios
a = {
    "Nombre": "Einstein",
    "Edad": 100,
    "Domicilio": "Av. La Palma 125"
}

print(a)
print(a["Nombre"])
print(a["Edad"])
print(a["Domicilio"])

# Modificar un valor
a["Edad"] = 101
print(a["Edad"])
# Agregar un nuevo par clave-valor
a["Profesión"] = "Físico"

a.keys()
a.values()
a.items()

for clave in a.keys():
    print(clave)

for valor in a.values():
    print(valor)

for clave, valor in a.items():
    print(f"{clave}: {valor}")


b = [ 
    {
    "Nombre": "Marie Curie",
    "Edad": 66,
    "Domicilio": "Calle 123",
    "Telefono": "555-1234"
    },
    {
    "Nombre": "Newton",
    "Edad": 84,
    "Domicilio": "Calle 321",
    "Telefono": "555-5678"
    },
    {
    "Nombre": "Einstein",
    "Edad": 100,
    "Domicilio": "Av. La Palma 125",
    "Telefono": ["555-8765", "555-4321"]
    }
]
print (b)

# A C T I V I D A D
print("\n////////////////////// Actividad //////////////////////\n")

#Agrega un diccionario mas a la lista
print("---Agregar un nuevo diccionario a la lista---\n")
b.append({
    "Nombre": "Tesla",
    "Edad": 86,
    "Domicilio": "Calle 132",
    "Telefono": "555-0000"
})
print(b)
print("\n")

#Agregar un elemento a Newton
print("---Agregar un elemento a Newton---\n")
for persona in b:
    if persona["Nombre"] == "Newton":
        persona["Correo"] = "newton@gmail.com"
print(b[1])
print("\n")

# Borrar el ultimo elemento del arreglo
print("---Borrar el ultimo elemento del arreglo---\n")
print("Antes de borrar:")
print(b)
b.pop()
print("Después de borrar:")
print(b)
print("\n")

# Modificar la edad de Einstein
print("---Modificar la edad de Einstein---\n")
for persona in b:
    if persona["Nombre"] == "Einstein":
        persona["Edad"] = 50
print(b[2])
print("\n")

# Mostrar el segundo telefono de Einstein
print("---Mostrar el segundo telefono de Einstein---\n")
for persona in b:
    if persona["Nombre"] == "Einstein":
        print(persona["Telefono"][1])
print(b[2])