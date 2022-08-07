from tkinter import *
from tkinter import ttk
import math

master = Tk()
master.geometry("876x291+527+312")
master.iconbitmap(default="icones\\ico.ico")
master.wm_resizable(width=False, height=False)
master.title("Calculadora de Potências")

def calcular():
    try:
        corrente = float(num1.get())
        tensao = float(num2.get())
        fp = float(num3.get())

        print ("corrente %f" %(corrente))
        print ("tensao %f" %(tensao))
        print ("fp %f" %(fp))

        graus = fp*(180/math.pi)      
        print ("graus %f" %(graus))
        potKVA = tensao * corrente
        potKW = potKVA * math.cos(graus)
        potKVAR = potKVA * math.sin(graus)

        print ("potKVA %f" %(potKVA))
        print ("potKW %f" %(potKW))
        print ("potKVAR %f" %(potKVAR))


        resultadoKVA['text'] = str(format(potKVA, '.2f'))
        resultadoKW['text'] = str(format(potKW, '.2f'))
        resultadoKVAR['text'] = str(format(potKVAR, '.2f'))

    except ValueError:
        resultadoKVA['text'] = "SÓ NÚMEROS"
        resultadoKW['text'] = "SÓ NÚMEROS"
        resultadoKVAR['text'] = "SÓ NÚMEROS"


def limpar():
    num1.delete(0, END)
    num2.delete(0, END)
    num3.delete(0, END)
    resultadoKW["text"] = ""
    resultadoKVA["text"] = ""
    resultadoKVAR["text"] = ""


imgFundo = PhotoImage(file="imagens\\img.png")

labelFundo = Label(master, image=imgFundo)
labelFundo.place(x=0, y=0)

info = Label(master, text="Calculadora de potências", bg="#EA4335", fg="white", font=("Calibri", 24, "bold"))
info.place(width=815, height=46, x=30, y=12)

labelTensao = Label(master, text="TENSÃO(V)", font=("Calibri", 12), bg="#E0E0E0")
labelTensao.place( x=390, y=58)

num1 = Entry(master, font=("Calibri", 20), justify=CENTER, bg="#E0E0E0")
num1.place(width=209, height=39, x=320, y=82)
num1.insert(END, 1)

labelCorrente = Label(master, text="CORRENTE (A)", font=("Calibri", 12), bg="#E0E0E0")
labelCorrente.place( x=101, y=58)

num2 = Entry(master, font=("Calibri", 20), justify=CENTER, bg="#E0E0E0")
num2.place(width=209, height=39, x=31, y=82)
num2.insert(END, 1)

labelFp = Label(master, text="F.P.", font=("Calibri", 12), bg="#E0E0E0")
labelFp.place( x=724, y=58)

num3 = Entry(master, font=("Calibri", 20), justify=CENTER, bg="#E0E0E0")
num3.place(width=209, height=39,  x=638, y=82)
num3.insert(END, 1)



labelResKVA = Label(master, text="Pot. VA", font=("Calibri", 12), bg="#E0E0E0")
labelResKVA.place( x=390, y=127)
resultadoKVA = Label(master, text="SAÍDA", font=("Calibri", 20), bg="#E0E0E0")
resultadoKVA.place(width=209, height=39,  x=31, y=151)


labelResKW = Label(master, text="Pot. W", font=("Calibri", 12), bg="#E0E0E0")
labelResKW.place( x=101, y=127)
resultadoKW = Label(master, text="SAÍDA", font=("Calibri", 20), bg="#E0E0E0")
resultadoKW.place(width=209, height=39,  x=320, y=151)

labelResKVAR = Label(master, text="Pot. VAr", font=("Calibri", 12), bg="#E0E0E0")
labelResKVAR.place( x=704, y=127)
resultadoKVAR = Label(master, text="SAÍDA", font=("Calibri", 20), bg="#E0E0E0")
resultadoKVAR.place(width=209, height=39,  x=638, y=151)


bt1 = Button(master, text="LIMPAR", font=("Calibri", 14, "bold"), bg="#EA4335", fg="white", command=limpar)
bt1.place(width=142, height=41, x=135, y=220)

bt2 = Button(master, text="CALCULAR", font=("Calibri", 14, "bold"), bg="#EA4335", fg="white", command=calcular)
bt2.place(width=143, height=42, x=599, y=221)

master.mainloop()
