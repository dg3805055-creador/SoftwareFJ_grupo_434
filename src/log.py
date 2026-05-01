# Este archivo tendrá funciones que gestionan el registro de eventos y errores. 
# Utilizando el módulo logging, se grabarán eventos de éxito (como el registro de clientes y servicios) 
# y errores (como entradas de datos inválidos). Los registros se guardarán en el archivo error_logs.txt dentro de la carpeta logs/.

import logging  # Usamos logging para guardar información de eventos o errores

# Aquí configuramos cómo se van a guardar los logs, todo se registrará en un archivo
logging.basicConfig(filename='logs/error_logs.txt', level=logging.INFO)  # Decimos que los mensajes se guardarán en este archivo

def registrar_log(message):  # Función que guarda un mensaje en el log
    logging.info(message)  # Simplemente registramos el mensaje como información

# Comentario explicativo:
# logging.basicConfig configura el sistema para que todo lo que pase importante (como errores o eventos) se guarde en un archivo llamado error_logs.txt.
# registrar_log es una forma simple de añadir mensajes al archivo para tener un historial de lo que pasa en el sistema.