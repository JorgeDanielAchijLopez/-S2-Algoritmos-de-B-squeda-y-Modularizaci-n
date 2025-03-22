class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return removed_data

    def is_empty(self):
        return self.front is None

    def size(self):
        return self._size


class InteractiveSystem:
    def __init__(self):
        self.task_manager = {"high_priority": Queue(), "normal": Queue()}
        self.customer_service = {"critico": Queue(), "bajo": Queue()}
       
    def add_task(self):
        task = input("Ingrese la descripción de la tarea: ")
        priority = input("¿Es una tarea de alta prioridad? (s/n): ").strip().lower()
        if priority == "s":
            self.task_manager["high_priority"].enqueue(task)
        else:
            self.task_manager["normal"].enqueue(task)
        print("Tarea agregada con éxito.")

    def process_task(self):
        if not self.task_manager["high_priority"].is_empty():
            print(f"Procesando tarea urgente: {self.task_manager['high_priority'].dequeue()}")
        elif not self.task_manager["normal"].is_empty():
            print(f"Procesando tarea normal: {self.task_manager['normal'].dequeue()}")
        else:
            print("No hay tareas pendientes.")

    def add_customer(self):
        name = input("Ingrese el nombre del cliente: ")

        dpi = input("Ingrese los 13 dígitos del DPI: ").strip()
        while not (dpi.isdigit() and len(dpi) == 13):
            print("Error: El DPI debe contener exactamente 13 dígitos numéricos.")
            dpi = input("Ingrese los 13 dígitos del DPI: ").strip()
        tipo = input("ingresa el tipo de sangre: ").strip()

        is_vip = input("¿estado critico o bajo? (s/n): ").strip().lower()

        customer_info = f"{name} (DPI: {dpi}) (tipo de Sangre: {tipo})"

        if is_vip == "s":
            self.customer_service["critico"].enqueue(customer_info)
        else:
            self.customer_service["bajo"].enqueue(customer_info)

        print("Cliente agregado con éxito.")

    def serve_customer(self):
        if not self.customer_service["critico"].is_empty():
            print(f"Atendiendo a cliente en estado critico: {self.customer_service['critico'].dequeue()}")
        elif not self.customer_service["bajo"].is_empty():
            print(f"Atendiendo a cliente en estado de bajo critico: {self.customer_service['bajo'].dequeue()}")
        else:
            print("No hay clientes en espera.")

    def menu(self):
        while True:
            print("1. Agregar tarea")
            print("2. Procesar tarea")
            print("3. Agregar cliente")
            print("4. Atender cliente")
            print("5. Salir")
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.add_task()
            elif opcion == "2":
                self.process_task()
            elif opcion == "1":
                self.add_customer()
            elif opcion == "2":
                self.serve_customer()
            elif opcion == "5":
                print("adios doctor")
                break
            else:
                print("opcion no encontrada, ingrese la correcta.")


# Ejecutar el programa interactivo
system = InteractiveSystem()
system.menu()
