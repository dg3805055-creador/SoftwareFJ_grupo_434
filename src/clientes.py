# Este archivo contendrá la clase Cliente, la cual gestionará la validación de los datos 
# personales de los clientes. Los datos como nombre, email y teléfono estarán encapsulados y validados 
# para asegurar que la información ingresada sea correcta.

from excepciones import DatosInvalidosError  # Traemos la excepción para manejar cuando los datos no sean válidos

# Clase Cliente: Aquí es donde guardamos y validamos la información del cliente

class Cliente:
    def __init__(self, nombre, email, telefono):  # Guardamos los datos que el cliente nos da
        self.nombre = nombre  # Guardamos el nombre del cliente
        self.email = email  # Guardamos el email del cliente
        self.telefono = telefono  # Guardamos el teléfono del cliente

    def validar(self):  # Validamos que el cliente tenga todos los datos importantes
        if not self.nombre or not self.email or not self.telefono:  # Si falta algún dato
            raise DatosInvalidosError("Faltan datos del cliente.")  # Lanzamos un error para decir que algo falta
        
#Comentario explicativo:
# En Cliente, guardamos los datos que un cliente nos da (como su nombre, email y teléfono).
# El método validar se asegura de que no falte nada importante y si falta algún dato, lanza un error para avisar.
