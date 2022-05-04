from typing import List
from test_agro.data.db_session import DbSession
from test_agro.data.customer import Customer



class CustomerService:
    
    @classmethod
    def get_customers(cls) -> List[Customer]:
        session = DbSession.create_session()
        #session = DbSession.factory()
        result = session.query(Customer).all()
        session.close()
        customers = [c.to_dict() for c in result]
        return customers

    @classmethod
    def add_customer(cls, cus: Customer):
        c = Customer()
        c.name = cus.name
        c.age = cus.age
        c.house_type = cus.house_type
        session = DbSession.create_session()
        session.add(c)
        session.commit()
        c.id = c.id
        return c
    
    @classmethod
    def customer_by_id(cls, cus_id):
        session = DbSession.create_session()
        cus = session.query(Customer).filter(Customer.id == cus_id).first()
        session.close()
        return cus
    
    @classmethod
    def update_customer(cls, cus):
        id = cus['id']
        session = DbSession.create_session()
        c = session.query(Customer).filter(Customer.id == id).first()
        if 'name' in list(cus.keys()):
            c.name = cus['name']
        if 'age' in list(cus.keys()):
            c.age = cus['age']
        if 'house_type' in list(cus.keys()):
            c.house_type = cus['house_type']
        session.commit()
        
        return c.to_dict()
    
    @classmethod
    def delete_customer(cls, list_ids):
        session = DbSession.create_session()
        for id in list_ids:
            c = session.query(Customer).filter(Customer.id == int(id)).first()
            if c:
                session.delete(c)
                session.commit()