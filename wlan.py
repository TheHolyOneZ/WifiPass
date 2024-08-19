import subprocess
import re
import tkinter as tk
from tkinter import messagebox

def get_connected_wifi_password():
    try:
        # Run the command to get the connected WiFi details
        result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], 
                                capture_output=True, text=True, 
                                encoding='cp850', errors='replace', check=True)
#TheZ        
        # Search for SSID
        ssid_search = re.search(r'SSID\s*:\s*(.+)', result.stdout)
        if ssid_search:
            ssid = ssid_search.group(1).strip()
        else:
            return "Not connected to any WiFi"

#TheZ
        # Run the command to get the WiFi profile details
        result = subprocess.run(['netsh', 'wlan', 'show', 'profile', f'name={ssid}', 'key=clear'], 
                                capture_output=True, text=True, 
                                encoding='cp850', errors='replace', check=True)
#TheZ        
        # Search for the password
        password_search = re.search(r'Schlüsselinhalt\s*:\s*(.+)', result.stdout)
        if password_search:
            password = password_search.group(1).strip()
            return f'Password for "{ssid}" is: {password}'
        else:
            return f'Could not find the password for "{ssid}"'
    except subprocess.CalledProcessError as e:
        return f'ERROR: {e}'
    except Exception as e:
        return f'Unexpected error: {e}'
#TheZ
def show_password():
    result = get_connected_wifi_password()
    messagebox.showinfo("WLAN Password", result)
#TheZ
# Create the Tkinter window
root = tk.Tk()
root.title("WLAN Password Display")
root.geometry("300x100")
#TheZ
# Add a button to show the password
button = tk.Button(root, text="Show WLAN Password", command=show_password)
button.pack(expand=True)
#TheZ
# Run the Tkinter main loop
root.mainloop()
#TheZ
