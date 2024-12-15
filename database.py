import sqlite3


class DatabaseManager:
    def __init__(self, db_path):
        """Initialize the database connection and create tables if needed."""
        self.connection = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        """Create tables for customers, pets, and appointments."""
        with self.connection:
            self.connection.executescript("""
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    contact TEXT NOT NULL,
                    address TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS pets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    breed TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    notes TEXT,
                    owner_id INTEGER NOT NULL,
                    FOREIGN KEY (owner_id) REFERENCES customers (id)
                );

                CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    time TEXT NOT NULL,
                    service TEXT NOT NULL,
                    pet_id INTEGER NOT NULL,
                    owner_id INTEGER NOT NULL,
                    FOREIGN KEY (pet_id) REFERENCES pets (id),
                    FOREIGN KEY (owner_id) REFERENCES customers (id)
                );
            """)

    # --- CUSTOMER METHODS --- #
    def add_customer(self, name, contact, address):
        """Add a new customer."""
        try:
            with self.connection:
                self.connection.execute(
                    "INSERT INTO customers (name, contact, address) VALUES (?, ?, ?)",
                    (name, contact, address)
                )
            return True
        except sqlite3.IntegrityError:
            return False

    def get_all_customers(self):
        """Fetch all customers."""
        with self.connection:
            return self.connection.execute("SELECT * FROM customers").fetchall()

    def get_customer_by_name(self, name):
        """Fetch a customer by name."""
        with self.connection:
            row = self.connection.execute(
                "SELECT * FROM customers WHERE name = ?", (name,)
            ).fetchone()
            return row if row else None

    def delete_customer(self, name):
        """Delete a customer by name."""
        with self.connection:
            result = self.connection.execute(
                "DELETE FROM customers WHERE name = ?", (name,)
            )
            return result.rowcount > 0

    # --- PET METHODS --- #
    def add_pet(self, name, breed, age, notes, owner_id):
        """Add a new pet."""
        try:
            with self.connection:
                self.connection.execute(
                    "INSERT INTO pets (name, breed, age, notes, owner_id) VALUES (?, ?, ?, ?, ?)",
                    (name, breed, age, notes, owner_id)
                )
            return True
        except sqlite3.IntegrityError:
            return False

    def get_all_pets(self):
        """Fetch all pets."""
        with self.connection:
            return self.connection.execute("SELECT * FROM pets").fetchall()

    def get_pet_by_name(self, name):
        """Fetch a pet by name."""
        with self.connection:
            row = self.connection.execute(
                "SELECT * FROM pets WHERE name = ?", (name,)
            ).fetchone()
            return row if row else None

    def delete_pet(self, pet_id):
        """Delete a pet by ID."""
        with self.connection:
            result = self.connection.execute(
                "DELETE FROM pets WHERE id = ?", (pet_id,)
            )
            return result.rowcount > 0

    # --- APPOINTMENT METHODS --- #
    def add_appointment(self, date, time, service, pet_id, owner_id):
        """Add a new appointment."""
        try:
            with self.connection:
                self.connection.execute(
                    """
                    INSERT INTO appointments (date, time, service, pet_id, owner_id)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (date, time, service, pet_id, owner_id)
                )
            return True
        except sqlite3.IntegrityError:
            return False

    def get_all_appointments(self):
        """Fetch all appointments."""
        with self.connection:
            return self.connection.execute("SELECT * FROM appointments").fetchall()

    def get_appointments_by_owner(self, owner_id):
        """Fetch appointments by owner ID."""
        with self.connection:
            rows = self.connection.execute(
                "SELECT * FROM appointments WHERE owner_id = ?", (owner_id,)
            ).fetchall()
            return rows if rows else []

    def delete_appointment(self, appointment_id):
        """Delete an appointment by ID."""
        with self.connection:
            result = self.connection.execute(
                "DELETE FROM appointments WHERE id = ?", (appointment_id,)
            )
            return result.rowcount > 0
