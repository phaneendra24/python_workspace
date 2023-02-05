
'''Timer'''
from colorama import Fore
import f
import time

t= int(input(Fore.YELLOW+"enter your timer :"))

def counter(t):
    while t :
        mins,secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(Fore.RED+timer,end='\r')
        time.sleep(1)
        t-=1
counter(t)
print(Fore.RED+"Times is up!")