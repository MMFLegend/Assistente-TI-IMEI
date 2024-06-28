from tkinter import *
import tkinter as tk


def Menu_Principal():
    root = tk.Tk()
    root.configure(bg='gray25')
    root.geometry("1420x650")
    
    def pag_montar_computador():
        root.destroy()
        montar_computador_preparacao()
     
    def pag_avarias_solucoes():
        root.destroy()
        avarias_solucoes()
    
    def pag_rede_local_fios():
        root.destroy()
        rede_local_fios()
        
    def pag_rede_local_wireless():
        root.destroy()
        rede_local_wireless()
        
    def pag_caracteristicas_hardware():
        root.destroy()
        caracteristicas_hardware()
        
    def pag_tipos_memorias():
        root.destroy()
        tipos_memorias()
    
    def pag_tipos_processadores():
        root.destroy()
        tipos_processadores()
        
    root.title("Assistente TI")
    
    titulo_pag_inicial = tk.Label(root, text="Assistente TI", font=('Arial', 46), bg="gray25", fg="darkorchid2")
    titulo_pag_inicial.place(x=460, y=50, heiht=50, width=500)
    
    botao_memorias = tk.Button(root, text="Como montar um Computar", command=pag_montar_computador, font=('Arial', 30),bg="darkorchid2",fg="white")
    botao_memorias.place(x=600, y=150, height=50, width=200)
    
    botao_memorias = tk.Button(root, text="Avarias & Solu��es", command=pag_avarias_solucoes, font=('Arial', 30),bg="darkorchid2",fg="white")
    botao_memorias.place(x=600, y=250, height=50, width=200)
    
    botao_memorias = tk.Button(root, text="Confiura��o de uma rede local com fios", command=pag_rede_local_fios, font=('Arial', 20),bg="darkorchid2",fg="white")
    botao_memorias.place(x=600, y=350, height=50, width=200)
    
    botao_memorias = tk.Button(root, text="Confiura��o de uma rede local sem fios", command=pag_rede_local_wireless, font=('Arial', 20),bg="darkorchid2",fg="white")
    botao_memorias.place(x=600, y=450, height=50, width=200)
    
    botao_memorias = tk.Button(root, text="Caracteristicas dos componentes", command=pag_caracteristicas_hardware, font=('Arial', 20),bg="darkorchid2",fg="white")
    botao_memorias.place(x=600, y=550, height=50, width=200)    
    
    botao_memorias = tk.Button(root, text="Tipos de Memorias", command=pag_tipos_memorias, font=('Arial', 20),bg="darkorchid2",fg="white")
    botao_memorias.place(x=600, y=650, height=50, width=200)
    
    botao_memorias = tk.Button(root, text="Tipos de Processadores", command=pag_tipos_processadores, font=('Arial', 20),bg="darkorchid2",fg="white")
    botao_memorias.place(x=600, y=750, height=50, width=200)
    
    root.mainloop()
    
    
                                 #   Fun��es dos But�es
#   Menu Montar computador
def montar_computador_preparacao():
    
    root = tk.Tk()
    root.configure(bg="grey25")
    
    root.geometry("1420x650")
    
    def seguinte_montar_computador_motherboard():
        root.destroy()
        montar_computador_motherboard()
        
    def botao_menu_voltar():
        root.destroy()
        Menu_Principal()
        
    root.title("Assistente TI - Como montar um Computar")
    
    titulo_montar_computador = tk.Label(root, text="Preparação", font = ('Arial', 40), bg="grey25",fg="white")
    titulo_montar_computador.place(x=475, y=150, height=50, width=500)
    
    texto1_montar_computador = tk.Label(root, text='Junte as peças e componentes no local de montagem', font = ('Arial', 30), bg="grey25",fg="white")
    texto1_montar_computador.place(x=475, y=250, height=50, width=500)
    
    texto2_montar_computador = tk.Label(root, text='Leia os manuais de intruções de cada componente para entender como montar cada componente', font = ('Arial', 30), bg="grey25",fg="white")
    texto2_montar_computador.place(x=475, y=70, height=50, width=500)
    
    text3_montar_computador = tk.Label(root, text='Recomendo o uso de uma pulseira antiestatica durante a montagem do computador.')
    text3_montar_computador.place(x=575, y=70, height=30, width=500)
    
    imagem = tk.PhotoImage(file="antiestatic-band.png")
    w = tk.Label(root, image=imagem)
    w.imagem = imagem
    w.place(x=50, y=250, height=250, width=500)
    
    seguinte1_montar_computador = tk.Button(root, text='Proximo Passo',command=seguinte_montar_computador_motherboard, font = ('Arial', 30), bg="grey25",fg="white")
    seguinte1_montar_computador.place(x=475, y=70, height=50, width=500)
    
    root.mainloop()
    
