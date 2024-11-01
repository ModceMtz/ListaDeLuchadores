import tkinter as tk
from tkinter import ttk, messagebox

class TableView:
    def __init__(self, parent):
        self.table = ttk.Treeview(parent, columns=("ID", "LUCHADOR", "Nombre", "Apellido", "Ciudad"), show="headings")
        for col in ("ID", "LUCHADOR", "Nombre", "Apellido", "Ciudad"):
            self.table.heading(col, text=col)


        scrollbar_y = ttk.Scrollbar(parent, orient="vertical", command=self.table.yview)
        scrollbar_x = ttk.Scrollbar(parent, orient="horizontal", command=self.table.xview)
        self.table.configure(yscroll=scrollbar_y.set, xscroll=scrollbar_x.set)


        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.table.pack(fill=tk.BOTH, expand=True)

    def load_data(self, data):
        """Carga los datos en la tabla."""
        self.clear_table()
        for record in data:
            self.table.insert("", "end", values=(record["id"], record["LUCHADOR"], record["Nombre"], record["Apellido"], record["Ciudad"]))

    def show_record(self, record):
        """Muestra un registro específico en la tabla."""
        self.clear_table()
        if record:
            self.table.insert("", "end", values=(record["id"], record["LUCHADOR"], record["Nombre"], record["Apellido"], record["Ciudad"]))
        else:
            messagebox.showinfo("Información", "Registro no encontrado.")

    def clear_table(self):
        """Limpia la tabla."""
        for row in self.table.get_children():
            self.table.delete(row)
