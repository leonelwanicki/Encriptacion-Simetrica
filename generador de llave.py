from Crypto.Random import get_random_bytes
import os

# Generar clave de 128 bits (16 bytes)
clave_128 = get_random_bytes(16)

# Ruta donde se guardará la clave
ruta = r"C:\Users\Leonel\Documents\Programacion\clave_128.key"

# Guardar la clave en el archivo
with open(ruta, "wb") as archivo:
    archivo.write(clave_128)

print(f"Clave generada y guardada en: {ruta}")
