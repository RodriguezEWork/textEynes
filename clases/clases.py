from tkinter import *
from functools import partial
import turtle

root = Tk()
root['bg'] = 'light blue'

class Circulo: #<-- Clase
    def __init__(self, radio): #<-- Constructor
        self.radio=radio
    def calcularArea(self): #<-- 1er Metodo
        pi = 3.14
        return (self.radio**2)*pi #<-- Operacion ** significa elevado
    def calcularPerimetro(self): #<-- 2do Metodo
        pi = 3.14
        return 2 * pi * self.radio
    def dibujarCirculo(self):
        t = turtle.Turtle()
        t.circle(self.radio)
        t.clear()

ratio = DoubleVar()
multiplicador = DoubleVar()

def cambiar(radiador):

    try:
        if (radiador <= 0):
            raise NameError("No se puede ingresar valor 0.")
        else:

            global cir 
            cir = Circulo(radiador)

            label5 = Label(root, font=('Times_New_Roman', 30))
            label6 = Label(root, font=('Times_New_Roman', 30))
            label5.config(text='' + str(cir.calcularArea()))
            label5.place(x=400, y=400)
            label6.config(text='' + str(cir.calcularPerimetro()))
            label6.place(x=400, y=500)

    except NameError:
        emergente = Toplevel()
        emergente.title('Mensaje de error')
        label7 = Label(emergente, text="El valor debe ser mayor a cero.", font=('Times_New_Roman', 30))
        label7.pack()

entry1 = Entry(root, textvariable=ratio, font=('Times_New_Roman', 30))
entry1.place(x=400, y=200)
label = Label(root, text='Ingresar radio', font=('Times_New_Roman', 30))
label.place(x=500, y=100)
label2 = Label(root, text='Radio = ', font=('Times_New_Roman', 30))
label2.place(x=200, y=200)
button1 = Button(root, text="Calcular Radio", font=('Times_New_Roman', 20), command=lambda: cambiar(ratio.get()))
button1.place(x=500, y=300)

label3 = Label(root, text='Area = ', font=('Times_New_Roman', 30))
label3.place(x=200, y=400)

label4 = Label(root, text='Diametro = ', font=('Times_New_Roman', 30))
label4.place(x=200, y=500)

entry1 = Entry(root, textvariable=multiplicador, font=('Times_New_Roman', 30))
entry1.place(x=400, y=700)
label = Label(root, text='Ingresar Multiplo', font=('Times_New_Roman', 30))
label.place(x=500, y=600)
label2 = Label(root, text='Multiplo = ', font=('Times_New_Roman', 30))
label2.place(x=200, y=700)
button2 = Button(root, text="Calcular multiplo", font=('Times_New_Roman', 20), command=lambda: cambiar(ratio.get() * multiplicador.get()))
button2.place(x=500, y=800)

button1 = Button(root, text="Dibujar Circulo", font=('Times_New_Roman', 20), command=lambda: cir.dibujarCirculo())
button1.place(x=500, y=900)


root.mainloop()