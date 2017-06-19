#!/usr/bin/env python2.7
import os
from PIL import Image
from Crypto.Cipher import AES

# random key
key = os.urandom(16)
# load image
img = Image.open("militarygrade.png")
img = img.convert("RGB")
# encrypt
cipher = AES.new(key)
cdata = cipher.encrypt(img.tobytes())
# create image from encrypted data
cimg = Image.frombytes(img.mode, img.size, cdata)
cimg.save("militarygrade_ecb.png")
cimg.show()
