# test_agro

### Endpoint

- /customer
- /product
- /order

Modo de uso de endpoint customer, product y order
### Método GET
Lista todos los customer
- /customer

Lista un customer
- /customer?id=1

## Método POST
- /customer

```json
    {
        "name": "JAMIL",
        "age": 39,
        "house_type": "LUXURY"
    }
```

## Método PATCH
- /customer
Actualiza name y age
```json
    {
        "id": 1,
        "name": "JAMIL",
        "age": 39,
    }
 ```
Actualiza  name,age y house_type
 ```json
   {
        "id": 1,
        "name": "JAMIL",
        "age": 39,
        "house_type": "LUXURY"
    }
 ```
 
 Actualiza  name
 ```json
   {
        "id": 1,
        "name": "JAMIL",
    }
 ```
 ## Método DELETE
 
 Elimina una lista de ids
  ```json
   {
        "ids": "1,2,"
    }
 ```
 
# JSON Customer
   ```json
     {
        "id": 2,
        "name": "ANA",
        "age": 38,
        "house_type": "VERY LUXURY"
    }
   ```
   
# JSON Product
 ```json

    {
        "id": 1,
        "quantity": 10,
        "price": "10",
        "product": "COCA"
    }
 ```

# JSON Order
 ```json
 {
    "id": 4,
    "quantity": 10,
    "time": "05/04/2022, 02:21:52",
    "customer_id":1, 
    "product_id": 1
}
 ```
# Post FormData keys
quantity, customer_id, price_id, Authorization con valor Bearer: 123456987*/-ABC
Solo metodo post
/order

