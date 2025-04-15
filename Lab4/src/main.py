from datetime import datetime
import lab1
from lab1 import *
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

def ECB(key_length):
    with open("../resources/file_1MB.txt", "rb") as f:
        plaintext = f.read()
        f.close()
    key = int(lab1.main(key_length), 2).to_bytes(len(lab1.main(key_length)) // 8, byteorder='big')
    cipher = AES.new(key, AES.MODE_ECB)
    start1 = datetime.now()
    ciphertext = cipher.encrypt(plaintext)
    end1 = datetime.now()
    time_diff1 = end1 - start1
    start = datetime.now()
    cipher.decrypt(ciphertext)
    end = datetime.now()
    time_diff = end - start
    print(f"Czas szyfrowania dla pliku 1 MB wynosi {round(time_diff1.total_seconds() * 1000,2)} milisekund")
    print(f"Czas odszyfrowania dla pliku 1 MB wynosi {round(time_diff.total_seconds() * 1000,2)} milisekund")

    with open("../resources/file_5MB.txt", "rb") as f:
        plaintext = f.read()
        f.close()
    cipher = AES.new(key, AES.MODE_ECB)
    start = datetime.now()
    ciphertext = cipher.encrypt(plaintext)
    end = datetime.now()
    time_diff = end - start
    print(f"Czas szyfrowania dla pliku 5 MB wynosi {round(time_diff.total_seconds() * 1000,2)} milisekund")
    start = datetime.now()
    cipher.decrypt(ciphertext)
    end = datetime.now()
    time_diff = end - start
    print(f"Czas odszyfrowania dla pliku 5 MB wynosi {round(time_diff.total_seconds() * 1000, 2)} milisekund")

    with open("../resources/file_10MB.txt", "rb") as f:
        plaintext = f.read()
        f.close()
    cipher = AES.new(key, AES.MODE_ECB)
    start = datetime.now()
    ciphertext = cipher.encrypt(plaintext)
    end = datetime.now()
    time_diff = end - start
    print(f"Czas szyfrowania dla pliku 10 MB wynosi {round(time_diff.total_seconds() * 1000,2)} milisekund")
    start = datetime.now()
    cipher.decrypt(ciphertext)
    end = datetime.now()
    time_diff = end - start
    print(f"Czas odszyfrowania dla pliku 10 MB wynosi {round(time_diff.total_seconds() * 1000, 2)} milisekund")

def CBC(key_length):
    with open("../resources/file_1MB.txt", "rb") as f:
        plaintext = f.read()
        f.close()
    key = int(lab1.main(key_length), 2).to_bytes(len(lab1.main(key_length)) // 8, byteorder='big')
    iv = int(lab1.main(128), 2).to_bytes(len(lab1.main(128)) // 8, byteorder='big')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    start = datetime.now()
    ciphertext = cipher.encrypt(pad(plaintext,AES.block_size))
    end = datetime.now()
    time_diff = end - start
    print(f"Czas szyfrowania dla pliku 1 MB wynosi {round(time_diff.total_seconds() * 1000,2)} milisekund")
    cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)
    start = datetime.now()
    unpad(cipher_decrypt.decrypt(ciphertext),AES.block_size)
    end = datetime.now()
    time_diff = end - start
    print(f"Czas odszyfrowania dla pliku 1 MB wynosi {round(time_diff.total_seconds() * 1000, 2)} milisekund")

    with open("../resources/file_5MB.txt", "rb") as f:
        plaintext = f.read()
        f.close()
    key = int(lab1.main(key_length), 2).to_bytes(len(lab1.main(key_length)) // 8, byteorder='big')
    iv = int(lab1.main(128), 2).to_bytes(len(lab1.main(128)) // 8, byteorder='big')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    start = datetime.now()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    end = datetime.now()
    time_diff = end - start
    print(f"Czas szyfrowania dla pliku 5 MB wynosi {round(time_diff.total_seconds() * 1000, 2)} milisekund")
    cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)
    start = datetime.now()
    unpad(cipher_decrypt.decrypt(ciphertext), AES.block_size)
    end = datetime.now()
    time_diff = end - start
    print(f"Czas odszyfrowania dla pliku 5 MB wynosi {round(time_diff.total_seconds() * 1000, 2)} milisekund")

    with open("../resources/file_10MB.txt", "rb") as f:
        plaintext = f.read()
        f.close()
    key = int(lab1.main(key_length), 2).to_bytes(len(lab1.main(key_length)) // 8, byteorder='big')
    iv = int(lab1.main(128), 2).to_bytes(len(lab1.main(128)) // 8, byteorder='big')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    start = datetime.now()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    end = datetime.now()
    time_diff = end - start
    print(f"Czas szyfrowania dla pliku 10 MB wynosi {round(time_diff.total_seconds() * 1000, 2)} milisekund")
    cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)
    start = datetime.now()
    unpad(cipher_decrypt.decrypt(ciphertext), AES.block_size)
    end = datetime.now()
    time_diff = end - start
    print(f"Czas odszyfrowania dla pliku 10 MB wynosi {round(time_diff.total_seconds() * 1000, 2)} milisekund")

def CTR(key_length):
    with open("../resources/file_1MB.txt", "rb") as f:
        plaintext = f.read()
        f.close()
    key = int(lab1.main(key_length), 2).to_bytes(len(lab1.main(key_length)) // 8, byteorder='big')
    nonce = int(lab1.main(64), 2).to_bytes(len(lab1.main(64)) // 8, byteorder='big')
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    start = datetime.now()
    ciphertext = cipher.encrypt(pad(plaintext,AES.block_size))
    end = datetime.now()
    time_diff = end - start
    print(f"Czas szyfrowania dla pliku 1 MB wynosi {round(time_diff.total_seconds() * 1000,2)} milisekund")
    cipher_decrypt = AES.new(key, AES.MODE_CTR, nonce=nonce)
    start = datetime.now()
    unpad(cipher_decrypt.decrypt(ciphertext),AES.block_size)
    end = datetime.now()
    time_diff = end - start
    print(f"Czas odszyfrowania dla pliku 1 MB wynosi {round(time_diff.total_seconds() * 1000, 2)} milisekund")

    with open("../resources/file_5MB.txt", "rb") as f:
        plaintext = f.read()
        f.close()
    key = int(lab1.main(key_length), 2).to_bytes(len(lab1.main(key_length)) // 8, byteorder='big')
    nonce = int(lab1.main(64), 2).to_bytes(len(lab1.main(64)) // 8, byteorder='big')
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    start = datetime.now()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    end = datetime.now()
    time_diff = end - start
    print(f"Czas szyfrowania dla pliku 5 MB wynosi {round(time_diff.total_seconds() * 1000, 2)} milisekund")
    cipher_decrypt = AES.new(key, AES.MODE_CTR, nonce=nonce)
    start = datetime.now()
    unpad(cipher_decrypt.decrypt(ciphertext), AES.block_size)
    end = datetime.now()
    time_diff = end - start
    print(f"Czas odszyfrowania dla pliku 5 MB wynosi {round(time_diff.total_seconds() * 1000, 2)} milisekund")

    with open("../resources/file_10MB.txt", "rb") as f:
        plaintext = f.read()
        f.close()
    key = int(lab1.main(key_length), 2).to_bytes(len(lab1.main(key_length)) // 8, byteorder='big')
    nonce = int(lab1.main(64), 2).to_bytes(len(lab1.main(64)) // 8, byteorder='big')
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    start = datetime.now()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    end = datetime.now()
    time_diff = end - start
    print(f"Czas szyfrowania dla pliku 10 MB wynosi {round(time_diff.total_seconds() * 1000, 2)} milisekund")
    cipher_decrypt = AES.new(key, AES.MODE_CTR, nonce=nonce)
    start = datetime.now()
    unpad(cipher_decrypt.decrypt(ciphertext), AES.block_size)
    end = datetime.now()
    time_diff = end - start
    print(f"Czas odszyfrowania dla pliku 10 MB wynosi {round(time_diff.total_seconds() * 1000, 2)} milisekund")

def main():
    key_length = input("Podaj długość klucza: ")
    print("========ECB========")
    ECB(int(key_length))
    print("========CBC========")
    CBC(int(key_length))
    print("========CTR=========")
    CTR(int(key_length))

if __name__ == '__main__':
    main()