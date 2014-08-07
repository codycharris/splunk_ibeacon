# sample beacon event generator
# sts 8/6/2014
#
# NOTES:
# - Events [ab]use the beacon_macaddr field such that it can be used in lieu of a host field 
# - RRSI values are random with values between 59 and 99
# - between each loop there is a random sleep interval between 5 and 15 seconds
#
#

import sys
from time import sleep, gmtime, strftime 
import random

i = 0;
events = [
    '{ "Timestamp":"$ts$", "beacon_macaddr":"R1", "beacon_uuid":"1","beacon_major":"13034","beacon_minor":"2024","tx_pwr_1m":"-59","RSSI":"-$rssi$" }',
    '{ "Timestamp":"$ts$", "beacon_macaddr":"R2", "beacon_uuid":"1","beacon_major":"13034","beacon_minor":"2024","tx_pwr_1m":"-59","RSSI":"-$rssi$" }',
    '{ "Timestamp":"$ts$", "beacon_macaddr":"R3", "beacon_uuid":"1","beacon_major":"13034","beacon_minor":"2024","tx_pwr_1m":"-59","RSSI":"-$rssi$" }',
    '{ "Timestamp":"$ts$", "beacon_macaddr":"R1", "beacon_uuid":"2","beacon_major":"13034","beacon_minor":"2024","tx_pwr_1m":"-59","RSSI":"-$rssi$" }',
    '{ "Timestamp":"$ts$", "beacon_macaddr":"R2", "beacon_uuid":"2","beacon_major":"13034","beacon_minor":"2024","tx_pwr_1m":"-59","RSSI":"-$rssi$" }',
    '{ "Timestamp":"$ts$", "beacon_macaddr":"R3", "beacon_uuid":"2","beacon_major":"13034","beacon_minor":"2024","tx_pwr_1m":"-59","RSSI":"-$rssi$" }',
    '{ "Timestamp":"$ts$", "beacon_macaddr":"R1", "beacon_uuid":"3","beacon_major":"13034","beacon_minor":"2024","tx_pwr_1m":"-59","RSSI":"-$rssi$" }',
    '{ "Timestamp":"$ts$", "beacon_macaddr":"R2", "beacon_uuid":"3","beacon_major":"13034","beacon_minor":"2024","tx_pwr_1m":"-59","RSSI":"-$rssi$" }',
    '{ "Timestamp":"$ts$", "beacon_macaddr":"R3", "beacon_uuid":"3","beacon_major":"13034","beacon_minor":"2024","tx_pwr_1m":"-59","RSSI":"-$rssi$" }'
 ]


while True:

#   Generate new timestamp
    ts = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    i+=1

    for x in range(0, len(events)):
        print events[x].replace('$ts$', ts).replace('$rssi$', str(random.randint(59,99)))
        sys.stdout.flush()

    sleep(random.randint(5,15))
    
#   In case I forget to kill it
    if( i>10000): 
        exit()