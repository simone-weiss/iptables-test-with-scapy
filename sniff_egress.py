#!/usr/bin/python3

from scapy.all import *

def packet3_check(x):
	if x[TCP].dport == 60001:
		print("PASS: recieved one packet and port is correct")
	else:
		print("FAIL: recieved one packet and port is not correct")

sniff(iface="tap0", filter="tcp and port 60001", count=1, prn=packet3_check)
