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

points =  [ [60, 90, 99], 
            [90, 99, 90],
            [99, 90, 60],
            [90, 60, 90],
            [75, 75, 75],
            [70, 70, 90],
            [70, 90, 90]
        ]

i = 0;


events = [
    '{ "Timestamp":"$ts$", "beacon_macaddr":"R1", "beacon_uuid":"$beacon$","beacon_major":"13034","beacon_minor":"2024","tx_pwr_1m":"-59","RSSI":"-$rssi1$" }',
    '{ "Timestamp":"$ts$", "beacon_macaddr":"R2", "beacon_uuid":"$beacon$","beacon_major":"13034","beacon_minor":"2024","tx_pwr_1m":"-59","RSSI":"-$rssi2$" }',
    '{ "Timestamp":"$ts$", "beacon_macaddr":"R3", "beacon_uuid":"$beacon$","beacon_major":"13034","beacon_minor":"2024","tx_pwr_1m":"-59","RSSI":"-$rssi3$" }'
 ]


while True:

#   Generate new timestamp
    ts = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    i+=1
#   Generate beaconId 
    beaconId = str(random.randint(1,3))
#   Select random point 
    p = points[random.randint(0,len(points)-1)];

    for x in range(0, len(events)):
        print events[x].replace('$ts$', ts).replace('$beacon$', beaconId).replace('$rssi1$', str(p[0])).replace('$rssi2$', str(p[1])).replace('$rssi3$', str(p[2]))
        sys.stdout.flush()

    sleep(5)
    
#   In case I forget to kill it
    if( i>10000): 
        exit()