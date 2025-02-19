def calculate_discount(price: int|float, discount: int|float) -> int|float:
    
    ## NOTE: this was the original function.. but because raw integer division will always return a float, its been modified to meet requirements for this.
    # return price - (price * discount / 100)
    
    if isinstance(price, int) and isinstance(discount, int):
        return price - (price * discount // 100)
    else:
        return price - (price * discount / 100)