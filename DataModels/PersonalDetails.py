from DataModels.Base import Base


class Personaldetails(Base):
    def __init__(self, address = None, payment_details = None):
        super().__init__()
        self.m_address = address
        self.m_payment_details = payment_details
