import requests
import colorama
from colorama import *
import os
import threading
import random
import pyfiglet
import datetime
'''
AND NOW ITS UNLOCKED + FREE XD
#now = datetime.date.today()
#target = datetime.date(2023, 9, 6)
#if now >= target:
#    exit('تفعيل تواصل @NN0WW')
#else:
#    print('مبروك اشتغلت')
'''
E = '\x1b[1;31m'
Z = '\x1b[1;31m'
R = '\x1b[1;31m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
C = '\x1b[1;97m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
E = '\x1b[1;31m'
B = '\x1b[2;36m'
S = '\x1b[1;33m'
C1 = '\x1b[2;35m'
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;34m'
C = '\x1b[2;35m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
M = '\x1b[1;37m'
S = '\x1b[1;33m'
U = '\x1b[1;37m'
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
BBlue = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'
r = Fore.RED
y = Fore.YELLOW
c = Fore.CYAN
rt = requests.session()
litters = '_qwertyuiopasdfghjklzxcvbnm1234567890_'
u = bytes([]).decode()
print(E + str(pyfiglet.figlet_format('بايثون')) + f'P{S} TIKTOK </>\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print(f'''{colorama.Fore.CYAN}{colorama.Fore.RESET}''')
token = input(r + ' \x1b[2;32m [\x1b[2;32m•\x1b[2;32m] \x1b[2;32m تــوكــنــك\x1b[2;32m [\x1b[2;32m+\x1b[2;32m]\xa0 ' + C1 + Y)
print(Z + '------------------------------------')
id = input(F + '⌯ ' + F + ' \x1b[1;33m [\x1b[1;33m•\x1b[1;33m] \x1b[1;33m أيـدي\x1b[1;33m [\x1b[1;33m+\x1b[1;33m]\xa0 ' + F + F)
print(Z + '------------------------------------')
print(B + ' ⌯ ' + X + ' 𝐖𝐀𝐈𝐓 ' + X + '....')
os.system('clear')
hea = {'user-agent': 'com.zhiliaoapp.musically/2007101933 (Linux; U; Android 11; ar_IQ_#u-nu-latn; ANY-LX2; Build/HONORANY-L22CQ; Cronet/58.0.2991.0)', 'upgrade-insecure-requests': '1', 'sec-fetch-user': '?1', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-dest': 'document', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"', 'cache-control': 'max-age=0', 'accept-language': 'en-US,en;q=0.9,ar;q=0.8', 'accept-encoding': 'gzip, deflate, br', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
def claf():
    user1 = ''.join(random.choice(litters) for _ in range(4))
    usernames = user1
    tiko = f'''https://www.tiktok.com/@{usernames}?'''
    reqsnd = rt.get(tiko, headers=hea).status_code
    if reqsnd == 404:
        print(F + 'متاح '+usernames)
        tlg = f'''NEW USER : {usernames} \n BY: @nn0ww - @nn0ww '''
        bot = f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={tlg}'''
        rt.get(bot)
    print(Z + {usernames} + ' مبند ')

Threads = []
for t in range(20):
    x = threading.Thread(claf, **('target',))
    x.start()
    Threads.append(x)
for Th in Threads:
    Th.join()
