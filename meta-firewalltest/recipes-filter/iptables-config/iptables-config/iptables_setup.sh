#!/bin/sh

echo "Loading iptable firewall rules"
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -A INPUT -p tcp -m ttl --ttl-eq 8 -m tcp --dport 1234 --tcp-flags FIN,SYN,RST,ACK SYN -j DROP
iptables -A INPUT -s 192.168.7.0/24 -i eth0 -p tcp -m tcp --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -t nat -A OUTPUT -d 192.168.7.1/32 -o eth0 -p tcp -m tcp --dport 100 -j REDIRECT --to-ports 60001

echo "Firewall:"
iptables-save -c
