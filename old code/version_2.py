import tkinter as tk
from tkinter import ttk, messagebox

import tkinter as tk
from tkinter import ttk, messagebox

# Apply Custom Styles
def apply_styles():
    style = ttk.Style()
    style.theme_use("clam")

    # Frame Styles
    style.configure("TFrame",
                    background="#ADD8E5")

    # Label Styles
    style.configure("TLabel",
                    background="#ADD8E5",
                    font=("Helvetica", 12, "bold"))

    # Entry Styles
    style.configure("TEntry",
                    padding=5,
                    font=("Helvetica", 12))
   
# Class Definitions
class Customer:
    def __init__(self, name, contact, address):
        self.name = name
        self.contact = contact
        self.address = address

    def __str__(self):
        return f"{self.name} - {self.contact} - {self.address}"


class Pet:
    def __init__(self, name, breed, age, notes, owner):
        self.name = name
        self.breed = breed
        self.age = age
        self.notes = notes
        self.owner = owner

    def __str__(self):
        return f"{self.name} ({self.breed}, {self.age} years) - {self.owner.name}"


class Appointment:
    def __init__(self, date, time, service_type, pet, owner):
        self.date = date
        self.time = time
        self.service_type = service_type
        self.pet = pet
        self.owner = owner
        self.status = "Scheduled"

    def __str__(self):
        return (f"{self.date} {self.time} - {self.service_type} for {self.pet.name} "
                f"(Owner: {self.owner.name}) - Status: {self.status}")


# Main System Class
class CanineCloud9System:
    def __init__(self):
        self.customers = []
        self.pets = []
        self.appointments = []


    def add_customer(self, name, contact, address):
        customer = Customer(name, contact, address)
        self.customers.append(customer)
        return customer

    def add_pet(self, name, breed, age, notes, owner_name):
        owner = next((c for c in self.customers if c.name == owner_name), None)
        if owner:
            pet = Pet(name, breed, age, notes, owner)
            self.pets.append(pet)
            return pet
        return None

    def schedule_appointment(self, date, time, service_type, pet_name):
        pet = next((p for p in self.pets if p.name == pet_name), None)
        if pet:
            appointment = Appointment(date, time, service_type, pet, pet.owner)
            self.appointments.append(appointment)
            return appointment
        return None


