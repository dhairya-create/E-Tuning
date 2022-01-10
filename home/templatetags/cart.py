from django import template

register = template.Library() 

@register.filter(name = 'is_in_cart')
def is_in_cart(product , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False

@register.filter(name = 'cart_quantity')
def cart_quantity(product , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0

@register.filter(name = 'stock_quantity')
def stock_quantity(product , message):
    keys = message.keys()
    for id in keys:
        if int(id) == product.id:
            return message.get(id)
    return 0


@register.filter(name = 'price_total')
def price_total(product , cart):
    return product.product_price * cart_quantity(product , cart)

@register.filter(name = 'total_cart_price')
def total_cart_price(product , cart):
    sum = 0
    for i in product:
        sum += price_total(i , cart)
    return sum

     
