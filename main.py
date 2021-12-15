import os
from replit import db
import discord
import requests
import json
import random
import time
import cryptobat
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from keep_alive import keep_alive
from discord.ext import commands, tasks
from itertools import cycle
from web3 import Web3

# TO DO:
# Convert syntax to commands

# DECLARATIONS
my_secret_D = os.environ['TOKEN_D']
my_secret_CMC = os.environ['TOKEN_CMC']
#client = discord.Client()
WEB3_INFURA_PROJECT_ID = os.environ['TOKEN_I']
infura_url = 'https://mainnet.infura.io/v3/'+WEB3_INFURA_PROJECT_ID
w3 = Web3(Web3.HTTPProvider(infura_url))

client = commands.Bot(command_prefix = ".")
botstatus = cycle([])

masterlist1000 = ('BHC','BTC', 'ETH', 'BNB', 'USDT', 'ADA', 'DOGE', 'XRP', 'DOT', 'USDC', 'UNI', 'ICP', 'LINK', 'BCH', 'LTC', 'MATIC', 'XLM', 'SOL', 'BUSD', 'VET', 'ETC', 'THETA', 'WBTC', 'EOS', 'TRX', 'FIL', 'XMR', 'AAVE', 'DAI', 'NEO', 'SHIB', 'MKR', 'MIOTA', 'CAKE', 'KLAY', 'KSM', 'BSV', 'FTT', 'XTZ', 'CRO', 'ATOM', 'HT', 'ALGO', 'LUNA', 'BTCB', 'LEO', 'RUNE', 'BTT', 'AVAX', 'COMP', 'DCR', 'DASH', 'HBAR', 'ZEC', 'UST', 'TFUEL', 'EGLD', 'CEL', 'XEM', 'YFI', 'TEL', 'CHZ', 'SUSHI', 'WAVES', 'HOT', 'SNX', 'ZIL', 'HNT', 'TUSD', 'MANA', 'ENJ', 'NEAR', 'PAX', 'ZEN', 'BAT', 'QTUM', 'NEXO', 'STX', 'MDX', 'BTG', 'ONE', 'DGB', 'REV', 'BAKE', 'GRT', 'ONT', 'NANO', 'BNT', 'ZRX', 'OKB', 'OMG', 'FTM', 'UMA', 'CELO', 'CHSB', 'CRV', 'SC', 'HUSD', 'ICX', 'RVN', 'ANKR', 'XDC', 'KCS', 'FLOW', '1INCH', 'REN', 'LPT', 'QNT', 'AR', 'VGX', 'IOST', 'WRX', 'RSR', 'BCD', 'KNC', 'LSK', 'LRC', 'XVG', 'SKL', 'RLC', 'CKB', 'DENT', 'CFX', 'ERG', 'GT', 'RENBTC', 'SNT', 'USDN', 'VTHO', 'OGN', 'BTMX', 'XVS', 'REEF', 'MAID', 'KAVA', 'STORJ', 'GLM', 'BTCST', 'INJ', 'EWT', 'OCEAN', 'REP', 'ONG', 'GNO', 'NKN', 'ABBC', 'CTSI', 'IOTX', 'FET', 'WAXP', 'CELR', 'NMR', 'SRM', 'FUN', 'OXT', 'ALPHA', 'PROM', 'SAND', 'CVC', 'ARDR', 'STMX', 'BAL', 'STEEM', 'WOO', 'UQC', 'NU', 'SUN', 'KMD', 'SXP', 'STRAX', 'ANT', 'ORBS', 'AMPL', 'DODO', 'MED', 'ZB', 'MCO', 'BAND', 'UBT', 'BTS', 'HIVE', 'ZKS', 'VLX', 'HXRO', 'COTI', 'WIN', 'JST', 'ARK', 'MONA', 'WAN', 'POLY', 'XHV', 'MTL', 'XOR', 'BORA', 'FX', 'UTK', 'MLN', 'RIF', 'AVA', 'DIVI', 'HEX', 'CTC', 'SAFEMOON', 'WBNB', 'FIDA', 'FEI', 'CCXX', 'AMP', 'TTT', 'DFI', 'STETH', 'XYM', 'HBTC', 'ARRR', 'XWC', 'LUSD', 'THR', 'vBNB', 'NXM', 'INO', 'BEST', 'ORC', 'MINA', 'OMI', 'BOTX', 'PUNDIX', 'ZLW', 'BCHA', 'HEDG', 'MIR', 'HNC', 'AXS', 'RAY', 'TKO', 'SUSD', 'XIN', 'SOLO', 'PERP', 'ALCX', 'TRIBE', 'DAWN', 'KSP', 'KLV', 'AGI', 'SYBC', 'XPRT', 'MVL', 'ORN', 'YOUC', 'AKT', 'ANC', 'TLM', 'ETN', 'TITAN', 'MATH', 'REV', 'LINA', 'DRS', 'NWC', 'vBTC', 'RPL', 'FORTH', 'C20', 'RFOX', 'vXVS', 'KEEP', 'GNY', 'PHA', 'ELF', 'SYS', 'RDD', 'META', 'SFP', 'TWT', 'AUDIO', 'LYXe', 'TOMO', 'PPT', 'BADGER', 'MARO', 'GUSD', 'MX', 'POLS', 'WNXM', 'OXY', 'QUICK', 'ROSE', 'QKC', 'SAPP', 'BTM', 'LOC', 'RNDR', 'STRK', 'EPS', 'ALICE', 'IQ', 'TRAC', 'ASTA', 'FRAX', 'SCRT', 'EUM', 'POWR', 'PAXG', 'DNT', 'PRQ', 'DKA', 'vETH', 'NOIA', 'ADX', 'MLK', 'TRB', 'BLCT', 'DAO', 'XNC', 'HNS', 'PAC', 'BNANA', 'HTR', 'HOGE', 'SWAP', 'RLY', 'KIN', 'AION', 'SURE', 'CENNZ', 'PNK', 'KAI', 'MWC', 'MFT', 'vUSDC', 'XCM', 'EURS', 'VAI', 'CHR', 'XYO', 'CREAM', 'GAS', 'MBN', 'NYE', 'SNL', 'BCN', 'TROY', 'MXC', 'VRA', 'RAMP', 'FIRO', 'SNM', 'GALA', 'UOS', 'LIT', 'OXEN', 'REQ', 'IRIS', 'EXRD', 'FLM', 'NRG', 'GRN', 'MASK', 'DIA', 'STC', 'ALBT', 'PCX', 'CRU', 'SUPER', 'LON', 'NRV', 'CRE', 'SERO', 'BOND', 'APL', 'LOTTO', 'LQTY', 'LOOM', 'BIFI', 'BZRX', 'BURGER', 'aEth', 'RGT', 'ERN', 'TLOS', 'ELON', 'VRSC', 'DVI', 'DATA', 'TT', 'YFII', 'PEAK', 'BEAM', 'AKRO', 'GRS', 'BOA', 'QC', 'WOZX', 'WHALE', 'DX', 'HEGIC', 'RBTC', 'POND', 'DDX', 'DEGO', 'LAMB', 'ELA', 'CTK', 'IGNIS', 'LTO', 'KDA', 'ATRI', 'JGN', 'WTC', 'BLZ', 'AE', 'BEL', 'EDG', 'CUMMIES', 'SBD', 'ZNN', 'CORE', 'SOLVE', 'VSP', 'BELT', 'NULS', 'RFR', 'NSBT', 'BDX', 'AXEL', 'STPT', 'TSHP', 'DAG', 'WICC', 'ATT', 'KARMA', 'EMC2', 'STAKE', 'TORN', 'PIVX', 'FSN', 'MBL', 'BTU', 'SLP', 'HAI', 'DSLA', 'vBUSD', 'PRO', 'LA', 'DRGN', 'DAD', 'PRT', 'PAID', 'LDO', 'HUM', 'ARPA', 'IHF', 'BFT', 'OM', 'GXC', 'API3', 'HARD', 'LBC', 'MITH', 'CXO', 'BFC', 'ANY', 'LGCY', 'ERC20', 'HMR', 'SFI', 'EDR', 'NXS', 'SHR', 'CUSD', 'TRU', 'UPP', 'GLCH', 'KRT', 'PZM', 'AUCTION', 'RKN', 'VSYS', 'NIM', 'AERGO', 'BAR', 'GET', 'ULT', 'VISR', 'DUSK', 'CET', 'DGD', 'QQQ', 'SUKU', 'SPI', 'RARI', 'TVK', 'AQT', 'CTXC', 'FRONT', 'ARMOR', 'MOF', 'HC', 'VITE', 'COS', 'CVP', 'NXT', 'VTC', 'BASID', 'FWT', 'MET', 'CLO', 'DOCK', 'PYR', 'UNFI', 'SNTVT', 'FIO', 'MRPH', 'BAX', 'DMT', 'HPT', 'BURST', 'VID', 'PIB', 'ILV', 'MOC', 'FARM', 'ID', 'SLT', 'VERI', 'MUSD', 'SRK', 'BSCPAD', 'FRM', 'XPR', 'GHST', 'AMO', 'DBC', 'ALEPH', 'EOSC', 'KYL', 'DPR', 'CND', 'PPC', 'UBX', 'PAI', 'RAI', 'RVP', 'XSN', 'FREE', 'CITY', 'KEY', 'CONV', 'USDX', 'DERO', 'SWTH', 'DG', 'QTCON', 'FXS', 'REVV', 'CVT', 'KICK', 'PNT', 'ROUTE', 'DEXT', 'ZEON', 'BNK', 'RCN', 'SOC', 'MHC', 'OBSR', 'BAN', 'PXL', 'YLD', 'BIP', 'SWINGBY', 'MAPS', 'ZCN', 'ZEE', 'PDEX', 'STAX', 'LOWB', 'NEX', 'ASK', 'AIOZ', 'BTRS', 'mSLV', 'BMI', 'PHB', 'WING', 'MASS', 'BMX', 'FINE', 'BOR', 'TNC', 'NCASH', 'GO', 'DIP', 'UFT', 'TMTG', 'mTSLA', 'SKY', 'IDEX', 'MOD', 'KAN', 'XSGD', 'NEST', 'DOGET', 'PNG', 'OLY', 'SOUL', 'ARIA20', 'mQQQ', 'QSP', 'VIDY', 'NAS', 'PERL', 'FXF', 'RAD', 'vUSDT', 'SUTER', 'XDB', 'mBABA', 'HUNT', 'BF', 'EAURIC', 'mTWTR', 'mAAPL', 'FLUX', 'WXT', 'ZANO', 'GRIN', 'AOA', 'NFTX', 'mMSFT', 'CAS', 'mUSO', 'ANW', 'mNFLX', 'USDK', 'VEE', 'AST', 'DEP', 'GBYTE', 'KP3R', 'PROPS', 'DVPN', 'INSUR', 'DG', 'NIF', 'ALY', 'QASH', 'BOSON', 'NMC', 'NEBL', 'CUDOS', 'HELMET', 'GTO', 'BONDLY', 'WABI', 'FOR', 'UPUNK', 'VIDT', 'BTR', 'BZ', 'GAME', 'BHAO', 'TCT', 'BAAS', 'TONE', 'DREP', 'APIX', 'MUSH', 'RING', 'MCI', 'XRT', 'AITRA', 'ONE', 'DF', 'JULD', 'SALT', 'BASIC', 'RDN', 'CFi', 'CUT', 'VITAE', 'WEST', 'DAC', 'GTN', 'COCOS', 'MDT', 'mAMZN', 'ARDX', 'APPC', 'HEZ', 'DUCATO', 'CARD', 'FCT', 'DCN', 'LMT', 'GAL', 'DEXE', 'NAV', 'APY', 'AUTO', 'LIKE', 'FST', 'TON', 'DVC', 'ESD', 'CORA', 'GVT', 'PSG', 'ZAP', 'EVZ', 'WOW', 'SOCKS', 'CDT', 'OXB', 'mIAU', 'SIX', 'QCX', 'CRPT', 'vLINK', 'MPH', 'IFC', 'FCT', 'COVER', 'NLG', 'PICKLE', 'VIA', 'ONG', 'MIX', 'LCMS', 'PI', 'DDIM', 'BAO', 'FLETA', 'KTN', 'DAPP', 'UNCX', 'STRONG', 'S4F', 'XCUR', 'BUX', 'XED', 'MDA', 'K21', 'LYM', 'EL', 'RFUEL', 'AEON', 'BLANK', 'mVIXY', 'vSXP', 'TRY', 'SPC', 'MTA', 'DYN', 'CWS', 'MITX', 'DXD', 'NEW', 'QRL', 'KDAG', 'ICHI', 'OAX', 'SAKE', 'LCX', 'BTSE', 'MTV', 'DORA', 'TRTL', 'BRD', 'PENDLE', 'BIKI', 'VAL', 'TIME', 'AWC', 'ARCH', 'DIGG', 'DHT', 'vLTC', 'BIDR', 'LGO', 'IBP', 'TRUE', 'FIS', 'GLQ', 'DMCH', 'ETP', 'LCC', 'ORAI', 'OPIUM', 'MARK', 'ACM', 'SLICE', 'CREDIT', 'PPAY', 'UBXT', 'USDJ', 'DOV', 'WOM', 'PAY', 'XDN', 'TRIAS', 'RINGX', 'PRE', 'SPIKE', 'TEMCO', 'BTCZ', 'BANK', 'WPR', 'BUNNY', 'GMB', 'RSTR', 'IDLE', 'RAINI', 'DNA', 'MEME', 'CS', 'GOC', 'ROOBEE', 'PTF', 'RBC', 'LAYER', 'NFY', 'VNT', 'EMRX', 'WPP', 'MRX', 'EASY', 'BIOT', 'JUV', 'CSP', 'OST', 'ABT', 'PROB', 'LABS', 'MUSE', 'TNB', 'OCTO', 'MWAT', 'SMART', 'SYLO', 'SHA', 'NVT', 'ELAMA', 'SWRV', 'TOP', 'BRG', 'IDV', 'EVX', 'BLOCK', 'BHD', 'PART', 'PLC', 'SENSO', 'SCC', 'FOAM', 'CMT', 'XCASH', 'WGR', 'MOON', 'BHP', 'BTC2', 'SHARD', 'PMON', 'MEETONE', 'IQN', 'UBQ', 'CBK', 'ENQ', 'HZN', 'DOUGH', 'MBOX', 'EFX', 'AMLT', 'POLK', 'NCT', 'PCL', 'SAITO', 'FNX', 'TERA', 'CYC', 'NIOX', 'ADK', 'BWF', 'RIO', 'YAXIS', 'DAFI', 'HORD', 'EXNT', 'CBC', 'SPARTA', 'HGET', 'UDOO', 'LTX', 'HPB', 'HAKKA', 'POA', 'PLR', 'DEC', 'MARSH', 'TENA', 'VNLA', 'SFT', 'ACT', 'SFUND', 'ABYSS', 'CRON', 'MOBI', 'TRV', 'APN', 'AME', 'ZYN', 'USDX', 'PLTC', 'MTRG', 'SAN', 'IPX', 'ΤBTC', 'VIB', 'MTH', 'TEN', 'PAINT', 'XSUTER', 'NPX', 'ANJ', 'BEPRO', 'CON', 'FKX', 'PKF', 'PUSH', 'WORLD', 'TRADE', 'ANCT', 'XMC', 'ODDZ', 'SPORE', 'YUSRA', 'AGA', 'RAZOR', 'BMXX', 'DUCK', 'SWFTC', 'APM', 'ZOOT', 'ACH', 'KRL', 'WATCH', 'OPCT', 'SHROOM', 'INF', 'VALOR', 'HTML', 'EBST', 'DMD', 'PMA', 'LEVL', 'ABL', 'BUY', 'HVN', 'NOKU', 'ITC', 'TXL', 'DTA', 'KONO', 'UIP', 'DLT', 'MXX', 'MAN', 'CGG', 'TAU', 'SCC', 'FLG', 'BLINK', 'ZT', 'L2', 'IGG', 'RAE', 'OCE', 'BTX', 'BTCP', 'OUSD', 'XIO', 'VEST', 'XEND', 'COVAL', 'TFBX', 'DOS', 'EGT', 'BSCS', 'MYST', 'KAT', 'RAVEN', 'QLC', 'TATA', 'BOND', 'ETHO', 'NAOS', 'CVR', 'RUFF', 'BDP', 'DEXA', 'THOR', 'ENS', 'XDEFI')
nonusr =  "You don't have any watchlist yet. Add one by using command: `$cryptoadd BTC`. You can add more than one coin by separating them with spaces: `$cryptoadd BTC ETH LUNA`"
botstatus = cycle(masterlist1000)



