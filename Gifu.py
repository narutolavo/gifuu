from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *

from googletrans import Translator
translator = Translator()

from datetime import datetime


#from tkinter import filedialog
from tkinter import Menu

from tkinter import messagebox

bd = []
listacaixa = []
bd_anki = []

def adicionaraquivo():
	textoagora = texto.get(1.0, END)
	with open("tekisuto.txt", "w") as armazena:
   		armazena.write(textoagora)

def adicionabd():
	abriarquivo = open("tekisuto.txt", "r")
	textoagoraa = abriarquivo.readlines()
	for line in textoagoraa:
	    # print(line)
	    line = line[:-1]  # retira a quebra de linha do texto.
	    bd.append(line.split(" "))
	    #print(bd)
	abriarquivo.close()


def lista_traduzidas(nometraduzi):
    palavrastraduzidas["text"] = "Aguarde"
    controlando = ' '
    controle_anki = ' '    #ajusta = 0
    tamanhodbarra = len(nometraduzi)
    valor = 0
    for x in nometraduzi:
        traduzi = translator.translate(x, dest='pt')
        traduzir = str(traduzi.text)
        controlando = " | " + x + ": " + traduzir + " |  "
        controle_anki = x + " " + traduzir
        listacaixa.append(controlando)
        bd_anki.append(controle_anki)
        valor += 1
        barraprogresso["value"] = valor
        barraprogresso["maximum"] = tamanhodbarra
        barraprogresso.update()
        if valor == tamanhodbarra:
        	transformav = str(tamanhodbarra)
        	palavrastraduzidas["text"] = "("+transformav+") Palavras traduzidas, aperte no botao mostrar palavras"
        	palavrastraduzidas["foreground"] = "red"
def adiciona_palavra(bd):
    nometraduzi = []  # cria lista para armazenar as palavras a serem traduzidas
    for x in bd:  # verifica cada linha da minha matriz
        for celula in x:  # olha cada celula da minha linha
            pal = str(celula)  # converte em string a minha celula
            palav = pal[0]  # pega a primeira letra da minha string e guarda numa variavel
            #print("funcao a BD: " + pal[0])                  #olhando se deu certo
            pala = '@'  # cria uma variavel que vai ta no texto que vai indica a palavra a ser traduzida
            if palav == pala:  # compara
                adiciona = pal[1:]  # agora vai excluir o caracter @ que ta na posição 0 e vai adiciona da 1 em diante
                nometraduzi.append(adiciona)  # adiciona a minha lista
    lista_traduzidas(nometraduzi)
    #print("nometraduzi")
    #print(nometraduzi)


def cp_mylista():
    imprimirminhalista()


def limparTextbox():
    texto.delete(1.0,END)
    minhalista.delete( 0, END)
    bd.clear()
    listacaixa.clear()
    barraprogresso.stop()
    palavrastraduzidas["text"]= "Insira o texto"
    #texto["font"] = ("Consolas",10)

#def aoClicar(mostra_texto):
    #mensagem["text"]= "palavras traduzidas:\n"+mostra_texto
	

def enviarpalavras():
	mostra_texto = texto.get(1.0, END)
	adicionaraquivo()
	adicionabd()
	adiciona_palavra(bd)

def cp_mylist():
    cp_mylista()

def imprimirlis():
	print("bd_anki")
	print(bd_anki)
	print("bd")	
	print(bd)
	print("listacaixa")
	print(listacaixa)

def cardAnki():
	armazenadoanki = ''
	for pala_du in bd_anki:
		armazenadoanki += pala_du + "\n"
	data_e_hora_atuais = datetime.now()
	data_e_hora_em_texto = data_e_hora_atuais.strftime("%d_%m_%Y %H:%M_%S")
	nuvemanki = open("BDanki/bdAnki_"+data_e_hora_em_texto+".txt", "w")
	nuvemanki.write(armazenadoanki)
	#armazenadoanki.close()
	nuvemanki.close()

janela = Tk()
janela.geometry("900x600+200+100")
janela.title("GIFU")
janela.wm_iconbitmap("@gifu.xbm") 

textoquadro = Frame(janela)
barraprogressoquadro = Frame(janela)
botaoquadro = Frame(janela)
listaquadro = Frame(janela)

textoquadro.pack(side= TOP, fill=X)
barraprogressoquadro.pack(side= TOP, fill=X)
botaoquadro.pack(side= LEFT)
listaquadro.pack(side= RIGHT, fill=X, expand=True)


texto = scrolledtext.ScrolledText(textoquadro,width=60,height=15)
texto.pack(fill='x', expand=False )
texto.insert(INSERT, "Limpe esse texto, e cole o seu a traduzir")

barraprogresso = Progressbar(barraprogressoquadro, length=200)
barraprogresso.pack()

bt=Button(botaoquadro, text="Limpar", command=limparTextbox)
bt.pack(side= TOP, fill=X, padx='10', pady='10')

botaoo=Button(botaoquadro, text="traduzir palavras", command=enviarpalavras)
botaoo.pack(side= TOP, fill=X, padx='10', pady='10')

botaooo=Button(botaoquadro, text="mostrar palavras", command=cp_mylist)
botaooo.pack(fill=X, padx='10', pady='10')

botaoooo=Button(botaoquadro, text="criar anki", command=cardAnki)
botaoooo.pack(fill=X, padx='10', pady='10')

botaoooo=Button(botaoquadro, text="ver bdS", command=imprimirlis)
botaoooo.pack(fill=X, padx='10', pady='10')

mensagem = Label(barraprogressoquadro, text="GIFU", font="impact 30")
mensagem.pack()

scrollbar = Scrollbar(listaquadro)
scrollbar.pack( side = RIGHT, fill=Y )

palavrastraduzidas = Label(barraprogressoquadro, text=" ", font="impact 10")
palavrastraduzidas.pack()

minhalista = Listbox(listaquadro, yscrollcommand = scrollbar.set, font="FreeSans 20")
def imprimirminhalista():
    for linha in listacaixa:
        minhalista.insert(END, linha)
       

minhalista.pack( side = RIGHT, fill = X, expand=True )
scrollbar.config( command = minhalista.yview )

#programa
janela.mainloop()