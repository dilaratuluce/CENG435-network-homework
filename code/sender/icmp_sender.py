from scapy.all import IP, ICMP, send

# Implement your ICMP sender here
target_ip = "172.18.0.3" # IP of the receiver container

packet = IP(dst=target_ip, ttl=1) / ICMP()
send(packet)
