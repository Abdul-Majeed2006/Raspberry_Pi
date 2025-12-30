# ==========================================================
# CAPSTONE: THE MARS ROVER (STARTER CODE)
# ==========================================================
# YOUR MISSION:
# 1. Connect to Wi-Fi.
# 2. Display the IP Address on the OLED.
# 3. Create a Web Server to listen for commands.
# 4. Drive the Motors based on those commands.
# ==========================================================

# --- IMPORTS (The Lego Bricks) ---
import machine
import time
import network
import socket
from drivers.AWD import AWD
from drivers.ssd1306 import SSD1306_I2C
try:
    from drivers import secrets
except ImportError:
    print("!!! ERROR: You forgot to create drivers/secrets.py !!!")

# --- HARDWARE CONFIGURATION ---
I2C_ID = 0; SCL_PIN = 1; SDA_PIN = 0

def connect_wifi():
    """
    Connects to Wi-Fi using the secrets file.
    Returns: The IP Address (string) or None if failed.
    """
    print("Contacting Mission Control (Wi-Fi)...")
    # TODO: Write the logic to connect to Wi-Fi!
    # Hint: Use network.WLAN(network.STA_IF)
    return "0.0.0.0" # Placeholder

def setup_oled():
    """
    Initializes the OLED Screen.
    Returns: The 'oled' object.
    """
    print("Initializing Systems Display...")
    # TODO: Initialize I2C and the SSD1306 driver
    # Hint: i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
    return None

def main():
    # 1. SETUP SYSTEMS
    # robot = AWD() # Uncomment when ready!
    oled = setup_oled()
    ip = connect_wifi()
    
    # 2. DISPLAY STATUS
    if oled:
        # TODO: Clear screen and print the IP Address
        pass
        
    print(f"Server listening on http://{ip}")
    
    # 3. WEB SERVER LOOP
    # TODO: Open a Socket on Port 80
    
    while True:
        # TODO: Accept Client Connection
        # TODO: Read Request (e.g., "GET /forward")
        # TODO: Move Robot
        time.sleep(0.1)

if __name__ == "__main__":
    main()