def montar_computador_motherboard():
    root = tk.Tk()
    root.configure(bg="grey25")
    
    root.geometry("1420x650")    
    
    def seguinte_montar_computador_processador():
        root.destroy()
        montar_computador_processador()

    def botao_menu_voltar():
        root.destroy()
        Menu_Principal()
        
    root.title("Assistente TI - Como montar um Computar")
    
    titulo_montar_computador = tk.Label(root, text="Motherboard", font = ('Arial', 40), bg="grey25",fg="white")
    titulo_montar_computador.place(x=475, y=70, height=50, width=500)
    
    texto4_montar_computador = tk.Label(root, text='Remova os parafusos necessarios do gabinete', font = ('Arial', 30), bg="grey25",fg="white")
    texto4_montar_computador.place(x=475, y=70, height=50, width=500)
    
    texto5_montar_computador = tk.Label(root, text='Alinhe a placa-mae corretamente com os encaixes de montagem', font = ('Arial', 30), bg="grey25",fg="white")
    texto5_montar_computador.place(x=475, y=70, height=50, width=500)
    
    texto6_montar_computador = tk.Label(root, text='Prenda a placa-mae ao gabinete usando os parafusos fornecidos', font = ('Arial', 30), bg="grey25",fg="white")
    texto6_montar_computador.place(x=475, y=70, height=50, width=500)
    
    seguinte_montar_computador = tk.Button(root, text='Proximo Passo', command=seguinte_montar_computador_processador, font = ('Arial', 30), bg="grey25",fg="white")
    seguinte_montar_computador.place(x=475, y=70, height=50, width=500)
    
    root.mainloop()

def montar_computador_processador():
    root = tk.Tk()
    root.configure(bg="grey25")
    
    root.geometry("1420x650")    
        
    def botao_menu_voltar():
        root.destroy()
        Menu_Principal()

    root.title("Assistente TI - Como montar um Computar")
    
    titulo_montar_computador = tk.Label(root, text="Processador", font = ('Arial', 30), bg="grey25",fg="white")
    titulo_montar_computador.place(x=475, y=70, height=50, width=500)
    
    texto7_montar_computador = tk.Label(root, text='Localize o soquete correto para o processador na placa-mae e abra a alavanca de liberacao.', font = ('Arial', 30), bg="grey25",fg="white")
    texto7_montar_computador.place(x=475, y=70, height=50, width=500)
    
    texto8_montar_computador = tk.Label(root, text='Remova a tampa protetora do soquete e alinhe corretamente o processador.', font = ('Arial', 30), bg="grey25",fg="white")
    texto8_montar_computador.place(x=475, y=70, height=50, width=500)
    
    texto9_montar_computador = tk.Label(root, text='Baixe suavemente o processador no soquete e feche a alavanca de liberacao para prende-lo.', font = ('Arial', 30), bg="grey25",fg="white")
    texto9_montar_computador.place(x=475, y=70, height=50, width=500)

    seguinte_montar_computador = tk.Button(root, text='Proximo Passo', font = ('Arial', 30), bg="grey25",fg="white")
    seguinte_montar_computador.place(x=475, y=70, height=50, width=500)

    
    root.mainloop()

def montar_computador_cooler():
    root = tk.Tk()
    root.configure(bg="grey25")
    
    root.geometry("1420x650")    
        
    def botao_menu_voltar():
        root.destroy()
        Menu_Principal()

    root.title("Assistente TI - Como montar um Computar")
    
    titulo_montar_computador = tk.Label(root, text="Cooler", font = ('Arial', 30), bg="grey25",fg="white")
    titulo_montar_computador.place(x=475, y=70, height=50, width=500)
    
    texto10_montar_computador = tk.Label(root, text='Aplique a pasta termica no processador (se necessario) e alinhe o cooler com os encaixes na placa-mae.', font = ('Arial', 30), bg="grey25",fg="white")
    texto10_montar_computador.place(x=475, y=70, height=50, width=500)
    
    texto11_montar_computador = tk.Label(root, text='Prenda o cooler usando os parafusos ou clipes fornecidos', font = ('Arial', 30), bg="grey25",fg="white")
    texto11_montar_computador.place(x=475, y=70, height=50, width=500)
    
    seguinte_montar_computador = tk.Button(root, text='Proximo Passo', font = ('Arial', 30), bg="grey25",fg="white")
    seguinte_montar_computador.place(x=475, y=70, height=50, width=500)

def montar_computador_ram():
    root = tk.Tk()
    root.configure(bg="grey25")

    root.geometry("1420x650")

    def botao_menu_voltar():
        root.destroy()
        Menu_Principal()
    
    root.title("Trabalho IMEI - Como montar um computador")

    titulo_montar_computador = tk.Label(root, text="Memoria RAM")
    titulo_montar_computador.place(x=475, y=100, height=50, width=500)
#   Menu Montar Computador


Menu_Principal()