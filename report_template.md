# 📄 Wi-Fi Security Assessment Report

## 🧠 Objective

This report outlines the findings of the Wi-Fi security assessment performed on your home network. The goal was to identify vulnerabilities such as weak passwords, open ports, and unauthorized devices connected to the network.

---

## 🛠️ Tools Used

- **Wireshark** – Used to capture network traffic and analyze the security of communication.
- **Aircrack-ng** – Used for cracking weak passwords and testing the security of the network.
- **Nmap** – Used to detect open ports and services running on devices connected to the network.

---

## 📊 Findings

### 1. **Devices on the Network**

| Device IP      | Device MAC        | Status            |
|----------------|-------------------|-------------------|
| 192.168.1.5    | 00:1A:2B:3C:4D:5E | Unauthorized      |
| 192.168.1.10   | 11:22:33:44:55:66 | Authorized        |

### 2. **Open Ports on Router (192.168.1.1)**

| Port | Service | State  |
|------|---------|--------|
| 22   | SSH     | Open   |
| 80   | HTTP    | Open   |

### 3. **Wi-Fi Password Strength**

- The password entered was **strong** (meets criteria of length, uppercase, numbers, and special characters).

### 4. **Traffic Analysis**

- No sensitive information was detected in the captured traffic.

---

## 📌 Recommendations

1. **Change Default Passwords**  
   Ensure all devices on the network, including the router, have strong passwords. Avoid using default passwords.

2. **Disable Unused Ports**  
   Close unused ports such as port 22 (SSH) to reduce the attack surface.

3. **Use WPA3 Encryption**  
   If your router supports it, use WPA3 encryption for better security. If not, at least ensure WPA2 is used.

4. **Monitor Network Traffic Regularly**  
   Regularly capture and inspect network traffic for any suspicious activity.

---

## ✅ Conclusion

The security assessment revealed some areas of concern, such as open ports and unauthorized devices. By following the recommendations, you can significantly improve the security of your home network.

---

*Prepared by: [Your Name]*  
*Date: YYYY-MM-DD*
