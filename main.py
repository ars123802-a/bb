import math
import telegram
from aiogram import Bot, Dispatcher, executor, types
from binance.client import Client
from binance.enums import *
import requests



bot = Bot(token='2095550533:AAFYbvvCBYad_BAs2FrZfaSYJNGylFs4Xmw')
api_key = 'UIQN9WJCgzoxf4kg0FDqBHiuhw9cnDgREmTe1hQp6ASTYIujBSkVTActa2Lgwv0D'
secret_key = '7O9Ci3UJfkrZxXFQ6F19JwNvhUFJas3fLqCYaEJwPl0ch8yjJxH05v2ExdFBZ2ix'
client = Client(api_key,secret_key)
dp = Dispatcher(bot)
a = {'BTCUSDT':2,'EOSUSDT':3,'ADAUSDT':5,'BNBUSDT':3,'LINKUSDT':3,'QTUMUSDT':3,'RLCUSDT':4,'SUSHIUSDT':4,'SXPUSDT':4,'COMPUSDT':2,'BCHUSDT':2,'ETCUSDT':3,'MATICUSDT':5,'THETAUSDT':4,'ALICEUSDT':3,'NEARUSDT':4,'1INCHUSDT':4,'ALPHAUSDT':5,'ATOMUSDT':3,'GRTUSDT':5,'ONTUSDT':4,'LUNAUSDT':4,'SRMUSDT':4,'AKROUSDT':5, 'DOGEUSDT':6, 'FTMUSDT':6, 'TRBUSDT':3, 'CTKUSDT':5, 'LINAUSDT':5, 'DENTUSDT':6, 'KSMUSDT':3, 'LITUSDT':3, 'REEFUSDT':6, 'AXSUSDT':5,'XRPUSDT':4,'UNFIUSDT':3,'ZILUSDT':5,'COTIUSDT':5}



@dp.message_handler(content_types=['text'])
async def cmd_test1(message):
    string = message.text
    list = string.split()
    list_numbers = []
    for word in list:
        try:
            list_numbers.append(float(word))
        except ValueError:
            pass
    print(list_numbers)
    if 'Лонгу' or 'Шорту' in list:
        long_or_short = ''
        long_or_short_order = ''
        if 'Лонгу' in list:
            long_or_short = 'BUY'
            long_or_short_order = 'SELL'
        if 'Шорту' in list:
            long_or_short = 'SELL'
            long_or_short_order = 'BUY'
        name = list[1]
        name_1 = name.replace('#','')
        name_2 = name_1.replace('PERP','')
        name_3 = name_2.replace('USDT','')
        entry_point = list_numbers[1]
        target1 = list_numbers[5]
        target2 = list_numbers[6]
        target3 = list_numbers[7]
        target4 = list_numbers[8]
        target5 = list_numbers[9]
        target6 = list_numbers[10]
        stop_loss = list_numbers[13]
        print(target2)
        print(stop_loss)


        def toFixed(numObj, digits):
            return f"{numObj:.{digits}f}"

        def get_price(name_3: str) -> float:
            data = {'symbol': f'{name_3}USDT'}
            response = requests.get('https://api3.binance.com/api/v3/avgPrice', data)
            return float(response.json()['price'])
        price = get_price(name_3)
        trade_size = 400
        tick_size = 6
        trade_quantity = trade_size/price
        trade_quantity_str = "{:0.0{}f}".format(trade_quantity, tick_size)

        symbol_info = client.get_symbol_info(name_2)
        step_size = 0.0
        for f in symbol_info['filters']:
            if f['filterType'] == 'LOT_SIZE':
                step_size = float(f['stepSize'])
        precision = int(round(-math.log(step_size, 10), 0))
        quantity = float(round(trade_quantity, precision))
        if 'очень высокая точность' in string and 'отличная динамика' in string or 'очень высокая точность' in string and 'хорошая динамика' in string or 'высокая точность' in string and 'отличная динамика' in string or 'высокая точность' in string and 'хорошая динамика' in string:
            client.futures_create_order(symbol=name_2, side=long_or_short, type='STOP_MARKET', quantity=quantity, stopPrice=toFixed(float(entry_point), a[name_2]))
            client.futures_create_order(symbol=name_2, side=long_or_short_order, type='LIMIT', quantity=quantity, price=toFixed(float(target2), a[name_2]), timeInForce='GTC')
            client.futures_create_order(symbol=name_2, side=long_or_short_order ,type='STOP_MARKET', quantity=quantity, stopPrice=toFixed(float(stop_loss), a[name_2]), reduceOnly='true')
            print('Order was made')
        else:
            print('Order was not made')
    else:
        print('---')
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
