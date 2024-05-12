from ViewModels.ViewProduct import ViewProduct


class ViewCart(ViewProduct):
    def __init__(self, item_id, title, description, price, available, pictures, owner_id, sections, quantity):
        super().__init__(item_id, title, description, price, available, pictures, owner_id, sections)
        self.quantity = quantity

