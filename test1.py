from py5paisa import FivePaisaClient
from py5paisa.order import Order, OrderType, Exchange
cred={
    "APP_NAME":"5P56685593",
    "APP_SOURCE":"7684",
    "USER_ID":"YQ6y3WhMykk",
    "PASSWORD":"LUce2JoPriR",
    "USER_KEY":"LVZpSiwHCezU4JR6SOmY8sDYDUeiPRQ1",
    "ENCRYPTION_KEY":"v3nqheNlBondN8jOBtau2TN2WvGK8VWA"
    }

client = FivePaisaClient(email="abhis.s2009@gmail.com", passwd="abhi2010", dob="19891201",cred=cred)
client.login()


test_order = Order(order_type='B',exchange='N',exchange_segment='D', scrip_code = 37848, quantity=50, price=236.5,is_intraday=True)
client.place_order(test_order)