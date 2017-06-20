# Military grade bad crypto demos

* ECB mode

* CTR mode with IV reuse (nonce misuse)

* GCM mode with IV reuse

These examples are double-plys bad because they also utilize PyCrypto.
Friends don't let friends use PyCrypto. Please use
https://github.com/pyca/cryptography
