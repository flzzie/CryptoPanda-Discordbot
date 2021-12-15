# CRYPTO BOT - A bot that can help you track the prices of different crypto currencies

This bot helps groups of friends or traders to keep track of crypto currency prices (via Coin Market Cap API). Each user can create and manage their own unique watchlist to easily track multiple coins at a time.

## Available commands:
#### BASIC COMMANDS: 
  - **$cryptohelp** - to show the list of available commands
  - **$cryptotop10** - shows the current top 10 cryptocurrencies by market cap
  - **$cryptoprice** *<COIN> <CURR>* - this shows the current price of the selected crypto currency in the target fiat amount
   > Where:
   > - *<COIN>* -  Ticker symbol of cryptocurrency (e.g. BTC, ETH, LUNA, etc.)
   > - *<CURR>* - Target fiat currency value of the crypto currency (e.g. USD, PHP, AUD, etc.)
   
   > Example: $crypto BTC USD
   
   > TIP: You may also convert from one cryptocurrency to another

   > Example: $crypto BTC ETH
#### WATCHLIST MANAGEMENT COMMANDS: 
  - **$cryptolist** - command to show your watch list. Each user has their own unique watchlist.
  - **$cryptoadd** *<COIN>* - command to create or add to your watchlist
   > Example: $cryptoadd BTC - This will add BTC to your watchlist
   
   > Example: $cryptoadd BTC ETH LUNA - You may also add more than one at a time by separating each coins with a space
  - **$cryptodel** *<COIN>* - command to delete items from your watchlist
   > Example: $cryptodel BTC - This will delete BTC from your watchlist
   
   > Example: $cryptodel BTC ETH LUNA - You may also delete more than one at a time by separating each coins with a space
   
   > TIP: You may delete or reset your watch list by using $cryptodel ALL

#### CALCULATOR COMMANDS: 
  - **$calc** - command to do simple two (2) number calculations (use these for operations: + - * /)
   > Example: $calc 2 + 2
  - **$convertcrypto** * <AMOUNT> <COIN> <CURR/COIN>* - this shows the current price of the selected crypto currency in the target fiat amount
   > Example: $convertcrypto 10000 DOGE USD or $convertcrypto 10000 DOGE ETH
  - **$convertfiat** *<AMOUNT> <CURR> <COIN>* - this shows the current price of the selected crypto currency in the target fiat amount
   > Example: $convertfiat 5000 USD ETH

#### ETHEREUM SPECIFIC COMMANDS: 
  - **$ETHBAL** *<ADDRESS>* - command to get the balance of an ethereum wallet
   > Example: $ethbal 0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B

  - **$ETHGAS** - command to get the current fastest gas fees.
   > Example: $ethgas

**DISCLAIMER**: This chat bot is for educational and entairtainment purposes only. Do not use for any trading or investing activity.