# GUI Implementation
class CanineCloud9App:
    def __init__(self, root):
        self.system = CanineCloud9System()
        self.root = root
        self.root.title("Canine Cloud 9 Management System")

        apply_styles()

        # Notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        # Tabs
        self.customer_tab = ttk.Frame(self.notebook)
        self.customer_tab.pack(fill="both", expand=True)

        self.pet_tab = ttk.Frame(self.notebook)
        self.pet_tab.pack(fill="both", expand=True)

    
        self.appointment_tab = ttk.Frame(self.notebook)
        self.appointment_tab.pack(fill="both", expand=True)

        self.notebook.add(self.customer_tab, text="Customers")
        self.notebook.add(self.pet_tab, text="Pets")
        self.notebook.add(self.appointment_tab, text="Appointments")

        self.setup_customer_tab()
        self.setup_pet_tab()
        self.setup_appointment_tab()

    def setup_customer_tab(self):
        tk.Label(self.customer_tab, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.customer_tab, text="Contact:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.customer_tab, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        # Use tk.Button for Custom Button
        self.add_button = tk.Button(
            self.customer_tab, text="Add Customer",
            bg="#FF0000", fg="white",
            font=("Helvetica", 12, "bold"), command=self.add_customer
        )
        self.add_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.customer_name = tk.Entry(self.customer_tab)
        self.customer_contact = tk.Entry(self.customer_tab)
        self.customer_address = tk.Entry(self.customer_tab)

        self.customer_name.grid(row=0, column=1, padx=5, pady=5)
        self.customer_contact.grid(row=1, column=1, padx=5, pady=5)
        self.customer_address.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(self.customer_tab, text="Add Customer", command=self.add_customer).grid(row=3, column=0, columnspan=2, pady=10)
        self.customer_list = tk.Listbox(self.customer_tab, width=50)
        self.customer_list.grid(row=4, column=0, columnspan=2, pady=10)

    def add_customer(self):
        name = self.customer_name.get()
        contact = self.customer_contact.get()
        address = self.customer_address.get()

        if name and contact and address:
            self.system.add_customer(name, contact, address)
            self.refresh_customer_list()
        else:
            messagebox.showerror("Error", "All fields are required.")

    def refresh_customer_list(self):
        self.customer_list.delete(0, tk.END)
        for customer in self.system.customers:
            self.customer_list.insert(tk.END, str(customer))

    def setup_pet_tab(self):
        tk.Label(self.pet_tab, text="Pet Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.pet_tab, text="Breed:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.pet_tab, text="Age:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(self.pet_tab, text="Notes:").grid(row=3, column=0, padx=5, pady=5)
        tk.Label(self.pet_tab, text="Owner Name:").grid(row=4, column=0, padx=5, pady=5)

        self.pet_name = tk.Entry(self.pet_tab)
        self.pet_breed = tk.Entry(self.pet_tab)
        self.pet_age = tk.Entry(self.pet_tab)
        self.pet_notes = tk.Entry(self.pet_tab)
        self.pet_owner_name = tk.Entry(self.pet_tab)

        self.pet_name.grid(row=0, column=1, padx=5, pady=5)
        self.pet_breed.grid(row=1, column=1, padx=5, pady=5)
        self.pet_age.grid(row=2, column=1, padx=5, pady=5)
        self.pet_notes.grid(row=3, column=1, padx=5, pady=5)
        self.pet_owner_name.grid(row=4, column=1, padx=5, pady=5)

        tk.Button(self.pet_tab, text="Add Pet", command=self.add_pet).grid(row=5, column=0, columnspan=2, pady=10)
        self.pet_list = tk.Listbox(self.pet_tab, width=50)
        self.pet_list.grid(row=6, column=0, columnspan=2, pady=10)

    def add_pet(self):
        name = self.pet_name.get()
        breed = self.pet_breed.get()
        age = self.pet_age.get()
        notes = self.pet_notes.get()
        owner_name = self.pet_owner_name.get()

        if name and breed and age and owner_name:
            pet = self.system.add_pet(name, breed, age, notes, owner_name)
            if pet:
                self.refresh_pet_list()
            else:
                messagebox.showerror("Error", "Owner not found.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def refresh_pet_list(self):
        self.pet_list.delete(0, tk.END)
        for pet in self.system.pets:
            self.pet_list.insert(tk.END, str(pet))
    def setup_appointment_tab(self):
        tk.Label(self.appointment_tab, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.appointment_tab, text="Time (HH:MM):").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.appointment_tab, text="Service Type:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(self.appointment_tab, text="Pet Name:").grid(row=3, column=0, padx=5, pady=5)

        self.appointment_date = tk.Entry(self.appointment_tab)
        self.appointment_time = tk.Entry(self.appointment_tab)
        self.appointment_service_type = tk.Entry(self.appointment_tab)
        self.appointment_pet_name = tk.Entry(self.appointment_tab)

        self.appointment_date.grid(row=0, column=1, padx=5, pady=5)
        self.appointment_time.grid(row=1, column=1, padx=5, pady=5)
        self.appointment_service_type.grid(row=2, column=1, padx=5, pady=5)
        self.appointment_pet_name.grid(row=3, column=1, padx=5, pady=5)

        tk.Button(self.appointment_tab, text="Schedule Appointment", command=self.add_appointment).grid(row=4, column=0, columnspan=2, pady=10)

        self.appointment_list = tk.Listbox(self.appointment_tab, width=50)
        self.appointment_list.grid(row=5, column=0, columnspan=2, pady=10)
    def add_appointment(self):
        date = self.appointment_date.get()
        time = self.appointment_time.get()
        service_type = self.appointment_service_type.get()
        pet_name = self.appointment_pet_name.get()

        if date and time and service_type and pet_name:
            appointment = self.system.schedule_appointment(date, time, service_type, pet_name)
            if appointment:
                self.refresh_appointment_list()
            else:
                messagebox.showerror("Error", "Pet not found.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def refresh_appointment_list(self):
        self.appointment_list.delete(0, tk.END)
        for appointment in self.system.appointments:
            self.appointment_list.insert(tk.END, str(appointment))


     


# Run the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = CanineCloud9App(root)
    root.mainloop()
