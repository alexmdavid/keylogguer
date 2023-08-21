import tkinter as tk
import random

def generar_numero_secreto():
    return random.randint(1, 100)

def comprobar_adivinanza(numero_secreto, intento):
    if intento < numero_secreto:
        return "El número secreto es mayor."
    elif intento > numero_secreto:
        return "El número secreto es menor."
    else:
        return "¡Felicidades! ¡Adivinaste el número!"

def jugar():
    numero_secreto = generar_numero_secreto()
    intentos = 0

    def verificar():
        nonlocal intentos
        intentos += 1
        try:
            intento = int(entry.get())
            resultado = comprobar_adivinanza(numero_secreto, intento)
            resultado_label.config(text=resultado)
            if resultado.startswith("¡Felicidades"):
                entry.config(state="disabled")
                verificar_button.config(state="disabled")
        except ValueError:
            resultado_label.config(text="Ingresa un número válido.")

    ventana = tk.Tk()
    ventana.title("Juego de Adivinanza")

    etiqueta = tk.Label(ventana, text="Adivina el número secreto entre 1 y 100:")
    etiqueta.pack(pady=10)

    entry = tk.Entry(ventana)
    entry.pack(pady=5)

    verificar_button = tk.Button(ventana, text="Verificar", command=verificar)
    verificar_button.pack(pady=5)

    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack(pady=10)

    ventana.mainloop()

jugar()