# EASTER EGGS
key_words = ["SATOSHI", "NAKAMOTO", "VITALIK", "KWON", "HOSKINSON", "CHARLES", "HODL"]
key_outputs = ["Hey, I know that guy.", "I think I saw him yesterday", "He still owes me 2 BTC!", "OMG!", "Buy the dip (and chips)!", "Scary!", "Sell! Sell! Sell!", "Buy! Buy! Buy!", "To the moon!", "Just HODL.", "Stay strong!", "Hmmm..", "Interesting..", "There's something there.."]

# FUNCTIONS : VALIDATE CRYPTO
def crypto_validate(inputlist):
  for x in inputlist:
    if x in masterlist1000:
        output = "OK"
    else:
        output = "I don't know this coin: " + x + ". Please try again."
        return output

  return output

# FUNCTIONS : DELETE FROM WATCHLIST
def crypto_del(cryptodel,whouser):
  userlist = db.keys()
  deleteditem = str()
#  firsttime = 0

  if str(whouser) in userlist:
    if "ALL" in cryptodel:
      del db[str(whouser)]
      cryptodelstat = "Your watchlist has been deleted."
    else:
      # Check if list is a valid crypto first
      crypto_val = crypto_validate(cryptodel)
      if crypto_val == "OK":
        usrdblist = db[str(whouser)]
        del db[str(whouser)]
        for w in cryptodel:
          usrdblist.remove(w)
          deleteditem = deleteditem + " " + w
        if len(usrdblist) == 0:
          del db[str(whouser)]
          deleteditem = "your watchlist."
        else:
          db[str(whouser)] = usrdblist
