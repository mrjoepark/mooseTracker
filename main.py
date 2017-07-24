import sys
from xml.dom import minidom
import urllib2
from time import sleep
import pygame
import RPi.GPIO as GPIO

pygame.mixer.init()
chant=pygame.mixer.Sound('/Users/JoePark/Desktop/Royals.wav')
bin_shr_check=[0]

GPIO.setmode(GPIO.BCM)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)



def GPIO_hrs():
    print bin_shr
    #turn inning lights on or off from bin_current_inning_list 
    if bin_shr[0]== '1':
        print ' first on'
	GPIO.output(8,1)
    else:
        print ' first off'
	GPIO.output(8,0)
    if bin_shr[1]== '1':
        print ' second on'
	GPIO.output(7,1)
    else:
        print ' second off'
	GPIO.output(7,0)
    if bin_shr[2]== '1':
        print ' third on'
	GPIO.output(4,1)
    else:
        print ' third off'
	GPIO.output(4,0)
    if bin_shr[3]== '1':
        print ' fourth on'
	GPIO.output(3,1)
    else:
        print ' fourth off'
	GPIO.output(3,0)
    if bin_shr[4]== '1':
        print ' fifth on'
	GPIO.output(2,1)
    else:
        print ' fifth off'
	GPIO.output(2,0)
    if bin_shr[5]== '1':
        print ' sixth on'
	GPIO.output(11,1)
    else:
        print ' sixth off'
	GPIO.output(11,0)

while True:
	try:
    		#get the xml. Use http://gd2.mlb.com/components/game/mlb/year_2017/batters/519058.xml
    		html=urllib2.urlopen('http://gd2.mlb.com/components/game/mlb/year_2017/batters/519058.xml')

    		#parse the xml
    		xmldoc=minidom.parse(html)

    		#get the xml tag and access it using dictionary syntax
    		game=xmldoc.getElementsByTagName('batting')

    		#can access tag attributes using dictionary index syntax
    		game_index=game[0]

    		#access attribute using dictionary syntax
    		batting_stats=game_index.attributes['s_hr']

    		#get values and turn the attirbutes into a int and use format to convert to binary
    		int_shr=int(batting_stats.value)

    		#format(value, '04' lead spaces, b=binary)
    		bin_shr=format(int_shr, '06b')

    		print bin_shr

    		#put str into lists in order to iterate
    		bin_shr=list(bin_shr)

    		GPIO_hrs()
    		print bin_shr_check
    			#if bin_shr_check!=bin_shr:
        		#	chant.play()        
    		sleep(60)
    		bin_shr_check=bin_shr

    		del html

	except KeyboardInterrupt:
		print('goodbye')
		GPIO.cleanup()
		sys.exit()
    
