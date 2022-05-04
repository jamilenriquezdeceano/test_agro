import sqlalchemy
from sqlalchemy.orm import relationship

from test_agro.data.model_base import SqlAlchemyBase


class Product(SqlAlchemyBase):
    __tablename__ = 'PRODUCT'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    quantity = sqlalchemy.Column('quantity', sqlalchemy.Integer, nullable=False)
    price =  sqlalchemy.Column('price', sqlalchemy.Numeric, nullable=False)
    product = sqlalchemy.Column('product', sqlalchemy.String, nullable=False)
    order = relationship("Order", backref="product", lazy="select")

    def to_dict(self):
        return {
            'id': self.id,
            'quantity': self.quantity,
            'price': str(self.price),
            'product': self.product
        }