#        for w in usrdblist:
#          print(w)
#          if w in cryptodel:
#            deleteditem = deleteditem + " " + w
#          else:
#            if firsttime == 0:
#              db[str(whouser)] = [w]
#              firsttime = firsttime + 1
#            else:
#              db[str(whouser)].append(str(w))
#            print(db[str(whouser)])
        cryptodelstat = "I deleted " + deleteditem
      else:
        return crypto_val
  else:
    cryptodelstat = nonusr

  return cryptodelstat

# FUNCTIONS : ADD TO PERSONAL WATCHLIST
def crypto_add(cryptoaddlist,whouser):
  crypto_val = crypto_validate(cryptoaddlist)
  userlist = db.keys()
  if str(whouser) in userlist:
  # User already exist
    if crypto_val == "OK":
      for w in cryptoaddlist:
        db[str(whouser)].append(str(w))
    else:
      return crypto_val 
  else:
  # New user create
    if crypto_val == "OK":
      print(type(cryptoaddlist))
      db[str(whouser)] = cryptoaddlist
    else:
      return crypto_val

  return "Ok, I added them to your list."

# FUNCTIONS : SHOW FAVORITES
def crypto_fav(whouser):
  usrfav = db[str(whouser)]
  print(usrfav)
  currency = "USD"
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  final_text = "\n"
  for _ in usrfav:  
      parameters = {
      'symbol' : _,
      'convert' : currency,
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
        coin = data['data']

        lastupdate = coin[_]['last_updated'][0:16]
        lastupdate = lastupdate.split("T")
        lastupdate = lastupdate[0] + " @ " + lastupdate[1] + "UTC"
        lastupdate = "Data from CoinMarketCap as of " + lastupdate

        change24 = coin[_]['quote'][currency]['percent_change_24h']
        if change24 > 0:
          changedir = ":arrow_up:by " + f'{change24:,.2f}' + "%"
          coin_color = ":green_square:"
        else:
          changedir = ":arrow_down:by " + f'{change24:,.2f}' + "%"
          coin_color = ":red_square:"

        price = coin[_]['quote'][currency]['price'] 
#        price = f'{price:,.7f}'
        if price < 1:
          price = str(f'{price:,.7f}')
        else:
          price = str(f'{price:,.2f}')
        print(price)
        price_text = "\n**" + coin_color + _ +  "** " + price + currency + " | " + changedir
        
        final_text = final_text + price_text
        final_title = str(whouser) + "'s Watchlist (Changes in last 24hrs):"
        
        embed = discord.Embed(title=final_title, colour=discord.Colour(0x2a2ac2), url="https://cointmarketcap.com", description=final_text)

        embed.set_footer(text=lastupdate, icon_url="https://i2.wp.com/blog.coinmarketcap.com/wp-content/uploads/2019/06/wp-favicon.png?fit=512%2C512&ssl=1")
      except (ConnectionError, Timeout, TooManyRedirects) as e_code:
        print(e_code)
        price_text = e_code

  return embed

# FUNCTIONS : CALCULATE
def bot_calc(myequation):
  equationlist = myequation.split(" ")
  equationlist[1] = float(equationlist[1])
  equationlist[3] = float(equationlist[3])

  if equationlist[2] == "+" or equationlist[2] == "PLUS" or equationlist[2] == "ADD":
    myanwer = equationlist[1] + equationlist[3]
  elif equationlist[2] == "-" or equationlist[2] == "MINUS" or equationlist[2] == "SUBTRACT":
    myanwer = equationlist[1] - equationlist[3]
  elif equationlist[2] == "*" or equationlist[2] == "X" or equationlist[2] == "TIMES" or equationlist[2] == "MULTIPLIEDBY":
    myanwer = equationlist[1] * equationlist[3]
  elif equationlist[2] == "/" or equationlist[2] == "DIVIDEDBY":
    myanwer = equationlist[1] / equationlist[3]
  elif equationlist[2] == "^" or equationlist[2] == "**":
    myanwer = equationlist[1] ** equationlist[3]
      
  return myanwer
# FUNCTIONS END : CALCULATE

# FUNCTIONS : COINMARKETCAP TOP10
def get_top10():
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start':'1',
    'limit':'10',
    'convert':'USD'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': my_secret_CMC,
  }

  top10string = "RANK | COIN | PRICE | MARKET CAP"
  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    coins = data['data']
    count = 1
    top10list = ("TOP 10 CRYPTO BY MARKETCAP","RANK / COIN / PRICE / MARKET CAP")
    for x in coins:
      top10price = x['quote']['USD']['price']
      # Cleanup Decimal Places of price for small and large numbers
      if top10price < 3:
        top10price = str(f'{top10price:,.7f}')
      else:
        top10price = str(f'{top10price:,.2f}')
      # Cleanup Market Cap to Billions
      top10cap = x['quote']['USD']['market_cap'] / 1000000000
      # Concatenate whole line
      top10item = str(count) + ") **" + x['symbol'] + "** \t| Price: " + top10price + " USD \t| MCAP: $ " + str(f'{top10cap:,.2f}') + "B"
      top10string = top10string + "\n " + str(top10item)
      top10list = top10list + (str(top10item),)
      count = count + 1
      footertime = str(x['quote']['USD']['last_updated'][0:16])
      footertime = footertime.split("T")
      footerstring = "Data from CoinMarketCap as of " + str(footertime[0]) + " @ " + str(footertime[1]) + "UTC"
    # END FOR LOOP

