from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from apikey import api, secret_api


class Pair:

    price = 0

    def __init__(self, name, client):
        self.name = name
        self.client = client
        # цена на момент создания пары
        self.price = float(self.client.get_margin_price_index(symbol=self.name)['price'])

    def check_currency(self):
        # Проверяем стоимость относительно цены на момент создания пары
        # При изменении цена на 1% программа выведет сообщение в консоль.
        currency = float(self.client.get_margin_price_index(symbol=self.name)['price'])
        percent = self.price / 100
        if self.price + percent <= currency:
            print('Цена на пару {pair}, растет'.format(pair=self.name))
            print('В данный момент цена равна {pair}'.format(pair=currency))
        elif self.price - percent >= currency:
            print('Цена на пару {pair}, падает'.format(pair=self.name))
            print('В данный момент цена равна {pair}'.format(pair=currency))


def start():
    # Задаем любую пару
    print('Задайте пару в формате, пример: XRPUSDT')
    pair = input('> ').upper()
    if len(pair) >= 6:
        my_account = Client(api, secret_api)
        test_pair = Pair(pair, my_account)
        while True:
            test_pair.check_currency()
    else:
        print('Неверный формат')
        start()


start()
