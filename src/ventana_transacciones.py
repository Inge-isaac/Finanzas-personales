import tkinter as tk
from tkinter import messagebox, ttk as tkk
import pyodbc
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from data.conexion import get_db_connection
from utils.center_windows import center_window as cw


class VentanaRegistrarTransaccion(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master)

        self.title("Registrar Transaccion")
        cw(self, 400, 500)
        self.config(bg="lightsteelblue")
        self.grab_set()

        self.conn_str = get_db_connection()

        self.crear_widgets()

    # =============================
    # CREAR INTERFAZ
    # =============================
    def crear_widgets(self):

        tk.Label(self, bg="steelblue", fg="white", font=("Arial", 12),
                 text="Id de la Cuenta:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_account = tk.Entry(self)
        self.entry_account.grid(row=0, column=1, pady=5, sticky="w")

        tk.Label(self, bg="steelblue", fg="white", font=("Arial", 12),
                 text="Registro de monto:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_amount = tk.Entry(self)
        self.entry_amount.grid(row=1, column=1, pady=5, sticky="w")

        tk.Label(self, bg="steelblue", fg="white", font=("Arial", 12),
                 text="Fecha de transacción:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.entry_transaction = tk.Entry(self)
        self.entry_transaction.grid(row=2, column=1, pady=5, sticky="w")

        tk.Label(self, bg="steelblue", fg="white", font=("Arial", 12),
                 text="Descripción:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.entry_description = tk.Entry(self)
        self.entry_description.grid(row=3, column=1, pady=5, sticky="w")

        tk.Label(self, bg="steelblue", fg="white", font=("Arial", 12),
                 text="Categoría:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.entry_category = tk.Entry(self)
        self.entry_category.grid(row=4, column=1, pady=5, sticky="w")

        tk.Label(self, bg="steelblue", fg="white", font=("Arial", 12),
                 text="Fecha creación:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
        self.entry_created = tk.Entry(self)
        self.entry_created.grid(row=5, column=1, pady=5, sticky="w")

        tk.Button(self, text="Registrar Transacción",
                  command=self.registrar_ingreso).grid(row=6, column=0, columnspan=2, pady=10)

        tk.Button(self, text="Actualizar Lista",
                  command=self.mostrar_registros).grid(row=7, column=0, pady=5)

        tk.Button(self, text="Ver Gráfico",
                  command=self.ventana_grafico).grid(row=7, column=1, pady=5)

        # ===== TABLA =====
        frame_tabla = tk.Frame(self)
        frame_tabla.grid(row=8, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        # ==== PERMITIR EXPANCION ====
        self.grid_rowconfigure(8, weight=1)
        self.grid_columnconfigure(1, weight=1)

        scroll_y = tk.Scrollbar(frame_tabla, orient="vertical")
        scroll_y.pack(side="right", fill="y")
        
        # ==== Scrollbar horizontal (opcional)
        scroll_x = tk.Scrollbar(frame_tabla, orient="horizontal")
        scroll_x.pack(side="bottom", fill="x")

        self.tabla = tkk.Treeview(
            frame_tabla,
            columns=("ID_Acount", "Monto", "Fecha", "Descripción", "Categoría", "Creado"),
            show="headings",
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        self.tabla.heading("ID_Acount", text="ID Cuenta")
        self.tabla.heading("Monto", text="Monto")
        self.tabla.heading("Fecha", text="Fecha")
        self.tabla.heading("Descripción", text="Descripción")
        self.tabla.heading("Categoría", text="Categoría")
        self.tabla.heading("Creado", text="Fecha Creación")
        
        self.tabla.column("ID_Acount", width=60, stretch=False)
        self.tabla.column("Monto", width=80, stretch=False)
        self.tabla.column("Fecha", width=120, stretch=False)
        self.tabla.column("Descripción", width=150, stretch=False)
        self.tabla.column("Categoría", width=100, stretch=False)
        self.tabla.column("Creado", width=120, stretch=False)
       
        self.tabla["displaycolumns"] = (
        "ID_Acount", "Monto", "Fecha",
        "Descripción", "Categoría", "Creado"
)

        self.tabla.pack(fill="both", expand=True)
        
        scroll_y.config(command=self.tabla.yview)
        scroll_x.config(command=self.tabla.xview)

    # =============================
    # REGISTRAR
    # =============================
    def registrar_ingreso(self):

        datos = (
            self.entry_account.get(),
            self.entry_amount.get(),
            self.entry_transaction.get(),
            self.entry_description.get(),
            self.entry_category.get(),
            self.entry_created.get()
        )

        if not all(datos):
            messagebox.showerror("Error", "Complete todos los campos")
            return

        try:
            conn = pyodbc.connect(self.conn_str, timeout=5)
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO transactions
                (account_id, amount, transaction_date, description, category, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, datos)

            conn.commit()
            messagebox.showinfo("Éxito", "Ingreso registrado")

            self.limpiar_campos()
            self.mostrar_registros()

        except Exception as e:
            messagebox.showerror("Error", str(e))

        finally:
            conn.close()

    # =============================
    def limpiar_campos(self):
        self.entry_account.delete(0, tk.END)
        self.entry_amount.delete(0, tk.END)
        self.entry_transaction.delete(0, tk.END)
        self.entry_description.delete(0, tk.END)
        self.entry_category.delete(0, tk.END)
        self.entry_created.delete(0, tk.END)

    # =============================
    # CONSULTAR
    # =============================
    def mostrar_registros(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        try:
            conn = pyodbc.connect(self.conn_str, timeout=5)
            cursor = conn.cursor()

            cursor.execute("SELECT account_id, amount, transaction_date, description, category, created_at FROM transactions")
            filas = cursor.fetchall()

            for f in filas:
                item = self.tabla.insert("", "end", values=(f[0], f[1], f[2], f[3], f[4], f[5]))

                if f[1] < 0:
                    self.tabla.item(self.tabla.get_children()[-1], tags=("negativo",))
                else:
                    self.tabla.item(item, tags=("positivo",))

            self.tabla.tag_configure("negativo", foreground="orangered")
            self.tabla.tag_configure("positivo", foreground="limegreen")

        except Exception as e:
            print(e)
        finally:
            conn.close()

    # =============================
    # GRAFICO
    # =============================
    def ventana_grafico(self):

        conn = pyodbc.connect(self.conn_str)
        df = pd.read_sql("SELECT amount, category FROM transactions", conn)
        conn.close()

        top = tk.Toplevel(self)
        top.title("Gráfico")

        fig = Figure(figsize=(7, 4))
        ax = fig.add_subplot(111)
        ax.bar(df["category"], df["amount"])

        canvas = FigureCanvasTkAgg(fig, master=top)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
