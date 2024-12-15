import tkinter as tk
from tkinter import ttk, messagebox


# Class Definitions (unchanged)
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

    def search_customers(self, keyword):
        return [customer for customer in self.customers if keyword.lower() in customer.name.lower()]

    def search_pets(self, keyword):
        return [pet for pet in self.pets if keyword.lower() in pet.name.lower()]

    def search_appointments(self, keyword):
        return [appt for appt in self.appointments if keyword.lower() in appt.pet.name.lower()]

    def update_appointment_status(self, pet_name, status):
        appointment = next((appt for appt in self.appointments if appt.pet.name == pet_name), None)
        if appointment:
            appointment.status = status
            return appointment
        return None


# GUI Implementation with Updates
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
        tk.Button(self.customer_tab, text="Search Customers", command=self.search_customers).grid(row=4, column=0, columnspan=2, pady=10)

        # Customer List
        self.customer_list = tk.Listbox(self.customer_tab, width=50)
        self.customer_list.grid(row=5, column=0, columnspan=2, pady=10)

    def setup_pet_tab(self):
        # Pet Form (unchanged)
        ...

    def setup_appointment_tab(self):
        # Appointment Form
        ...

    def add_customer(self):
        name = self.customer_name.get()
        contact = self.customer_contact.get()
        address = self.customer_address.get()

        if name and contact and address:
            customer = self.system.add_customer(name, contact, address)
            self.refresh_customer_list()
        else:
            messagebox.showerror("Error", "All fields are required.")

    def refresh_customer_list(self):
        self.customer_list.delete(0, tk.END)
        for customer in self.system.customers:
            self.customer_list.insert(tk.END, str(customer))

    def search_customers(self):
        keyword = self.customer_name.get()
        results = self.system.search_customers(keyword)
        self.customer_list.delete(0, tk.END)
        for customer in results:
            self.customer_list.insert(tk.END, str(customer))


# Run the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = CanineCloud9App(root)
    root.mainloop()
