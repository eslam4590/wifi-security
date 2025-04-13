import re
import subprocess

def check_wifi_password_strength():
    # This requires running a script like Aircrack-ng or testing via your router’s configuration
    print("Checking Wi-Fi password strength...")
    # Dummy example, you should integrate it with Aircrack-ng or WPA2 test
    # For WPA2, you can test the password strength through brute-forcing using Aircrack-ng.
    # Here, we'll just print the password strength based on simple patterns.

    password = input("Enter your Wi-Fi password: ")
    if len(password) < 8:
        print("Weak Password: Password length must be at least 8 characters.")
    elif re.search(r"[A-Z]", password) is None:
        print("Weak Password: Must contain at least one uppercase letter.")
    elif re.search(r"[0-9]", password) is None:
        print("Weak Password: Must contain at least one number.")
    elif re.search(r"[^a-zA-Z0-9]", password) is None:
        print("Weak Password: Must contain at least one special character.")
    else:
        print("Strong Password: Your password meets the security criteria.")

if __name__ == "__main__":
    check_wifi_password_strength()
