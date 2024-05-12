from DataModels.Product import Product


class CartProduct (Product):
    def __init__(self, product: Product, quantity):
        super().__init__(product_origin = product)
        self.product = product
        self.quantity = quantity

    def to_dict(self):
        return {
            'quantity': self.quantity,
            'product_id': self.product.to_dict()
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
