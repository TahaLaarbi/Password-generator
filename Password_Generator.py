import random

'''chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789²&é\"'\/(-è_çà)=*$ù!:;,.<>~#{[|`^@]}"

while True:
    length = int(input("Enter your password's length : "))
    count = int(input("How many passwords you want : "))
    for i in range(count):
        print("Here's password ", i+1,":", ''.join(random.choices(chars, k=length)))'''


sma = "abcdefghijklmnopqrstuvwxyz"
cap = sma.upper()
num = "0123456789"
sym = "&#!?@<>{[|`\^]}/"
print(sma+cap)
print(cap)
