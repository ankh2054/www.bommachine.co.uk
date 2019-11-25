#Get BTC price
import cryptocompare





# Get BTC price 
def btcprice():
    # Retreive BTC data
    btcprice = cryptocompare.get_price('BTC',curr='USD')
    # Get current BTC price 
    btc_price = float(btcprice['BTC']['USD'])
    return btc_price
