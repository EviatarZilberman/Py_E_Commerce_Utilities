from DataModels.Base import Base


class Product (Base):
    m_owner_id = None
    m_price = 0
    m_name = None
    m_description = None
    m_pictures = list()
    m_quantity = 1
    m_search_keys = list()
    m_section = list()

    def __init__(self, price, name, section, quantity = 1, description = None, pictures = None):
        super().__init__()
        self.m_price = price
        self.m_name = name
        self.m_quantity = quantity
        self.m_description = description
        self.m_pictures = pictures
        self.m_section = section
        self.m_search_keys = Product.__initialize_search_keys(name)

    @staticmethod
    def __initialize_search_keys(name : str) -> list:
        pop_words = ["to", "from", "at", "in", "too", "not"]
        keys = name.split()

        for i in keys:
            for j in pop_words:
                if j.__eq__(i):
                    keys.remove(i)

        return keys

