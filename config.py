import strategies
import datetime

# fmt:off

alpacaKey        = "PKMLTJHQBITIULAGEU9J"
alpacaSecretKey  = "beuquAzOgRVujbba4qBkNnG7y/NqzJLD3U1Az5C6"
finnhubKey       = "bracvl7rh5rf5hpo2ia0"
quandlKey        = "e_xBiTWo2xX28_vxFL9a"
tiingoKey        = '05cbda12baab2f7ed96be81bc6a2c2d809572553'

startCash        = 10000
fromDate         = datetime.date(2018, 1, 1)
toDate           = datetime.date(2020, 1, 1)
ticker           = 'NKE'
tradingFrequency = 'daily'  # 'minute' or 'daily'
strategy         = strategies.myStrategy
broker_commision = 0.001