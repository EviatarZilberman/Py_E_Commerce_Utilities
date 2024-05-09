from DataModels.Base import Base


class Address (Base):
    def __init__(self, p_country, p_city, p_street, p_number, p_floor, p_apartment, p_entrance = None, p_mail_box = None, p_id = None, p_created_at = None):
        super().__init__()
        self.country = p_country
        self.city = p_city
        self.street = p_street
        self.number = p_number
        self.floor = p_floor
        self.apartment = p_apartment
        self.entrance = p_entrance
        self.mail_box = p_mail_box
        if p_id:
            self.internal_id = p_id
        if p_created_at:
            self.created_at = p_created_at

    def to_dict(self):
        return {
                "_id": str(self.internal_id), "created_at": str(self.created_at),
                "city": self.city, "street": self.street, "number": self.number,
                "floor": self.floor, "apartment": self.apartment,
                "entrance": self.entrance, "mail_box": self.mail_box, "country": self.country }

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
            item_id = dictionary["_id"]
        else:
            item_id = None
        if "created_at" in dictionary:
            created_at = dictionary["created_at"]
        else:
            created_at = None

        res = Address(dictionary["country"], dictionary["city"], dictionary["street"], dictionary["number"],
                      dictionary["floor"], dictionary["apartment"], entrance,
                      mail_box, item_id, created_at)
        return res
