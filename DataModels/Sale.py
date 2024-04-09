import datetime
from DataModels.Base import Base
from Enums.SaleType import SaleType


class Sale(Base):
    m_type = SaleType.Regular
    m_product_id = None
    m_min_price = 0
    m_end_time = datetime.MAXYEAR
    m_bidders = list()

    def __init__(self, product_id, min_price = 0, bidders = None, type = None, end_time = None):
        super().__init__()
        self.m_product_id = product_id
        self.m_type = type
        self.m_end_time = end_time
        self.m_bidders = bidders
        if min_price <= 0:
            self.m_min_price = 0
        else:
            self.m_min_price = min_price

