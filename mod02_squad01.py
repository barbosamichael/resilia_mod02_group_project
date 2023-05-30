#!/usr/bin/env python
# coding: utf-8

# ## Projeto modulo02 pesquisa

# In[ ]:


from time import strftime
import csv


# In[ ]:


strftime("%a,%d %b %Y %H:%M:%S")


# In[ ]:





# In[ ]:


def tela_inicial():
    print("Bem vindo a pesquisa abcdefh")
    print("\nQueira inserir as informações pedidas abaixo :)")


# In[ ]:


usuarios=[]
idade=0
while idade !="00":
    tela_inicial()
    
    idade = str(input("Idade: "))
    if idade == "00":
        break
    genero = str(input("Gênero: "))
    resposta_1 = int(input("questao01: "))
    resposta_2 = int(input("questao02: "))
    resposta_3 = int(input("questao03: "))
    resposta_4 = int(input("questao04: "))
    data_registro = strftime("%a,%d %b %Y %H:%M:%S")
    print("\nPara encerrar digite 00 no campo idade")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




