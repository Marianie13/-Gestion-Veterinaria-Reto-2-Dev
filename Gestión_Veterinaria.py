import datetime

class Persona:
    def __init__(self, nombre, contacto, direccion):
        self.nombre = nombre
        self.contacto = contacto
        self.direccion = direccion

class Cliente(Persona):
    def __init__(self, nombre, contacto, direccion):
        super().__init__(nombre, contacto, direccion)
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

class Veterinario(Persona):
    def __init__(self, nombre, contacto, direccion, especialidad):
        super().__init__(nombre, contacto, direccion)
        self.especialidad = especialidad

class Mascota:
    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.historial_citas = []

class Cita:
    def __init__(self, fecha, hora, servicio, veterinario, mascota):
        self.fecha = fecha
        self.hora = hora
        self.servicio = servicio
        self.veterinario = veterinario
        self.mascota = mascota

class Servicio:
    def __init__(self, tipo):
        self.tipo = tipo

class Consulta(Servicio):
    def __init__(self):
        super().__init__("Consulta")

class Vacunacion(Servicio):
    def __init__(self):
        super().__init__("Vacunación")

# Base de datos en listas
clientes = []
veterinarios = [Veterinario("Dr. Pérez", "3001234567", "Calle 123", "General")]

def registrar_cliente():
    nombre = input("Nombre del cliente: ")
    contacto = input("Contacto: ")
    direccion = input("Dirección: ")
    cliente = Cliente(nombre, contacto, direccion)
    clientes.append(cliente)
    print("Cliente registrado con éxito.")

def registrar_mascota():
    if not clientes:
        print("No hay clientes registrados. Registre un cliente primero.")
        return
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)
    if not cliente:
        print("Cliente no encontrado.")
        return
    
    nombre = input("Nombre de la mascota: ")
    especie = input("Especie: ")
    raza = input("Raza: ")
    edad = input("Edad: ")
    mascota = Mascota(nombre, especie, raza, edad)
    cliente.agregar_mascota(mascota)
    print("Mascota registrada con éxito.")

def programar_cita():
    if not clientes:
        print("No hay clientes registrados.")
        return
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)
    if not cliente:
        print("Cliente no encontrado.")
        return
    
    nombre_mascota = input("Ingrese el nombre de la mascota: ")
    mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
    if not mascota:
        print("Mascota no encontrada.")
        return
    
    fecha = input("Fecha (YYYY-MM-DD): ")
    hora = input("Hora (HH:MM): ")
    print("Tipos de servicio: 1. Consulta 2. Vacunación")
    tipo_servicio = input("Seleccione un servicio: ")
    servicio = Consulta() if tipo_servicio == "1" else Vacunacion()
    
    print("Veterinarios disponibles:")
    for i, vet in enumerate(veterinarios):
        print(f"{i + 1}. {vet.nombre} - {vet.especialidad}")

    vet_index = int(input("Seleccione un veterinario: ")) - 1
    if vet_index < 0 or vet_index >= len(veterinarios):
        print("Selección inválida.")
        return
    
    veterinario = veterinarios[vet_index]
    cita = Cita(fecha, hora, servicio, veterinario, mascota)
    mascota.historial_citas.append(cita)
    print("Cita programada con éxito.")

def ver_historial():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)
    if not cliente:
        print("Cliente no encontrado.")
        return

    nombre_mascota = input("Ingrese el nombre de la mascota: ")
    mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
    if not mascota:
        print("Mascota no encontrada.")
        return

    if not mascota.historial_citas:
        print("No hay citas registradas.")
        return

    print(f"Historial de citas para {mascota.nombre}:")
    for cita in mascota.historial_citas:
        print(f"Fecha: {cita.fecha}, Hora: {cita.hora}, Servicio: {cita.servicio.tipo}, Veterinario: {cita.veterinario.nombre}")

def mostrar_menu():
    while True:
        print("\n--- Menú Veterinaria Huella Feliz ---")
        print("1. Registrar Cliente")
        print("2. Registrar Mascota")
        print("3. Programar Cita")
        print("4. Ver Historial de Mascota")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            registrar_mascota()
        elif opcion == "3":
            programar_cita()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

# Ejecutar el menú
mostrar_menu()
