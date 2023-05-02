from tkinter import *
from tkinter import messagebox
import tkinter as tk
v = ""
islem=""
tut=0
def temizle():
    global v
    global tut
    global islem
    v=""
    tut=0
    islem=""
    veri.delete(0,END)
    veri.focus()
    veri.insert(0,"0")
    
def yaz(sayi):
    global v
    global tut
    global islem
    kontrol=str(sayi)
    if(kontrol!="+" and kontrol!="-" and kontrol!="*" and kontrol!="/" and kontrol!=" " and kontrol!="=" and kontrol!=","):
        v=v+str(sayi)
        veri.delete(0,END)
        veri.insert(0,v)
    elif(kontrol=="="):
        if(islem=="*"):
            sonuc=tut*int(v)
        elif(islem=="-"):
            sonuc=tut-int(v)
        elif(islem=="+"):
            sonuc=tut+int(v)
        elif(islem=="/"):
            sonuc=tut/int(v)
        veri.delete(0,END)
        veri.insert(0,str(sonuc))
    else:
        tut=int(v)
        veri.delete(0,END)
        veri.insert(0,str(sayi))
        v=""
        islem=str(sayi)
        
    
    
form=Tk()
form.title('Hesap Makinası V 1.0')
form.geometry("290x320")
form.configure(bg="gray")
form.resizable(False,False)
veri = Entry(form, bd =2,  width=21, font=('Arial 15'),justify='right')
veri.place(x=25, y=15)
veri.insert(0,"0")
veri.focus()
#buton seti başlangıç
yedi = tk.Button(form, text="7", font="Arial 14 bold", width=4,command=lambda:yaz(7))
yedi.place(x=25, y=50)
sekiz = tk.Button(form, text="8", font="Arial 14 bold", width=4,command=lambda:yaz(8))
sekiz.place(x=85, y=50)
dokuz = tk.Button(form, text="9", font="Arial 14 bold", width=4,command=lambda:yaz(9))
dokuz.place(x=145, y=50)
carpi = tk.Button(form, text="X", font="Arial 14 bold", width=4,command=lambda:yaz("*"))
carpi.place(x=205, y=50)
dort = tk.Button(form, text="4", font="Arial 14 bold", width=4,command=lambda:yaz(4))
dort.place(x=25, y=90)
bes = tk.Button(form, text="5", font="Arial 14 bold", width=4,command=lambda:yaz(5))
bes.place(x=85, y=90)
alti = tk.Button(form, text="6", font="Arial 14 bold", width=4,command=lambda:yaz(6))
alti.place(x=145, y=90)
cikarma = tk.Button(form, text="-", font="Arial 14 bold", width=4,command=lambda:yaz("-"))
cikarma.place(x=205, y=90)
bir = tk.Button(form, text="1", font="Arial 14 bold", width=4,command=lambda:yaz(1))
bir.place(x=25, y=130)
iki= tk.Button(form, text="2", font="Arial 14 bold", width=4,command=lambda:yaz(2))
iki.place(x=85, y=130)
uc = tk.Button(form, text="3", font="Arial 14 bold", width=4,command=lambda:yaz(3))
uc.place(x=145, y=130)
toplama = tk.Button(form, text="+", font="Arial 14 bold", width=4,command=lambda:yaz("+"))
toplama.place(x=205, y=130)
artieksi = tk.Button(form, text="+/-", font="Arial 14 bold", width=4,command=lambda:yaz(" "))
artieksi.place(x=25, y=170)
sifir= tk.Button(form, text="0", font="Arial 14 bold", width=4,command=lambda:yaz(0))
sifir.place(x=85, y=170)
virgul = tk.Button(form, text=",", font="Arial 14 bold", width=4,command=lambda:yaz(","))
virgul.place(x=145, y=170)
bolme = tk.Button(form, text="÷", font="Arial 14 bold", width=4,command=lambda:yaz("/"))
bolme.place(x=205, y=170)
esittir = tk.Button(form, text="=",bg="azure3" ,font="Arial 14 bold", width=19,command=lambda:yaz("="))
esittir.place(x=25, y=210)
clr = tk.Button(form, text="Clr",bg="azure3" ,font="Arial 14 bold", width=19,command=lambda:temizle())
clr.place(x=25, y=250)
#buton seti bitiş
form.mainloop()
