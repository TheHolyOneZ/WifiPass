import subprocess
import re
import tkinter as tk
from tkinter import messagebox

def get_connected_wifi_password():
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True, check=True)
        ssid_search = re.search(r'SSID\s*:\s*(.+)', result.stdout)
        if ssid_search:
            ssid = ssid_search.group(1).strip()
        else:
            return "Not connected to any WiFi"
        
        result = subprocess.run(['netsh', 'wlan', 'show', 'profile', f'name={ssid}', 'key=clear'], capture_output=True, text=True, check=True)
        password_search = re.search(r'Schlüsselinhalt\s*:\s*(.+)', result.stdout)
        if password_search:
            password = password_search.group(1).strip()
            return f'Password is: "{ssid}" ist: {password}'
        else:
            return f'Could be the password "{ssid}" Cant be found'
    except subprocess.CalledProcessError as e:
        return f'ERROR: {e}'

def show_password():
    result = get_connected_wifi_password()
    messagebox.showinfo("WLAN-Passwort", result)

root = tk.Tk()
root.title("WLAN-Passwort Anzeige")
root.geometry("300x100")

button = tk.Button(root, text="WLAN-Passwort anzeigen", command=show_password)
button.pack(expand=True)

root.mainloop()
