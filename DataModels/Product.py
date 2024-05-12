from datetime import datetime

from DataModels.Base import Base
from Enums.ProductSection import ProductSection
from Enums.ProductStatus import ProductStatus


class Product (Base):
    def __init__(self, owner_id = None, price = None, title = None, section = None, description = None,
                 available_for_sale = None, product_status = None,
                 pictures = None, internal_id = None, created_at = None, product_origin: 'Product' = None):
        super().__init__()
        if product_origin:
            self.title = product_origin.title
            self.owner_id = product_origin.owner_id
            self.price = product_origin.price
            self.available_for_sale = product_origin.available_for_sale
            self.description = product_origin.description
            self.internal_id = product_origin.internal_id
            self.created_at = product_origin.created_at
            self.pictures = product_origin.pictures
            self.product_status = product_origin.product_status
            self.search_keys = product_origin.search_keys
        else:
            self.owner_id = owner_id
            self.price = price
            self.title = title
            self.available_for_sale = available_for_sale
            self.description = description
            self.pictures = pictures if pictures is not None else None
            self.product_status = product_status if product_status else ProductStatus.DISPLAY
            self.section = section if isinstance(section, list) else [section] if section else [ProductSection.Others]
            self.internal_id = internal_id
            self.created_at = created_at or datetime.now()  # Provide default value if created_at is not provided
            self.search_keys = Product.initialize_search_keys(title)
    @staticmethod
    def initialize_search_keys(name : str) -> list:
        pop_words = ["to", "from", "at", "in", "too", "not"]
        keys = name.split()

        for i in keys:
            for j in pop_words:
                if j.__eq__(i):
                    keys.remove(i)

        return keys

    def to_dict(self):
        return {
            "_id": self.internal_id,
            "created_at": str(self.created_at),
            "price": self.price,
            "section": self.section,
            "title": self.title,
            "description": self.description,
            "available_for_sale": self.available_for_sale,
            "pictures": self.pictures,
            "search_keys": self.search_keys,
            "owner_id": self.owner_id
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
        if 'product_status' in dictionary:
            product_status = dictionary['product_status']
        else:
            product_status = ProductStatus.DISPLAY

        p = Product(dictionary["owner_id"], dictionary["price"],
                    dictionary["title"], section,
                    dictionary["description"],
                    avail_for_sale, product_status,
                    pictures, _id, created_at)
        return p