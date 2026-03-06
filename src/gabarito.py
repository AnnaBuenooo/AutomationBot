import pyautogui as py
import time

py.PAUSE = 1    
link =  "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

py.press("win")
py.write("chrome") 
py.press("enter")
py.click(x=680, y=480)
py.write(link)
py.press("enter")
time.sleep(3)
py.click(x=717, y=370)

py.write("annabuenotest@gmail.com")
py.press("tab")
py.write("doismilevinteseis")
py.press("tab") 
py.press("enter")
time.sleep(3)

import pandas as pd

tabela = pd.read_csv("data/produtos.csv")
print(tabela)


for linha in tabela.index:
    py.click(x=679, y=259)
    codigo = str(tabela.loc[linha, "codigo"])
    py.write(codigo)
    py.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    py.write(marca)
    py.press("tab")


    tipo = str(tabela.loc[linha, "tipo"])
    py.write(tipo)
    py.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    py.write(categoria)
    py.press("tab")

    preco = str(tabela.loc[linha, "preco_unitario"])
    py.write(preco)
    py.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    py.write(custo)
    py.press("tab")  


    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        py.write(obs)
    py.press("tab")

    py.press("enter")

    py.scroll(5000)



