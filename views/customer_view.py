import tkinter as tk
from tkinter import ttk, messagebox


class CustomerView:
    def __init__(self, parent, db):
        self.db = db
        self.frame = ttk.Frame(parent)

        # Define Style
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=5)
        style.configure("Hover.TButton", background="#000000", foreground="white")

        self.setup_customer_tab()

    # Setup the customer tab
    def setup_customer_tab(self):
        main_frame = ttk.Frame(self.frame, padding=15)
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Labels and Entries
        ttk.Label(main_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(main_frame, text="Contact:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(main_frame, text="Address:").grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.name_entry = ttk.Entry(main_frame, width=30)
        self.contact_entry = ttk.Entry(main_frame, width=30)
        self.address_entry = ttk.Entry(main_frame, width=30)

        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.contact_entry.grid(row=1, column=1, padx=5, pady=5)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        # Add Buttons with Hover Effects
        add_button = ttk.Button(main_frame, text="Add Customer", command=self.add_customer)
        add_button.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")
        add_button.bind("<Enter>", self.on_enter)
        add_button.bind("<Leave>", self.on_leave)

        delete_button = ttk.Button(main_frame, text="Delete Selected", command=self.delete_selected_customer)
        delete_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")
        delete_button.bind("<Enter>", self.on_enter)
        delete_button.bind("<Leave>", self.on_leave)

        # Treeview for Customers
        self.customer_tree = ttk.Treeview(
            main_frame, columns=("Name", "Contact", "Address"), show="headings", height=10
        )
        self.customer_tree.heading("Name", text="Name")
        self.customer_tree.heading("Contact", text="Contact")
        self.customer_tree.heading("Address", text="Address")
        self.customer_tree.column("Name", width=150)
        self.customer_tree.column("Contact", width=100)
        self.customer_tree.column("Address", width=200)
        self.customer_tree.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew")

        self.refresh_customer_list()

    def on_enter(self, event):
        event.widget.config(style="Hover.TButton")

    def on_leave(self, event):
        event.widget.config(style="TButton")

    def add_customer(self):
        name = self.name_entry.get().strip()
        contact = self.contact_entry.get().strip()
        address = self.address_entry.get().strip()

        if not (name and contact and address):
            messagebox.showerror("Error", "All fields are required.")
            return

        success = self.db.add_customer(name, contact, address)
        if success:
            messagebox.showinfo("Success", "Customer added successfully!")
            self.refresh_customer_list()

            self.name_entry.delete(0, tk.END)
            self.contact_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Customer already exists.")

    def delete_selected_customer(self):
        selected_item = self.customer_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No customer selected.")
            return

        customer_name = self.customer_tree.item(selected_item, "values")[0]
        confirm = messagebox.askyesno("Confirm Delete", f"Delete '{customer_name}'?")
        if not confirm:
            return

        deleted = self.db.delete_customer(customer_name)
        if deleted:
            messagebox.showinfo("Success", f"'{customer_name}' deleted.")
            self.refresh_customer_list()
        else:
            messagebox.showerror("Error", "Could not delete customer.")

    def refresh_customer_list(self):
        for row in self.customer_tree.get_children():
            self.customer_tree.delete(row)

        customers = self.db.get_all_customers()
        for customer in customers:
            self.customer_tree.insert(
                "", tk.END, values=(customer[1], customer[2], customer[3])
            )
