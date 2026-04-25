import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Programas para subir a repositorio")
ventana.geometry("400x250")
ventana.configure(bg="#1e1e2f")  # color de fondo oscuro moderno

# Crear etiqueta con mejor tipografía y colores
etiqueta = tk.Label(
    ventana,
    text="Este programa es de Sara y Nahome",
    font=("Helvetica", 16, "bold"),  # tipografía grande y en negrita
    fg="#00ffcc",  # color del texto (verde llamativo)
    bg="#1e1e2f"   # mismo fondo que la ventana
)

etiqueta.pack(pady=40)

# Ejecutar ventana
ventana.mainloop()