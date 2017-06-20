#!/usr/bin/env python3
import os

from PIL import Image

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)


def encrypt_image(name, key, iv, ad):
    img = Image.open(name)
    img = img.convert(mode='RGB')
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=default_backend()
    ).encryptor()
    encryptor.authenticate_additional_data(ad)
    ciphertext = encryptor.update(img.tobytes()) + encryptor.finalize()
    return ciphertext, encryptor.tag, img

# random key for AES-256
key = os.urandom(32)
# random IV for GCM
iv = os.urandom(12)
ad = b'nonce misuse'

enc1, tag1, img1 = encrypt_image("militarygrade.png", key, iv, ad)
enc2, tag2, img2 = encrypt_image("tux.png", key, iv, ad)

assert img1.size == img2.size

# xor images
xor = bytes(a ^ b for a, b in zip(enc1, enc2))

# create image from encrypted data
cimg = Image.frombytes(img1.mode, img1.size, xor)
cimg.save("militarygrade_gcm.png")
cimg.show()
