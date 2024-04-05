from DataModels.Base import Base


class Address (Base):
    def __init__(self, city, street, number, floor, apartment, entrance = None, mail_box = None, id = None, created_at = None):
        super().__init__()
        self.m_city = city
        self.m_street = street
        self.m_number = number
        self.m_floor = floor
        self.m_apartment = apartment
        self.m_entrance = entrance
        self.m_mail_box = mail_box
        if id:
            self.m_internal_id = id
        if created_at:
            self.m_created_at = created_at

    def to_dict(self):
        return {
                "_id": str(self.m_internal_id), "created_at": str(self.m_created_at),
                "city": self.m_city, "street": self.m_street, "number": self.m_number,
                "floor": self.m_floor, "apartment": self.m_apartment,
                "entrance": self.m_entrance, "mail_box": self.m_mail_box }

    @staticmethod
    def from_dict(dictionary):
        if "entrance" in dictionary:
            entrance = dictionary['entrance']
        else:
            entrance = None
        if "mail_box" in dictionary:
            mail_box = dictionary['mail_box']
        else:
            mail_box = None
        if "_id" in dictionary:
            id = dictionary["_id"]
        else:
            id = None
        if "created_at" in dictionary:
            created_at = dictionary["created_at"]
        else:
            created_at = None

        res = Address(dictionary["city"], dictionary["street"], dictionary["number"],
                      dictionary["floor"], dictionary["apartment"], entrance,
                      mail_box, id, created_at)
        return res
