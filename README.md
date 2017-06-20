# Military grade bad crypto demos

## ECB mode

![ECB mode](https://raw.githubusercontent.com/tiran/militarygrade/master/militarygrade_ecb.png)

## CTR and GCM mode with IV reuse (nonce misuse)

The start value / IV for streaming modes like AES-CTR and AES-GCM must be a
nonce (number only used once). When the combination of encryption key and IV
is ever used twice, then the encryption can be reversed by simply applying
XOR. The image shows ``encrypted_image1 XOR encrypted_image2``. The output of
``encrypted_image1 XOR encrypted_image2 XOR original_image1`` is
``original_image2``.

![CTR mode](https://raw.githubusercontent.com/tiran/militarygrade/master/militarygrade_ctr.png)

## Original images

![AES encryption added and removed here](https://raw.githubusercontent.com/tiran/militarygrade/master/militarygrade.png)

![tux](https://raw.githubusercontent.com/tiran/militarygrade/master/tux.png)

## Note

Some examples are double-plus bad because they also utilize PyCrypto.
Friends don't let friends use PyCrypto. Please use
https://github.com/pyca/cryptography
