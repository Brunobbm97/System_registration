from tkinter import *
from tkinter import Tk, StringVar, ttk


from PIL import Image, ImageTk

from tkcalendar import Calendar, DateEntry
from datetime import date


co0 = "#2e2d2b"   # Preto
co1 = "#feffff"   # branca
co2 = "#4fa882"   # verde
co3 = "#38576b"   # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co9 = "#e9edf5"


# Criando janela

janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Criando os frames
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# Trabalhando no frame cima
# Abrindo Imagem
app_img = Image.open('inventory.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=' Home Inventory ', width=900, compound=LEFT, relief=RAISED, anchor=NW,
                 font=('Verdana 20 bold'), bg=co1, fg=co4)

app_logo.place(x=0, y=0)


# Trabalhando no frame Meio

# Criando entradas
l_name = Label(frameMeio, text='Name', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_name.place(x=10, y=10)
e_name = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_name.place(x=130, y=11)

l_local = Label(frameMeio, text='Sala/Area', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_local.place(x=10, y=40)
e_local = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_local.place(x=130, y=41)

l_description = Label(frameMeio, text='Description', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_description.place(x=10, y=70)
e_description = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_description.place(x=130, y=71)

l_brand = Label(frameMeio, text='Brand/Model', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_brand.place(x=10, y=100)
e_brand = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_brand.place(x=130, y=101)

l_cal = Label(frameMeio, text='Date ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cal.place(x=10, y=130)
e_cal = DateEntry(frameMeio, width=12, background='darkblue', bordewidth=2, year=2024)
e_cal.place(x=130, y=131)

l_valor = Label(frameMeio, text='Valor da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_valor.place(x=10, y=160)
e_valor = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_valor.place(x=130, y=161)

l_serie = Label(frameMeio, text='Number of serie', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_serie.place(x=10, y=190)
e_serie = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_serie.place(x=130, y=191)


janela.mainloop()
