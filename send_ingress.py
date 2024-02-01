#!/usr/bin/python3

from scapy.all import *

#Ingress Testcase 1
packet1_0=IP(ttl=8, dst="192.168.7.2")/TCP(dport=1234, flags=0x01) # wrong flags but sniff only once!
send(packet1_0, iface="tap0")
packet1_1=IP(ttl=8, dst="192.168.7.2")/TCP(dport=1234, flags=0x02)
send(packet1_1, iface="tap0")

#Ingress Testcase 2
packet2_0=IP(src="192.168.7.0", dst="192.168.7.2")/TCP(dport=23)  # wrong flags but sniff only once!
send(packet2_0, iface="tap0")
packet2_1=IP(src="192.168.7.0", dst="192.168.7.2")/TCP(dport=22)
send(packet2_1, iface="tap0")
