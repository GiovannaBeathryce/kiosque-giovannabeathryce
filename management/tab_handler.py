from menu import products

def calculate_tab(menu, kwargs):
    subtotal = 0.00
    for i in kwargs:
        for p in menu:
            if p["_id"] == i['_id']:
                subtotal += p['price']*i['amount']
    return(f'subtotal:{subtotal:,.2f}')
    ...