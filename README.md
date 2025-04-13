# 🔐 Wi-Fi Security

This repository contains tools, scripts, and guides for conducting a Wi-Fi security assessment on your home network. The goal is to check for weak passwords, open ports, and unauthorized devices to improve overall security.

---

## 🧠 Objective

Conduct a security assessment on your home Wi-Fi network to identify vulnerabilities such as weak passwords, open ports, and unauthorized devices connected to the network. Based on the findings, implement security recommendations to enhance the network's defense against unauthorized access.

---

## 🛠️ Tools Used

- **Wireshark** – Network protocol analyzer to capture and inspect network traffic.
- **Aircrack-ng** – Tool for cracking WEP and WPA-PSK passwords.
- **Nmap** – Network scanner to detect open ports, services, and devices on the network.

---

## 📂 Scripts Included

1. **`scan_network_devices.py`** – Scans the Wi-Fi network for unauthorized devices.
2. **`check_open_ports.py`** – Scans for open ports on your router and other devices.
3. **`wifi_password_strength.py`** – Checks the strength of your Wi-Fi password.
4. **`wifi_traffic_analysis.py`** – Captures and analyzes traffic using Wireshark.

---

## 🚀 How to Use

1. **Clone this repository:**

    ```bash
    git clone https://github.com/your-username/wifi-security-assessment.git
    cd wifi-security-assessment
    ```

2. **Install dependencies:**

    ```bash
    pip install scapy nmap
    ```

3. **Run the scripts** to check for vulnerabilities:
   - **Scan Devices**: Detect unauthorized devices connected to your network.
   - **Check Open Ports**: Check if your Wi-Fi router has open ports.
   - **Wi-Fi Password Strength**: Check the strength of your Wi-Fi password.
   - **Traffic Analysis**: Capture and analyze traffic on your network.

---

## ⚠️ Ethical Disclaimer

This repository is designed for **personal use only** to assess the security of your own Wi-Fi network. Performing these tests on other networks without permission is illegal and unethical. Always get explicit consent before testing other networks.

---

## 📊 Deliverable

- **Wi-Fi Security Assessment Report** – Includes details of vulnerabilities discovered and recommendations for improving security.

---

## 📩 Contact

For issues or feedback, feel free to open an issue or contact eslam4590(https://github.com/eslam4590).

---

## 📄 License

MIT License
