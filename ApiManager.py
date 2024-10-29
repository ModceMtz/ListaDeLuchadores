import requests
from tkinter import messagebox

class APIManager:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        """Función para obtener los registros de la API."""
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"No se pudo obtener datos: {e}")
            return []
