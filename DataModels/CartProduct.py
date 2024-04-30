from DataModels.Base import Base


class CartProduct (Base):
    def __init__(self, product_id, count):
        super().__init__()
        self.internal_id = product_id
        self.count = count

    def to_dict(self):
        return {
            "_id": self.internal_id,
            "created_at": str(self.created_at),
            "count": self.count
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
        if 'count' in dictionary:
            count = dictionary['count']
        else:
            count = None
        if 'product_id' in dictionary:
            product_id = dictionary['product_id']
        else:
            product_id = None
        p = CartProduct(product_id, count)
        p.created_at = created_at
        return p