# EMBED FORMATTING
      embed = discord.Embed(title="TOP 10 COINS BY MARKET CAP", colour=discord.Colour(0x2a2ac2), url="https://coinmarketcap.com", description=top10string)

      embed.set_footer(text=footerstring, icon_url="https://i2.wp.com/blog.coinmarketcap.com/wp-content/uploads/2019/06/wp-favicon.png?fit=512%2C512&ssl=1")

  except (ConnectionError, Timeout, TooManyRedirects) as e_code:
    print(e_code)

  return(embed)
# FUNCTIONS END : COINMARKETCAP TOP10

# FUNCTIONS : COINMARKETCAP PRICE
def get_price(crypto,currency):
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  parameters = {
  'symbol' : crypto,
  'convert' : currency,
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
    coin = data['data']
    lastupdate = coin[crypto]['last_updated'][0:16]
    lastupdate = lastupdate.split("T")
    lastupdate = str(lastupdate[0]) + " @ " + str(lastupdate[1])    
    crank = coin[crypto]['cmc_rank']
    change24 = coin[crypto]['quote'][currency]['percent_change_24h']
    if change24 > 0:
      changedir = ":green_square::arrow_up:by " + f'{change24:,.2f}' + "% in the past 24hrs."
    else:
      changedir = ":red_square::arrow_down:by " + f'{change24:,.2f}' + "% in the past 24hrs."

    price = coin[crypto]['quote'][currency]['price'] 
    price = f'{price:,.7f}'
    price_text = "1 " + crypto + " = " + currency + " " + str(price) + " as of " + lastupdate + " | " + changedir + "Market Cap Rank #" + str(crank)
  except (ConnectionError, Timeout, TooManyRedirects) as e_code:
    print(e_code)
    price_text = e_code

  return(price_text)
# FUNCTIONS END : COINMARKETCAP PRICE

# FUNCTIONS : COINMARKETCAP PRICE V2
def get_price2(crypto,currency,coin_qty=1,conv_mode="info"):

  # COINMARKETCAP API PRICE
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  parameters = {
  'symbol' : crypto,
  'convert' : currency,
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': my_secret_CMC,
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data1 = json.loads(response.text)
    coin = data1['data']

# COINMARKETCAP API METADATA
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
    parameters = {
    'symbol' : crypto
    }
    try:
      response = session.get(url, params=parameters)
      data2 = json.loads(response.text)
      coinmeta = data2['data']
    except (ConnectionError, Timeout, TooManyRedirects) as e_code:
      print(e_code)
      price_text = e_code

# COIN INFO
    coin_name = coin[crypto]['name']
    coin_symbol = coin[crypto]['symbol']
    coin_rank = coin[crypto]['cmc_rank']    

    coin_lastupdate = coin[crypto]['last_updated'][0:16]
    coin_lastupdate = coin_lastupdate.split("T")
    coin_lastupdate = "Data from CoinMarketCap as of " + str(coin_lastupdate[0]) + " @ " + str(coin_lastupdate[1]) + " UTC"

# COIN INFO - clean up price decimal
    # Remove Comma in Amount
    if type(coin_qty) == str:
      if "," in coin_qty:
        coin_qty = coin_qty.replace(",","")
    # Use correct mode
    if conv_mode == "crypto" or conv_mode == "info":
      coin_price = coin[crypto]['quote'][currency]['price'] * float(coin_qty)
    elif conv_mode == "fiat":
      coin_price = float(coin_qty) / coin[crypto]['quote'][currency]['price'] 

    if coin_price < 3: #TODO CONVERT THIS TO FUNCTION
      coin_price = str(f'{coin_price:,.7f}')
    else:
      coin_price = str(f'{coin_price:,.2f}')

# COIN INFO - create change phrase
    change24 = coin[crypto]['quote'][currency]['percent_change_24h']
    if change24 > 0:
      changedir = "\n**Price Change:** :green_square::arrow_up:by " + f'{change24:,.2f}' + "% in the past 24hrs."
    else:
      changedir = "\n**Price Change:** :red_square::arrow_down:by " + f'{change24:,.2f}' + "% in the past 24hrs."
    coin_change = changedir

 # COIN INFO - clean up big numbers format     
    coin_cap = coin[crypto]['quote'][currency]['market_cap'] / 1000000000
    coin_cap = "\n**Market Cap:** " + str(f'{coin_cap:,.2f}') + "**B** " + currency

    coin_supply_max = coin[crypto]['max_supply']
    if coin_supply_max != None:
      coin_supply_max = str(f'{coin_supply_max:,}')
      coin_supply_max = "\n**Max Supply:** " + str(coin_supply_max)
    else:
       coin_supply_max = "\n**Max Supply:** None"     

    coin_supply_circ = coin[crypto]['circulating_supply']
#    coin_supply_circ = str(coin_supply_circ)
    coin_supply_circ = str(f'{coin_supply_circ:,.0f}')
    coin_supply_circ = "\n**Circulating Supply:** " + coin_supply_circ
    
    coin_supply_tot = coin[crypto]['total_supply']
#   coin_supply_tot = str(coin_supply_tot)
    coin_supply_tot = str(f'{coin_supply_tot:,.0f}')
    coin_supply_tot = "\n**Total Supply:** " + coin_supply_tot

# COIN META    
    coin_desc = "\n\n" + coinmeta[crypto]['description']
    coin_logo = coinmeta[crypto]['logo']

# COIN TEXT BUILDS    
    coin_title = "$" + coin_symbol + " - " + coin_name + " || Rank: #" + str(coin_rank)
    if conv_mode == "crypto" or conv_mode == "info":
      coin_description = "``` " + str(coin_qty) + " " + coin_symbol + " = " + coin_price + " " + currency + "```" + coin_change
    # Removed coin details to simplify results
    # + coin_cap + coin_supply_max + coin_supply_circ + coin_supply_tot + coin_desc
    elif conv_mode == "fiat":  
      coin_description = "``` " + str(coin_qty) + " " + currency + " = " + coin_price + " " + coin_symbol + "```" + coin_change
    if conv_mode == "info":
    # Additional coin meta data for coin details/info
       coin_description += coin_cap + coin_supply_max + coin_supply_circ + coin_supply_tot + coin_desc

  except (ConnectionError, Timeout, TooManyRedirects) as e_code:
    print(e_code)
    price_text = e_code

# RICH MESSAGE EMBED BUILD
  embed = discord.Embed(title=coin_title, colour=discord.Colour(0x2a2ac2), url="https://coinmarketcap.com", description=coin_description)

  embed.set_thumbnail(url=coin_logo)
  embed.set_footer(text=coin_lastupdate, icon_url="https://i2.wp.com/blog.coinmarketcap.com/wp-content/uploads/2019/06/wp-favicon.png?fit=512%2C512&ssl=1") #TODO change this pic to CMC -DONE

  return(embed)
# FUNCTIONS END : COINMARKETCAP PRICE V2

# FUNCTIONS START : COINMARKETCAP WATCH
def watch_price(crypto,currency="USD"):

# COINMARKETCAP API PRICE
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  parameters = {
  'symbol' : crypto,
  'convert' : currency,
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': my_secret_CMC,
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data1 = json.loads(response.text)
    coin = data1['data']
    coin_price = coin[crypto]['quote'][currency]['price']

  except (ConnectionError, Timeout, TooManyRedirects) as e_code:
    print(e_code)
    price_text = e_code

  return(coin_price)
# FUNCTIONS END : COINMARKETCAP WATCH

############################################
# EVENTS : START BOT ON_READY
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game("Ask help: $cryptohelp"))
#  change_status.start()
  print('{0.user} is locked and loaded!'.format(client))
#  watch_mode = "OFF"
#  print(watch_mode)

############################################
# EVENTS : BACKGROUND TASKS
@tasks.loop(seconds=7200)
async def change_status():
  cryptostat = next(botstatus) 
  combostat = cryptostat + "|| Ask me: $cryptohelp"
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=combostat))
# WATCH MODE CODE
#  if watch_mode == "ON":
#    price_check = watch_price(crypto)
#    if price_check < watch_price:
#      await message.channel.send(crypto+" is below "+watch_price+".")

