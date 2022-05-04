import sqlalchemy
from test_agro.data.model_base import SqlAlchemyBase
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .customer import Customer
from .product import Product
from datetime import datetime


class Order(SqlAlchemyBase):
    __tablename__ = 'ORDER'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    time = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    quantity = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    customer_id =  sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('CUSTOMER.id'))
    product_id =  sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('PRODUCT.id'))
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'quantity': self.quantity,
            'time': str(self.time.strftime("%m/%d/%Y, %H:%M:%S")),
            'customer': self.customer_id,
            'product': self.product_id
        }
    
