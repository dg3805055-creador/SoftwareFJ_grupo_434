# Aquí se definirá una clase abstracta Entidad que servirá como base para otras clases importantes como 
# Cliente, Reserva, y cualquier otra entidad que se pueda agregar en el futuro.
# Esta clase abstracta no tendrá una implementación directa, sino que definirá la estructura general que deben seguir sus clases hijas.

from abc import ABC, abstractmethod  # Usamos estas herramientas para crear clases que no se pueden usar directamente

class Entidad(ABC):  # Esta clase será la base para otras clases, como Cliente o Reserva.
    
    @abstractmethod
    def descripcion(self):  # Este método es para describir de qué trata la entidad (Cliente, Reserva, etc.)
        pass  # Lo dejaremos vacío aquí porque cada clase que herede de Entidad lo va a definir a su manera
    
    @abstractmethod
    def validar(self):  # Este método es para validar que la entidad tenga todos los datos correctos
        pass  # Igual que el anterior, cada clase hija va a implementar cómo se valida.

# Comentario explicativo:
# Entidad es una base común que todas las demás clases (como Cliente o Reserva) deben seguir. 
# Los métodos descripcion y validar se definen en esta clase, pero se completan en las clases hijas.