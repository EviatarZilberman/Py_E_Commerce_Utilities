from DataModels.Owned import Owned


class Address (Owned):
    def __init__(self, owner_id, city, street, number, floor, department, entrance, mail_box):
        super().__init__(owner_id)
        self.m_city = city
        self.m_street = street
        self.m_number = number
        self.m_floor = floor
        self.m_department = department
        self.m_entrance = entrance
        self.m_mail_box = mail_box
