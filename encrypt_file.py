from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as f:
        f.write(key)
        f.close()

def cargar_key():
    return open("key.key","r").read()





if __name__ == "__main__":
    generate_key()
    k = cargar_key()
    print(k)

    k1 = Fernet(Fernet.generate_key())
    k1.encrypt(b"hola mundo")