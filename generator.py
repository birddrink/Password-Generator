import random
import string
numOfDigits = int(input("Insert the number of digits for your password (8 or more):\n"))
#Checks if you insert a number lower than 8
if numOfDigits < 8:
    print("Please insert a higher number of digits")
if numOfDigits >= 8:
    str = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    print("".join(random.sample(str,numOfDigits)))