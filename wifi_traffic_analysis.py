import subprocess

def capture_traffic(interface):
    print(f"Capturing Wi-Fi traffic on {interface}...")
    # Wireshark can be invoked from the command line to start traffic capture
    subprocess.run(["sudo", "wireshark", "-i", interface])  # Start Wireshark for traffic capture

def main():
    interface = "wlan0"  # Adjust based on your system's interface
    capture_traffic(interface)

if __name__ == "__main__":
    main()
