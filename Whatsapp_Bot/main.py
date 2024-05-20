import pywhatkit
from datetime import datetime

# PHONE_NUMBER = input("Enter Phone Number: ")
# MESSAGE = input("Enter Message: ")
# HR = int(input("Enter Hour: "))     # 24 Hour Format
# MIN = int(input("Enter Minutes:"))

PHONE_NUMBER = "+40775346554"
MESSAGE = "Ala bala portocale"
HR = datetime.now().hour
MIN = datetime.now().minute + 1

pywhatkit.sendwhatmsg(PHONE_NUMBER, MESSAGE, HR, MIN)
