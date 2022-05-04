import json
from pyramid.response import Response
from pyramid.request import Request

from cornice import Service
from test_agro.viewmodel.product_viewmodel import CreateProductViewModel
from test_agro.services.product_service import  ProductService
from test_agro.data.product import Product

product = Service(name='product', path='/product', description="Product")


@product.get(renderer='json')
def all_product(request:Request):
    id = None
    if 'id' in list(request.GET.keys()):
        id=request.GET['id']
        pro = ProductService.product_by_id(int(id))
        if pro:
            #return Response(status=202, json_body={'id': pro.id, 'product':pro.product, 'price':pro.price, 'quantity':pro.quantity})
            return Response(status=202, json_body=pro.to_dict())
        msg = "The product with id '{}' was not found.".format(id)
        return Response(status=404, json_body={'error': msg})
    return ProductService.get_products()


@product.post(renderer='json')
def add_product(request: Request):
    try:
        product_data = request.json_body
        print(product_data)
    except Exception as x:
        return Response(status=400, body='Could not parse your post as JSON.' + str(x))
    vm = CreateProductViewModel(product_data)
    vm.compute_details()

    if vm.errors:
        return Response(status=400, body=vm.error_msg)
    
    try:
        r = ProductService.add_product(vm.product)
        return Response(status=201, json_body=r.to_dict())
    except Exception as x:
        return Response(status=500, body='Could not save product. ' + str(x))

@product.patch(renderer='json')
def update_product(request: Request):
    pro_id = request.json_body.get('id')
    pro = ProductService.product_by_id(pro_id)
    pro_data = None
    if not pro:
        msg = "The product with id '{}' was not found.".format(pro_id)
        return Response(status=404, json_body={'error': msg})
    try:
        pro_data = request.json_body
    except:
        return Response(status=400, body='Could not parse your post as JSON.')
    try:
        r = ProductService.update_product(pro_data)
        return Response(status=202, json_body=r)
    except:
        return Response(status=400, body='Could not update product.')

@product.delete(renderer='json')
def delete_product(request: Request):
    pro_ids = str(request.json_body.get('ids'))
    list_ids = list(pro_ids.split(","))
    ProductService.delete_product(list_ids)
    return Response(status=204)







    



