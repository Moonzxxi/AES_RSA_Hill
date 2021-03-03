from cryptography.fernet import Fernet #para la implementacion de la llave secreta
import rsa

#abre el file de la llave simetrica
simkey= open('symmetric.key','rb')
key = simkey.read()

#crea el cifrado
cipher = Fernet(key)

#abre el file para el cifrado
myfile = open('cripto','rb')
myfiledata = myfile.read()

#cifra los datos
encdata = cipher.encrypt(myfiledata)
edata = open('encrypted_file','wb')
edata.write(encdata)

print(encdata)

#abre el file de la llave publica
pkey = open('publickey.key','rb')
pkdata = pkey.read()

#carga el file
pubkey = rsa.PublicKey.load_pkcs1(pkdata)

#cifra el file de la llave simetrica con la llave publica
enckey = rsa.encrypt(key,pubkey)

#escribe la llave simetrica cifrada en un file
ekey = open('encrypted_key','wb')
ekey.write(enckey)

print(enckey)
