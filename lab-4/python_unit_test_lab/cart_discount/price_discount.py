def main():

    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?

def discount(item_prices):
    """ Function that returns the discount earned for a list of item prices.
    If a customer has ordered more than three items, the cheapest item is free.
    If a customer has ordered less than three items, function returns None value, 
    indicating customer is ineligible for the discount. 
    Ensures also that prices aren't negative numbers.
    This way another function can use this None value to determine what next to do.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """

    if type(item_prices) == list: # Ensure that item_prices is list object
        for price in item_prices:
            if price < 0:
                item_prices.remove(price) # Can't have negative prices - remove if so
    else:
        return None # If item_prices isn't a list

    if len(item_prices) >= 3: # Check if customer is eligible to recieve lowest priced item free
        item_prices.sort() # Sort list so that lowest price is first
        return item_prices[0] # Return lowest price    
    else:
        return None # Else user ineligible for discount

if __name__ == '__main__':
    main()