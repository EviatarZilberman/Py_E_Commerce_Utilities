from DataModels import Base
from DataModels.CartDataProduct import CartDataProduct
from DataModels.CartProduct import CartProduct
from DataModels.PersonalDetails import PersonalDetails


class User(Base.Base):
    username = None
    first_name = None
    last_name = None
    email = None
    password = None
    products_for_sell = list() # List of product id
    cart: list[CartDataProduct] = None # List of CartDataProduct
    personal_details: PersonalDetails = None

    def __init__(self, username, f_name, l_name, email, password, item_id = None, creation_date = None,
                 sell_products: list = None, cart: list = None, personal_details = None):
        super().__init__()
        if item_id is not None:
            self.internal_id = item_id
        if creation_date is not None:
            self.created_at = creation_date
        self.username = username
        self.first_name = f_name
        self.last_name = l_name
        self.email = email
        self.password = password
        self.products_for_sell = sell_products
        if isinstance(cart, list):
            self.cart = cart
        else:
            self.cart = []
        self.personal_details: PersonalDetails = personal_details

    @staticmethod
    def __strong_password(password) -> list:
        error_list = list()
        if password is None or password == '':
            error_list.append('Password is empty.')

        if len(password) < 8 or len(password) > 25:
            error_list.append('Password is invalid (longer than 8 and shorter than 26).')

        capital = 0
        lower = 0
        number = 0
        special = 0
        for i in range(len(password)):
            if password[i].isupper():
                capital += 1
            elif password[i].islower():
                lower += 1
            elif password[i].isnumeric():
                number += 1
            else:
                special += 1

        if capital < 1:
            error_list.append('Not enough capital letters.')
        if lower < 1:
            error_list.append('Not enough lower letters.')
        if number < 1:
            error_list.append('Not enough numbers.')
        if special < 1:
            error_list.append('Not enough special characters.')
        return error_list

    @staticmethod
    def valid_password(password, confirm_password) -> list:
        error_list = list()
        if not password == confirm_password:
            error_list.append('Password and Confirm Password are not the same.')

        new_error_list = list()
        new_error_list = User.__strong_password(password)

        if len(error_list) == 1:
            new_error_list.append(error_list[0])

        return new_error_list

    def to_dict(self):
        personal_details_dict = self.personal_details.to_dict() if self.personal_details else None
        cart_dict_list = []
        if isinstance(self.cart, list):
            cart_dict_list = [cart_product.to_dict() for cart_product in self.cart if
                              isinstance(cart_product, CartProduct)]
        return {
            '_id': str(self.internal_id),
            'created_at': str(self.created_at),
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'products_for_sell': self.products_for_sell,
            'cart': cart_dict_list,
            'personal_details': personal_details_dict
        }

    @staticmethod
    def from_dict(dictionary):
        if 'cart' in dictionary:
            cart = dictionary['cart']
        else:
            cart = None
        if 'personal_details' in dictionary:
            personal_details_dict = dictionary['personal_details']
            if personal_details_dict:
                personal_details = PersonalDetails.from_dict(personal_details_dict)
            else:
                personal_details = None
        else:
            personal_details = None
        if 'products_for_sell' in dictionary:
            sell_list = dictionary['products_for_sell']
        else:
            sell_list = None

        user = User(dictionary['username'], dictionary['first_name'], dictionary['last_name'], dictionary['email'],
                    dictionary['password'], dictionary['_id'], dictionary['created_at'],
                    sell_list, cart, personal_details)
        return user

    def clear_list(self):
        for item in self.cart:
            if not item:
                self.cart.remove(item)


#  Folder/
# | 
# ├──   E_Commerce_Application/
# │          │
# │          ├── app.py
# |          ├── BrowserModels/
#|              ├── CookieManager
#|              ├── init.py
# │          ├── DataModels/
# │             ├── Base.py
# │             ├── User.py
# │             ├── __init__.py
# │             └── ...
# |          ├── static/
# |             ├── __init__.py
# |             ├── functions.js
# |          ├── templates/
# |             ├── __init__.py
# |             ├── add_new_product.html
# |             ├── ...
# |         ├── venv/
# |             ├── ...
# |         ├── views.py.py
# |         ├── .env
# |         ├── __init__.py
# ├── VSC_PyMongoDb/
# │        |── Interface/
# │             ├── IPyMongoDb.py
# │             ├── __init__.py
# │         └── MongoDbManager/
#               ├── MongoDbSingleton.py 
            #   ├── __init__.py
    #           ├── __init__.py
#           └── ...
