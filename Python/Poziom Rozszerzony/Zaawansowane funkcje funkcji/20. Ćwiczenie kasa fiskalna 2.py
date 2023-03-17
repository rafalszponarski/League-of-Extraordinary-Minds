import math as m

from cash1200 import finalPrice as f

    
def ultimateFinalPrice(price, discount, likedCustomer):
    if likedCustomer:
        return f(price, m.floor)-discount
    else:
        return f(price, m.ceil)-discount
    