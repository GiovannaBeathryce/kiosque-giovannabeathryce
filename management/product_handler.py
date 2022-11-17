from menu import products
import collections

def get_product_by_id(product_id: int):
    for item in products:
        if item['_id'] == product_id:
            return print(item)
    print({})
    ...


def get_products_by_type(type_product: str):
    p = []
    for item in products:
        if item['type'] == type_product:
            p.append(item)
    print(list(p))
    ...


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

    print(f'Products Count: {number_products} - Average Price: ${media:,.2f} - Most Common Type: {highest_occurrence[0]}')
    ...

