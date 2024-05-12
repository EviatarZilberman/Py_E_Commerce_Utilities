class ViewProduct:
    def __init__(self, item_id, title, description, price, available, pictures, owner_id, sections):
        self.internal_id = item_id
        self.title = title
        self.description = description
        self.price = price
        self.available_for_sale = available
        self.pictures = pictures
        self.owner_id = owner_id
        self.sections = ViewProduct.__sections_to_string(sections)

    @staticmethod
    def __sections_to_string(sections):
        if not sections:
            return 'Others'
        if isinstance(sections, list):
            result = ', '.join(sections)
            return result

        else:
            return sections
