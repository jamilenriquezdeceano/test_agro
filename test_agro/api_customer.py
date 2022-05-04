import json
from pyramid.response import Response
from pyramid.request import Request

from cornice import Service
from test_agro.viewmodel.customer_viewmodel import CreateCustomerViewModel
from test_agro.services.customer_service import  CustomerService
from test_agro.data.customer import Customer

customer = Service(name='customer', path='/customer', description="Customer")

@customer.get(renderer='json')
def all_customers(request:Request):
    id = None
    if 'id' in list(request.GET.keys()):
        id=request.GET['id']
        cus = CustomerService.customer_by_id(int(id))
        if cus:
            return Response(status=202, json_body={'id': cus.id, 'name':cus.name, 'age':cus.age, 'house_type':cus.house_type})
        msg = "The customer with id '{}' was not found.".format(id)
        return Response(status=404, json_body={'error': msg})
    return CustomerService.get_customers()

@customer.post(renderer='json')
def add_customer(request: Request):
    try:
        customer_data = request.json_body
    except Exception as x:
        return Response(status=400, body='Could not parse your post as JSON.' + str(x))
    
    vm = CreateCustomerViewModel(customer_data)
    vm.compute_details()

    if vm.errors:
        return Response(status=400, body=vm.error_msg)
    
    try:
        r = CustomerService.add_customer(vm.customer)
        return Response(status=201, json_body=r.to_dict())
    except Exception as x:
        return Response(status=500, body='Could not save customer. ' + str(x))

@customer.patch(renderer='json')
def update_customer(request: Request):
    cus_id = request.json_body.get('id')
    cus = CustomerService.customer_by_id(cus_id)
    cus_data = None
    if not cus:
        msg = "The customer with id '{}' was not found.".format(cus_id)
        return Response(status=404, json_body={'error': msg})
    try:
        cus_data = request.json_body
    except:
        return Response(status=400, body='Could not parse your post as JSON.')

    try:
        r = CustomerService.update_customer(cus_data)
        return Response(status=202, json_body=r)
    except:
        return Response(status=400, body='Could not update customer.')

@customer.delete(renderer='json')
def delete_customers(request: Request):
    cus_ids = request.json_body.get('ids')
    list_ids = list(cus_ids.split(","))
    CustomerService.delete_customer(list_ids)
    return Response(status=204)







    



