from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(32) # Genera la llave
dataenc = 'Esto es tarea de criptografia!' # Son los datos

# === Cifrado ===

# Convierte los datos en bytes, usando .encode
data = dataenc.encode('utf-8')

#Crea el objecto de cifrado, y cifra los datos
cipherenc = AES.new(key, AES.MODE_CFB)
ciphbytes = cipherenc.encrypt(data)

# Aqui se presentan nuestros datos
iv = cipherenc.iv
ciphdata = ciphbytes

print(ciphdata)

# === Decifrado ===

# Crea el objeto de cifrado y decifra los datos
ciphdec = AES.new(key, AES.MODE_CFB, iv=iv)
decbytes = ciphdec.decrypt(ciphdata)

# Convierte los bytes a string
decdata = decbytes.decode('utf-8')

print(decdata)
# === Prueba para comparar los datos ===

assert dataenc == decdata, 'La data original no concuerda con el resultado'