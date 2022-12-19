from num2words import num2words
from tkinter import *

num = int(input('Digite um número inteiro: '))

def traduzir():
    num_en = num2words (num, lang = 'en')
    num_en_ord = num2words (num, lang = 'en', to = 'ordinal')
 
    num_br = num2words (num, lang = 'pt-br')
    num_br_ord = num2words (num, lang = 'pt-br', to = 'ordinal')

    num_es = num2words (num, lang = 'es')
    num_es_ord = num2words (num, lang = 'es', to = 'ordinal')
  
    num_fr = num2words (num, lang = 'fr')
    num_fr_ord = num2words (num, lang = 'fr', to = 'ordinal')
    
    num_al = num2words (num, lang = 'de')
    num_al_ord = num2words (num, lang = 'de', to = 'ordinal')

    num_it = num2words (num, lang = 'it')
    num_it_ord = num2words (num, lang = 'it', to = 'ordinal')
    
    texto_resposta['text'] = f'''
    Em inglês é: {num_en.capitalize()}
    Em inglês(ordinal): {num_en_ord.capitalize()}
    Em português é: {num_br.capitalize()}
    Em português(ordinal): {num_br_ord.capitalize()}
    Em espanhol é: {num_es.capitalize()}
    Em espanhol (ordinal): {num_es_ord.capitalize()}
    Em francês é: {num_es.capitalize()}
    Em francês (ordinal): {num_fr_ord.capitalize()}
    Em alemão é: {num_al.capitalize()}
    Em alemão (ordinal): {num_al_ord.capitalize()}
    Em italiano é: {num_it.capitalize()}
    Em italiano (ordinal): {num_it_ord.capitalize()}
    '''

janela = Tk()
janela.title("Números em Outros Idiomas")
texto = Label(janela, text="Clique no botão para ver o número em outras línguas")
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Resposta", command=traduzir)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()