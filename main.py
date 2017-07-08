from xml.dom import minidom
import urllib2
from time import sleep 

#get the xml. Use http://gd2.mlb.com/components/game/mlb/year_2017/batters/519058.xml
html=urllib2.urlopen('http://gd2.mlb.com/components/game/mlb/year_2017/batters/519058.xml')

#parse the xml
xmldoc=minidom.parse(html)

#get the xml tag and access it using dictionary syntax
game=xmldoc.getElementsByTagName('game')

#can access tag attributes using dictionary index syntax
game_index=game[0]

#access attribute using dictionary syntax
batting_stats=game_index.attributes['batting']

#get values and turn the attirbutes into a int and use format to convert to binary
int_shr=int(batting_stats.value)


#format(value, '04' lead spaces, b=binary)
bin_shr=format(int_shr, '04b')

print bin_shr

#put str into lists in order to iterate on lns 57 on down
bin_shr=list(bin_shr)

#define GPIO on/off functions here
#figure out runner on base status pattern 

    
def GPIO_hrs():
    print GPIO hrs
    #turn inning lights on or off from bin_current_inning_list 
    if bin_shr[0]== '1':
        print ' first on'
    else:
        print ' first off'
    if bin_shr[1]== '1':
        print ' second on'
    else:
        print ' second off'
    if bin_shr[2]== '1':
        print ' third on'
    else:
        print ' third off'
    if bin_shr[3]== '1':
        print ' fourth on'
    else:
        print ' fourth off'
    if bin_shr[4]== '1':
        print ' fifth on'
    else:
        print ' fifth off'    
        
#loop 
while True:
 
    #GPIO functions
    GPIO_hrs()
    sleep(60)
    
