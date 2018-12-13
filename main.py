# import cryptography
import base64
import hashlib

import tools

if __name__ == '__main__':
    text = 'abcdefg hijklmn'
    # tools.CTFTools.caesar_cipher_list(text)
    tools.CTFTools.flashback(text, ' ')
    tools.CTFTools.qwe_encrypt(text)
    tools.CTFTools.qwe_decrypt(text)
    tools.CTFTools.fence_cipher_encrypt(text, 2)
    tools.CTFTools.fence_cipher_decrypt(text)
    tools.CTFTools.rot13(text)
