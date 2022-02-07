# - *- coding: utf- 8 - *-
#chargement des dependances.
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
import pandas as pd
from pandas.io.json import json_normalize
import requests
import pytz
from datetime import datetime, timedelta
import os
import subprocess
import sys
os.chdir("path to binary")
wallet_cli = './helium-wallet'
hotSpotAddress = 'address of the hotspot'
wallet_tosend = 'fill with wallet of address'
os.environ['HELIUM_WALLET_PASSWORD'] = 'password of your wallet'
cg.get_price(ids='helium', vs_currencies='eur')
valeur = cg.get_price(ids='helium', vs_currencies='eur')['helium']
taux = valeur['eur']
#test connexion pour avoir le prix du moment
print(taux)

#definitions des periodes de date
now = datetime.today()
#before_yesterday = int(day)-2
yesterday = datetime.today() - timedelta(1)
oneWeekAgo = datetime.today() - timedelta(7)
before_yesterday = datetime.today() - timedelta(1)
yesterday_complete = yesterday.strftime('%Y-%m-%d')
before_yesterday_complete = before_yesterday.strftime('%Y-%m-%d')
oneWeekAgo_complete = oneWeekAgo.strftime('%Y-%m-%d')
today = now.strftime('%Y-%m-%d')
oneWeekAgo
yesterday_complete
oneWeekAgo_complete

r = requests.get("https://api.helium.io/v1/hotspots/"+hotSpotAddress+"/rewards?max_time="+today+"&min_time="+oneWeekAgo_complete)
#r = requests.get("https://api.helium.wtf/v1/hotspots/"+hotSpotAddress+"/rewards?max_time="+today+"&min_time="+oneWeekAgo_complete)
data1 = r.json()
data1
cursor=data1['cursor']
if data1['cursor']!='':
  #print(cursor)
  req = "https://api.helium.io/v1/hotspots/"+hotSpotAddress+"/rewards?max_time="+today+"&min_time="+oneWeekAgo_complete+"&cursor="+cursor
#  req = "https://api.helium.wtf/v1/hotspots/"+hotSpotAddress+"/rewards?max_time="+today+"&min_time="+oneWeekAgo_complete+"&cursor="+cursor
  r1 = requests.get(req)
  data1 = r1.json()
  df_hs=pd.DataFrame(data1['data'])
  df_hs.timestamp = pd.to_datetime(df_hs.timestamp)
#  df_hs.timestamp = df_hs.timestamp.dt.tz_convert('Europe/Paris')
else:
  df_hs=pd.DataFrame(data1['data'])
df_hs.timestamp = pd.to_datetime(df_hs.timestamp)
df_hs.timestamp = df_hs.timestamp.apply(lambda a: datetime.strftime(a,"%Y-%m-%d %H:%M:%S"))
df_hs['amount'] = df_hs['amount']/100000000
df_hs['Montant en Euro'] = df_hs['amount']*taux
df_hs["description"] = 'revenue de minage'
df_hs[['timestamp','amount','Montant en Euro','description']]
df_hs[df_hs['timestamp'].between(yesterday_complete,today)]
#df_hs[['timestamp','amount','Montant en Euro','description']].to_excel('revenue_minage '+today+'.xls')
df_hs[['timestamp','amount','Montant en Euro','description']]
#df_hs['timestamp']
gains = df_hs.amount.sum()
gainsHS= gains*0.4
gainsHS = round(gainsHS,7)
print(gainsHS)
commande = "pay one "+str(wallet_tosend)+" "+str(gainsHS)
fullcommnand= wallet_cli+"helium-wallet "+commande
print(fullcommnand)
pid=os.system(fullcommnand)
