#!/bin/sh

echo "Loading iptable firewall rules"

ip6tables -A INPUT -d fe80::10 -p ipv6-icmp -i lo -m icmp6 --icmpv6-type 135/0 -j ACCEPT
ip6tables -t nat -A OUTPUT -o eth0.42 -p tcp -d 2001:db8::2 --dport 60000 -m owner ! --uid-owner mail -j REDIRECT --to-ports 60001
ip6tables -A OUTPUT -m mark --mark 0x11110000 -m limit --limit 20/sec --limit-burst 1 -j NFLOG --nflog-prefix "found.a.fancy.packet" --nflog-group 30

echo "Firewall:"
ip6tables-save -c
