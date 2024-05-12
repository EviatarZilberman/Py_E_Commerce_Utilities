from DataModels.Product import Product


class CartProduct (Product):
    def __init__(self, product: Product, quantity):
        super().__init__(product_origin = product)
        self.quantity = quantity

    def to_dict(self):
        return {
            'quantity': self.quantity,
            '_id': self.internal_id,
            'created_at': str(self.created_at),
            'price': self.price,
            'section': self.section,
            'title': self.title,
            'description': self.description,
            'available_for_sale': self.available_for_sale,
            'pictures': self.pictures,
            'search_keys': self.search_keys,
            'owner_id': self.owner_id
        }

    @staticmethod
    def from_dict(dictionary):
        product = Product.from_dict(dictionary['product'])
        cart_product = CartProduct(product, dictionary['quantity'])
        return cart_product
