import tkinter as tk
from tkinter import ttk, messagebox


class PetView:
    def __init__(self, parent, db):
        self.db = db
        self.frame = ttk.Frame(parent)
        self.setup_pet_tab()

    # Setup the pet tab
    def setup_pet_tab(self):
        # Labels
        ttk.Label(self.frame, text="Pet Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(self.frame, text="Breed:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(self.frame, text="Age:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(self.frame, text="Notes:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(self.frame, text="Owner Name:").grid(row=4, column=0, padx=5, pady=5, sticky="w")

        # Entry Fields
        self.pet_name_entry = ttk.Entry(self.frame, width=30)
        self.pet_breed_entry = ttk.Entry(self.frame, width=30)
        self.pet_age_entry = ttk.Entry(self.frame, width=30)
        self.pet_notes_entry = ttk.Entry(self.frame, width=30)
        self.owner_name_entry = ttk.Entry(self.frame, width=30)

        # Grid Placement
        self.pet_name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.pet_breed_entry.grid(row=1, column=1, padx=5, pady=5)
        self.pet_age_entry.grid(row=2, column=1, padx=5, pady=5)
        self.pet_notes_entry.grid(row=3, column=1, padx=5, pady=5)
        self.owner_name_entry.grid(row=4, column=1, padx=5, pady=5)

        # Buttons
        ttk.Button(
            self.frame, text="Add Pet", command=self.add_pet
        ).grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")

        ttk.Button(
            self.frame, text="Sort by Name", command=self.sort_pet_list
        ).grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")

        # Treeview for Pets
        self.pet_tree = ttk.Treeview(
            self.frame, columns=("Name", "Breed", "Age", "Owner"), show="headings", height=10
        )
        self.pet_tree.heading("Name", text="Pet Name")
        self.pet_tree.heading("Breed", text="Breed")
        self.pet_tree.heading("Age", text="Age")
        self.pet_tree.heading("Owner", text="Owner Name")

        self.pet_tree.column("Name", width=150)
        self.pet_tree.column("Breed", width=150)
        self.pet_tree.column("Age", width=100)
        self.pet_tree.column("Owner", width=200)

        self.pet_tree.grid(row=7, column=0, columnspan=2, pady=10, sticky="nsew")

        self.refresh_pet_list()

    # Add pet to database
    def add_pet(self):
        pet_name = self.pet_name_entry.get().strip()
        pet_breed = self.pet_breed_entry.get().strip()
        pet_age = self.pet_age_entry.get().strip()
        pet_notes = self.pet_notes_entry.get().strip()
        owner_name = self.owner_name_entry.get().strip()

        # Validate Owner Exists
        owner = next((c for c in self.db.get_all_customers() if c[1] == owner_name), None)
        if not owner:
            messagebox.showerror("Error", "Owner not found. Please add the owner first.")
            return

        # Insert Pet into Database
        success = self.db.add_pet(pet_name, pet_breed, pet_age, pet_notes, owner[0])
        if success:
            messagebox.showinfo("Success", "Pet added successfully!")
            self.refresh_pet_list()
            self.clear_pet_entries()
        else:
            messagebox.showerror("Error", "Could not add pet. Ensure all fields are correct.")

    # Refresh pet list
    def refresh_pet_list(self):
        for row in self.pet_tree.get_children():
            self.pet_tree.delete(row)

        pets = self.db.get_all_pets()
        for pet in pets:
            self.pet_tree.insert(
                "", tk.END, values=(pet[1], pet[2], pet[3], pet[5])
            )

    # Sort pets by name
    def sort_pet_list(self):
        pets = sorted(self.db.get_all_pets(), key=lambda x: x[1].lower())
        self.pet_tree.delete(*self.pet_tree.get_children())

        for pet in pets:
            self.pet_tree.insert(
                "", tk.END, values=(pet[1], pet[2], pet[3], pet[5])
            )

    # Clear entries after adding
    def clear_pet_entries(self):
        self.pet_name_entry.delete(0, tk.END)
        self.pet_breed_entry.delete(0, tk.END)
        self.pet_age_entry.delete(0, tk.END)
        self.pet_notes_entry.delete(0, tk.END)
        self.owner_name_entry.delete(0, tk.END)
