import json
import os
import datetime
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

# GLOBAL VARIABLES
my_secret_CMC = os.environ['TOKEN_CMC']
my_watch_list = ['ADA','BHC','BTC','BTT','DOGE','DOT','ETH','IOTA','LUNA','MIOTA','PUNDIX','RUNE','SHIB','SOL','TEL','USDT','VET']
rank_award = {0:':trophy:',1:':first_place:',2:':second_place:',3:':third_place:'}
player_value = {'JETH':0,'IVIN':0,'DANIEL':0,'PAOTI':0,}
player_rank = []
player_list = {
'JETH':{ 
'BTC':{
'port_entry':39690.09,
'port_alloc':300000,
},
'ETH':{
'port_entry':2438.92,
'port_alloc':300000
},
'LUNA':{
'port_entry':9.48,
'port_alloc':200000
},
'RUNE':{
'port_entry':11.58,
'port_alloc':100000
},
'DOT':{
'port_entry':25.02,
'port_alloc':50000
},
'SOL':{
'port_entry':35.09,
'port_alloc':50000
}},  
'PAOTI':{
'ETH':{
'port_entry':2438.92,
'port_alloc':500000,
},
'ADA':{
'port_entry':1.4663,
'port_alloc':200000
},
'TEL':{
'port_entry':0.02565902,
'port_alloc':200000
},
'MIOTA':{
'port_entry':1.1294,
'port_alloc':100000
}},
'DANIEL':{
'USDT':{
'port_entry':1.0000001,
'port_alloc':250000
},
'ETH':{
'port_entry':2438.92,
'port_alloc':200000
},
'VET':{
'port_entry':0.10533,
'port_alloc':150000
},
'BTT':{
'port_entry':0.00369370,
'port_alloc':150000
},
'MIOTA':{
'port_entry':1.1294,
'port_alloc':150000
},
'SHIB':{
'port_entry':0.00000907,
'port_alloc':50000
},
'DOGE':{
'port_entry':0.32945000,
'port_alloc':50000
}},
'IVIN':{
'BTC':{
'port_entry':39690.09,
'port_alloc':500000,
},
'ADA':{
'port_entry':1.46630,
'port_alloc':300000
},
'PUNDIX':{
'port_entry':1.40100,
'port_alloc':100000
},
'VET':{
'port_entry':0.10533,
'port_alloc':50000
},
'BHC':{
'port_entry':81.80,
'port_alloc':50000
}}}

######### START OF FUNCTIONS #########

def get_crypto_list():
    print("CMC API START:",datetime.datetime.now())
    process_start = datetime.datetime.now()
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'2000',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': my_secret_CMC,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        r_coin_list = data['data']
    except (ConnectionError, Timeout, TooManyRedirects) as e_code:
        print(e_code)
        r_coin_list = e_code
    
    print("CMC API RUNTIME:",datetime.datetime.now()-process_start)
    return r_coin_list
##########################
def update_player_data(coin_list):
    my_counter = 0
    rune_counter = 0
    #output_text = "**PORTFOLIO BATTLE PRICE UPDATES (past 24hrs):**"
    for x in coin_list:
        try:
            if x['symbol'] in my_watch_list:
                if x['symbol'] == 'RUNE' and rune_counter == 1:
                    continue
                for player in player_list:
                    #line_text = "" + player
                    #print(player)
                    for coins in player_list[player]:
                        if coins == x['symbol']:
                            player_list[player][coins]['port_curr_price'] = x['quote']['USD']['price']
                            player_list[player][coins]['port_value'] = player_list[player][coins]['port_alloc'] + (player_list[player][coins]['port_alloc']*((x['quote']['USD']['price'] - player_list[player][coins]['port_entry'])/player_list[player][coins]['port_entry']))
                            player_value[player] = player_value[player] + player_list[player][coins]['port_value']
                            if player_list[player][coins]['port_entry'] > player_list[player][coins]['port_curr_price']:
                                player_list[player][coins]['port_emoji'] = ":red_square:"
                            else:
                                player_list[player][coins]['port_emoji'] = ":green_square:"
                            my_counter += 1
                            if x['symbol'] == 'RUNE':
                                 rune_counter = 1            
            update_result = 0            
        except:
            print('Error with Coin Market Cap API')
            update_result = 4
    print('TOTAL LINES PROCESSED:',my_counter)
    return update_result
##########################
def number_format(number):
    if number > 1:
        if number > 100:
            return str(f'{number:,.0f}')
        else:
            return str(f'{number:,.2f}')
    elif number < 1:
        return str(f'{number:,.7f}')
##########################
def update_player_rank():
    sorted_values = sorted(player_value.values(), reverse=True)
    print(sorted_values)
    for amounts in sorted_values:
        for player in player_value:
            if player_value[player] == amounts:
                player_rank.append(player)
    print(player_rank)
    return 0
##########################    
def get_portfolio():
    rank_num = 1
    line_text = "**PORTFOLIO BATTLE - RANK UPDATES:**\n:trophy:**" + player_rank[0] + " is currently leading with $" + number_format(player_value[player_rank[0]]) + "\n:moneybag:Current prize: 0.002211 BTC or $" + number_format(0.002211*player_list['JETH']['BTC']['port_curr_price']) + "**\n"

    for player in player_rank:
        line_text = line_text + "\n** #" + str(rank_num) + rank_award[rank_num-1] + player + "'s Total Portfolio Value: $" + number_format(player_value[player]) + "**\nCOIN: CURRENT | ENTRY | ALLOCATION | VALUE\n"
        rank_num += 1
        for coins in player_list[player]:
            coins_port =  player_list[player][coins]['port_emoji'] + "**" + coins + "**: ``" + number_format(player_list[player][coins]['port_curr_price']) + "|" + number_format(player_list[player][coins]['port_entry']) + "|" + number_format(player_list[player][coins]['port_alloc']) + "|" + number_format(player_list[player][coins]['port_value'])  + "``\n"
            line_text = line_text + coins_port
    return line_text
##########################
def clear_variables():
  global player_value
  global player_rank
  player_value = {'JETH':0,'IVIN':0,'DANIEL':0,'PAOTI':0,}
  player_rank = []

def main():
    # PROCESS TIMER
    print("STARTING PROCESS:",datetime.datetime.now())
    process_start = datetime.datetime.now()
    
    # GET 2000 COINS FROM CMC API
    coin_list = get_crypto_list()

    # CREATE OUTPUT TEXT
    update_result = update_player_data(coin_list)
    if update_result == 0:
        # CREATE PLAYER RANK
        update_player_rank()
        my_output = get_portfolio()
    else:
        my_output = 'Error with Coin Market Cap API'
    
    clear_variables()
    
    print("ENDING PROCESS:",datetime.datetime.now())
    print('TOTAL RUNTIME:',datetime.datetime.now()-process_start)
    return my_output

######### MAIN RUN #########
if __name__ == '__main__':
    main()