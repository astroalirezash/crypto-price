import requests
# import time

header = {
   'x-access-token': 'coinranking9cd015a1a4c71e5ade271f5323592f89a5b6b6113f3eaf12'
}

searched_coin = 'Bitcoin'
#
# while True:
#     response = requests.request('GET', f'https://api.coinranking.com/v2/search-suggestions?query={searched_coin}',
#                                 headers=header
#                                 )
#
#     res = response.json()['data']['coins']
#     # print(res)
#
#     coin = None
#
#     for i in res:
#         if i['name'] == searched_coin or i['symbol'] == searched_coin:
#             coin = i
#             break
#
#     if coin:
#         att_all = f'Coin Name: "{coin["name"]}", Symbol: "{coin["symbol"]}", Price: "{coin["price"]}"'
#         # print(att_all)
#     else:
#         print('No items found.')
#
#     print(f'Price of {coin["name"]}: {coin["price"]}')
#     time.sleep(10)
#     print('------------------------------------------------------------')


def res1(coin_name):
    try:
        response = requests.request('GET', f'https://api.coinranking.com/v2/search-suggestions?query={coin_name}',
                                    headers=header
                                    )

        res = response.json()['data']['coins']

        coin = None

        for i in res:
            if i['name'] == searched_coin or i['symbol'] == searched_coin:
                coin = i
                break

        if coin:
            att_all = f'{coin["name"]}/"{coin["symbol"]}" price: "{round(float(coin["price"]), 2)} USDT"'
            return att_all
        else:
            return 'Coin did not found!'
    except:
        print(ConnectionError(
            f'Unable to Connect "https://api.coinranking.com/v2/search-suggestions?query={coin_name}"'))
        return 'No Connection'
