
from test_agro.data.customer import Customer
from test_agro.viewmodel.base_viewmodel import ViewModelBase

class CreateCustomerViewModel(ViewModelBase):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.customer = None

    def compute_details(self):
        name = self.data_dict.get('name')
        age  = self.data_dict.get('age')
        house_type = self.data_dict.get('house_type')

        if not name:
            self.errors.append("Name is a required field.")
        if not age:
            self.errors.append("Age is a required field.")
        if not house_type:
            self.errors.append("House type is a required field.")
        if not type(name) == str:
            self.errors.append("Name should be string.")
        if not type(age) == int:
            self.errors.append("Age should be number.")
        if not type(house_type) == str:
            self.errors.append("House type should be string.")
        
        if not self.errors:
            customer = Customer()
            customer.name = name
            customer.age = age
            customer.house_type = house_type
            self.customer = customer


        
        

