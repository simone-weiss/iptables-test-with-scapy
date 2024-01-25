#!/bin/bash

echo "Loading iptable firewall rules"

ip6tables -A INPUT -d fe80::10 -p ipv6-icmp -i lo -m icmp6 --icmpv6-type 135/0 -j ACCEPT
ip6tables -A OUTPUT -p tcp –m tcp –s 2001:db8::1 –d 2001:db8:2 -i lo --sport 12345 –dport 80 -m mark --mark 0x10000000/0xffffffff -m conntrack --ctstate NEW, ESTABLISHED -j ACCEPT


echo "print interfaces"
ip a
