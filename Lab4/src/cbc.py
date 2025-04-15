from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

import lab1

def xor_bytes(block1, block2):
    return bytes(a ^ b for a, b in zip(block1, block2))

def main(key_length):
    data = b"Wiadomosc do zaszyfrowania przy uzyciu wlasnorecznego CBC"
    key = int(lab1.main(key_length), 2).to_bytes(len(lab1.main(key_length)) // 8, byteorder='big')
    iv = int(lab1.main(128), 2).to_bytes(len(lab1.main(128)) // 8, byteorder='big')

    cipher = AES.new(key, AES.MODE_ECB)
    data = pad(data, AES.block_size)

    previous_block = iv
    ciphertext = b''

    for i in range(0,len(data), AES.block_size):
        block = data[i:i+AES.block_size]
        xored = xor_bytes(block, previous_block)
        encrypted_block = cipher.encrypt(xored)
        ciphertext += encrypted_block
        previous_block = encrypted_block

    print(f"Zaszyfrowana wiadomość: {ciphertext.hex()}")

    decipher = AES.new(key, AES.MODE_CBC, iv)
    #unpad(cipher_decrypt.decrypt(ciphertext), AES.block_size)
    plaintext = unpad(decipher.decrypt(ciphertext),AES.block_size)
    print(f"Odszyfrowana wiadomość: {plaintext}")

if __name__ == "__main__":
    key_length = input("Podaj długość klucza: ")
    main(int(key_length))