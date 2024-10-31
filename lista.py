import tkinter as tk
from tkinter import ttk, messagebox
import requests

# URL del servidor Mockapi actualizada
URL = "https://671be4172c842d92c381a4aa.mockapi.io/Test"


# Función para obtener los datos desde la API
def fetch_data():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        messagebox.showerror("Error", f"No se pudo conectar al servidor: {e}")
        return []


# Función para cargar todos los datos en la tabla principal
def load_data():
    # Limpiar la tabla antes de cargar datos nuevos
    for row in table.get_children():
        table.delete(row)

    data = fetch_data()
    for record in data:
        table.insert("", "end",
                     values=(record["id"], record["Luchador"], record["Nombre"], record["Apellido"], record["Ciudad"]))


# Función para mostrar un registro específico por ID en la tabla principal
def show_record_by_id():
    record_id = entry_id.get().strip()
    if not record_id:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un ID válido.")
        return

    # Buscar el registro por ID en los datos obtenidos de la API
    data = fetch_data()
    selected_record = next((record for record in data if record["id"] == record_id), None)

    # Limpiar la tabla principal antes de mostrar solo el registro seleccionado
    for row in table.get_children():
        table.delete(row)

    if selected_record:
        # Insertar solo el registro seleccionado en la tabla principal
        table.insert("", "end", values=(
            selected_record["id"], selected_record["Luchador"],
            selected_record["Nombre"], selected_record["Apellido"], selected_record["Ciudad"]
        ))
    else:
        messagebox.showinfo("Información", f"No se encontró un registro con el ID {record_id}.")


# Configuración de la ventana principal
root = tk.Tk()
root.title("Aplicación de Luchadores")
root.geometry("600x500")
root.resizable(False, False)

# Frame para la tabla y los scrollbars
table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# Tabla para mostrar los registros
columns = ("ID", "Luchador", "Nombre", "Apellido", "Ciudad")
table = ttk.Treeview(table_frame, columns=columns, show="headings")
for col in columns:
    table.heading(col, text=col)

# Scrollbar vertical
scrollbar_y = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
table.configure(yscroll=scrollbar_y.set)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

# Scrollbar horizontal
scrollbar_x = ttk.Scrollbar(table_frame, orient="horizontal", command=table.xview)
table.configure(xscroll=scrollbar_x.set)
scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

table.pack(fill=tk.BOTH, expand=True)

# Campo de entrada y botón para seleccionar el registro por ID
frame_select = tk.Frame(root)
frame_select.pack(pady=10)

label_id = tk.Label(frame_select, text="Ingresa el ID del registro:")
label_id.pack(side=tk.LEFT, padx=5)

entry_id = tk.Entry(frame_select)
entry_id.pack(side=tk.LEFT, padx=5)

select_button = tk.Button(frame_select, text="Mostrar registro", command=show_record_by_id)
select_button.pack(side=tk.LEFT, padx=5)

# Botones para cargar todos los registros y actualizar la tabla
load_button = tk.Button(root, text="Cargar todos los registros", command=load_data)
load_button.pack(pady=5)

update_button = tk.Button(root, text="Actualizar tabla", command=load_data)
update_button.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()

