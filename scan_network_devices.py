import scapy.all as scapy

def scan_network(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    devices = []
    for element in answered_list:
        devices.append(element[1].psrc)
    return devices

def main():
    ip_range = "192.168.1.1/24"  # Adjust to your network's IP range
    devices = scan_network(ip_range)
    print("Devices on your network:")
    for device in devices:
        print(device)

if __name__ == "__main__":
    main()
