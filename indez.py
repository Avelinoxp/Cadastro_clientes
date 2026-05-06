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
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    data_nascimento = entry_data_nascimento.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    convenio_sus = entry_convenio_sus.get()
    contato_emergencia = entry_contato_emergencia.get()
    if nome == '' or cpf == ''or data_nascimento == '' or telefone == '' or email == '' or convenio_sus == '' or contato_emergencia == '':
        messagebox.showwarning('Erro', 'Preencha todos os campos corretamente!')
    else:
        tabela.insert('', END, values=(nome, cpf, data_nascimento, telefone, email, convenio_sus, contato_emergencia) )
        entry_nome.delete(0, END)
        entry_cpf.delete(0, END)
        entry_data_nascimento.delete(0, END)
        entry_telefone.delete(0, END)
        entry_email.delete(0, END) 
        entry_convenio_sus.delete(0, END)
        entry_contato_emergencia.delete(0, END)
        messagebox.showinfo('Sucesso', 'Paciente Cadastrado')

##Aba Cadastro
Label(aba1, text='Nome').pack(pady=6)
entry_nome = Entry(aba1, width=60)
entry_nome.pack()

Label(aba1, text='CPF').pack(pady=6)
entry_cpf = Entry(aba1, width=40)
entry_cpf.pack()

Label(aba1, text='Data de Nascimento').pack(pady=6)
entry_data_nascimento = Entry(aba1, width=40)
entry_data_nascimento.pack()

Label(aba1, text='Telefone').pack(pady=6)
entry_telefone = Entry(aba1, width=40)
entry_telefone.pack()

Label(aba1, text='Email').pack(pady=6)
entry_email = Entry(aba1, width=40)
entry_email.pack()

Label(aba1, text='Convênio/SUS').pack(pady=6)
entry_convenio_sus = Entry(aba1, width=40)
entry_convenio_sus.pack()

Label(aba1, text='Contato de Emergência').pack(pady=6)
entry_contato_emergencia = Entry(aba1, width=40)
entry_contato_emergencia.pack()

Button(
    aba1,
    text='Cadastrar Paciente',
    bg='Blue',
    fg='white',
    command=Cadastrar
).pack(pady=20)

colunas = ('Nome','cpf','Data de Nascimento','Telefone','Email','Convênio/SUS','Contato de Emergência')

tabela=ttk.Treeview(
    aba2,
    columns=colunas,
    show= 'headings'
)

tabela.pack(fill="both", expand=True, pady=20)


for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=150)




janela.mainloop()