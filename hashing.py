import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii

# Importing keys from files, converting it into the RsaKey object
pr_key = RSA.import_key(open('private_key.pem', 'r').read())
pu_key = RSA.import_key(open('public_key.pem', 'r').read())


# Generate 1024-bit RSA key pair (private + public key)
keyPair = pr_key
pubKey = pu_key

# Sign the message using the PKCS#1 v1.5 signature scheme (RSASP1)
msg = 'Message for RSA signing'
hash = SHA256.new(msg.encode())
signer = PKCS115_SigScheme(keyPair)
signature = signer.sign(hash)
print("Signature:", binascii.hexlify(signature))

# Verify valid PKCS#1 v1.5 signature (RSAVP1)
msg = 'Message for RSA signing'
hash = SHA256.new(msg.encode())
verifier = PKCS115_SigScheme(pubKey)
try:
    verifier.verify(hash, signature)
    print("Signature is valid.")
except:
    print("Signature is invalid.")

# Verify invalid PKCS#1 v1.5 signature (RSAVP1)
msg = 'A tampered message'
hash = SHA256.new(msg.encode())
verifier = PKCS115_SigScheme(pubKey)
try:
    verifier.verify(hash, signature)
    print("Signature is valid.")
except:
    print("Signature is invalid.")


# Read file as hash
# filename = "vgsales.csv"
# with open(filename, "rb") as f:
#     bytes = f.read()  # read entire file as bytes
#     readable_hash = hashlib.sha256(bytes).hexdigest()
#     print(readable_hash)