############################################
# BOT COMMANDS
@client.command()
async def clear(ctx,amount=2):
  await ctx.channel.purge(limit=amount)
#  await ctx.channel.send("Last "+str(amount)+" were deleted.")

# CONVERTED COMMANDS
@client.command()
async def convertcrypto(ctx, coin_qty:int,crypto:str,currency:str):
    coin_embed = get_price2(crypto,currency,coin_qty,"crypto")
    await ctx.channel.send(embed=coin_embed)

############################################
# EVENTS : ON_MESSAGE
@client.event
async def on_message(message):
  msg_eth = message.content
  msg = message.content.upper()
  whouser = message.author
  bot = client.user
# AVOIND BOT LOOP to MESSAGE ITSELF
  if message.author == bot:
    return

# HIDDEN COMMANDS
  if msg.startswith('$HI'):
    hey = "Hey, " + str(whouser) + "! What's up?"
    await message.channel.send(hey)

  if msg.startswith('$C1'):
    crypto = msg.split(" ")[1]
    if len(msg.split(" ")) == 2:
      currency = "USD"
    elif len(msg.split(" ")) == 3:
      currency = msg.split(" ")[2]
    price_text = get_price(crypto,currency)
    await message.channel.send(price_text)



# EASTER EGGS
  if any(word in msg for word in key_words):
    await message.channel.send(random.choice(key_outputs))    
