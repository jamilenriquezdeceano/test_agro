from typing import List
from test_agro.data.db_session import DbSession
from test_agro.data.product import Product



class ProductService:
    
    @classmethod
    def get_products(cls) -> List[Product]:
        session = DbSession.create_session()
        result = session.query(Product).all()
        session.close()
        products = [c.to_dict() for c in result]
        return products

    @classmethod
    def add_product(cls, pro: Product):
        p = Product()
        p.product = pro.product
        p.price = pro.price
        p.quantity = pro.quantity
        session = DbSession.create_session()
        session.add(p)
        session.commit()
        p.id = p.id
        return p

   
    @classmethod
    def product_by_id(cls, pro_id):
        session = DbSession.create_session()
        pro = session.query(Product).filter(Product.id == pro_id).first()
        session.close()
        return pro
    
    @classmethod
    def update_product(cls, pro):
        id = pro['id']
        session = DbSession.create_session()
        p = session.query(Product).filter(Product.id == id).first()
        if 'product' in list(pro.keys()):
            p.product = pro['product']
        if 'quantity' in list(pro.keys()):
            p.quantity = pro['quantity']
        if 'price' in list(pro.keys()):
            p.price = pro['price']
        session.commit()
        
        return p.to_dict()
    
    @classmethod
    def delete_product(cls, list_ids):
        session = DbSession.create_session()
        for id in list_ids:
            p = session.query(Product).filter(Product.id == int(id)).first()
            if p:
                session.delete(p)
                session.commit()
