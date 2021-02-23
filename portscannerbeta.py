import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
import time
import datetime
import os
import sys
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
 |_|                                                1.3""")
print(white,"PORT SCANNER[BETA 1.3], REISS CLAN, REVENGE")
w()
pl=[]
print(cyan,"""
1>>>SCAN BY NAME
2>>>SCAN BY IP
3>>>SHOW MY DEVICE IP""")
w()
p=0
while p==0 :
	print(yellow)
	scanbychoice=input("YOUR CHOICE: ")
	
	if scanbychoice=="1":
			p=1
	elif scanbychoice=="2":
			p=1
	elif scanbychoice=="3":
		w()
		devname=socket.gethostname()
		ip=socket.gethostbyname(devname)
		print("YOUR DEVICE HOST NAME: ",devname)
		w()
		print("YOUR DEVICE IP:",ip)
		sys.exit()
		
		
	else:
			w()
			print(red,"your choice dosen't exist, please insert choice")
			w()

w()
print(cyan,"""
1>>>check DOS attack availablity
2>>>Normal scan""")
w()
jj=0
while jj==0:
	print(yellow)
	scanbytype=input("YOUR CHOICE: ")
	if scanbytype=="1":
			jj=1
	elif scanbytype=="2":
			jj=1
	else:
			print (red,"your choice dosen't exist, please inser choice")
			
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
	
	   	

t1=datetime.datetime.now()
if scanbytype=="1":
	for port in range(0,65535) :
							try:
								s.connect_ex((ip,port))
								nn=socket.getservbyport(port)
								s.send(bytes("REVENGE","utf-8"))
								print(green,"PORT {} OPEN, IT SERVICE:".format(port), nn)
								pl.append(port)
							except:
								print(red,"PORT {} UNAVAILABLE".format(port))
elif scanbytype=="2":
						for port in range(0,65535) :
							try:
								s.connect_ex((ip,port))
								nn=socket.getservbyport(port)
								print(green,"PORT {} OPEN, IT SERVICE:".format(port),nn)
								pl.append(port)
								
							except:
									print(red,"PORT {} UNAVAILABLE".format(port))
						
						
t2=datetime.datetime.now()
t3=t2-t1
w()
print(purple,"OPEN PORTS FOUNDED: ",green,pl)
print(yellow," scannig completed with {} sec/min only!".format(t3))
time.sleep(2)
print("BYE")
