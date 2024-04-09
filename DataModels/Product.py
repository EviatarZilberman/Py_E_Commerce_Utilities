from DataModels.Base import Base
from Enums.ProductSection import ProductSection


class Product (Base):
    m_owner_id = None
    m_price = 0
    m_title = None
    m_description = None
    m_pictures = list()
    m_available_for_sale = 1
    m_search_keys = list()
    m_section = list()

    def __init__(self, owner_id, price, title, section, description, available_for_sale = 1,
                 pictures = None, internal_id = None, created_at = None):
        super().__init__()
        if internal_id:
            self.m_internal_id = internal_id
        if created_at:
            self.m_created_at = created_at
        self.m_owner_id = owner_id
        self.m_price = price
        self.m_title = title
        self.m_available_for_sale = available_for_sale
        self.m_description = description
        self.m_pictures = pictures
        if section is list():
            self.m_section = section # Type of the product (toys, food...)
        else:
            self.m_section.append(ProductSection.Others)
        self.m_search_keys = Product.__initialize_search_keys(title)

    @staticmethod
    def __initialize_search_keys(name : str) -> list:
        pop_words = ["to", "from", "at", "in", "too", "not"]
        keys = name.split()

        for i in keys:
            for j in pop_words:
                if j.__eq__(i):
                    keys.remove(i)

        return keys

    def to_dict(self):
        return {
            "_id": self.m_internal_id,
            "created_at": self.m_created_at,
            "price": self.m_price,
            "section": self.m_section,
            "title": self.m_title,
            "description": self.m_description,
            "available_for_sale": self.m_available_for_sale,
            "pictures": self.m_pictures,
            "search_keys": self.m_search_keys
        }

    @staticmethod
    def from_dict(dictionary):
        if '_id' in dictionary:
            _id = dictionary["_id"]
        else:
            _id = None
        if 'created_at' in dictionary:
            created_at = dictionary["created_at"]
        else:
            created_at = None
        if 'pictures' in dictionary:
            pictures = dictionary["pictures"]
        else:
            pictures = None
        if 'available_for_sale' in dictionary:
            avail_for_sale = int(dictionary["available_for_sale"])
            if avail_for_sale < 1:
                avail_for_sale = 1
        else:
            avail_for_sale = 1
        if 'dropdown' in dictionary:
            section = dictionary["dropdown"]
        elif 'section' in dictionary:
            section = dictionary["section"]
        else:
            section = str(ProductSection.Others)

        product = Product(dictionary["owner_id"], dictionary["price"],
                          dictionary["title"], section,
                          dictionary["description"],
                          avail_for_sale,
                          pictures, _id, created_at)
        return product