# PREDICTION
  if msg.startswith('$CRYPTOPREDICT'):
    size = len(msg.split(" "))
    if size < 2:
      error_list = ["The future seems foggy.","I don't know COIN that is.","Give me a crypto to check.","Give me a coin to analyze","Give me something to work with."]
      await message.channel.send(random.choice(error_list))
    else:
      crypto = msg.split(" ")[1]
      prediction_list = [" will go up."," will go down."," will consolidate.","goes up and down, and move it all around.","? I don't know, ask your mommy."]
      prediction_txt = random.choice(prediction_list)
      prediction_msg = crypto + prediction_txt
      await message.channel.send("Analyzing...")
      time.sleep(1.5)
      await message.channel.send(prediction_msg)

# NORMAL COMMANDS
  if msg.startswith('$CRYPTOHELP'):
#    await message.channel.send("Commands:")
#    await message.channel.send("$TOP10 - shows the current top 10 coins by market cap")
#    await message.channel.send("$CRYPTO COIN CUR - shows the price of the selected cryptocurrency in selected fiat currency (ex. $crypto BTC PHP). If no currency is provided, it will default to USD.")
    await message.channel.send(content="**BASIC COMMANDS:** ```js\n$cryptoprice <COIN> <CURR>```This shows the current price of the cryptocurrency <COIN> in the target currency pair <CURR> (default is USD if left blank, can also be another cryptocurrency). \nExamples: `$cryptoprice BTC` or `$cryptoprice BTC PHP` or `$cryptoprice BTC ETH` ```$cryptotop10```This shows the current top 10 cryptocurrencies ranked by market cap \n\n**WATCHLIST COMMANDS**```$cryptolist```This shows your own custom watch list. You may start creating by using $cryptoadd (see below).```$cryptoadd <COIN> <COIN>...<COIN>```This will ADD cryptocurrencies to your own watch list. You may ADD one at a time or all at once. You may also use this command to ADD more later on. Ensure each coin is separated by space. \nExample: `$cryptoadd BTC ETH LUNA RUNE` ```\n$cryptodel <COIN> <COIN>...<COIN>```This will DELETE cryptocurrencies to your own watch list. You may DELETE one at a time or all at once. You may also use this command to DELETE more later on. Ensure each coin is separated by space. \nExample: `$cryptodel BTC ETH`\n**TIP:** You can reset your watch list by using `$cryptodel ALL` \n\n**CALCULATOR COMMANDS:**```$convertcrypto <AMOUNT> <COIN> <CURR/COIN>```Use this to convert an amount of cryptocurrency into fiat or to another cryptocurrency. \nExample: `$convertcrypto .5 BTC USD` or `$convertcrypto 10 ETH BTC` ```$convertfiat <AMOUNT> <CURR> <COIN>```Use this to convert an amount of cryptocurrency into fiat \nExample: `$convertfiat 5000 USD ETH` or `$convertfiat 150000 PHP ETH` ```$calc <NUMBER1> <OPERATION> <NUMBER2>```Use this to do simple two (2) numnber math operations. (Operands: + - * x /) Example: `$calc 100 x 200` \n\n**ETHEREUM SPECIFIC COMMANDS:**```$ETHBAL <ADDRESS> ```Use this to get a wallet's current ETH balance. \nExample: `$ETHBAL 0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B` ```$ETHGAS```Use this to get the current fastest gas fees. \nExample: `$ETHGAS`")

  if msg.startswith('$CALC'):
    calcanswer = bot_calc(msg)
    await message.channel.send(calcanswer)

  if msg.startswith('$CRYPTOTOP10'):
    top10 = get_top10()
    await message.channel.send(embed=top10)

