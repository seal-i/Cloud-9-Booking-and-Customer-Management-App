class Appointment:
    def __init__(self, appointment_id, date, time, service, pet_id, owner_id):
        self.appointment_id = appointment_id
        self.date = date
        self.time = time
        self.service = service
        self.pet_id = pet_id
        self.owner_id = owner_id

    def __repr__(self):
        return f"Appointment({self.appointment_id}, {self.date}, {self.time}, {self.service}, Pet: {self.pet_id}, Owner: {self.owner_id})"

    def to_dict(self):
        return {
            "appointment_id": self.appointment_id,
            "date": self.date,
            "time": self.time,
            "service": self.service,
            "pet_id": self.pet_id,
            "owner_id": self.owner_id,
        }
