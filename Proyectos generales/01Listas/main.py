print ("Hello, World!")
# L I S T A S
a = []
print(a)

a = [1, 2, 3, 4, 5]
print(a)
print("a[2] =", a[2])

# Agregar elementos a la lista
a [0] = 10
print(a)

a.append(6)
print(a)

a.insert(0, 1)
print(a)

# Eliminar elementos de la lista
a.remove(3)
print(a)

del a[0]
print(a)

a.pop() # borra el ultimo elemento
print(a)

a.clear() # borra todos los elementos
print(a)

# Funciones
a = [1, 2, 3, 4, 5, 2]
print(a.count(2)) # cuenta cuantas veces aparece el elemento

print(len(a)) # longitud de la lista

print(a.index(4)) # posición del elemento

a.sort() # ordena la lista
print(a)