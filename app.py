import tkinter as tk
from data_display import DataDisplay

API_URL = "https://671be4172c842d92c381a4aa.mockapi.io/Test"

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.data_display = DataDisplay(self.root, API_URL)
        self.root.mainloop()

if __name__ == "__main__":
    App()
