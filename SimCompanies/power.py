import requests


class Power:
    ''' Get the current market price for power based on the quality of power. '''
    
    market_url = 'https://www.simcompanies.com/api/v2/market/1'
    market_json = ''
    market_prices = []
    market_fee = 0.03 # percent taken for using the exchange

    def __init__(self, quality=None):
        if quality == None:
            self.quality = 0
        else:
            self.quality = quality
        self.get_json()
        self.get_by_quality()
        

    def get_json(self):
        r = requests.get(self.market_url)
        self.market_json = r.json()

    def get_by_quality(self):
        for key in self.market_json:
            if key['quality'] == self.quality:
                self.market_prices.append(key['price'])

    def get_highest_price(self):
        ''' Return the highest price found listed for that qulity.'''
        return self.market_prices[-1]

    def get_lowest_price(self):
        ''' Return the lowest price found listed for that qulity.'''
        return self.market_prices[0]

    def get_difference(self):
        ''' Return the difference between the highest and lowest price.'''
        return self.market_prices[-1] - self.market_prices[0]

    def exchange_lowest_price(self, quantity=None):
        if quantity == None:
            quantity = 1000000
        '''Return the money that would be earned selling X quantity on the exchange'''
        list_price = self.market_prices[0] * quantity
        return list_price * (1 - self.market_fee)

    def contract_sell_price(self, quantity=None):
        if quantity == None:
            quantity = 1000000
        e = self.exchange_lowest_price(quantity)
        return e / quantity
        

    

def contract(price, quantity):
    return price * quantity




if __name__ == "__main__":
    price = 0.238
    c = contract(price, 1000000)
    p = Power(quality=3)
    
    print("Lowest Exchange Price @ 1,000,000 units")
    exchange = round(p.exchange_lowest_price(), 3)
    print(exchange)
    
    print("Contract Sell Equivelent per unit")
    should_sell_at = round(p.contract_sell_price(), 3)
    print(should_sell_at)
    
    print("Meet in the middle per unit")
    combine = should_sell_at + price
    divide = combine / 2
    print(round(divide, 3))
    
