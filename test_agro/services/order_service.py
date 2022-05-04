from typing import List
from test_agro.data.db_session import DbSession
from test_agro.data.order import Order
from test_agro.data.customer import Customer
from test_agro.data.product import Product

from test_agro.services.customer_service import CustomerService
from test_agro.services.product_service import ProductService


class OrderService:

    @classmethod
    def add_order(cls, qty, pro, cus):
      session = DbSession.create_session()
      p = Order()
      p.quantity = qty
      p.customer_id = cus
      p.product_id = pro
      session.add(p)
      session.commit()
      p.id = p.id
      return p

    @classmethod
    def order_by_id(cls, ord_id) -> Order:
        session = DbSession.create_session()
        o = session.query(Order).filter(Order.id == ord_id).first()
        session.close()
        return o

    @classmethod
    def update_order(cls, orde):
        id = orde['id']
        session = DbSession.create_session()
        o = session.query(Order).filter(Order.id == id).first()
        data = list(orde.keys())
        if 'product_id' in data:
            pr = ProductService.product_by_id(int(orde['product_id']))
            if pr:
                o.product_id = orde['product_id']
        if 'quantity' in data:
            o.quantity = orde['quantity']
        if 'customer_id' in data:
            cu = CustomerService.customer_by_id(int(orde['customer_id']))
            if cu:
                o.customer_id = orde['customer_id']
        session.commit()
        opr = ProductService.product_by_id(o.product_id)
        ocu = CustomerService.customer_by_id(o.customer_id)
        odict = o.to_dict()
        odict["customer"] = ocu.to_dict()
        odict["product"] = opr.to_dict()
        return odict

    @classmethod
    def delete_order(cls, list_ids):
        session = DbSession.create_session()
        for id in list_ids:
            c = session.query(Order).filter(Order.id == int(id)).first()
            if c:
                session.delete(c)
                session.commit()

    @classmethod
    def get_orders(cls) -> List[Order]:
        session = DbSession.create_session()
        result = session.query(Order).all()
        session.close()
        orders = [c.to_dict() for c in result]
        return orders

