# Projeto Base para criação simples de senha gerada -
---
# Primeiro solicitamos ao Python a importação da Biclioteca Tkinter através das funções:
## From Tkinter import * (importa todo o conteúdo da Biblioteca)
-----
## From Tkinter import ttk (Importa os Widgets como abas e páginas)
-----
## From Tkinter import messagebox (Importa a mensagem descritiva pós a ação realizada)
-----
# Utilizamos diverças funções como:
     len(): Retorna o número de itens em um objeto (o "comprimento"). Funciona com strings, listas, tuplas, etc.

     def: A palavra-chave usada para definir uma função. É onde você cria blocos de código reutilizáveis.

    .get(): Usado em dicionários ou em campos de entrada do Tkinter (Entry) para recuperar um valor.

    .delete(): Remove um item. No Tkinter, é comum em campos de texto para apagar caracteres de uma posição inicial até uma final.
    
    Label: Um widget usado para exibir textos ou imagens na tela que o usuário não edita.

    Frame: Funciona como um container. É uma caixa invisível usada para organizar e agrupar outros widgets.

    Notebook: Parte do ttk (widgets temáticos). Cria aquela interface de abas (tabs), permitindo várias páginas em uma mesma janela.

    Treeview: Um widget poderoso para exibir dados em formato de árvore ou tabela (com linhas e colunas).

    columns: Parâmetro do Treeview que define os identificadores das colunas.

    heading: Define o texto que aparece no "cabeçalho" (topo) de cada coluna.
    
    .pack(): Um dos gerenciadores de layout. Ele "empacota" o widget na janela, colocando um após o outro.

    expand: Opção do .pack(). Se True, o widget ocupará o espaço extra disponível no container pai.

    fill: Define se o widget deve "esticar" para preencher o espaço (pode ser X, Y ou BOTH).

    pady: Adiciona espaçamento externo vertical (em pixels) acima e abaixo do widget.

    width: Define a largura do widget.
    
    command: Um parâmetro (geralmente de Botões) que define qual função será executada quando o usuário clicar no widget.

    mainloop(): É o "coração" do programa. Ele inicia um loop infinito que mantém a janela aberta e escutando eventos (como cliques e teclas) até que você a feche.
