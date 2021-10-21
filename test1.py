from flask import Flask, request, jsonify
app = Flask(__name__)
from py5paisa import FivePaisaClient
from py5paisa.order import *
import json

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

def order(OrderType, Exchange, ExchangeSegment, ScripCode, Quantity, Price, IsIntraday):
    try:
        #print("sending order")
        #order = bo_co_order(scrip_code = ScripCode, BuySell=OrderType, Qty=1, ExchType='D', Exch='N', RequestType='P', AtMarket=True)
        #place_order = client.bo_order(order)
        order = Order(order_type=OrderType,exchange=Exchange,exchange_segment=ExchangeSegment, scrip_code = ScripCode, quantity=Quantity, price=Price,is_intraday=IsIntraday, atmarket=True)
        place_order = client.place_order(order)
        print(place_order)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False

    return order
    
    
@app.route('/')
def hello_world():
    return 'Hello, Nagesh'

@app.route('/login')
def whatever():
  print("hello")
  login_response = client.login()
  print(login_response)
  return{
    "message": "Invalid passphrase"
}

@app.route('/webhook', methods=['POST'])
def webhook():
    print(request.data)
    data = json.loads(request.data)

    OrderType = "S"
    if data['order_type'] == "buy":
        OrderType = "B"
    Exchange = data['exchange']
    ExchangeSegment = data['exchange_segment']
    ScripCode = data['scrip_code']
    Quantity = data['quantity']
    Price = data['price']
    IsIntraday = data['is_intraday']
    #print(OrderType)
    """
    side = data['strategy']['order_action'].upper()
    tick = data['ticker']
    quantity = data['strategy']['order_contracts']
    formatQuantity = format(quantity, '.5')
    """
    order_response = order(OrderType, Exchange, ExchangeSegment, ScripCode, Quantity, Price, IsIntraday)

    #print(order_response)

    return{
        "code": "success",
        "message": "order Executed"
    }

#test_order = Order(order_type='B',exchange='N',exchange_segment='D', scrip_code = 37848, quantity=50, price=236.5,is_intraday=True)
#client.place_order(test_order)
