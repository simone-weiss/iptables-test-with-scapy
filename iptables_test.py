#!/usr/bin/env/python3

import scapy as s

#testcase 1
packet_test1 = s.IPv6(dst="fe80::10")/ICMPv6NS(), iface="eth3"
s.send(packet_test1)

#testcase 2
packet_test2 = s.IPv6(src="2001:db8::1", dst="2001:db8::2")/TCP(sport=12345, dport=80)/Raw("Hello, World!")/"\x00\x00\x00\x00\x10\x00\x00\x00"), iface="eth3"
s.send(packet_test2)
