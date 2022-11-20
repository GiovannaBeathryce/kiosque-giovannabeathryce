from menu import products
import collections

menu = []

def get_product_by_id(product_id: int):
    for item in products:
        if item['_id'] == product_id:
            return item
    if product_id != int:
        raise TypeError("product id must be an int")
    return {}
    ...


def get_products_by_type(type_product: str):
    products_of_type = [item for item in products if item['type'] == type_product]

    if type(type_product) != str:
        raise TypeError("product type must be a str")
    
    return products_of_type


def menu_report():
    price = 0.00
    number_products = 0
    types = []

    for item in products:
        number_products += 1
        types.append(item['type'])
        price += float(item['price'])

    media = price/number_products
    number_of_occurrences= collections.Counter(types)
    highest_occurrence = list(number_of_occurrences.keys())

    return f'Products Count: {number_products} - Average Price: ${media:,.2f} - Most Common Type: {highest_occurrence[0]}'
    ...


def add_product(menu, *args):
    id = len(menu)
    id += 1
    new_product = {
            "_id": f'{id}',
            "title": f'{args[0]}',
            "price": f'{args[1]}',
            "rating": f'{args[2]}',
            "description": f'{args[3]}',
            "type": f'{args[4]}'
        }
    menu.append(new_product)

    created_product = [p for p in menu if p['_id'] == new_product['_id']]
    return created_product
    ...


