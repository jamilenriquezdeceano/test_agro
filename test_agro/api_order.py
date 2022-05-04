from pyramid.response import Response
from pyramid.request import Request
from cornice import Service
from pyramid.httpexceptions import HTTPUnauthorized
from test_agro.services.order_service import  OrderService
from test_agro.services.customer_service import CustomerService
from test_agro.services.product_service import ProductService


order = Service(name='order', path='/order', description="Order")

def valid_token(request, **kwargs):
    header = 'Authorization'
    htoken = request.headers.get(header)
    if htoken is None:
        raise HTTPUnauthorized()
    try:
        token = htoken.split()[1]
    except ValueError:
        raise HTTPUnauthorized()
    valid = "123456987*/-ABC" == token
    if not valid:
        raise HTTPUnauthorized()
    



@order.post(validators=valid_token, renderer='json')
def add_order(request: Request):
    data = list(request.POST)
    errors = []
    if not ('quantity' in data) and not ('product_id' in data) and not('customer_id' in data):
        return Response(status=400, json_body={'msg':'Form data should have  quantity, product_id, customer_id fields'})
    qty = int(request.POST['quantity'])
    c = CustomerService.customer_by_id(int(request.POST['customer_id']))
    p = ProductService.product_by_id(int(request.POST['product_id']))

    if not c:
        errors.append({'product_id':'Product not found'})
    if not p:
        errors.append({'customer_id':'Customer not found'})
    if len(errors) > 0:
        return Response(status=400, body=errors)
    try:
        r = OrderService.add_order(qty, p.id, c.id)
        return Response(status=201, json_body={'id':r.id, 'quantity':r.quantity, 'product':p.to_dict(), 'customer': c.to_dict()})
    except Exception as x:
        return Response(status=500, body='Could not save order. ' + str(x))


@order.patch(renderer='json')
def update_order(request: Request):
    ord_id = request.json_body.get('id')
    orde = OrderService.order_by_id(ord_id)
    ord_data = None
    if not orde:
        msg = "The order with id '{}' was not found.".format(ord_id)
        return Response(status=404, json_body={'error': msg})
    try:
        ord_data = request.json_body
    except:
        return Response(status=400, body='Could not parse your post as JSON.')
    try:
        r = OrderService.update_order(ord_data)
        return Response(status=202, json_body=r)
    except:
        return Response(status=400, body='Could not update order.')

@order.delete(renderer='json')
def delete_orders(request: Request):
    cus_ids = request.json_body.get('ids')
    list_ids = list(cus_ids.split(","))
    OrderService.delete_order(list_ids)
    return Response(status=204)


@order.get(renderer='json')
def all_orders(request:Request):
    id = None
    if 'id' in list(request.GET.keys()):
        id=request.GET['id']
        orde = OrderService.order_by_id(int(id))
        if orde:
            c = CustomerService.customer_by_id(orde.customer_id)
            p = ProductService.product_by_id(orde.product_id)
            odict = orde.to_dict()
            odict["product"] = p.to_dict()
            odict["customer"] = c.to_dict()
            return Response(status=202, json_body=odict)
        msg = "The orders with id '{}' was not found.".format(id)
        return Response(status=404, json_body={'error': msg})
    all_ord = OrderService.get_orders()
    for o in all_ord:
        obj2 = CustomerService.customer_by_id(o["product"])
        obj1 = ProductService.product_by_id(o["customer"])
        o["customer"] = obj1.to_dict()
        o["product"] = obj2.to_dict()
    return all_ord
    
