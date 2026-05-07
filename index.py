from tkinter import *
from tkinter import messagebox

Cliente=Tk()
Cliente.title('Solicitar Senha')
Cliente.geometry('300x250')
Cliente.configure(bg= 'PeachPuff2')

#Variaveris compartilhadas

contador = 1
fila = []
senha_atual = StringVar()
senha_atual.set('---')

#Tela2 Administrador

admin = Toplevel(Cliente)
admin.title('Administrador')
admin.geometry('300x350')
admin.configure(bg= 'PeachPuff2')

#Lista da fila no administrador
Label(admin, text='Fila de Senhas', font=('Arial', 14)).pack(pady=10)


lista_admin = Listbox(admin, width=20, height=10)
lista_admin.pack(pady=10)

#Tla 3 (Painel)
painel = Toplevel(Cliente)
painel.title('Painel de Senhas')
painel.geometry('400x300')
painel.configure(bg= 'PeachPuff2')
Label(painel, text='Senha Atual', font=('Arial', 14)).pack(pady=10)

Label(
    painel, textvariable=senha_atual,
    font=('Arial', 40),
    fg='red'
).pack(pady=20)

#Função
def chamar_senha():
        if len(fila) == 0:
            messagebox.showinfo('Fila Vazia', 'Não há mais senhas na fila.')
        else:
            senha = fila.pop(0)
            lista_admin.delete(0)
            senha_atual.set(senha)
def solicitar_senha():
    global contador
    senha = f'A{contador: 03}'
    fila.append(senha)

    lista_admin.insert(END, senha)
    messagebox.showinfo('Senha Gerada', f'Sua senha é: {senha}')
    contador += 1

#INTERFACE - Cliente
Label(Cliente, text='Retirar Senha', font=('Arial', 16)).pack(pady=20)

Button(
    Cliente,
    text='Gerar Senha',
    width=20,
    command=solicitar_senha
).pack(pady=10)
Button(
    admin,
    text='Chamar Senha',
    width=20,
    command=chamar_senha
).pack(pady=10)

Cliente.mainloop()