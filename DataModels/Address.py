from DataModels.Base import Base


class Address (Base):
    def __init__(self, city, street, number, floor, department, entrance, mail_box):
        super().__init__()
        self.m_city = city
        self.m_street = street
        self.m_number = number
        self.m_floor = floor
        self.m_department = department
        self.m_entrance = entrance
        self.m_mail_box = mail_box
