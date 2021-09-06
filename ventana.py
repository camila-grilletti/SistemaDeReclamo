from tkinter import *
import os

def login():
    global ventana_login
    ventana_login=Toplevel(ventana_principal)
    ventana_login.geometry("300x250")
    ventana_login.title("Login")
    Label(ventana_login, text="Introduzca sus datos").pack()
    Label(ventana_login, text="").pack()

    global verifica_usuario
    global verifica_clave
    global entrada_usuario
    global entrada_clave

    verifica_usuario=StringVar()
    verifica_clave=StringVar()

    Label(ventana_login, text="Nombre usuario: ").pack()
    entrada_usuario=Entry(ventana_login, textvariable=verifica_usuario)
    entrada_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña: ").pack()
    entrada_clave.pack()
    Label(ventana_login, text="").pack()
    button(ventana_login, text="Acceder", width="10", height="1", command=verifica_login).pack()

def verifica_login():
    usuario1=verifica_usuario.get()
    clave1=verifica_clave.get()
    entrada_usuario.delete(0, END)
    entrada_clave.delete(0, END)

    lista_archivos=os.listdir()
    if usuario1 in lista_archivos():
        archivo1=open(usuario1, "r")
        verifica=archivo1.read().splitlines()
        if clave1 in verifica:
            exito_login()
        else:
            no_clave()
    else:
        no_usuario()

def register():
    global ventana_registro
    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave

    ventana_registro=Toplevel(ventana_principal)
    ventana_registro.geometry("300x250")
    ventana_registro.title("Registrarse")

    nombre=StringVar()
    clave=StringVar()

    Label(ventana_registro, text="Introduzca sus datos", bg="Lightgreen").pack()
    Label(ventana_registro, text="").pack()
    etiqueta_nombre=Label(ventana_registro, text="Nombre de usuario: ")
    etiqueta_nombre.pack()
    etiqueta_nombre=Entry(ventana_registro, textvariable=nombre_usuario)
    etiqueta_nombre.pack()
    etiqueta_clave=Label(ventana_registro, text="Contraseña: ")
    etiqueta_clave.pack()
    etiqueta_clave=Entry(ventana_registro, textvariable=clave, show="*")
    etiqueta_clave.pack()
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width="10", height="1", bg="Lightgreen", command=registro_usuario).pack()

def registro_usuario():
    usuario_info=nombre_usuario.get()
    clave_info=clave.get()
    
    file=open(usuario_info, "w")
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()

    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)

    Label(ventana_registro, text="Registro exitoso", fg="green", font=("Calibri", 11)).pack()


def ventana_inicio():
    global ventana_principal
    pestaña_color="Dark Grey"
    ventana_principal=Tk()
    ventana_principal.geometry("300x250")
    ventana_principal.title("Login")
    Label(text="Escoja su opción", bg="Lightgreen", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Acceder", height="2", width="30", bg=pestaña_color, command=login).pack()
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg=pestaña_color, command=register).pack()
    Label(text="").pack()

ventana_inicio()