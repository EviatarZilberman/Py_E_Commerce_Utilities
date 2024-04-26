from DataModels.Base import Base
from Enums.ProductSection import ProductSection
from Enums.ProductStatus import ProductStatus


class Product (Base):
    owner_id = None
    price = 0
    title = None
    description = None
    pictures = list()
    available_for_sale = 1
    search_keys = list()
    section = list()

    def __init__(self, owner_id, price, title, section, description, available_for_sale = 1, product_status = ProductStatus.CREATE,
                 pictures = None, internal_id = None, created_at = None):
        super().__init__()
        if internal_id:
            self.internal_id = internal_id
        if created_at:
            self.created_at = created_at
        self.owner_id = owner_id
        self.price = price
        self.title = title
        self.available_for_sale = available_for_sale
        self.description = description
        self.pictures = pictures
        if product_status == ProductStatus.CREATE:
            if isinstance(section, list):
                self.section = section # Type of the product (toys, food...)
            else:
                self.section.append(ProductSection.Others)
        else:
            self.section = section
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

        p = Product(dictionary["owner_id"], dictionary["price"],
                    dictionary["title"], section,
                    dictionary["description"],
                    avail_for_sale,
                    pictures, _id, created_at)
        return p

    def to_string(self):
        return (f"id: {self.internal_id}, created: {self.created_at}, price: {self.price}, title: {self.title},"
                f" des: {self.description}, section: {self.section}"
                f"avail: {self.available_for_sale}, search: {self.search_keys}, owner: {self.owner_id}")
