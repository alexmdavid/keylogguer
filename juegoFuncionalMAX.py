import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

# Función para generar un número aleatorio entre 1 y 100
def generar_numero_secreto():
    return random.randint(1, 100)

# Función para crear la ventana principal
def crear_ventana():
    ventana = QMainWindow()
    ventana.setWindowTitle("Juego de Adivinar el Número")
    ventana.setGeometry(100, 100, 400, 200)
    return ventana

# Función para crear un label con texto en la ventana
def crear_label(ventana, texto, x, y, ancho, alto):
    label = QLabel(texto, ventana)
    label.setGeometry(x, y, ancho, alto)
    label.setStyleSheet("font-size: 14px; font-weight: bold; color: #333;")
    return label

# Función para crear un input en la ventana
def crear_input(ventana, x, y, ancho, alto):
    input_widget = QLineEdit(ventana)
    input_widget.setGeometry(x, y, ancho, alto)
    input_widget.setStyleSheet("font-size: 14px; padding: 5px;")
    return input_widget

# Función para crear un botón en la ventana
def crear_boton(ventana, texto, x, y, ancho, alto, funcion):
    boton = QPushButton(texto, ventana)
    boton.setGeometry(x, y, ancho, alto)
    boton.setStyleSheet("font-size: 14px; padding: 5px; background-color: #4CAF50; color: white; border: none;")
    boton.clicked.connect(funcion)
    return boton

# Función para mostrar un mensaje de resultado en la ventana
def mostrar_mensaje_resultado(ventana, mensaje):
    resultado_label = QLabel(mensaje, ventana)
    resultado_label.setGeometry(50, 120, 300, 30)
    resultado_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #FF5733;")
    return resultado_label

# Función que maneja el intento de adivinar el número
def adivinar_numero(input_widget, numero_secreto, resultado_label):
    try:
        numero_adivinado = int(input_widget.text())
        if numero_adivinado < numero_secreto:
            resultado_label.setText("El número es mayor.")
        elif numero_adivinado > numero_secreto:
            resultado_label.setText("El número es menor.")
        else:
            resultado_label.setText("¡Felicitaciones! ¡Adivinaste el número!")
    except ValueError:
        resultado_label.setText("Por favor, ingresa un número válido.")

# Función principal
def main():
    # Generar un número secreto
    numero_secreto = generar_numero_secreto()
    # Crear la aplicación y la ventana principal
    app = QApplication(sys.argv)
    ventana = crear_ventana()
    # Crear elementos en la ventana
    label_instrucciones = crear_label(ventana, "Ingresa un número del 1 al 100:", 50, 20, 300, 30)
    input_numero = crear_input(ventana, 50, 60, 200, 30)
    resultado_label = crear_label(ventana, "", 50, 120, 300, 30)
    boton_adivinar = crear_boton(ventana, "Adivinar", 260, 60, 80, 30, lambda: adivinar_numero(input_numero, numero_secreto, resultado_label))
    # Mostrar la ventana y ejecutar la aplicación
    ventana.show()
    sys.exit(app.exec_())

# Iniciar la aplicación si este archivo es el programa principal
if __name__ == "__main__":
    main()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main()
