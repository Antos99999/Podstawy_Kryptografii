import hashlib
from datetime import datetime

def MD5():
    start = datetime.now()
    md5_1mb = hashlib.md5()
    with open("../resources/file_1MB.txt", "rb") as f:
        while chunk := f.read(1024):
            md5_1mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file1_mb_time = round(time_diff.total_seconds() * 1000,2)
    file1_mb_hash = md5_1mb.hexdigest()

    md5_5mb = hashlib.md5()
    start = datetime.now()
    with open("../resources/file_5MB.txt", "rb") as f:
        while chunk := f.read(1024):
            md5_5mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file5_mb_time = round(time_diff.total_seconds() * 1000,2)
    file5_mb_hash = md5_5mb.hexdigest()

    md5 = hashlib.md5()
    start = datetime.now()
    with open("../resources/file_10MB.txt", "rb") as f:
        while chunk := f.read(1024):
            md5.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file10_mb_time = round(time_diff.total_seconds() * 1000,2)
    file10_mb_hash = md5.hexdigest()

    return file1_mb_time, file5_mb_time, file10_mb_time, file1_mb_hash, file5_mb_hash, file10_mb_hash

def SHA1():
    start = datetime.now()
    sha1_1mb = hashlib.sha1()
    with open("../resources/file_1MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha1_1mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file1_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file1_mb_hash = sha1_1mb.hexdigest()

    sha1_5mb = hashlib.sha1()
    start = datetime.now()
    with open("../resources/file_5MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha1_5mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file5_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file5_mb_hash = sha1_5mb.hexdigest()

    sha1 = hashlib.sha1()
    start = datetime.now()
    with open("../resources/file_10MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha1.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file10_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file10_mb_hash = sha1.hexdigest()

    return file1_mb_time, file5_mb_time, file10_mb_time, file1_mb_hash, file5_mb_hash, file10_mb_hash

def SHA224():
    start = datetime.now()
    sha224_1mb = hashlib.sha224()
    with open("../resources/file_1MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha224_1mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file1_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file1_mb_hash = sha224_1mb.hexdigest()

    sha224_5mb = hashlib.sha224()
    start = datetime.now()
    with open("../resources/file_5MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha224_5mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file5_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file5_mb_hash = sha224_5mb.hexdigest()

    sha224 = hashlib.sha224()
    start = datetime.now()
    with open("../resources/file_10MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha224.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file10_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file10_mb_hash = sha224.hexdigest()

    return file1_mb_time, file5_mb_time, file10_mb_time, file1_mb_hash, file5_mb_hash, file10_mb_hash

def SHA256():
    start = datetime.now()
    sha256_1mb = hashlib.sha256()
    with open("../resources/file_1MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha256_1mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file1_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file1_mb_hash = sha256_1mb.hexdigest()

    sha256_5mb = hashlib.sha256()
    start = datetime.now()
    with open("../resources/file_5MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha256_5mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file5_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file5_mb_hash = sha256_5mb.hexdigest()

    sha256 = hashlib.sha256()
    start = datetime.now()
    with open("../resources/file_10MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha256.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file10_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file10_mb_hash = sha256.hexdigest()

    return file1_mb_time, file5_mb_time, file10_mb_time, file1_mb_hash, file5_mb_hash, file10_mb_hash

def SHA384():
    start = datetime.now()
    sha384_1mb = hashlib.sha384()
    with open("../resources/file_1MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha384_1mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file1_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file1_mb_hash = sha384_1mb.hexdigest()

    sha384_5mb = hashlib.sha384()
    start = datetime.now()
    with open("../resources/file_5MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha384_5mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file5_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file5_mb_hash = sha384_5mb.hexdigest()

    sha384 = hashlib.sha384()
    start = datetime.now()
    with open("../resources/file_10MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha384.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file10_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file10_mb_hash = sha384.hexdigest()

    return file1_mb_time, file5_mb_time, file10_mb_time, file1_mb_hash, file5_mb_hash, file10_mb_hash

def SHA512():
    start = datetime.now()
    sha512_1mb = hashlib.sha512()
    with open("../resources/file_1MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha512_1mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file1_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file1_mb_hash = sha512_1mb.hexdigest()

    sha512_5mb = hashlib.sha512()
    start = datetime.now()
    with open("../resources/file_5MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha512_5mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file5_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file5_mb_hash = sha512_5mb.hexdigest()

    sha512 = hashlib.sha512()
    start = datetime.now()
    with open("../resources/file_10MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha512.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file10_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file10_mb_hash = sha512.hexdigest()

    return file1_mb_time, file5_mb_time, file10_mb_time, file1_mb_hash, file5_mb_hash, file10_mb_hash

def SHA_3_224():
    start = datetime.now()
    sha3_224_1mb = hashlib.sha3_224()
    with open("../resources/file_1MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha3_224_1mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file1_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file1_mb_hash = sha3_224_1mb.hexdigest()

    sha3_224_5mb = hashlib.sha3_224()
    start = datetime.now()
    with open("../resources/file_5MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha3_224_5mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file5_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file5_mb_hash = sha3_224_5mb.hexdigest()

    sha3_224 = hashlib.sha3_224()
    start = datetime.now()
    with open("../resources/file_10MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha3_224.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file10_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file10_mb_hash = sha3_224.hexdigest()

    return file1_mb_time, file5_mb_time, file10_mb_time, file1_mb_hash, file5_mb_hash, file10_mb_hash

def SHA_3_256():
    start = datetime.now()
    sha3_256_1mb = hashlib.sha3_256()
    with open("../resources/file_1MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha3_256_1mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file1_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file1_mb_hash = sha3_256_1mb.hexdigest()

    sha3_256_5mb = hashlib.sha3_256()
    start = datetime.now()
    with open("../resources/file_5MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha3_256_5mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file5_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file5_mb_hash = sha3_256_5mb.hexdigest()

    sha3_256 = hashlib.sha3_256()
    start = datetime.now()
    with open("../resources/file_10MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha3_256.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file10_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file10_mb_hash = sha3_256.hexdigest()

    return file1_mb_time, file5_mb_time, file10_mb_time, file1_mb_hash, file5_mb_hash, file10_mb_hash

def SHA_3_384():
    start = datetime.now()
    sha3_384_1mb = hashlib.sha3_384()
    with open("../resources/file_1MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha3_384_1mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file1_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file1_mb_hash = sha3_384_1mb.hexdigest()

    sha3_384_5mb = hashlib.sha3_384()
    start = datetime.now()
    with open("../resources/file_5MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha3_384_5mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file5_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file5_mb_hash = sha3_384_5mb.hexdigest()

    sha3_384 = hashlib.sha3_384()
    start = datetime.now()
    with open("../resources/file_10MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha3_384.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file10_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file10_mb_hash = sha3_384.hexdigest()

    return file1_mb_time, file5_mb_time, file10_mb_time, file1_mb_hash, file5_mb_hash, file10_mb_hash

def SHA_3_512():
    start = datetime.now()
    sha3_512_1mb = hashlib.sha3_512()
    with open("../resources/file_1MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha3_512_1mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file1_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file1_mb_hash = sha3_512_1mb.hexdigest()

    sha3_512_5mb = hashlib.sha3_512()
    start = datetime.now()
    with open("../resources/file_5MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha3_512_5mb.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file5_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file5_mb_hash = sha3_512_5mb.hexdigest()

    sha3_512 = hashlib.sha3_512()
    start = datetime.now()
    with open("../resources/file_10MB.txt", "rb") as f:
        while chunk := f.read(1024):
            sha3_512.update(chunk)
    end = datetime.now()
    time_diff = end - start
    file10_mb_time = round(time_diff.total_seconds() * 1000, 2)
    file10_mb_hash = sha3_512.hexdigest()

    return file1_mb_time, file5_mb_time, file10_mb_time, file1_mb_hash, file5_mb_hash, file10_mb_hash

def main():
    while True:
        print("\nChoose hash Aglorithms\n")
        print("1. MD5")
        print("2. SHA-1")
        print("3. SHA-224")
        print("4. SHA-256")
        print("5. SHA-384")
        print("6. SHA-512")
        print("7. SHA-3-224")
        print("8. SHA-3-256")
        print("9. SHA-3-384")
        print("10. SHA-3-512")
        print("11. Exit\n")

        option = input("Enter your choice: ")
        if option == "11":
            break

        if option == "1":
            time_1mb, time_5mb, time_10mb, hash_1mb, hash_5mb, hash_10mb = MD5()
            print("\nWyniki dla MD5\n")
            print(f"Time for 1MB file: {time_1mb} ms")
            print(f"Output for 1MB file: {hash_1mb}\n")
            print(f"Time for 5MB file: {time_5mb} ms")
            print(f"Output for 5MB file: {hash_5mb}\n")
            print(f"Time for 10MB file: {time_10mb} ms")
            print(f"Output for 10MB file: {hash_10mb}")
        elif option == "2":
            time_1mb, time_5mb, time_10mb, hash_1mb, hash_5mb, hash_10mb = SHA1()
            print("\nWyniki dla SHA-1\n")
            print(f"Time for 1MB file: {time_1mb} ms")
            print(f"Output for 1MB file: {hash_1mb}\n")
            print(f"Time for 5MB file: {time_5mb} ms")
            print(f"Output for 5MB file: {hash_5mb}\n")
            print(f"Time for 10MB file: {time_10mb} ms")
            print(f"Output for 10MB file: {hash_10mb}")
        elif option == "3":
            time_1mb, time_5mb, time_10mb, hash_1mb, hash_5mb, hash_10mb = SHA224()
            print("\nWyniki dla SHA-224\n")
            print(f"Time for 1MB file: {time_1mb} ms")
            print(f"Output for 1MB file: {hash_1mb}\n")
            print(f"Time for 5MB file: {time_5mb} ms")
            print(f"Output for 5MB file: {hash_5mb}\n")
            print(f"Time for 10MB file: {time_10mb} ms")
            print(f"Output for 10MB file: {hash_10mb}")
        elif option == "4":
            time_1mb, time_5mb, time_10mb, hash_1mb, hash_5mb, hash_10mb = SHA256()
            print("\nWyniki dla SHA-256\n")
            print(f"Time for 1MB file: {time_1mb} ms")
            print(f"Output for 1MB file: {hash_1mb}\n")
            print(f"Time for 5MB file: {time_5mb} ms")
            print(f"Output for 5MB file: {hash_5mb}\n")
            print(f"Time for 10MB file: {time_10mb} ms")
            print(f"Output for 10MB file: {hash_10mb}")
        elif option == "5":
            time_1mb, time_5mb, time_10mb, hash_1mb, hash_5mb, hash_10mb = SHA384()
            print("\nWyniki dla SHA-384\n")
            print(f"Time for 1MB file: {time_1mb} ms")
            print(f"Output for 1MB file: {hash_1mb}\n")
            print(f"Time for 5MB file: {time_5mb} ms")
            print(f"Output for 5MB file: {hash_5mb}\n")
            print(f"Time for 10MB file: {time_10mb} ms")
            print(f"Output for 10MB file: {hash_10mb}")
        elif option == "6":
            time_1mb, time_5mb, time_10mb, hash_1mb, hash_5mb, hash_10mb = SHA512()
            print("\nWyniki dla SHA-512\n")
            print(f"Time for 1MB file: {time_1mb} ms")
            print(f"Output for 1MB file: {hash_1mb}\n")
            print(f"Time for 5MB file: {time_5mb} ms")
            print(f"Output for 5MB file: {hash_5mb}\n")
            print(f"Time for 10MB file: {time_10mb} ms")
            print(f"Output for 10MB file: {hash_10mb}")
        elif option == "7":
            time_1mb, time_5mb, time_10mb, hash_1mb, hash_5mb, hash_10mb = SHA_3_224()
            print("\nWyniki dla SHA-3-224\n")
            print(f"Time for 1MB file: {time_1mb} ms")
            print(f"Output for 1MB file: {hash_1mb}\n")
            print(f"Time for 5MB file: {time_5mb} ms")
            print(f"Output for 5MB file: {hash_5mb}\n")
            print(f"Time for 10MB file: {time_10mb} ms")
            print(f"Output for 10MB file: {hash_10mb}")
        elif option == "8":
            time_1mb, time_5mb, time_10mb, hash_1mb, hash_5mb, hash_10mb = SHA_3_256()
            print("\nWyniki dla SHA-3-256\n")
            print(f"Time for 1MB file: {time_1mb} ms")
            print(f"Output for 1MB file: {hash_1mb}\n")
            print(f"Time for 5MB file: {time_5mb} ms")
            print(f"Output for 5MB file: {hash_5mb}\n")
            print(f"Time for 10MB file: {time_10mb} ms")
            print(f"Output for 10MB file: {hash_10mb}")
        elif option == "9":
            time_1mb, time_5mb, time_10mb, hash_1mb, hash_5mb, hash_10mb = SHA_3_384()
            print("\nWyniki dla SHA-3-384\n")
            print(f"Time for 1MB file: {time_1mb} ms")
            print(f"Output for 1MB file: {hash_1mb}\n")
            print(f"Time for 5MB file: {time_5mb} ms")
            print(f"Output for 5MB file: {hash_5mb}\n")
            print(f"Time for 10MB file: {time_10mb} ms")
            print(f"Output for 10MB file: {hash_10mb}")
        elif option == "10":
            time_1mb, time_5mb, time_10mb, hash_1mb, hash_5mb, hash_10mb = SHA_3_512()
            print("\nWyniki dla SHA-3-512\n")
            print(f"Time for 1MB file: {time_1mb} ms")
            print(f"Output for 1MB file: {hash_1mb}\n")
            print(f"Time for 5MB file: {time_5mb} ms")
            print(f"Output for 5MB file: {hash_5mb}\n")
            print(f"Time for 10MB file: {time_10mb} ms")
            print(f"Output for 10MB file: {hash_10mb}")

if __name__ == '__main__':
    main()