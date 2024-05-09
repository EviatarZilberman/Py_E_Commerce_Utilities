from DataModels.Base import Base


class CartProduct (Base):
    def __init__(self, product_id, quantity):
        super().__init__()
        self.product_id = product_id
        self.quantity = quantity

    def to_dict(self):
        return {
            '_id': self.internal_id,
            'created_at': str(self.created_at),
            'quantity': self.quantity,
            'product_id': self.product_id
        }

    @staticmethod
    def from_dict(dictionary):
        if '_id' in dictionary:
            _id = dictionary['_id']
        else:
            _id = None
        if 'created_at' in dictionary:
            created_at = dictionary['created_at']
        else:
            created_at = None
        if 'quantity' in dictionary:
            quantity = dictionary['quantity']
        else:
            quantity = None
        if 'product_id' in dictionary:
            product_id = dictionary['product_id']
        else:
            product_id = None
        p = CartProduct(product_id, quantity)
        p.created_at = created_at
        p.internal_id = _id
        return p
