import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AppointmentView:
    def __init__(self, parent, db):
        self.db = db
        self.frame = ttk.Frame(parent)
        self.setup_appointment_tab()

    def setup_appointment_tab(self):
        # Labels
        ttk.Label(self.frame, text="Date:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.frame, text="Time (HH:MM):").grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(self.frame, text="Service Type:").grid(row=2, column=0, padx=5, pady=5)
        ttk.Label(self.frame, text="Pet Name:").grid(row=3, column=0, padx=5, pady=5)
        ttk.Label(self.frame, text="Owner Name:").grid(row=4, column=0, padx=5, pady=5)

        # Entry Fields
        self.date_entry = DateEntry(self.frame, width=20, background="darkblue", foreground="white", borderwidth=2)
        self.time_entry = ttk.Entry(self.frame)
        self.service_entry = ttk.Entry(self.frame)
        self.pet_name_entry = ttk.Entry(self.frame)
        self.owner_name_entry = ttk.Entry(self.frame)

        self.date_entry.grid(row=0, column=1, padx=5, pady=5)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)
        self.service_entry.grid(row=2, column=1, padx=5, pady=5)
        self.pet_name_entry.grid(row=3, column=1, padx=5, pady=5)
        self.owner_name_entry.grid(row=4, column=1, padx=5, pady=5)

        # Add Appointment Button
        ttk.Button(
            self.frame, text="Add Appointment", command=self.add_appointment
        ).grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")

        # Appointment Listbox
        self.appointment_listbox = tk.Listbox(self.frame, width=60)
        self.appointment_listbox.grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")

        # Populate the List on Load
        self.refresh_appointment_list()

    def add_appointment(self):
        # Collect Data
        date = self.date_entry.get().strip()
        time = self.time_entry.get().strip()
        service_type = self.service_entry.get().strip()
        pet_name = self.pet_name_entry.get().strip()
        owner_name = self.owner_name_entry.get().strip()

        # Validate Data
        pet = next((p for p in self.db.get_all_pets() if p.name == pet_name), None)
        owner = next((o for o in self.db.get_all_customers() if o.name == owner_name), None)

        if not (date and time and service_type and pet and owner):
            messagebox.showerror("Error", "All fields are required and must match existing records.")
            return

        # Add Appointment to Database
        success = self.db.add_appointment(date, time, service_type, pet.pet_id, owner.customer_id)
        if success:
            messagebox.showinfo("Success", "Appointment added successfully!")
            self.refresh_appointment_list()
        else:
            messagebox.showerror("Error", "Failed to add appointment.")

    def refresh_appointment_list(self):
        self.appointment_listbox.delete(0, tk.END)
        appointments = self.db.get_all_appointments()

        for appointment in appointments:
            app_info = (
                f"{appointment.date} | {appointment.time} | "
                f"{appointment.service} | Pet ID: {appointment.pet_id} | Owner ID: {appointment.owner_id}"
            )
            self.appointment_listbox.insert(tk.END, app_info)
