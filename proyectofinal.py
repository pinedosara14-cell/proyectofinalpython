import tkinter as tk 
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# -------------------------
# FUNCIONES
# -------------------------
def abrir_registro_productos():
   messagebox.showinfo("Registro de Productos", "Aquí irá el módulo de registro de productos.")

def abrir_registro_ventas():
   messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_reportes():
   messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
   messagebox.showinfo("Acerca de", "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0")

# -------------------------
# FUNCION HOVER
# -------------------------
def on_enter(e):
    e.widget['background'] = "#1f00cc"

def on_leave(e):
    e.widget['background'] = 'red'

# -------------------------
# VENTANA
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - POSns")
ventana.geometry("500x700")
ventana.configure(bg="white")
ventana.resizable(False, False)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -------------------------
# LOGO
# -------------------------
try:
    imagen = Image.open(os.path.join(BASE_DIR,"logo.png"))
    imagen = imagen.resize((180, 180))
    img_logo = ImageTk.PhotoImage(imagen)

    tk.Label(ventana, image=img_logo, bg="white").pack(pady=10)
except:
    tk.Label(ventana, text="LOGO", font=("Arial", 16), bg="white").pack(pady=20)

# -------------------------
# IMAGEN POS
# -------------------------
try:
    img_pos = Image.open(os.path.join(BASE_DIR,"pos.png"))
    img_pos = img_pos.resize((100, 100))
    img_pos_tk = ImageTk.PhotoImage(img_pos)

    tk.Label(ventana, image=img_pos_tk, bg="white").pack(pady=5)
except:
    tk.Label(ventana, text="POS", font=("Arial", 12), bg="white").pack(pady=10)

# -------------------------
# CONTENEDOR BOTONES
# -------------------------
frame_botones = tk.Frame(ventana, bg="white")
frame_botones.pack(pady=20)

# -------------------------
# FUNCION CREAR BOTON
# -------------------------
def crear_boton(texto, comando):
    btn = tk.Button(
        frame_botones,
        text=texto,
        command=comando,
        font=("Arial", 12),
        bg="red",
        fg="black",
        activebackground="#1b1c72",
        activeforeground="black",
        width=25,
        height=2,
        bd=0,
        cursor="hand2"
    )
    btn.pack(pady=8)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    return btn

# -------------------------
# BOTONES
# -------------------------
crear_boton("🛒 Registro de Productos", abrir_registro_productos)
crear_boton("💳 Registro de Ventas", abrir_registro_ventas)
crear_boton("📊 Reportes", abrir_reportes)
crear_boton("ℹ️ Acerca de", abrir_acerca_de)

# -------------------------
# FOOTER
# -------------------------
tk.Label(
    ventana,
    text="Sistema POS - 2026",
    bg="white",
    fg="gray",
    font=("Arial", 10)
).pack(side="bottom", pady=10)

# -------------------------
# INICIO
# -------------------------
ventana.mainloop()