# PORTFOLIO MANAGEMENT COMMANDS
  if msg.startswith('$CRYPTOADD'):
    cryptoaddlist = msg.split(" ")[1:]
    cryptoaddstat = crypto_add(cryptoaddlist,whouser)
    await message.channel.send(cryptoaddstat)    

  if msg.startswith('$CRYPTOLIST'):
    userlist = db.keys()
    if str(whouser) in userlist:
      usrfav = crypto_fav(whouser)
      await message.channel.send(embed=usrfav)
    else:
      await message.channel.send(nonusr)

  if msg.startswith('$CRYPTODEL'):
    cryptodellist = msg.split(" ")[1:]
    cryptodelstat = crypto_del(cryptodellist,whouser)
    await message.channel.send(cryptodelstat)  

# PRICE COMMANDS
  if msg.startswith('$CRYPTOPRICE'):
    crypto = msg.split(" ")[1]
    if len(msg.split(" ")) == 2:
      currency = "USD"
    elif len(msg.split(" ")) == 3:
      currency = msg.split(" ")[2]
    coin_embed = get_price2(crypto,currency,1,"info")
    await message.channel.send(embed=coin_embed)

# BATTLE COMMANDS
  if msg.startswith('$CRYPTOBATTLE'):
    await message.channel.send(cryptobat.main())

