json
{
	"order_type": "{{strategy.order.action}}",
	"exchange": "N",
	"exchange_segment": "D",
	"scrip_code": 51601,
	"quantity": 50,
	"price": "{{strategy.order.price}}",
	"is_intraday": true
}
Run on Local

set FLASK_APP = test1
python -m flask run

To view logs type in powershell

heroku logs -a nifty-test --tail

