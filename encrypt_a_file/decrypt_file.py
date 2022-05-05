from cryptography.fernet import Fernet

def cargar_key():
        return open("key.key","rb").read()


def decrypt_file(file,key):
    llave = Fernet(key)

    with open(file,"rb") as f:
        f_data = f.read()
        f.close()
    decrypt_data = llave.decrypt(f_data)
    with open(file,"wb") as f:
        f.write(decrypt_data)
        f.close()


if __name__ == "__main__":
    k = cargar_key()
    decrypt_file("texto.yml",k)