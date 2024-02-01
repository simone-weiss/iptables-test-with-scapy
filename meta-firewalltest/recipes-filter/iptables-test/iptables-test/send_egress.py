#!/usr/bin/python3

from scapy.all import *
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
s.setsockopt(socket.SOL_SOCKET, 25, str("eth0" + '\0').encode('utf-8'))
s.bind(('192.168.7.2', 0))

pkt = TCP(dport=100)
s.sendto(bytes(pkt), ("192.168.7.1", 0))
s.close()
