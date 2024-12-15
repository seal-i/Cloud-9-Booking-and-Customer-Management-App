import tkinter as tk  # Correct Import
from tkinter import ttk
from views import CustomerView, PetView, AppointmentView
from database import DatabaseManager
from settings import DATABASE_PATH, APP_TITLE

# Apply Global Style
def apply_style(root):
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("TButton", font=("Arial", 12), padding=5)
    style.configure("Hover.TButton", background="#000000", foreground="white")
    style.configure("TLabel", font=("Arial", 12), padding=5)
    style.configure("TEntry", font=("Arial", 12), padding=5)
    style.configure("Treeview.Heading", font=("Arial Bold", 12))
    style.configure("Treeview", rowheight=25, font=("Arial", 11))


class CanineCloud9App:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.db = DatabaseManager(DATABASE_PATH)

        # Apply Global Theme
        apply_style(self.root)

        # Create Menu Bar
        self.menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=self.menu_bar)

        # Create Notebook for Tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Create Tabs
        self.customer_tab = CustomerView(self.notebook, self.db)
        self.pet_tab = PetView(self.notebook, self.db)
        self.appointment_tab = AppointmentView(self.notebook, self.db)

        # Add Tabs to Notebook
        self.notebook.add(self.customer_tab.frame, text="Customers")
        self.notebook.add(self.pet_tab.frame, text="Pets")
        self.notebook.add(self.appointment_tab.frame, text="Appointments")


# Run the App
if __name__ == "__main__":
    root = tk.Tk()  # Correctly Defined Tkinter Root
    app = CanineCloud9App(root)
    root.mainloop()
