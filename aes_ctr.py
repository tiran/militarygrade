#!/usr/bin/env python2.7
import os
import struct

from PIL import Image

from Crypto.Cipher import AES
from Crypto.Util import Counter


def encrypt_image(name, key, iv):
    img = Image.open(name)
    img = img.convert(mode='RGB')
    counter = Counter.new(128, initial_value=iv)
    cipher = AES.new(key, AES.MODE_CTR, counter=counter)
    return cipher.encrypt(img.tobytes()), img


# random key for AES-256
key = os.urandom(32)
# random start value for CTR
iv = struct.unpack("Q", os.urandom(8))[0]

enc1, img1 = encrypt_image("militarygrade.png", key, iv)
enc2, img2 = encrypt_image("tux.png", key, iv)

assert img1.size == img2.size

# xor images
xor = b''.join(chr(ord(a) ^ ord(b)) for a, b in zip(enc1, enc2))

# create image from encrypted data
cimg = Image.frombytes(img1.mode, img1.size, xor)
cimg.save("militarygrade_ctr.png")
cimg.show()
