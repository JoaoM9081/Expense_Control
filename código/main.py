# importando tkinter e seus estilos
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

# Importando Pillow
from PIL import Image, ImageTk

# Importando barra de progresso do tkinter
from tkinter.ttk import Progressbar

# importando Matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# importando tkcalendar
from tkcalendar import DateEntry

# importando view
from view import *

class ExpenseControl:
    def __init__(self):
        # Cores do projeto
        self.co0 = "#2e2d2b"  # Preta
        self.co1 = "#feffff"  # branca
        self.co2 = "#4fa882"  # verde
        self.co3 = "#38576b"  # valor
        self.co4 = "#403d3d"  # letra
        self.co5 = "#e06636"
        self.co6 = "#038cfc"
        self.co7 = "#3fbfb9"
        self.co8 = "#263238"
        self.co9 = "#e9edf5"

        self.colors = ['#5588bb', '#66bbbb', '#99bb55', '#ee9944', '#444466', '#bb5555']

        # Configurando o window
        self.window = Tk()
        self.window.title("Controle de Despesas")
        self.window.geometry('900x650')
        self.window.configure(background=self.co9)
        self.window.resizable(width=FALSE, height=FALSE)

        # Escolhendo estilo
        self.style = ttk.Style(self.window)
        self.style.theme_use("clam")

        # Criando frames
        self.frameCima = Frame(self.window, width=1043, height=50, bg=self.co1, relief="flat")
        self.frameCima.grid(row=0, column=0)

        self.frameMeio = Frame(self.window, width=1043, height=361, bg=self.co1, relief="raised", pady=20)
        self.frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        self.frameBaixo = Frame(self.window, width=1043, height=300, bg=self.co1, relief="flat")
        self.frameBaixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

        self.frame_graPizza = Frame(self.frameMeio, width=500, height=250, bg=self.co2)
        self.frame_graPizza.place(x=415, y=5)

        # Logo
        self.logo = Image.open("icons/logo.png")
        self.logo = self.logo.resize((45, 45))
        self.logo = ImageTk.PhotoImage(self.logo)

        # Inserindo label do logo
        self.logo_text = Label(self.frameCima, image=self.logo, text=" Controle de Despesas", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=self.co1, fg=self.co4)
        self.logo_text.place(x=0, y=0)

        global tree 

        # Chamando funções
        self.porcentagens()
        self.grafico_bar()
        self.resumo()
        self.grafico_pizza()

        # Criando frame renda
        self.frameRenda = Frame(self.frameBaixo, width=300, height=250, bg=self.co1)
        self.frameRenda.grid(row=0, column=0)

        # Criando frame com operações
        self.frameOperacoes = Frame(self.frameBaixo, width=220, height=250, bg=self.co1)
        self.frameOperacoes.grid(row=0, column=1, padx=5)

        # Criando frame de configurações
        self.frameConfigure = Frame(self.frameBaixo, width=220, height=250, bg=self.co1)
        self.frameConfigure.grid(row=0, column=2, padx=5)

        # Tabela renda mensal
        self.tabela_renda = Label(self.frameMeio, text="Tabela de Receitas e Despesas", anchor=NW, font=('Verdana 12'), bg=self.co1, fg=self.co4)
        self.tabela_renda.place(x=5, y=309)

        # Chamando a função com a tabela de rendas e despesas
        self.mostrar_tabela()

        # Configurando as despesas
        self.l_info = Label(self.frameOperacoes, text="Insira novas despesas", height=1, anchor=NW, font=("Verdana 10 bold"), bg=self.co1, fg=self.co4)
        self.l_info.place(x=10, y=10)

        # categoria
        self.l_categoria = Label(self.frameOperacoes, text="Categoria:", height=1, anchor=NW, font=("Ivy 10"), bg=self.co1, fg=self.co4)
        self.l_categoria.place(x=10, y=40)

        # usando categorias
        self.cat_funcao = ver_categoria()
        self.cat = []

        for i in self.cat_funcao:
            self.cat.append(i[1])

        # criando Combobox
        self.cat_combo_despesa = ttk.Combobox(self.frameOperacoes, width=10, font=("Ivy 10"))
        self.cat_combo_despesa['values'] = (self.cat)
        self.cat_combo_despesa.place(x=110, y=41)

        # despesas calendário
        self.l_despesas_cal = Label(self.frameOperacoes, text="Data:", height=1, anchor=NW, font=("Ivy 10"), bg=self.co1, fg=self.co4)
        self.l_despesas_cal.place(x=10, y=70)

        # criando entrada de dados para data
        self.cal_despesas = DateEntry(self.frameOperacoes, width=12, background='grey', foreground='white', borderwidth=2, year=2024)
        self.cal_despesas.place(x=110, y=71)

        # valor despesas
        self.l_valor_despesas = Label(self.frameOperacoes, text="Quantia Total:", height=1, anchor=NW, font=("Ivy 10"), bg=self.co1, fg=self.co4)
        self.l_valor_despesas.place(x=10, y=100)

        # criando entrada de dados
        self.valor_despesas = Entry(self.frameOperacoes, width=14, justify='left', relief='solid')
        self.valor_despesas.place(x=110, y=101)

        # Botão inserir
        self.img_inserir_d = Image.open("icons/mais.png")
        self.img_inserir_d = self.img_inserir_d.resize((17, 17))
        self.img_inserir_d = ImageTk.PhotoImage(self.img_inserir_d)
        self.bt_inserir_d = Button(self.frameOperacoes, image=self.img_inserir_d, text=" ADICIONAR",command=self.inserir_desp, width=80, compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=self.co1, fg=self.co0, overrelief=RIDGE)
        self.bt_inserir_d.place(x=110, y=131)

        # label do botão deletar
        self.l_excluir = Label(self.frameOperacoes, text="Deletar:", height=1, anchor=NW, font=("Ivy 10 bold"), bg=self.co1, fg=self.co4)
        self.l_excluir.place(x=10, y=190)

        # botão deletar
        self.img_deletar = Image.open("icons/excluir.png")
        self.img_deletar = self.img_deletar.resize((17, 17))
        self.img_deletar = ImageTk.PhotoImage(self.img_deletar)
        self.bt_deletar = Button(self.frameOperacoes, image=self.img_deletar, text=" DELETAR", width=80, command=self.deletar,compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=self.co1, fg=self.co0, overrelief=RIDGE)
        self.bt_deletar.place(x=110, y=190)

        # Configurando Receitas
        self.l_info = Label(self.frameConfigure, text="Insira novas receitas", height=1, anchor=NW, font=("Verdana 10 bold"), bg=self.co1, fg=self.co4)
        self.l_info.place(x=10, y=10)

        # calendário receitas
        self.l_receitas_cal = Label(self.frameConfigure, text="Data:", height=1, anchor=NW, font=("Ivy 10"), bg=self.co1, fg=self.co4)
        self.l_receitas_cal.place(x=10, y=40)
        self.cal_receitas = DateEntry(self.frameConfigure, width=12, background='grey', foreground='white', borderwidth=2, year=2024)
        self.cal_receitas.place(x=110, y=41)

        # valor receitas
        self.l_valor_receitas = Label(self.frameConfigure, text="Quantia Total:", height=1, anchor=NW, font=("Ivy 10"), bg=self.co1, fg=self.co4)
        self.l_valor_receitas.place(x=10, y=70)
        self.valor_receitas = Entry(self.frameConfigure, width=14, justify='left', relief='solid')
        self.valor_receitas.place(x=110, y=71)

        # botão receitas
        self.img_inserir_r = Image.open("icons/mais.png")
        self.img_inserir_r = self.img_inserir_r.resize((17, 17))
        self.img_inserir_r = ImageTk.PhotoImage(self.img_inserir_r)
        self.bt_inserir_r = Button(self.frameConfigure, image=self.img_inserir_r, text=" ADICIONAR", command=self.inserir_rec, width=80, compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=self.co1, fg=self.co0, overrelief=RIDGE)
        self.bt_inserir_r.place(x=110, y=111)

        # Categoria nova 
        self.l_categoria_n = Label(self.frameConfigure, text="Categoria", height=1, anchor=NW, font=("Ivy 10 bold"), bg=self.co1, fg=self.co4)
        self.l_categoria_n.place(x=10, y=160)
        self.categoria_n = Entry(self.frameConfigure, width=14, justify='left', relief='solid')
        self.categoria_n.place(x=110, y=162)

        # Botão inserir categoria
        self.img_inserir_cat = Image.open("icons/mais.png")
        self.img_inserir_cat = self.img_inserir_cat.resize((17, 17))
        self.img_inserir_cat = ImageTk.PhotoImage(self.img_inserir_cat)
        self.bt_inserir_cat = Button(self.frameConfigure, image=self.img_inserir_cat, text=" ADICIONAR", command=self.inserir_cat, width=80, compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=self.co1, fg=self.co0, overrelief=RIDGE)
        self.bt_inserir_cat.place(x=110, y=190)

        self.window.mainloop()

    # Porcentagens
    def porcentagens(self):
        self.l_nome = Label(self.frameMeio, text="Porcentagem do Saldo Restante", height=1, anchor=NW, font=("Verdana 12"), bg=self.co1, fg=self.co4)
        self.l_nome.place(x=7, y=5)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("black.Horizontal.TProgressbar", background='#daed6b')
        style.configure("TProgressbar", thickness=25)

        bar = Progressbar(self.frameMeio, length=180, style='black.Horizontal.TProgressbar')
        bar.place(x=10, y=35)
        bar['value'] = valores_porcent()

        valor = valores_porcent()

        self.l_porcentagem = Label(self.frameMeio, text="{:,.2f}%".format(valor), anchor=NW, font=("Verdana 12"), bg=self.co1, fg=self.co4)
        self.l_porcentagem.place(x=200, y=35)

    # Função que gera um gráfico de barras
    def grafico_bar(self):
        lista_categorias = ['Rendas', 'Despesas', 'Saldo']
        lista_valores = bar_valores()

        figura = plt.Figure(figsize=(4, 3.45), dpi=60)
        ax = figura.add_subplot(111)
        ax.autoscale(enable=True, axis='both', tight=None)

        ax.bar(lista_categorias, lista_valores, color=self.colors, width=0.9)

        c = 0
        for i in ax.patches:
            ax.text(i.get_x() - .001, i.get_height() + .5,
                    str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',
                    verticalalignment='bottom', color='dimgrey')
            c += 1

        # Definir ticks e depois os rótulos
        ax.set_xticks(range(len(lista_categorias)))  # Definir os ticks para o eixo x
        ax.set_xticklabels(lista_categorias, fontsize=16)  # Definir os rótulos

        # Personalizações dos eixos
        ax.patch.set_facecolor('#ffffff')
        ax.spines['bottom'].set_color('#CCCCCC')
        ax.spines['bottom'].set_linewidth(1)
        ax.spines['right'].set_linewidth(0)
        ax.spines['top'].set_linewidth(0)
        ax.spines['left'].set_color('#CCCCCC')
        ax.spines['left'].set_linewidth(1)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.tick_params(bottom=False, left=False)
        ax.set_axisbelow(True)

        # Desativar a grade
        ax.yaxis.grid(False)
        ax.xaxis.grid(False)

        canva = FigureCanvasTkAgg(figura, self.frameMeio)
        canva.get_tk_widget().place(x=10, y=70)

    # Função de resumo total
    def resumo(self):
        valor = bar_valores()

        l_linha = Label(self.frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
        l_linha.place(x=309, y=52)
        l_sum = Label(self.frameMeio, text="Total RENDA                       ".upper(), anchor=NW, font=('Verdana 11'), bg=self.co1, fg="#83a9e6")
        l_sum.place(x=309, y=35)
        l_sum = Label(self.frameMeio, text="R$ {:,.2f}".format(valor[0]), anchor=NW, font=('Arial 17'), bg=self.co1, fg="#545454")
        l_sum.place(x=309, y=70)

        l_linha = Label(self.frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
        l_linha.place(x=309, y=132)
        l_sum = Label(self.frameMeio, text="TOTAL DESPESAS                 ".upper(), anchor=NW, font=('Verdana 11'), bg=self.co1, fg="#83a9e6")
        l_sum.place(x=309, y=115)
        l_sum = Label(self.frameMeio, text="R$ {:,.2f}".format(valor[1]), anchor=NW, font=('Arial 17'), bg=self.co1, fg="#545454")
        l_sum.place(x=309, y=150)

        l_linha = Label(self.frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
        l_linha.place(x=309, y=207)
        l_sum = Label(self.frameMeio, text="TOTAL SALDO ACUMULADO  ".upper(), anchor=NW, font=('Verdana 11'), bg=self.co1, fg="#83a9e6")
        l_sum.place(x=309, y=190)
        l_sum = Label(self.frameMeio, text="R$ {:,.2f}".format(valor[2]), anchor=NW, font=('Arial 17'), bg=self.co1, fg="#545454")
        l_sum.place(x=309, y=230)

    # função gráfico pizza
    def grafico_pizza(self):

        figura = plt.Figure(figsize=(5, 3), dpi=90)
        ax = figura.add_subplot(111)

        lista_valores = valores_graficoPizza()[1]
        lista_categorias = valores_graficoPizza()[0]

        explode = []
        for i in lista_categorias:
            explode.append(0.05)

        ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=self.colors,shadow=True, startangle=90)
        ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

        canva_categoria = FigureCanvasTkAgg(figura, self.frame_graPizza)
        canva_categoria.get_tk_widget().grid(row=0, column=0)

    # função para mostrar tabela de renda 
    def mostrar_tabela(self):

        # Cabeçalho da tabela
        tabela_head = ['#Id', 'Categoria', 'Data', 'Quantia']

        # Dados da tabela
        lista_itens = tabela()

        global tree

        # Cria Treeview para exibir a tabela
        tree = ttk.Treeview(self.frameRenda, selectmode="extended", columns=tabela_head, show="headings")

        # Scrollbars (vertical e horizontal)
        vsb = ttk.Scrollbar(self.frameRenda, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(self.frameRenda, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # Posiciona a Treeview e as barras de rolagem
        tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        # Configura o cabeçalho e colunas da tabela
        hd = ["center", "center", "center", "center"]
        h = [30, 100, 100, 100]
        n = 0

        for col in tabela_head:
            tree.heading(col, text=col.title(), anchor=CENTER)
            tree.column(col, width=h[n], anchor=hd[n])
            n += 1

        # Insere os dados na tabela
        for item in lista_itens:
            tree.insert('', 'end', values=item)

    # função inserir categoria
    def inserir_cat(self):
        nome = self.categoria_n.get()
        list_inserir = [nome]

        for i in list_inserir:
            if(i==''):
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return 
            
        # passando a lista para a função da view
        inserir_categoria(list_inserir)

        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

        self.categoria_n.delete(0, 'end')

        # atualizando dados
        categorias_f = ver_categoria()
        categoria = []

        for i in categorias_f:
            categoria.append(i[1])

        # atualizando a lista de categorias
        self.cat_combo_despesa['values'] = (categoria)

    # função inserir receitas
    def inserir_rec(self):
        nome = 'Receita'
        data = self.cal_receitas.get()
        valor = self.valor_receitas.get()

        list_inserir = [nome, data, valor]

        for i in list_inserir:
            if(i==''):
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return 
            
        # chamando a função inserir receitas da view
        inserir_receita(list_inserir)

        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

        self.cal_receitas.delete(0, 'end')
        self.valor_receitas.delete(0,'end')

        # atualizando dados
        self.mostrar_tabela()
        self.porcentagens()
        self.grafico_bar()
        self.resumo()
        self.grafico_pizza()

    # função inserir despesas
    def inserir_desp(self):
        nome = self.cat_combo_despesa.get()
        data = self.cal_despesas.get()
        valor = self.valor_despesas.get()

        list_inserir = [nome, data, valor]

        for i in list_inserir:
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return 
            
        # chamando a função inserir gastos da view
        inserir_gasto(list_inserir)

        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

        self.cat_combo_despesa.delete(0, 'end')
        self.cal_despesas.delete(0, 'end')
        self.valor_despesas.delete(0,'end')

        # atualizando dados
        self.mostrar_tabela()
        self.porcentagens()
        self.grafico_bar()
        self.resumo()
        self.grafico_pizza()

    # função deletar 
    def deletar(self):
        try:
            treev_dados = tree.focus()
            treev_dic = tree.item(treev_dados)
            treev_list = treev_dic['values']
            valor = treev_list[0]   
            nome = treev_list[1]

            if nome =='Receita':
                deletar_receita([valor])
                messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso!')

                # atualizando dados
                self.mostrar_tabela()
                self.porcentagens()
                self.grafico_bar()
                self.resumo()
                self.grafico_pizza()
            else:
                deletar_gasto([valor])
                messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso!')

                # atualizando dados
                self.mostrar_tabela()
                self.porcentagens()
                self.grafico_bar()
                self.resumo()
                self.grafico_pizza()

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos dados da tabela')
                            
# Executando código
if __name__ == '__main__':
    app = ExpenseControl()