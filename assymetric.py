# RSA key gen

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Generate a private key.
private_key = rsa.generate_private_key(
     public_exponent=65537,
     key_size=2048,
     backend=default_backend()
)

public_key = private_key.public_key()

# encrypt/decrypt
data = b'encrypt this message'
encrypted = public_key.encrypt(data, padding.PKCS1v15())
decrypted = private_key.decrypt(encrypted, padding.PKCS1v15())
print(decrypted)

# sign/verify
signature = private_key.sign(data, padding.PKCS1v15(), hashes.SHA256())

try:
  decrypted = public_key.verify(signature, data, padding.PKCS1v15(), hashes.SHA256())
  print("signature ok")
except:
  print("invalid signature")

try:
  data = b'Encrypt this message' # alter the data
  decrypted = public_key.verify(signature, data, padding.PKCS1v15(), hashes.SHA256())
  print("signature ok")
except:
  print("invalid signature")