# heliumpercentagetx

Install with pip the required libraries : pandas, coingecko-api 

This script permit to send automatically 40% of earned token to a dedicated wallet.
change values : 
path_to_wallet_cli = './helium-wallet-rs/bin/'
hotSpotAddress = 'address of the hotspot'
wallet_tosend = 'fill with wallet of address'
os.environ['HELIUM_WALLET_PASSWORD'] = 'password of your wallet'

and if you want to give more HNT to the destination wallet change value : 
gainsMicha= gains*0.4

with this version no money will go to the dest wallet  you must add -- commit at the end like this : 
fullcommnand= "/mnt/data/helium-wallet-rs/bin/helium-wallet "+commande + ' --commit'
to ensure that money is transfered (security reason :p) 
