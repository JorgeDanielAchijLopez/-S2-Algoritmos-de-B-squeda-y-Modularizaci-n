import random

# Clase Usuario
class Usuario:
    def __init__(self, id, nombre, apellido, edad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __repr__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}"


nombres = ["Ana", "Juan", "Luis", "Maria", "Carlos", "Elena", "Pedro", "Sofia"]
apellidos = ["Juarez", "Molina", "Martinez", "Gonzales", "Mendez", "Cifuentes"]

# generador de limite 100,000 usuarios 
ids_unicos = random.sample(range(1, 100001), 100000)

# Crear los usuarios
usuarios = [Usuario(ids_unicos[i], random.choice(nombres), random.choice(apellidos), random.randint(18, 100)) for i in range(100000)]

# eso nos ordenara la lista
usuarios.sort(key=lambda x: x.id)

# Función de búsqueda lineal
def busqueda_lineal(lista, id_buscar):
    for usuario in lista:
        if usuario.id == id_buscar:
            return usuario
    return None

# esto nos va ayudar a que ordenen los usarios de forma binaria 
def busqueda_binaria(lista, id_buscar):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio].id == id_buscar:
            return lista[medio]
        elif lista[medio].id < id_buscar:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None

#  creamos un bucle para hacer genrar usuarios del 1 al 100,000
while True:
    opcion = input("\nEscribe un número entre 1 y 100,000 para buscar un usuario o 'salir' para cerrar: ").strip().lower()
    
    if opcion == "salir":
        print("Programa cerrado. ¡orale!")
        break  

    if opcion == "random":  # Si el usuario quiere un ID aleatorio
        id_prueba = random.randint(1, 100000)
        print(f"\nBuscando usuario con ID aleatorio: {id_prueba}")
    else:
        if not opcion.isdigit():  # Verifica que el input sea un número
            print("Ingresa un numero válido o escribe 'salir'.")
            continue
        id_prueba = int(opcion)

    resultado_binaria = busqueda_binaria(usuarios, id_prueba)

    if resultado_binaria:
        print("Usuario encontrado:", resultado_binaria)
    else:
        print("No se encontró ningún usuario con ese ID.")
