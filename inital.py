#-*-coding:utf8;-*-

#===importing modules needed
import sys
import time
import os
#from core import banner
#from core import region
#from core import email_list

#====request for root accesss
if os.getuid !=0:
    print("Due to security purposes you need root access to use Sms-Gateway")
    sys.exit()

def main():
    banner()
    time.sleep(5)
    
    region = raw_input("please select the region you want to send the text>>\n")
    
    if (region == 01 or region == 1):
        north-america()
    elif (region == 02 or region == 2):
        south-america()
    elif (region == 03 or region == 3):
        carribean()
    elif (region == 04 or region == 4):
        africa()
    elif (region == 05 or region == 5):
        europe()
    elif (region == 06 or region == 6):
        asia()
    elif (region == 07 or region == 7):
        australia()
    elif (region == 08 or region == 8):
        middle-east()
    elif (region == 09 or region == 9):
        globe()
    elif (region == 00):
        sys.exit()
    else:
        print("please enter a valid input\n")
        time.sleep(3)
        os.system("clear")
        
        return main()

    
if__name__ == "__main__":
    main()
    

    
    


