#-*-coding:utf8;-*-

import time
import sys

def american_samoa():
    print("01-bluesky communication\n")
    
    results = raw_input("please choose the service provider>>\n")
    
    if (results == 01 or results == 1):
        bluesky_communication()
    else:
        print("please select a valid input\n")
        time.sleep(3)
        return american_samoa()

def argentina():
    print("01-CTI Movil")
    print("02-Movistar")
    print("03-Nextel")
    print("04-Personal")
    
    results = raw_input("please choose the network provider>>\n")
    if (results == 01 or results == 1):
        cti-movil()
    if (results == 02 or results == 2):
        movistar()
    if (results == 03 or results == 3):
        nextel()
    if (results == 04 or results == 4):
        personal()
    else:
        print("please select a valid input\n")
        time.sleep(3)   
        return argentina()
    
def australia2():
    print("01-Optus mobile")
    print("02-Telstra")
    
    results = raw_input("please choose the service provider>>\n")
    
    if (results == 01 or results == 1):
        optus-mobile()
    elif (results == 02 or results == 2):
        telstra()
    else:
        print("please select a valid input\n")
        banner()
        time.sleep(3)
        return australia2()
        
def austria():
    print("01-MaxMobil")
    print("02-One connect")
    print("03-T-mobile")
    
    results = raw_input("please chose the network provider>>\n")
    
    if (results == 01 or results == 1):
        maxmobil()
    if (results == 02 or results == 2):
        one-connect()
    if (results == 03 or results == 3):
        t-mobile()
    else:
        print("please enter a valid input\n")
        banner()
        time.sleep(3)
        return austria()
        
def belgium():
    print("01-Mobistar")
    
    results = raw_input("please choose the network provider>>\n")
    
    if (results == 01 or results == 1):
        mobistar()
    else:
        print("please select a valud input\n")
        banner()
        time.sleep(3)
        return belgium
        
def bermuda():
    print("01-Mobility")
    
    results = raw_input("please choose a service provider>>\n")
    
    if (results == 01 or results == 1):
       
    
        
