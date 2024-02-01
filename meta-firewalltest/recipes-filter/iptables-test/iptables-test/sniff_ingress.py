#!/usr/bin/python3

from scapy.all import *

def packet1_check(x):
	if x.ttl == 8 and x[TCP].flags == "S":
		print("received one packet and flags are correct, this should be accpeted in FW")
	else:
		print("received one packet and flags are not correct, this should be rejected in FW")

sniff(iface="eth0", filter="tcp and port 1234", count=1, prn=packet1_check)
sniff(iface="eth0", filter="tcp and port 1234", count=1, prn=packet1_check)

def packet2_check(x):
	if x[TCP].dport == 22:
		print("received one packet and port is correct, this should be accpeted in FW")
	else:
		print("received one packet and port is correct, this should be rejected in FW")

sniff(iface="eth0", filter="tcp and src 192.168.7.0", count=1, prn=packet2_check)
sniff(iface="eth0", filter="tcp and src 192.168.7.0", count=1, prn=packet2_check)
