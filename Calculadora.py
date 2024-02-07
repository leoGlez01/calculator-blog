from tkinter import *

ventana = Tk()
ventana.title("Calculadora")
i = 0

# Entradas
e_texto = Entry(ventana, font = ("Calibri 20"))
e_texto.grid(row=0, column=0, columnspan=4, padx=50, pady=5)

# Funciones
def clickBoton(valor):
    global i
    e_texto.insert(i, valor)
    i+=1

def borrar():
    e_texto.delete(0,END)
    i = 0

def operacion():
    ecuacion= e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0,resultado)
    i = 0

# Botones
boton1 = Button(ventana, text="1", width=7, height=2, command= lambda: clickBoton(1))
boton2 = Button(ventana, text="2", width=7, height=2, command= lambda: clickBoton(2))
boton3 = Button(ventana, text="3", width=7, height=2, command= lambda: clickBoton(3))
boton4 = Button(ventana, text="4", width=7, height=2, command= lambda: clickBoton(4))
boton5 = Button(ventana, text="5", width=7, height=2, command= lambda: clickBoton(5))
boton6 = Button(ventana, text="6", width=7, height=2, command= lambda: clickBoton(6))
boton7 = Button(ventana, text="7", width=7, height=2, command= lambda: clickBoton(7))
boton8 = Button(ventana, text="8", width=7, height=2, command= lambda: clickBoton(8))
boton9 = Button(ventana, text="9", width=7, height=2, command= lambda: clickBoton(9))
boton0 = Button(ventana, text="0", width=20, height=2, command= lambda: clickBoton(0))

botonBorrar = Button(ventana, text="AC", width=7, height=2,foreground= "White",background="Red", command= lambda: borrar())
botonParentesis1 = Button(ventana, text="(", width=7, height=2, command= lambda: clickBoton("("))
botonParentesis2 = Button(ventana, text=")", width=7, height=2, command= lambda: clickBoton(")"))
botonPunto = Button(ventana, text=".", width=7, height=2, command= lambda: clickBoton("."))

botonSumar = Button(ventana, text="+", width=7, height=2, command= lambda: clickBoton("+"))
botonRestar = Button(ventana, text="-", width=7, height=2, command= lambda: clickBoton("-"))
botonMult = Button(ventana, text="x", width=7, height=2, command= lambda: clickBoton("*"))
botonDiv = Button(ventana, text="/", width=7, height=2, command= lambda: clickBoton("/"))

botonIgual = Button(ventana, text="=", width=7, height=2, command= lambda: operacion())

# Agregar Botones en Pantalla
botonBorrar.grid(row = 1, column= 0, padx= 5, pady= 5)
botonParentesis1.grid(row = 1, column= 1, padx= 5, pady= 5)
botonParentesis2.grid(row = 1, column= 2, padx= 5, pady= 5)
botonDiv.grid(row = 1, column= 3, padx= 5, pady= 5)

boton7.grid(row = 2, column= 0, padx= 5, pady= 5)
boton8.grid(row = 2, column= 1, padx= 5, pady= 5)
boton9.grid(row = 2, column= 2, padx= 5, pady= 5)
botonMult.grid(row = 2, column= 3, padx= 5, pady= 5)

boton4.grid(row = 3, column = 0, padx = 5, pady = 5)
boton5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton6.grid(row = 3, column = 2, padx = 5, pady = 5)
botonRestar.grid(row = 3, column = 3, padx = 5, pady = 5)

boton1.grid(row = 4, column = 0, padx =5, pady = 5)
boton2.grid(row = 4, column = 1, padx =5, pady = 5)
boton3.grid(row = 4, column = 2, padx =5, pady = 5)
botonSumar.grid(row = 4, column = 3, padx =5, pady = 5)

boton0.grid(row = 5, column = 0,columnspan = 2, padx = 5, pady =5)
botonPunto.grid(row = 5, column = 2, padx = 5, pady =5)
botonIgual.grid(row = 5, column = 3, padx = 5, pady =5)




ventana.mainloop()