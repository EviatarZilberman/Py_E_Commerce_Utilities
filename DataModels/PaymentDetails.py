from DataModels.Base import Base


class PaymentDetails(Base):
    def __init__(self, credit_card_number, three_digits_in_back, expiry_date, id):
        super().__init__()
        self.m_credit_card_number = credit_card_number
        self.m_three_digits_in_back = three_digits_in_back
        self.m_expiry_date = expiry_date
        self.m_id = id
