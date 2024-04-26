from DataModels.Address import Address
from DataModels.Base import Base
from DataModels.PaymentDetails import PaymentDetails


class PersonalDetails(Base):
    def __init__(self, address: Address = None, payment_details: PaymentDetails = None, internal_id = None, created_at = None):
        super().__init__()
        if address:
            self.address: Address = address
        if payment_details:
            self.payment_details: PaymentDetails = payment_details
        if internal_id:
            self.internal_id = internal_id
        if created_at:
            self.created_at = created_at

    @staticmethod
    def from_dict(dictionary):
        if "address" in dictionary:
            adr_dict = dictionary["address"]
            if adr_dict:
                address = Address.from_dict(adr_dict)
            else:
                address = None
        else:
            address = None
        if "payment_details" in dictionary:
            pay_dict = dictionary["payment_details"]
            payment_details = PaymentDetails.from_dict(pay_dict)
        else:
            payment_details = None
        personal_details = PersonalDetails(address, payment_details, dictionary["_id"], dictionary["created_at"])
        return personal_details

    def to_dict(self):
        try:
            address_dict = self.address.to_dict()
        except:
            address_dict = None
        try:
            payment_details_dict = self.payment_details.to_dict()
        except:
            payment_details_dict = None
        return {"_id": str(self.internal_id), "created_at": str(self.created_at),
                "address": address_dict,
                "payment_details": payment_details_dict}

