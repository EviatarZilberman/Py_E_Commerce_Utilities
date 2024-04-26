import datetime
from DataModels.Base import Base
from Enums.SaleType import SaleType


class Sale(Base):
    type = SaleType.Regular
    product_id = None
    min_price = 0
    end_time = datetime.MAXYEAR
    bidders = list()

    def __init__(self, product_id, min_price = 0, bidders = None, item_type = None, end_time = None):
        super().__init__()
        self.product_id = product_id
        self.type = item_type
        self.end_time = end_time
        self.bidders = bidders
        if min_price < 0:
            self.min_price = 0
        else:
            self.min_price = min_price

