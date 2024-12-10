import tkinter as tk
from tkinter import messagebox

# Función para calcular la cantidad de billetes necesarios
def cajero_automatico():
    try:
        # Obtener y validar el monto ingresado
        entrada = entry_monto.get()
        
        if '.' in entrada:
            messagebox.showerror("Error", "Este cajero no cuenta con monedas maestro Leonel :).")
            return

        monto = int(entrada)

        # Lista de denominaciones de billetes disponibles en el cajero
        billetes = [100, 50, 20, 10, 5, 1]
        resultado = ""

        # Calcular y mostrar la cantidad de billetes necesarios
        for billete in billetes:
            cantidad = monto // billete
            if cantidad > 0:
                resultado += f"{cantidad} billetes de {billete}\n"
            monto %= billete

        # Mostrar el resultado en la etiqueta
        label_resultado.config(text=resultado)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Cajero Automático")
root.geometry("400x300")


# Etiqueta y campo de entrada para el monto
label_monto = tk.Label(root, text="Ingrese el monto a retirar:")
label_monto.pack()

entry_monto = tk.Entry(root)
entry_monto.pack()

# Botón para calcular
boton_calcular = tk.Button(root, text="Calcular", command=cajero_automatico)
boton_calcular.pack()

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack()

# Iniciar la aplicación
root.mainloop()
