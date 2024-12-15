class Pet:
    def __init__(self, pet_id, name, breed, age, notes, owner_id):
        self.pet_id = pet_id
        self.name = name
        self.breed = breed
        self.age = age
        self.notes = notes
        self.owner_id = owner_id

    def __repr__(self):
        return f"Pet({self.pet_id}, {self.name}, {self.breed}, {self.age}, {self.notes}, Owner: {self.owner_id})"

    def to_dict(self):
        return {
            "pet_id": self.pet_id,
            "name": self.name,
            "breed": self.breed,
            "age": self.age,
            "notes": self.notes,
            "owner_id": self.owner_id,
        }
