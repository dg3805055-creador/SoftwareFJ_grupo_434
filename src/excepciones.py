# En este módulo se definirán las excepciones personalizadas, como DatosInvalidosError y 
# ServicioNoDisponibleError, que se lanzarán en situaciones donde los datos no sean válidos o un servicio no esté disponible. 
# Estas excepciones permitirán manejar errores específicos de una manera más controlada y eficiente.

# Aquí definimos nuestras propias excepciones para casos específicos en el sistema

class DatosInvalidosError(Exception):  # Cuando los datos del cliente no son correctos
    """Esta excepción se lanza cuando los datos del cliente no son válidos."""  # El mensaje es simplemente para saber lo que salió mal
    pass  # No necesitamos hacer nada más, solo dejamos la excepción lista para usarla

class ServicioNoDisponibleError(Exception):  # Cuando el servicio no está disponible
    """Esta excepción se lanza cuando intentas usar un servicio que no está disponible."""  # Lo mismo que antes, solo la definimos
    pass  # Solo la dejamos lista para ser lanzada más tarde

class OperacionNoPermitidaError(Exception):  # Cuando se intenta hacer algo que no está permitido
    """Esta excepción se lanza cuando se intenta realizar una operación no permitida."""  # Un mensaje para ayudar a entender el error
    pass  # Igual que las demás, solo definimos la excepción

#Comentario explicativo:
# Aquí creamos excepciones propias para manejar errores específicos de nuestro sistema. 
# Son como mensajes personalizados que nos ayudan a identificar qué salió mal.