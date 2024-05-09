from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Error import *

window = Tk()
window.title("Zero Division Error")
window.geometry("450x350")

frame = Frame(window, bg="lightblue")
frame.pack(fill="both", expand="yes")

Label(frame, text="Zero Division Error", fg="darkblue", bg="lightblue", font=("Modern", 20, "bold")).pack(pady=(10, 10))


dividendo = StringVar()
dividendoLabel = Label(frame, text="Dividendo:", bg="lightblue", font=("Lexend", 10))
dividendoLabel.pack(pady=(10, 0))
dividendoInput = Entry(frame, textvariable=dividendo)
dividendoInput.pack()

divisor = StringVar()
divisorLabel = Label(frame, text="Divisor:", bg="lightblue", font=("Lexend", 10))
divisorLabel.pack(pady=(10, 0))
divisorInput = Entry(frame, textvariable=divisor)
divisorInput.pack(pady=(0, 10))

clase = Error()

def divideError(divisor, dividendo):
    resultado = clase.divideError(divisor, dividendo)
    print(messagebox.showinfo("Resultado", f"El resultado de la división es: {resultado}"))

def divideCatch(divisor, dividendo):
    resultado = clase.divideCatch(divisor, dividendo)
    if resultado == False:
        print(messagebox.showwarning("Cuidado", "No se puede dividir entre zero"))
    else:
        print(messagebox.showinfo("Resultado", f"El resultado de la división es: {resultado}"))

btnError = Button(frame, text="Dividir (Error)", bg="darkblue", fg="white", font=("Lexend", 8), command=lambda:divideError(dividendo.get(), divisor.get()))
btnError.pack(pady=(0,10))

btnDivide = Button(frame, text="Dividir (Try - Catch)", bg="darkblue", fg="white", font=("Lexend", 8), command=lambda:divideCatch(dividendo.get(), divisor.get()))
btnDivide.pack(pady=(0,10))

window.mainloop()