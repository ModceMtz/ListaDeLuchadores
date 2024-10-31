import tkinter as tk
from tkinter import messagebox
from classFetchData import FetchData
from classTableView import TableView

class window:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Luchadores")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        # Inicializa FetchData
        self.fetch_data_client = FetchData()

        # Tabla
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        self.table_view = TableView(table_frame)

        # Campo de entrada y botones
        self.entry_id = tk.Entry(self.root)
        self.entry_id.pack(pady=10)

        self.select_button = tk.Button(self.root, text="Mostrar registro", command=self.show_record_by_id)
        self.select_button.pack(pady=5)

        self.load_button = tk.Button(self.root, text="Cargar todos los registros", command=self.load_data)
        self.load_button.pack(pady=5)

        self.load_button = tk.Button(self.root, text="Actualizar tabla", command=self.load_data)
        self.load_button.pack(pady=5)

    def load_data(self):
        """Carga todos los datos en la tabla."""
        data = self.fetch_data_client.fetch_data()
        self.table_view.load_data(data)

    def show_record_by_id(self):
        """Muestra un registro específico por ID."""
        record_id = self.entry_id.get().strip()
        if not record_id:
            messagebox.showwarning("Advertencia", "Por favor, ingresa un ID válido.")
            return

        record = self.fetch_data_client.fetch_data_by_id(record_id)
        self.table_view.show_record(record)


