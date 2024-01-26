#!/usr/bin/python3

import scapy as s

#testcase 1
s.sniff(iface="lo", counter=1)
packet_test1 = s.IPv6(dst="fe80::10")/ICMP(type=135, code=0)
s.send(packet_test1, iface="lo")

#testcase 2
s.sniff(iface="lo", counter=4, filter="tcp")
packet_test2 = s.IPv6(src="2001:db8::1", dst="2001:db8::2")/TCP(sport=12345, dport=80)/Raw(("Hello, World!")/"\x00\x00\x00\x00\x10\x00\x00\x00")
s.send(packet_test2, iface="lo")
