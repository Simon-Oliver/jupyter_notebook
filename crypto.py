from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

message = b'Public and Private keys encryption'

# # Generate a public/ private key pair using 4096 bits key length (512 bytes)
# new_key = RSA.generate(4096, e=65537)

# # The private key in PEM format
# private_key = new_key.exportKey("PEM")

# # The public key in PEM Format
# public_key = new_key.publickey().exportKey("PEM")

# print(private_key)
# fd = open("private_key.pem", "wb")
# fd.write(private_key)
# fd.close()

# print(public_key)
# fd = open("public_key.pem", "wb")
# fd.write(public_key)
# fd.close()

# Importing keys from files, converting it into the RsaKey object
pr_key = RSA.import_key(open('private_key.pem', 'r').read())
pu_key = RSA.import_key(open('public_key.pem', 'r').read())
# print(type(pr_key), type(pu_key))
# Instantiating PKCS1_OAEP object with the public key for encryption
cipher = PKCS1_OAEP.new(key=pu_key)
# Encrypting the message with the PKCS1_OAEP object
cipher_text = cipher.encrypt(message)
print(cipher_text)
# Instantiating PKCS1_OAEP object with the private key for decryption
decrypt = PKCS1_OAEP.new(key=pr_key)
# Decrypting the message with the PKCS1_OAEP object
decrypted_message = decrypt.decrypt(cipher_text)
print(decrypted_message)
