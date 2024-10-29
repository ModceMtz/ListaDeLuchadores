import tkinter as tk
from tkinter import ttk, messagebox
from api_manager import APIManager

class DataDisplay:
    def __init__(self, root, api_url):
        self.api_manager = APIManager(api_url)
        self.root = root
        self.setup_ui()
        self.load_combobox()

    def setup_ui(self):
        """Configurar la interfaz de usuario."""
        self.root.title("Registro de Luchadores")
        self.root.resizable(False, False)

        self.combo = ttk.Combobox(self.root, state="readonly")
        self.combo.pack(pady=10)
        self.combo.bind("<<ComboboxSelected>>", self.display_selected_data)

        self.count_label = tk.Label(self.root, text="Número de Registros: 0")
        self.count_label.pack(pady=5)

        self.btn_show_all = tk.Button(self.root, text="Mostrar Todos los Registros", command=self.display_all_data)
        self.btn_show_all.pack(pady=5)

        self.columns = ("ID", "Luchador", "Apellido", "Ciudad", "Calle")
        self.tree = ttk.Treeview(self.root, columns=self.columns, show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Luchador", text="Luchador")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.heading("Ciudad", text="Ciudad")
        self.tree.heading("Calle", text="Calle")

    def load_combobox(self):
        """Función para cargar los registros en el combobox y mostrar el conteo."""
        records = self.api_manager.fetch_data()

        self.combo['values'] = [f"{record['id']} - {record['Luchador']} {record['Apellido']}" for record in records]
        if records:
            self.combo.current(0)

        record_count = len(records)
        self.count_label.config(text=f"Número de Registros: {record_count}")

    def display_selected_data(self, event=None):
        """Función para mostrar el registro seleccionado en el combobox."""
        selected_index = self.combo.current()
        records = self.api_manager.fetch_data()

        if records:
            selected_record = records[selected_index]
            messagebox.showinfo("Registro Seleccionado",
                                f"ID: {selected_record['id']}\nLuchador: {selected_record['Luchador']}\nApellido: {selected_record['Apellido']}\nCiudad: {selected_record['Ciudad']}\nCalle: {selected_record['Calle']}")

    def display_all_data(self):
        """Función para mostrar todos los registros en la tabla."""
        records = self.api_manager.fetch_data()

        self.tree.pack(expand=True, fill=tk.BOTH)

        for row in self.tree.get_children():
            self.tree.delete(row)

        for record in records:
            self.tree.insert("", tk.END, values=(
            record['id'], record['Luchador'], record['Apellido'], record['Ciudad'], record['Calle']))
