from datetime import datetime
from DataModels.Base import Base


class PaymentDetails(Base):
    def __init__(self, credit_card_number = None, three_digits_in_back = None, expiry_date = None, item_id = None):
        super().__init__()
        self.credit_card_number = credit_card_number
        self.three_digits_in_back = three_digits_in_back
        self.expiry_date = expiry_date
        self.id = item_id

    @staticmethod
    def details_validation(form_data):
        error_list = list()
        if not form_data:
            return ["No fields were filled!"]
        credit_card_number = form_data.get("credit_card_number")
        if len(credit_card_number) > 19 or len(credit_card_number) < 8:
            error_list.append("Credit card number is incorrect")

        temp_number = int(form_data["credit_card_number"])
        if temp_number < 0:
            error_list.append("Credit card number is negative")

        temp_number = int(form_data["three_digits_in_back"])
        if temp_number < 0:
            error_list.append("3 digits are incorrect")

        correct_expiry_date = PaymentDetails.__validate_date(form_data["expiry_date"])
        if not correct_expiry_date:
            error_list.append("Expiry date is incorrect")

        correct_id = PaymentDetails.__israeli_id_validation(form_data["id"])
        if not correct_id:
            error_list.append("Id is incorrect")

        return error_list

    @staticmethod
    def __israeli_id_validation(item_id):
        sum = 0
        for i in range(len(item_id)):
            temp_id = int(item_id[i])
            if i == 0:
                sum += temp_id
            else:
                if i % 2 != 0:
                    temp_id = temp_id * 2
                    if temp_id > 9:
                        temp_id = temp_id % 10 + temp_id // 10
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

    @staticmethod
    def from_dict(dictionary):
        if dictionary is None:
            return None
        payment_details = PaymentDetails(dictionary["credit_card_number"], dictionary["three_digits_in_back"],
                                         dictionary["expiry_date"], dictionary["id"])
        return payment_details

    def to_dict(self):
        return {"_id": str(self.internal_id), "created_at": str(self.created_at),
                "credit_card_number": self.credit_card_number,
                "three_digits_in_back": self.three_digits_in_back, "expiry_date": str(self.expiry_date),
                "id": self.id }
