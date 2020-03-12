import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# AES = Advanced Encryption Standard
aes_key = os.urandom(16)
print("AES Key:" + str(aes_key))

message1 = b'super secret msg'
message2 = b'super secret msg'

#block
aesCipher = Cipher(algorithms.AES(aes_key), modes.ECB(), backend=default_backend())
aesEncryptor = aesCipher.encryptor()
crypted_msg1 = aesEncryptor.update(message1)
crypted_msg2 = aesEncryptor.update(message2)
print(str(crypted_msg1) + " " + str(crypted_msg2))

aesDecryptor = aesCipher.decryptor()
decoded_msg = aesDecryptor.update(crypted_msg1)
print(decoded_msg)
decoded_msg = aesDecryptor.update(crypted_msg2)
print(decoded_msg)

#blockchain
iv = os.urandom(16)
aesCipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
aesEncryptor = aesCipher.encryptor()
crypted_msg1 = aesEncryptor.update(message1)
crypted_msg2 = aesEncryptor.update(message2)
print(str(crypted_msg1) + " " + str(crypted_msg2))

aesDecryptor = aesCipher.decryptor()
decoded_msg = aesDecryptor.update(crypted_msg1)
print(decoded_msg)
decoded_msg = aesDecryptor.update(crypted_msg2)
print(decoded_msg)