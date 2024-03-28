from DataModels.Owned import Owned


class Personaldetails(Owned):
    def __init__(self, owner_id, address = None, payment_details = None):
        super().__init__(owner_id)
        self.m_address = address
        self.m_payment_details = payment_details
