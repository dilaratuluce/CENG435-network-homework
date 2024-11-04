from scapy.all import sniff, IP, ICMP

# Implement your ICMP receiver here
def capture_icmp(packet):
    if ICMP in packet and packet[IP].ttl == 1:
        packet.show()

sniff(prn=capture_icmp)
