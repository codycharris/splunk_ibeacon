# sample beacon event generator
# sts 8/6/2014
#
# NOTES:
# - Events [ab]use the beacon_macaddr field such that it can be used in lieu of a host field 
# - RRSI values are selected randomly from a set of valid points
# - between each loop there is a 5-second nap
#
#

import sys
from time import sleep, gmtime, strftime 
import random

rssi_values = [60, 90, 99, 59, 62, 78, 64, 59, 86, 59, 72, 88 ];
rssi_fluct = [ 0, -5, 5 ];

i = 0;


events = [
    '{ "Timestamp":"$ts$", "beacon_macaddr":"R4", "beacon_uuid":"$beacon$","beacon_major":"13034","beacon_minor":"2024","tx_pwr_1m":"-59","RSSI":"-$rssi$" }',
    '{ "Timestamp":"$ts$", "beacon_macaddr":"R4", "beacon_uuid":"$beacon$","beacon_major":"13034","beacon_minor":"2024","tx_pwr_1m":"-59","RSSI":"-$rssi$" }',
    '{ "Timestamp":"$ts$", "beacon_macaddr":"R4", "beacon_uuid":"$beacon$","beacon_major":"13034","beacon_minor":"2024","tx_pwr_1m":"-59","RSSI":"-$rssi$" }'
 ]


while True:

#   Generate new timestamp
    ts = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    i+=1
#   Generate beaconId 
    beaconId = str(random.randint(1,3))
    #   Select a random rssi value 
    basep = rssi_values[random.randint(0,len(rssi_values)-1)];

    print 'New base RSSI value: '+str(basep)

    for x in range(0, len(events)):
        p = basep + ((basep * rssi_fluct[x])/100) ;
        print events[x].replace('$ts$', ts).replace('$beacon$', beaconId).replace('$rssi$', str(p))
        sys.stdout.flush()

    sleep(5)
    
#   In case I forget to kill it
    if( i>10000): 
        exit()