"""
Este programa permite al usuario encriptar o desencriptar mensajes utilizando el algoritmo AES en modo CFB.

Carga de la clave:
La clave AES debe estar guardada en un archivo llamado 'clave_128.key' dentro del mismo repositorio que este script.
El archivo debe contener exactamente 16 bytes (128 bits) para que sea compatible con AES-128.

Para generar una clave válida, puedes usar el siguiente código una vez:
from Crypto.Random import get_random_bytes
import os

# Generar clave de 128 bits (16 bytes)
clave_128 = get_random_bytes(16)

# Ruta donde se guardará la clave
ruta = r"COMPLETAR/LA/RUTA"

# Guardar la clave en el archivo
with open(ruta, "wb") as archivo:
    archivo.write(clave_128)

print(f"Clave generada y guardada en: {ruta}")

Luego, este programa leerá la clave desde ese archivo para realizar el cifrado o descifrado.

Requisitos:
- Instalar la librería 'pycryptodome' con: pip install pycryptodome
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Ruta completa de la clave
ruta_clave = r"C:\Users\Leonel\Documents\Programacion\clave_128.key"

# Leer la clave desde el archivo en modo binario
with open(ruta_clave, "rb") as archivo:
    clave = archivo.read()

# Menú para el usuario
print("¿Qué desea hacer?")
print("1. Encriptar un mensaje")
print("2. Desencriptar un mensaje")
opcion = input("Ingrese 1 o 2: ")

if opcion == "1":
    # Encriptar
    mensaje = input("Ingrese el mensaje a cifrar: ").encode()
    iv = get_random_bytes(16)
    cipher = AES.new(clave, AES.MODE_CFB, iv=iv)
    ciphertext = cipher.encrypt(mensaje)
    print("\nResultado:")
    print("IV:", iv.hex())
    print("Mensaje cifrado:", ciphertext.hex())

elif opcion == "2":
    # Desencriptar
    iv_hex = input("Ingrese el IV (en hexadecimal): ")
    ciphertext_hex = input("Ingrese el mensaje cifrado (en hexadecimal): ")
    iv = bytes.fromhex(iv_hex)
    ciphertext = bytes.fromhex(ciphertext_hex)
    cipher = AES.new(clave, AES.MODE_CFB, iv=iv)
    mensaje_descifrado = cipher.decrypt(ciphertext)
    print("\nMensaje descifrado:", mensaje_descifrado.decode())

else:
    print("Opción inválida. Por favor, ingrese 1 o 2.")
