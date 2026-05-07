import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os

# =========================================
# FUNCIONES
# =========================================
def abrir_registro_productos():

    # -------------------------------------
    # VENTANA REGISTRO
    # -------------------------------------
    reg = tk.Toplevel()
    reg.title("Registro de Productos")
    reg.geometry("500x550")
    reg.configure(bg="#f4f6f9")
    reg.resizable(False, False)

    # -------------------------------------
    # TITULO
    # -------------------------------------
    titulo = tk.Label(
        reg,
        text="🛒 Registro de Productos",
        font=("Montserrat", 22, "bold"),
        bg="#f4f6f9",
        fg="#1b1c72"
    )
    titulo.pack(pady=20)

    # -------------------------------------
    # FRAME PRINCIPAL
    # -------------------------------------
    frame = tk.Frame(
        reg,
        bg="white",
        bd=0
    )
    frame.pack(padx=30, pady=10, fill="both", expand=True)

    # -------------------------------------
    # FUNCIONES ESTILO
    # -------------------------------------
    def crear_label(texto):
        return tk.Label(
            frame,
            text=texto,
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#333333"
        )

    def crear_entry():
        return tk.Entry(
            frame,
            font=("Arial", 12),
            bg="#f1f3f6",
            relief="flat",
            width=30
        )

    # =====================================
    # ID PRODUCTO
    # =====================================
    crear_label("ID del Producto").pack(anchor="w", padx=30, pady=(20, 5))

    txt_id = crear_entry()
    txt_id.pack(ipady=8, pady=5)

    # =====================================
    # DESCRIPCION
    # =====================================
    crear_label("Descripción").pack(anchor="w", padx=30, pady=(15, 5))

    txt_desc = crear_entry()
    txt_desc.pack(ipady=8, pady=5)

    # =====================================
    # PRECIO
    # =====================================
    crear_label("Precio").pack(anchor="w", padx=30, pady=(15, 5))

    txt_precio = crear_entry()
    txt_precio.pack(ipady=8, pady=5)

    # =====================================
    # CATEGORIA
    # =====================================
    crear_label("Categoría").pack(anchor="w", padx=30, pady=(15, 5))

    categorias = [
        "Playeras",
        "Pantalones",
        "Sudaderas",
        "Zapatos",
        "Accesorios"
    ]

    txt_categoria = ttk.Combobox(
        frame,
        values=categorias,
        font=("Arial", 11),
        state="readonly",
        width=28
    )

    txt_categoria.pack(ipady=5, pady=5)

    # =====================================
    # FUNCION GUARDAR
    # =====================================
    def guardar_producto():

        id_prod = txt_id.get().strip()
        descripcion = txt_desc.get().strip()
        precio = txt_precio.get().strip()
        categoria = txt_categoria.get().strip()

        # VALIDAR CAMPOS
        if (
            id_prod == "" or
            descripcion == "" or
            precio == "" or
            categoria == ""
        ):
            messagebox.showwarning(
                "Campos Vacíos",
                "Completa todos los campos."
            )
            return

        # VALIDAR PRECIO
        try:
            float(precio)
        except:
            messagebox.showerror(
                "Error",
                "El precio debe ser numérico."
            )
            return

        # GUARDAR
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        archivo = os.path.join(BASE_DIR, "productos.txt")

        with open(archivo, "a", encoding="utf-8") as f:
            f.write(
                f"{id_prod}|{descripcion}|{precio}|{categoria}\n"
            )

        messagebox.showinfo(
            "Guardado",
            "Producto registrado correctamente."
        )

        # LIMPIAR CAMPOS
        txt_id.delete(0, tk.END)
        txt_desc.delete(0, tk.END)
        txt_precio.delete(0, tk.END)
        txt_categoria.set("")

    # =====================================
    # BOTONES
    # =====================================
    frame_botones = tk.Frame(frame, bg="white")
    frame_botones.pack(pady=35)

    btn_guardar = tk.Button(
        frame_botones,
        text="Guardar Producto",
        command=guardar_producto,
        bg="#1b1c72",
        fg="white",
        activebackground="#283593",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        font=("Arial", 11, "bold"),
        width=18,
        height=2
    )

    btn_guardar.grid(row=0, column=0, padx=10)

    # BOTON LIMPIAR
    def limpiar():
        txt_id.delete(0, tk.END)
        txt_desc.delete(0, tk.END)
        txt_precio.delete(0, tk.END)
        txt_categoria.set("")

    btn_limpiar = tk.Button(
        frame_botones,
        text="Limpiar",
        command=limpiar,
        bg="#e53935",
        fg="white",
        activebackground="#c62828",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        font=("Arial", 11, "bold"),
        width=12,
        height=2
    )

    btn_limpiar.grid(row=0, column=1, padx=10)

# =========================================
# OTRAS FUNCIONES
# =========================================
def abrir_registro_ventas():
    messagebox.showinfo(
        "Registro de Ventas",
        "Aquí irá el módulo de ventas."
    )

def abrir_reportes():
    messagebox.showinfo(
        "Reportes",
        "Aquí irán los reportes."
    )

def abrir_acerca_de():
    messagebox.showinfo(
        "Acerca de",
        "Sistema POS ELEVENTA\nVersión 1.0"
    )

# =========================================
# VENTANA PRINCIPAL
# =========================================
ventana = tk.Tk()
ventana.title("Punto de Venta - ELEVENTA")
ventana.geometry("500x650")
ventana.configure(bg="white")
ventana.resizable(False, False)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# =========================================
# LOGO
# =========================================
try:
    logo = Image.open(os.path.join(BASE_DIR, "logo.png"))
    logo = logo.resize((180, 180))

    img_logo = ImageTk.PhotoImage(logo)

    lbl_logo = tk.Label(
        ventana,
        image=img_logo,
        bg="white"
    )

    lbl_logo.pack(pady=20)

except:
    tk.Label(
        ventana,
        text="LOGO",
        font=("Arial", 20),
        bg="white"
    ).pack(pady=20)

# =========================================
# TITULO
# =========================================
titulo = tk.Label(
    ventana,
    text="Sistema Punto de Venta",
    font=("Arial", 20, "bold"),
    bg="white",
    fg="#ff00f2"
)

titulo.pack(pady=10)

# =========================================
# FRAME BOTONES
# =========================================
frame = tk.Frame(ventana, bg="white")
frame.pack(pady=20)

# =========================================
# CREAR BOTON MODERNO
# =========================================
def crear_boton(texto, comando):

    btn = tk.Button(
        frame,
        text=texto,
        command=comando,
        font=("Arial", 12, "bold"),
        bg=
        "#aa1050",
        fg="white",
        activebackground="#F61DFD",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=25,
        height=2
    )

    btn.pack(pady=12)

    return btn

# =========================================
# BOTONES
# =========================================
crear_boton("🛒 Registro de Productos", abrir_registro_productos)
crear_boton("💳 Registro de Ventas", abrir_registro_ventas)
crear_boton("📊 Reportes", abrir_reportes)
crear_boton("ℹ️ Acerca de", abrir_acerca_de)

# =========================================
# FOOTER
# =========================================
footer = tk.Label(
    ventana,
    text="ELEVENTA POS © 2026",
    bg="white",
    fg="gray",
    font=("Arial", 10)
)

footer.pack(side="bottom", pady=15)

# =========================================
# INICIO
# =========================================
ventana.mainloop()