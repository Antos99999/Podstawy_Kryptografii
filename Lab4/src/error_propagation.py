from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import lab1

def count_byte_differences(original: bytes, modified: bytes) -> int:
    max_len = max(len(original), len(modified))
    diff_count = 0

    for i in range(max_len):
        o = original[i] if i < len(original) else None
        m = modified[i] if i < len(modified) else None
        if o != m:
            diff_count += 1

    return diff_count


def main(key_length):
    data = b"Wiadomosc przed zaszyforwaniem Wiadomosc przed zaszyforwaniem Wiadomosc przed zaszyforwaniem Wiadomosc przed zaszyforwaniem"
    modified_data = bytearray(data)
    modified_data[5] ^= 0x01
    key = int(lab1.main(key_length), 2).to_bytes(len(lab1.main(key_length)) // 8, byteorder='big')
    iv = int(lab1.main(128), 2).to_bytes(len(lab1.main(128)) // 8, byteorder='big')
    nonce = int(lab1.main(64), 2).to_bytes(len(lab1.main(64)) // 8, byteorder='big')

    print("=========================ECB=============================")
    cipher = AES.new(key, AES.MODE_ECB)
    cyphertext_original = cipher.encrypt(pad(data,AES.block_size))
    first_block = cyphertext_original[:AES.block_size]
    print("Pierwszy zaszyfrowany blok:", first_block.hex())
    print(cyphertext_original.hex())
    cyphertext = cipher.encrypt(pad(modified_data,AES.block_size))
    print(cyphertext.hex())
    print("Zmiana 1 bajtu w tekście wejściowym zmodyfikowała tylko blok (16 bajtów) w którym nastąpiła zmiana\n")

    corrupted_data = bytearray(cyphertext_original)
    corrupted_data[5] ^= 0x01

    decipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(decipher.decrypt(corrupted_data),AES.block_size)
    print(f"Odszyfrowana wiadomość : {plaintext}\n")
    print("Zmiana 1 bajtu powoduje niemożliwość odszyfrowania bloku w którym nastąpiła zmiana\n")

    roznica_ecb = count_byte_differences(data,plaintext)

    print("=========================CBC=============================")
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
    plaintext = unpad(decipher.decrypt(corrupted_data),AES.block_size)
    print(f"Odszyfrowana wiadomość : {plaintext}\n")
    print("Zmiana 1 bajtu powoduje niemożliwość odszyfrowania bloku w którym nastąpiła zmiana oraz zmodyfikowaniem bajtu w następnym bloku (zaszygorwaniem zamiast zaszyfrowaniem)\n")

    roznica_cbc = count_byte_differences(data,plaintext)

    print("=========================CTR=============================")
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
    plaintext = unpad(decipher.decrypt(corrupted_data),AES.block_size)
    print(f"Odszyfrowana wiadomość : {plaintext}\n")
    print("Zmiana 1 bajtu powoduje zmiane jednego bajtu w bloku gdzie nastąpiła zmiana (Wiadolosc zamiast Wiadomosc)\n")

    roznica_ctr = count_byte_differences(data,plaintext)

    print("=========================Podsumowanie==============================")
    print(f"Ilość zmienionych bajtów w ECB {roznica_ecb}")
    print(f"Ilość zmienionych bajtów w CBC {roznica_cbc}")
    print(f"Ilość zmienionych bajtów w CTR {roznica_ctr}")
if __name__ == '__main__':
    key_length = input("Podaj długość klucza: ")
    main(int(key_length))