import rsa
from cryptography.fernet import Fernet #para la implementacion de la llave secreta

#crea la llave simetrica
key = Fernet.generate_key()

#escribe la llave simetrica a un file
k = open('symmetric.key','wb')
k.write(key)
k.close()

#crea las llaves publicas y privadas, de 2048 bits
(pubkey,privkey)= rsa.newkeys(2048)

#escribe la llave publica en un file
pukey= open( 'publickey.key','wb')
pukey.write(pubkey.save_pkcs1('PEM'))
pukey.close()

#escribe la llave privada en un file
prkey= open('privkey.key','wb')
prkey.write(privkey.save_pkcs1('PEM'))
prkey.close()