from tkinter import *

janela = Tk()
janela['bg'] = 'black'
janela.title('Calculadora By:WS')

lb0 = Label(janela, width='30', height='2', text='CALCULATOR', bg='orange')
lb0.place(x=90, y=28)


def tempo(choice):
    from time import localtime
    relogio = localtime()
    ano = relogio.tm_year
    mes = relogio.tm_mon
    dia = relogio.tm_mday
    horas = relogio.tm_hour
    minutos = relogio.tm_min
    segundos = relogio.tm_sec
    if choice == 'ano':
        return ano
    elif choice == 'mes':
        return mes 
    elif choice == 'dia':
        return dia
    elif choice == 'horas':
        return horas
    elif choice == 'minutos':
        return minutos
    elif choice == 'segundos':
        return segundos


def bt1_click():
    def btIGUAL1_click():
        if (str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
            num1 = int(ed1.get())
            num2 = int(ed2.get())
            lbRESULTADO1['text'] = num1 + num2
        else:
            lbRESULTADO1['text'] = 'Inválido'
    lbSOMA = Label(janela, width='1', text='+', bg='green')
    lbSOMA.place(x=210, y=103)
    ed1 = Entry(janela, width='10')
    ed1.place(x=140, y=103)
    ed2 = Entry(janela, width='10')
    ed2.place(x=230, y=103)
    btIGUAL1 = Button(janela, width=5, text='=', bg='green', command=btIGUAL1_click)
    btIGUAL1.place(x=300, y=100)
    lbRESULTADO1 = Label(janela, width='7', text='')
    lbRESULTADO1.place(x=344, y=101)


def bt2_click():
    def btIGUAL2_click():
        if (str(ed3.get()).isnumeric() and str(ed4.get()).isnumeric()):
            num1 = int(ed3.get())
            num2 = int(ed4.get())
            lbRESULTADO2['text'] = num1 - num2
        else:
            lbRESULTADO2['text'] = 'Inválido'
    lbSUBTRACAO = Label(janela, width='1', text='-', bg='blue')
    lbSUBTRACAO.place(x=210, y=133)
    ed3 = Entry(janela, width='10')
    ed3.place(x=140, y=133)
    ed4 = Entry(janela, width='10')
    ed4.place(x=230, y=133)
    btIGUAL2 = Button(janela, width=5, text='=', bg='blue', command=btIGUAL2_click)
    btIGUAL2.place(x=300, y=133)
    lbRESULTADO2 = Label(janela, width='7', text='')
    lbRESULTADO2.place(x=344, y=133)


def bt3_click():
    def btIGUAL3_click():
        if (str(ed5.get()).isnumeric() and str(ed6.get()).isnumeric()):
            num1 = int(ed5.get())
            num2 = int(ed6.get())
            lbRESULTADO3['text'] = num1 * num2
        else:
            lbRESULTADO3['text'] = 'Inválido'
    lbMULTIPLICACAO = Label(janela, width='1', text='x', bg='yellow')
    lbMULTIPLICACAO.place(x=210, y=163)
    ed5 = Entry(janela, width='10')
    ed5.place(x=140, y=163)
    ed6 = Entry(janela, width='10')
    ed6.place(x=230, y=163)
    btIGUAL3 = Button(janela, width=5, text='=', bg='yellow', command=btIGUAL3_click)
    btIGUAL3.place(x=300, y=163)
    lbRESULTADO3 = Label(janela, width='7', text='')
    lbRESULTADO3.place(x=344, y=163)


def bt4_click():
    def btIGUAL4_click():
        if (str(ed7.get()).isnumeric() and str(ed8.get()).isnumeric()):
            num1 = float(ed7.get())
            num2 = float(ed8.get())
            lbRESULTADO4['text'] = num1 / num2
        else:
            lbRESULTADO4['text'] = 'Inválido'
    lbDIVISAO = Label(janela, width='1', text='/', bg='purple')
    lbDIVISAO.place(x=210, y=193)
    ed7 = Entry(janela, width='10')
    ed7.place(x=140, y=193)
    ed8 = Entry(janela, width='10')
    ed8.place(x=230, y=193)
    btIGUAL4 = Button(janela, width=5, text='=', bg='purple', command=btIGUAL4_click)
    btIGUAL4.place(x=300, y=193)
    lbRESULTADO4 = Label(janela, width='7', text='')
    lbRESULTADO4.place(x=344, y=193)


lb1 = Label(janela, text='By: Wallace Santos', bg='red')
lb1.pack(side=BOTTOM)

data = f"{tempo('dia')}/{tempo('mes')}/{tempo('ano')} - {tempo('horas')}:{tempo('minutos')}:{tempo('segundos')}"
lb2 = Label(janela, width='40', height='2', text=data, bg='white')
lb2.place(x=90, y=320)

bt1 = Button(janela, width=15, text='SOMA', bg='green', command=bt1_click)
bt2 = Button(janela, width=15, text='SUBTRAÇÂO', bg='blue', command=bt2_click)
bt3 = Button(janela, width=15, text='MULTIPLICAÇÂO', bg='yellow', command=bt3_click)
bt4 = Button(janela, width=15, text='DIVISÂO', bg='purple', command=bt4_click)

bt1.place(x=30, y=100)
bt2.place(x=30, y=130)
bt3.place(x=30, y=160)
bt4.place(x=30, y=190)

janela.geometry('400x400+500+150')
janela.mainloop()
