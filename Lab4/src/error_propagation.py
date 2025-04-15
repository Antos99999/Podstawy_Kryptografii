from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import lab1


def main(key_length):
    data = b"Wiadomosc przed zaszyforwaniem Wiadomosc przed zaszyforwaniem Wiadomosc przed zaszyforwaniem Wiadomosc przed zaszyforwaniem"
    modified_data = bytearray(data)
    modified_data[5] ^= 0x01
    key = int(lab1.main(key_length), 2).to_bytes(len(lab1.main(key_length)) // 8, byteorder='big')
    iv = int(lab1.main(128), 2).to_bytes(len(lab1.main(128)) // 8, byteorder='big')
    nonce = int(lab1.main(64), 2).to_bytes(len(lab1.main(64)) // 8, byteorder='big')

    cipher = AES.new(key, AES.MODE_ECB)
    cyphertext_original = cipher.encrypt(pad(data,AES.block_size))
    first_block = cyphertext_original[:AES.block_size]
    print("Pierwszy zaszyfrowany blok:", first_block.hex())
    print(cyphertext_original.hex())
    cyphertext = cipher.encrypt(pad(modified_data,AES.block_size))
    print(cyphertext.hex())
    print("Zmiana 1 bajtu w tekście wejściowym zmodyfikowała tylko blok w którym nastąpiła zmiana\n")

    corrupted_data = bytearray(cyphertext_original)
    corrupted_data[5] ^= 0x01

    decipher = AES.new(key, AES.MODE_ECB)
    plaintext = decipher.decrypt(corrupted_data)
    print(f"Odszyfrowana wiadomość : {plaintext}\n")
    print("Zmiana 1 bajtu powoduje niemożliwość odszyfrowania bloku w którym nastąpiła zmiana\n")

    cipher = AES.new(key, AES.MODE_CBC, iv)
    cyphertext_original = cipher.encrypt(pad(data,AES.block_size))
    first_block = cyphertext_original[:AES.block_size]
    print("Pierwszy zaszyfrowany blok:", first_block.hex())
    print(cyphertext_original.hex())
    cyphertext = cipher.encrypt(pad(modified_data, AES.block_size))
    print(cyphertext.hex())
    print("Zmiana 1 bajtu w tekście wejściowym zmodyfikowała cały szyfrogram\n")

    corrupted_data = bytearray(cyphertext_original)
    corrupted_data[5] ^= 0x01

    decipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = decipher.decrypt(corrupted_data)
    print(f"Odszyfrowana wiadomość : {plaintext}\n")
    print("Zmiana 1 bajtu powoduje niemożliwość odszyfrowania bloku w którym nastąpiła zmiana\n")

    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    cyphertext_original = cipher.encrypt(pad(data, AES.block_size))
    first_block = cyphertext_original[:AES.block_size]
    print("Pierwszy zaszyfrowany blok:", first_block.hex())
    print(cyphertext_original.hex())
    cyphertext = cipher.encrypt(pad(modified_data, AES.block_size))
    print(cyphertext.hex())
    print("Zmiana 1 bajtu w tekście wejściowym zmodyfikowała cały szyfrogram\n")

    corrupted_data = bytearray(cyphertext_original)
    corrupted_data[5] ^= 0x01

    decipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    plaintext = decipher.decrypt(corrupted_data)
    print(f"Odszyfrowana wiadomość : {plaintext}\n")
    print("Zmiana 1 bajtu powoduje możliwość odszyfrowania całej wiadomości\n")

if __name__ == '__main__':
    key_length = input("Podaj długość klucza: ")
    main(int(key_length))