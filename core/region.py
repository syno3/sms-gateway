#-*-coding:utf8;-*-
#====**this shit is masssive**==!
#

#importing modules needed

import time
import sys
import os
#from core import main
#from core import banner2

def north-america():
    print("01-canada")
    print("02-mexico")
    print("03-USA\n")
    print("00-exit sms-gateway")
    
    country = raw_input("please select the country>>\n")
    
    if (country == 01 or country == 1):
        canada()
    elif (country == 02 or country == 2):
        mexico()
    elif (country == 03 or country == 3):
        usa()
    elif (country == 00):
        banner2()
        time.sleep(3)
        sys.exit()
        
    else:
        print("please select a valid input")
        os.system("clear")
        time.sleep(3)
        
        return north-america()
        

def south-america():
    print("01-argentina")
    print("02-brazil")
    print("03-chile")
    print("04-colombia")
    print("05-nicaragua\n")
    print("00-exit sms-gateway")
    
    country = raw_input("please select a country>>\n")
    
    if (country == 01 or country == 1):
        argentina()
    elif (country == 02 or country == 2):
        brazil()
    elif (country == 03 or country == 3):
        chile()
    elif (country == 04 or country == 4):
        colombia()
    elif (country == 05 or country == 5):
        nicaragua()
    elif (country == 00):
        banner2()
        time.sleep(3)
        sys.exit()
    else:
        print("please enter a valid input")
        os.system("clear")
        time.sleep(3)
        
        return south-america()
        

def carribean():
    print("01-american samoa")
    print("02-bermuda")
    print("03-costa rica")
    print("04-dominica")
    print("05-dominican rep")
    print("06-jamaica")
    print("07-panama")
    print("08-puerto rico\n")
    print("00-exit sms-gateway")
    
    country = raw_input("please select a country>>\n")
    
    if (country == 01 or country == 1):
        american-samoa()
    elif (country == 02 or country == 2):
        bermuda()
    elif (country == 03 or country == 3):
        costa-rica()
    elif (country == 04 or country == 4):
        dominica()
    elif (country == 05 or country == 5):
        dominican-rep()
    elif (country == 06 or country == 07):
        jamaica
    elif (country == 07 or country == 7):
        panama()
    elif (country == 08 or country == 8):
        puerto-rico()
    elif (country == 00):
        banner2()
        time.sleep(3)
        sys.exit
    else:
        print("please enter a valid input")
        os.system("clear")
        time.sleep(3)
        
        return carribean()
    

def africa():
    print("01-south africa")
    print("02-tanzania\n")
    print("03-exit sms-gateway")
    
    
    country = raw_input("please select a country>>\n")
    
    if (country == 01 or country == 1):
        south-africa()
    elif (country == 02 or country == 2):
        tanzania()
    elif (country == 00):
        banner2()
        time.sleep(3)
        sys.exit()
    else:
        print("please enter a valid input")
        os.system("clear")
        time.sleep(3)
        
        return africa()

def europe():
    print("01-austria")
    print("02-belarus")
    print("03-belgium")
    print("04-bosnia")
    print("05-bulgaria")
    print("06-croatia")
    print("07-czech")
    print("08-denmark")
    print("09-estonia")
    print("10-france")
    print("11-georgia")
    print("12-hungary")
    print("13-ireland")
    print("14-italy")
    print("15-lavtia")
    print("16-lithuania")
    print("17-luxemborg")
    print("18-netherlands")
    print("19-norway")
    print("20-poland")
    print("21-portugal")
    print("22-serbia")
    print("23-slovenia")
    print("24-spain")
    print("25-sweden")
    print("26-switzerland")
    print("27-uk")
    print("28-ukraine\n")
    print("00-exit sms-gateway")
    
     country = raw_input("please select a country>>\n")
    
    if (country == 01 or country == 1):
        austria()
    elif (country == 02 or country == 2):
        belarus()
    elif (country == 03 or country == 3):
        belgium()
    elif (country == 04 or country == 4):
        bosnia()
    elif (country == 05 or country == 5):
        bulgaria()
    elif (country == 06 or country == 6):
        croatia()
    elif (country == 07 or country == 7):
        czech()
    elif (country == 08 or country == 8):
        denmark()
    elif (country == 09 or country == 9):
        estonia()
    elif (country == 10):
        france()
    elif (country == 11):
        georgia()
    elif (country == 12):
        hungary()
    elif (country == 13):
        ireland()
    elif (country == 14):
        italy()
    elif (country == 15):
        lavtia()
    elif (country == 16):
        lithuania()
    elif (country == 17):
        luxemborg()
    elif (country == 18):
        netherlands()
    elif (country == 19):
        norway()
    elif (country == 20):
        poland()
    elif (country == 21):
        portugal()
    elif (country == 22):
        serbia()
    elif (country == 23):
        slovenia()
    elif (country == 24):
        spain()
    elif (country == 25):
        sweden()
    elif (country == 26):
        switzerland()
    elif (country == 27):
        uk()
    elif (country == 28):
        ukraine()
    elif (country == 29):
        pass
    elif (country == 00):
        banner2()
        time.sleep(3)
        sys.exit()
    else:
        print("please enter a valid input")
        os.system("clear")
        time.sleep(3)
        
        return europe()
    
def asia():
    print("01-china")
    print("02-india")
    print("03-japan")
    print("04-malaysia")
    print("05-nepal")
    print("06-pakistan")
    print("07-philipines")
    print("08-russia")
    print("09-singapore")
    print("10-south korea")
    print("11-sri lanka\n")
    print("00-exit sms-gateway")
    
    
    country = raw_input("please select a country>>\n")
    
    if (country == 01 or country == 1):
        china()
    elif (country == 02 or country == 2):
        india()
    elif (country == 03 or country == 3):
        japan()
    elif (country == 04 or country == 4):
        malaysia()
    elif (country == 05 or country == 5):
        nepal()
    elif (country == 06 or country == 6):
        pakistan()
    elif (country == 07 or country == 7):
        philipines()
    elif (country == 08 or country == 8):
        russia()
    elif (country == 09 or country == 9):
        singapore()
    elif (country == 10):
        south_korea()
    elif (country == 11):
        sri_lanka()
    elif (country == 00):
        banner2()
        time.sleep(3)
        sys.exit()
    else:
        print("please enter a valid input")
        os.system("clear")
        time.sleep(3)
        
        return asia()

def australia():
    print("01-australia")
    print("02-new zealand")
    print("00-exit sms-gateway")
    
    country = raw_input("please choose a country>>\n")
    
    if (country == 01 or country == 1):
        australia2()
    elif (country == 02 or country == 2):
        new_zealand()
    elif (country == 00):
        banner2()
        time.sleep(3)
        sys.exit
    else:
        print("please enter a valud input")
        os.system("clear")
        time.sleep(3)
        
        return australia()

def middle-east():
    print("01-lebanon")
    print("02-israel\n")
    print("00-exit sms-gateway")
    
    country = raw_input("please choose a country>>\n")
    
    if (country == 01 or country == 1):
        lebanon()
    elif (country == 02 or country == 2):
        israel()
    elif (country == 00):
        banner2()
        time.sleep(3)
        sys.exit()
    else:
        print("please enter a valud input")
        os.system("clear")
        time.sleep(3)
        
        return middle-east()
    	
