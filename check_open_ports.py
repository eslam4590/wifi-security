import nmap

def scan_ports(target_ip):
    scanner = nmap.PortScanner()
    print(f"Scanning open ports for {target_ip}...")
    scanner.scan(target_ip, '1-1024')  # Scans ports 1 to 1024
    for protocol in scanner[target_ip].all_protocols():
        print(f"\nProtocol: {protocol}")
        ports = scanner[target_ip][protocol].keys()
        for port in ports:
            print(f"Port: {port}, State: {scanner[target_ip][protocol][port]['state']}")

def main():
    target_ip = "192.168.1.1"  # Router IP
    scan_ports(target_ip)

if __name__ == "__main__":
    main()