# PRICE WATCH COMMANDS
  if msg.startswith('$CRYPTOWATCH'):
    await message.channel.send("This command has been replaced. Use `$cryptolist` instead to check your watchlist.")
#    crypto = msg.split(" ")[2]
#    if crypto == "OFF":
#      watch_mode = "OFF"
#      await message.channel.send("Watch mode has been turned off.")
#    else:
#      if watch_mode == "ON":
#        await message.channel.send("I am already watching "+crypto+ " in case it hits "+watch_price+".")
#      else:
#      watch_price = msg.split(" ")[1]
#      watch_mode = "ON"
#      print(watch_price(crypto,"USD"))
#      await message.channel.send(watch_mode+": I will message you if "+crypto+"hits this price USD"+watch_price+".")

    

# CONVERT COMMANDS
  if msg.startswith('$CONVERTCRYPTO'):
    if len(msg.split(" ")) == 4:
      coin_qty = msg.split(" ")[1]
      crypto = msg.split(" ")[2]
      currency = msg.split(" ")[3]
      coin_embed = get_price2(crypto,currency,coin_qty,"crypto")
      await message.channel.send(embed=coin_embed)
    else:
      await message.channel.send("Incorrect syntax. Usage example: $convertcrypto 5 BTC USD or $convertcrypto 10 ETH BTC")

# CONVERT COMMANDS
  if msg.startswith('$CONVERTFIAT'):
    if len(msg.split(" ")) == 4:
      coin_qty = msg.split(" ")[1]
      crypto = msg.split(" ")[3]
      currency = msg.split(" ")[2]
      coin_embed = get_price2(crypto,currency,coin_qty,"fiat")
      await message.channel.send(embed=coin_embed)
    else:
      await message.channel.send("Incorrect syntax. Usage example: $convertfiat 50000 USD BTC or $ convertfiat 150000 PHP ETH")

# ETHEREUM COMMANDS
  if msg_eth.startswith('$ETHBAL') or msg_eth.startswith('$ethbal'):
    eth_address =  msg_eth.split(" ")[1]
    print(eth_address)
    eth_balance = w3.eth.get_balance(eth_address) / 1000000000000000000
    eth_balance = f'{eth_balance:,.6f}'
    await message.channel.send('Wallet balance is '+str(eth_balance)+' ETH')

  if msg_eth.startswith('$ETHGAS') or msg_eth.startswith('$ethgas'):
    eth_gas = w3.eth.estimateGas({'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601', 'from': '0x742d35Cc6634C0532925a3b844Bc454e4438f44e', 'value': 1000})
    print(eth_gas)  
    eth_gas = eth_gas / 1000  
    eth_gas = f'{eth_gas:.0f}'
    await message.channel.send('Current gas fee estimate for sending 1 ETH the fastest is '+str(eth_gas)+' gwei.')


#===== START ERRORS
@clear.error
async def clear_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(error)


# RUNBOT
keep_alive()
client.run(my_secret_D)
