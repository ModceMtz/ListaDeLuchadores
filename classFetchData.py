import requests
from tkinter import messagebox

class FetchData:
    __URL = "https://671be4172c842d92c381a4aa.mockapi.io/Test"

    def fetch_data(self):
        """Obtiene los datos desde la API."""
        try:
            response = requests.get(self.__URL)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            messagebox.showerror("Error", f"No se pudo conectar al servidor: {e}")
            return []

    def fetch_data_by_id(self, record_id):
        """Obtiene un registro específico por ID."""
        data = self.fetch_data()
        return next((record for record in data if record["id"] == record_id), None)
