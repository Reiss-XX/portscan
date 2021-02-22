import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
import time
import datetime
import os
os.system("clear")
def w() :
	time.sleep(0.5)
	print("\n")
red="\033[31m"
green="\033[32m"
yellow="\033[33m"
blue="\033[34m"
purple="\033[35m"
cyan="\033[36m"
white="\033[37m"

print(red,"""                _                                   
  _ __  ___ _ _| |_   ___ __ __ _ _ _  _ _  ___ _ _ 
 | '_ \/ _ \ '_|  _| (_-</ _/ _` | ' \| ' \/ -_) '_|
 | .__/\___/_|  \__| /__/\__\__,_|_||_|_||_\___|_|  
 |_|                                                """)
print(white,"PORT SCANNER[BETA], REISS CLAN, REVENGE")
w()
pl=[]
print(cyan,"""
1>>>SCAN BY NAME
2>>>SCAM BY IP""")
w()
p=0
while p==0 :
	print(yellow)
	scanbychoice=input("YOUR CHOICE: ")
	
	if scanbychoice=="1":
			p=1
	elif scanbychoice=="2":
			p=1
	else:
			w()
			print(red,"your choice dosen't exist, please insert choice")
			w()
			
o=0
while o==0:
	if scanbychoice=="1" :
		w()
		print(yellow)
		hostname=input("HOST NAME: ")
		w()
		try:
			ip=socket.gethostbyname(hostname)
			print(ip)
			o=1
		except:
			print(red,"wrong host name")
		
	elif scanbychoice=="2" :
		w()
		print(red,"PLEASE MAKE SURE THE IP IS CORRECT")
		w()
		time.sleep(3)
		print(yellow)
		ip=input("INSERT IP: ")
		o=1
print (white,"scanning...")
t1=datetime.datetime.now()
for port in range(0,65535) :
						try:
							s.connect_ex((ip,port))
							nn=socket.getservbyport(port)
							print(green,"PORT {} OPEN, IT SERVICE:".format(port), nn)
							pl.append(port)
						except :
							print(red,"PORT {} UNAVAILABLE".format(port))
							pass
						
t2=datetime.datetime.now()
t3=t2-t1
w()
print(purple,"OPEN PORTS FOUNDED: ",green,pl)
print(yellow," scannig completed with {} sec/min only!".format(t3))
