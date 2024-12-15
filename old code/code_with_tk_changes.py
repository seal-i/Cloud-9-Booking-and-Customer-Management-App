# Improved Pet Grooming Management System with Tkinter
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Apply Custom Styles
def apply_styles():
    style = ttk.Style()
    style.theme_use("clam")

    # Frame Styles
    style.configure("TFrame", background="#ADD8E5")

    # Label Styles
    style.configure("TLabel", background="#ADD8E5", font=("Helvetica", 12, "bold"))

    # Entry Styles
    style.configure("TEntry", padding=5, font=("Helvetica", 12))

    # Button Styles
    style.configure("Red.TButton", background="#FF0000", foreground="white", font=("Helvetica", 12, "bold"))

# Database Setup
def setup_database():
    conn = sqlite3.connect("canine_cloud9.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        contact TEXT NOT NULL,
        address TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        breed TEXT NOT NULL,
        age INTEGER NOT NULL,
        notes TEXT,
        owner_id INTEGER NOT NULL,
        FOREIGN KEY (owner_id) REFERENCES customers (id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        service_type TEXT NOT NULL,
        pet_id INTEGER NOT NULL,
        owner_id INTEGER NOT NULL,
        status TEXT DEFAULT "Scheduled",
        FOREIGN KEY (pet_id) REFERENCES pets (id),
        FOREIGN KEY (owner_id) REFERENCES customers (id)
    )''')
    conn.commit()
    conn.close()

# Main System Class
class CanineCloud9App:
    def __init__(self, root):
        self.root = root
        self.root.title("Canine Cloud 9 Management System")
        apply_styles()
        setup_database()

        # Notebook for Tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        # Tabs
        self.customer_tab = ttk.Frame(self.notebook, style="TFrame")
        self.pet_tab = ttk.Frame(self.notebook, style="TFrame")
        self.appointment_tab = ttk.Frame(self.notebook, style="TFrame")
        self.notebook.add(self.customer_tab, text="Customers")
        self.notebook.add(self.pet_tab, text="Pets")
        self.notebook.add(self.appointment_tab, text="Appointments")

        # Setup Tabs
        self.setup_customer_tab()
        self.setup_pet_tab()
        self.setup_appointment_tab()

    def clear_entries(self, *entries):
        for entry in entries:
            entry.delete(0, tk.END)

    def setup_customer_tab(self):
        ttk.Label(self.customer_tab, text="Name:", style="TLabel").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.customer_tab, text="Contact:", style="TLabel").grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(self.customer_tab, text="Address:", style="TLabel").grid(row=2, column=0, padx=5, pady=5)

        self.customer_name = ttk.Entry(self.customer_tab, style="TEntry")
        self.customer_contact = ttk.Entry(self.customer_tab, style="TEntry")
        self.customer_address = ttk.Entry(self.customer_tab, style="TEntry")

        self.customer_name.grid(row=0, column=1, padx=5, pady=5)
        self.customer_contact.grid(row=1, column=1, padx=5, pady=5)
        self.customer_address.grid(row=2, column=1, padx=5, pady=5)

        self.add_customer_button = ttk.Button(
            self.customer_tab, text="Add Customer", style="Red.TButton", command=self.add_customer
        )
        self.add_customer_button.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

        self.customer_list = tk.Listbox(self.customer_tab, width=60)
        self.customer_scroll = tk.Scrollbar(self.customer_tab, command=self.customer_list.yview)
        self.customer_list.config(yscrollcommand=self.customer_scroll.set)

        self.customer_list.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")
        self.customer_scroll.grid(row=4, column=2, sticky="ns")

    def add_customer(self):
        name = self.customer_name.get().strip()
        contact = self.customer_contact.get().strip()
        address = self.customer_address.get().strip()

        if not (name and contact and address):
            messagebox.showerror("Error", "All fields are required.")
            return

        conn = sqlite3.connect("canine_cloud9.db")
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO customers (name, contact, address) VALUES (?, ?, ?)", (name, contact, address)
            )
            conn.commit()
            messagebox.showinfo("Success", "Customer added successfully!")
            self.refresh_customer_list()
            self.clear_entries(self.customer_name, self.customer_contact, self.customer_address)
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Customer already exists.")
        conn.close()

    def refresh_customer_list(self):
        self.customer_list.delete(0, tk.END)
        conn = sqlite3.connect("canine_cloud9.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers")
        for row in cursor.fetchall():
            self.customer_list.insert(tk.END, f"{row[1]} - {row[2]} - {row[3]}")
        conn.close()

    def add_pet(self):
        pet_name = self.pet_name.get().strip()
        pet_breed = self.pet_breed.get().strip()
        pet_age = self.pet_age.get().strip()
        pet_notes = self.pet_notes.get().strip()
        owner_name = self.pet_owner_name.get().strip()

        if not (pet_name and pet_breed and pet_age and owner_name):
            messagebox.showerror("Error", "All fields except notes are required.")
            return

        conn = sqlite3.connect("canine_cloud9.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM customers WHERE name = ?", (owner_name,))
        owner = cursor.fetchone()

        if not owner:
            messagebox.showerror("Error", "Owner not found. Please add the owner first.")
            conn.close()
            return

        cursor.execute(
            "INSERT INTO pets (name, breed, age, notes, owner_id) VALUES (?, ?, ?, ?, ?)",
            (pet_name, pet_breed, pet_age, pet_notes, owner[0])
        )
        conn.commit()
        messagebox.showinfo("Success", "Pet added successfully!")
        self.clear_entries(self.pet_name, self.pet_breed, self.pet_age, self.pet_notes, self.pet_owner_name)
        conn.close()

# Run the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = CanineCloud9App(root)
    root.mainloop()
