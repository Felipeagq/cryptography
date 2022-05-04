from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as f:
        f.write(key)
        f.close()

def cargar_key():
    return open("key.key","r").read()

def encrypt_file(file,key):
    llave = Fernet(key)
    with open(file,"rb") as f:
        f_data = f.read()
        f.close()
    encrypt_data = llave.encrypt(f_data)
    with open(file,"wb") as f:
        f.write(encrypt_data)
        f.close()



if __name__ == "__main__":
    generate_key()
    k = cargar_key()
    print(k)

    encrypt_file("texto.txt",k)