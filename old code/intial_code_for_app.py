import tkinter as tk
from tkinter import ttk, messagebox

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
        return f"{self.date} {self.time} - {self.service_type} for {self.pet.name} (Owner: {self.owner.name})"


# Main System
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

        # Notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        # Tabs
        self.customer_tab = ttk.Frame(self.notebook)
        self.pet_tab = ttk.Frame(self.notebook)
        self.appointment_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.customer_tab, text="Customers")
        self.notebook.add(self.pet_tab, text="Pets")
        self.notebook.add(self.appointment_tab, text="Appointments")

        self.setup_customer_tab()
        self.setup_pet_tab()
        self.setup_appointment_tab()

    def setup_customer_tab(self):
        # Customer Form
        tk.Label(self.customer_tab, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.customer_tab, text="Contact:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.customer_tab, text="Address:").grid(row=2, column=0, padx=5, pady=5)

        self.customer_name = tk.Entry(self.customer_tab)
        self.customer_contact = tk.Entry(self.customer_tab)
        self.customer_address = tk.Entry(self.customer_tab)

        self.customer_name.grid(row=0, column=1, padx=5, pady=5)
        self.customer_contact.grid(row=1, column=1, padx=5, pady=5)
        self.customer_address.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(self.customer_tab, text="Add Customer", command=self.add_customer).grid(row=3, column=0, columnspan=2, pady=10)

        # Customer List
        self.customer_list = tk.Listbox(self.customer_tab, width=50)
        self.customer_list.grid(row=4, column=0, columnspan=2, pady=10)

    def setup_pet_tab(self):
        # Pet Form
        tk.Label(self.pet_tab, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.pet_tab, text="Breed:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.pet_tab, text="Age:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(self.pet_tab, text="Notes:").grid(row=3, column=0, padx=5, pady=5)
        tk.Label(self.pet_tab, text="Owner:").grid(row=4, column=0, padx=5, pady=5)

        self.pet_name = tk.Entry(self.pet_tab)
        self.pet_breed = tk.Entry(self.pet_tab)
        self.pet_age = tk.Entry(self.pet_tab)
        self.pet_notes = tk.Entry(self.pet_tab)
        self.pet_owner = tk.Entry(self.pet_tab)

        self.pet_name.grid(row=0, column=1, padx=5, pady=5)
        self.pet_breed.grid(row=1, column=1, padx=5, pady=5)
        self.pet_age.grid(row=2, column=1, padx=5, pady=5)
        self.pet_notes.grid(row=3, column=1, padx=5, pady=5)
        self.pet_owner.grid(row=4, column=1, padx=5, pady=5)

        tk.Button(self.pet_tab, text="Add Pet", command=self.add_pet).grid(row=5, column=0, columnspan=2, pady=10)

        # Pet List
        self.pet_list = tk.Listbox(self.pet_tab, width=50)
        self.pet_list.grid(row=6, column=0, columnspan=2, pady=10)

    def setup_appointment_tab(self):
        # Appointment Form
        tk.Label(self.appointment_tab, text="Date:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.appointment_tab, text="Time:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.appointment_tab, text="Service Type:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(self.appointment_tab, text="Pet Name:").grid(row=3, column=0, padx=5, pady=5)

        self.app_date = tk.Entry(self.appointment_tab)
        self.app_time = tk.Entry(self.appointment_tab)
        self.app_service = tk.Entry(self.appointment_tab)
        self.app_pet_name = tk.Entry(self.appointment_tab)

        self.app_date.grid(row=0, column=1, padx=5, pady=5)
        self.app_time.grid(row=1, column=1, padx=5, pady=5)
        self.app_service.grid(row=2, column=1, padx=5, pady=5)
        self.app_pet_name.grid(row=3, column=1, padx=5, pady=5)

        tk.Button(self.appointment_tab, text="Add Appointment", command=self.add_appointment).grid(row=4, column=0, columnspan=2, pady=10)

        # Appointment List
        self.appointment_list = tk.Listbox(self.appointment_tab, width=50)
        self.appointment_list.grid(row=5, column=0, columnspan=2, pady=10)

    def add_customer(self):
        name = self.customer_name.get()
        contact = self.customer_contact.get()
        address = self.customer_address.get()

        if name and contact and address:
            customer = self.system.add_customer(name, contact, address)
            self.customer_list.insert(tk.END, str(customer))
            self.customer_name.delete(0, tk.END)
            self.customer_contact.delete(0, tk.END)
            self.customer_address.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def add_pet(self):
        name = self.pet_name.get()
        breed = self.pet_breed.get()
        age = self.pet_age.get()
        notes = self.pet_notes.get()
        owner_name = self.pet_owner.get()

        if name and breed and age and owner_name:
            pet = self.system.add_pet(name, breed, age, notes, owner_name)
            if pet:
                self.pet_list.insert(tk.END, str(pet))
                self.pet_name.delete(0, tk.END)
                self.pet_breed.delete(0, tk.END)
                self.pet_age.delete(0, tk.END)
                self.pet_notes.delete(0, tk.END)
                self.pet_owner.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Owner not found. Add the owner first.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def add_appointment(self):
        date = self.app_date.get()
        time = self.app_time.get()
        service_type = self.app_service.get()
        pet_name = self.app_pet_name.get()

        if date and time and service_type and pet_name:
            appointment = self.system.schedule_appointment(date, time, service_type, pet_name)
            if appointment:
                self.appointment_list.insert(tk.END, str(appointment))
                self.app_date.delete(0, tk.END)
                self.app_time.delete(0, tk.END)
                self.app_service.delete(0, tk.END)
                self.app_pet_name.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Pet not found. Add the pet first.")
        else:
            messagebox.showerror("Error", "All fields are required.")


# Run the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = CanineCloud9App(root)
    root.mainloop()
