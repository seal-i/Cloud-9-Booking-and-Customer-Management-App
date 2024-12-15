

class CustomerController:
    def __init__(self, db):
        self.db = db

    def delete_customer(self, customer_name):
        result = self.db.delete_customer(customer_name)
        return result
