import requests
import time

print ('Tunggu 1 Menit')
import sys,time
def spin():
        try:
                L="/-\\|"
                for q in range(100):
                        time.sleep(0.1)
                        sys.stdout.write("\r["+L[q % len(L)]+"]")
                        sys.stdout.flush()
        except:
                exit()

spin()

import sys,time
def spin():
        try:
                L="/-\\|"
                for q in range(100):
                        time.sleep(0.1)
                        sys.stdout.write("\r["+L[q % len(L)]+"]")
                        sys.stdout.flush()
        except:
                exit()

spin()
print ('\n		    HARAP LOGIN MENGGUNAKAN USERNAME AND PASSWORD!!!')
username = "kali"
password = "kali"

def login (user_name, pass_word) :
    if user_name != username and Pass_word != password :
        hasil = False
    else :
        hasil = True

    return hasil

i=3
while i>=1:
    userName_=input("masukan username :")
    password_=input("masukan password :")
    hasil=(login(userName_, password_))
    if hasil == True :
        print ("login user berhasil")
        break
    else :
        i-=1
        print("gagal login, sisa percobaan login adalah :", i )
        
        import sys,time
def spin():
        try:
                L="/-\\|"
                for q in range(100):
                        time.sleep(0.1)
                        sys.stdout.write("\r["+L[q % len(L)]+"]")
                        sys.stdout.flush()
        except:
                exit()

spin()
print('Berhasil Login...')
        
import sys,time
def run(teks):
    putih = "\033[0m"
    kuning= "\033[91m"
    teks = teks+" "
    try:
        num = 0
        while num < 1:
            for i,char in enumerate(teks):
                if i == 0:
                    sys.stdout.write('\r%s%s%s%s' % (putih,char.lower(),kuning,teks[1:])),
                    sys.stdout.flush()
                else:
                    if i == 1:
                        zbl = teks[0].lower()
                        sys.stdout.write('\r%s%s%s%s%s%s' % (kuning,zbl,putih,char.lower(),putih,teks[2:])),
                        sys.stdout.flush()
                    else:
                        if i == i:
                            zbl = teks[0:i].lower()
                            sys.stdout.write('\r%s%s%s%s%s%s' % (kuning,zbl,putih,char.lower(),putih,teks[i+1:])),
                            sys.stdout.flush()
                    time.sleep(0.1)
            num += 1
    except: exit()

run("**********#############################################************")
#logo
print ('\n-------------------------------------------------------------')
print ('[+]----------------------HACKER CIREBON----------------------')
print ('[+] creator : ./RELL-HACK')
print ('[+] whatsaApp : +62 83148042183')
print ('[+]------------------ARJAWINANGUN BLACK HAT------------------')
print ('-------------------------------------------------------------')
print ('\n[+] Nomor Di Awali 8xxx')

#Run Nomor 
nomor = input('[+] Nomor Terget   :')
req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text 
if 'terkirim' in req:
	  print ('[√] Spam Terkirim')
else:
	   print ('[!] Spam Gagal')
                 
