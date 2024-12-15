class Customer:
    def __init__(self, customer_id, name, contact, address):
        self.customer_id = customer_id
        self.name = name
        self.contact = contact
        self.address = address

    def __repr__(self):
        return f"Customer({self.customer_id}, {self.name}, {self.contact}, {self.address})"

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "contact": self.contact,
            "address": self.address,
        }
