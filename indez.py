from tkinter import *
from tkinter import ttk
from tkinter import messagebox

janela = Tk()
janela.title('Cadastro de pacientes')
janela.geometry('1200x600')

abas =ttk.Notebook(janela)
abas.pack(fill='both', expand=True)
aba1 = Frame(abas)
abas.add(aba1, text='Cadastro de Paciente')
aba2 = Frame(abas)
abas.add(aba2, text='Consulta de Paciente')

def Cadastrar():
    nome = Entry.nome.get()
    cpf = Entry.cpf.get()
    data_nascimento = Entry.data_nascimento.get()
    telefone = Entry.telefone.get()
    email = Entry.email.get()
    convenio_sus = Entry.convenio_sus.get()
    contato_emergencia = Entry.contato_emergencia.get()
    if nome == '' or cpf == ''or data_nascimento == '' or telefone == '' or email == '' or convenio_sus == '' or contato_emergencia == '':
        messagebox.showwarning('Erro', 'Preencha todos os campos corretamente!')
    else:
        tabela.insert('', END, values=(nome, cpf, data_nascimento, telefone, email, convenio_sus, contato_emergencia) )
        Entry_nome.delete(0, END)
        Entry_cpf.delete(0, END)
        Entry_data_nascimento.delete(0, END)
        Entry_telefone.delete(0, END)
        Entry_email.delete(0, END) 
        Entry_convenio_sus.delete(0, END)
        Entry_contato_emergencia.delete(0, END)
        messagebox.showinfo('Sucesso', 'Paciente Cadastrado')

Label(aba1, text='Nome').pack(pady=6)
Entry_nome = Entry(aba1, width=60)
Entry_nome.pack()

Label(aba1, text='CPF').pack(pady=6)
Entry_cpf = Entry(aba1, width=40)
Entry_cpf.pack()

Label(aba1, text='Data de Nascimento').pack(pady=6)
Entry_data_nascimento = Entry(aba1, width=40)
Entry_data_nascimento.pack()

Label(aba1, text='Telefone').pack(pady=6)
Entry_telefone = Entry(aba1, width=40)
Entry_telefone.pack()

Label(aba1, text='Email').pack(pady=6)
Entry_email = Entry(aba1, width=40)
Entry_email.pack()

Label(aba1, text='Convênio/SUS').pack(pady=6)
Entry_convenio_sus = Entry(aba1, width=40)
Entry_convenio_sus.pack()

Label(aba1, text='Contato de Emergência').pack(pady=6)
Entry_contato_emergencia = Entry(aba1, width=40)
Entry_contato_emergencia.pack()

Button(
    aba1,
    text='Cadastrar Paciente',
    bg='darkgreen',
    fg='black',
    command=Cadastrar
).pack(pady=20)

colunas = ('Nome','CPF','Data de Nascimento','Telefone','Email','Convênio/SUS','Contato de Emergência')

tabela = ttk.Treeview(aba1, columns=('Nome','CPF','Data de Nascimento','Telefone','Email','Convênio/SUS','Contato de Emergência'), show='headings')

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=150)




janela.mainloop()