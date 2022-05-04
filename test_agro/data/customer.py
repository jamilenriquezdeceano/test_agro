import sqlalchemy
from sqlalchemy.orm import relationship

from test_agro.data.model_base import SqlAlchemyBase


class Customer(SqlAlchemyBase):
    __tablename__ = 'CUSTOMER'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column('name', sqlalchemy.String, nullable=False)
    age =  sqlalchemy.Column('age', sqlalchemy.Integer, nullable=False)
    house_type = sqlalchemy.Column('house_type', sqlalchemy.String, nullable=False)
    order = relationship("Order", backref="customer")
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'house_type': self.house_type
        }
    
