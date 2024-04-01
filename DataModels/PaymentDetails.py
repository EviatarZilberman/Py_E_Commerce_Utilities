from datetime import datetime

from DataModels.Base import Base


class PaymentDetails(Base):
    def __init__(self, credit_card_number, three_digits_in_back, expiry_date, id):
        super().__init__()
        self.m_credit_card_number = credit_card_number
        self.m_three_digits_in_back = three_digits_in_back
        self.m_expiry_date = expiry_date
        self.m_id = id


    #TODO = FIX THIS FUNCTION!
    @staticmethod
    def details_validation(form_data):
        error_list = list()
        if not form_data:
            return ["No fields were filled!"]

        if len(form_data["credit_card_number"]) > 19 or len(form_data["credit_card_number"]) < 8:
            error_list.append("Credit card number is incorrect")

        temp_number = int(form_data["credit_card_number"])
        if temp_number < 0:
            error_list.append("Credit card number is negative")

        temp_number = int(form_data["three_digits_in_back"])
        if temp_number < 0:
            error_list.append("3 digits are incorrect")

        correct_expiry_date = PaymentDetails.__validate_date(form_data.m_expiry_date)
        if not correct_expiry_date:
            error_list.append("Expiry date is incorrect")

        correct_id = PaymentDetails.__israeli_id_validation(form_data.m_id)
        if not correct_id:
            error_list.append("Id is incorrect")

        return error_list


    @staticmethod
    def __israeli_id_validation(id):
        sum = 0
        for digit in id:
            temp_id = int(digit)
            if digit % 2 == 0:
                temp_id = temp_id * 2
                sum += temp_id
            else:
                sum += temp_id

        if sum % 10 == 0:
            return True
        else:
            return False

    @staticmethod
    def __validate_date(date_str, date_format='%Y-%m-%d'):
        try:
            datetime.strptime(date_str, date_format)
            return True
        except ValueError:
            return False
