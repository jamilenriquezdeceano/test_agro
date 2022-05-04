
from test_agro.data.product import Product
from test_agro.viewmodel.base_viewmodel import ViewModelBase
from decimal import Decimal

class CreateProductViewModel(ViewModelBase):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.product = None

    def compute_details(self):
        quantity = self.data_dict.get('quantity')
        price  = self.data_dict.get('price')
        product_ = self.data_dict.get('product')

        if not quantity:
            self.errors.append("Quantity is a required field.")
        if not price:
            self.errors.append("Price is a required field.")
        if not product_:
            self.errors.append("Product type is a required field.")
        if not type(quantity) == int:
            self.errors.append("Quantity should be number.")
        if not type(price) == str:
            self.errors.append("Price should be decimal number.")
        if not type(product_) == str:
            self.errors.append("Product type should be string.")

        if not self.errors:
            item = Product()
            item.product = product_
            item.quantity = int(quantity)
            item.price = price
            self.product = item


        
        

