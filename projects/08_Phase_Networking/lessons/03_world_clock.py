# ==========================================================
# LESSON 03: THE WORLD CLOCK (WEB SERVER)
# ==========================================================
# Goal: Host a Website on the Pico that shows the time.
# Concept: Sockets. We open a "Door" (Port 80) and listen
#          for web browsers knocking.
# ==========================================================

import network
import socket
import time
import secrets
import machine
import ntptime

# --- SETUP TIME ---
def setup_net_and_time():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(secrets.SSID, secrets.PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
    print("IP Address:", wlan.ifconfig()[0])
    try:
        ntptime.settime() 
    except: 
        pass

# --- HTML GENERATOR ---
def get_html(time_str):
    html = f"""<!DOCTYPE html>
    <html>
    <head> <title>Pico Clock</title> <meta http-equiv="refresh" content="5"> 
    <style>
        body {{ font-family: sans-serif; text-align: center; background-color: #111; color: #0f0; }}
        h1 {{ font-size: 3rem; }}
        p {{ font-size: 1.5rem; color: #fff; }}
    </style>
    </head>
    <body>
        <h1>Pico World Clock</h1>
        <p>Current System Time:</p>
        <div style="border: 2px solid #0f0; display: inline-block; padding: 20px;">
            <h1>{time_str}</h1>
        </div>
        <p>Updates every 5 seconds.</p>
    </body>
    </html>
    """
    return html

def main():
    setup_net_and_time()
    
    # Open Socket (Port 80 = HTTP)
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allow fast restart
    s.bind(addr)
    s.listen(1)

    print("--- SERVER LISTENING ---")
    
    while True:
        try:
            cl, addr = s.accept()
            # print('Client connected from', addr)
            
            # Read Request (Ignored, we serve same page to everyone)
            request = cl.recv(1024)
            # print(request)
            
            # Get Time
            tm = time.localtime()
            t_str = "{:02d}:{:02d}:{:02d}".format(tm[3], tm[4], tm[5])
            
            # Send Response
            response = get_html(t_str)
            cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            cl.send(response)
            cl.close()
            
        except Exception as e:
            print("Conn Error:", e)
            try: cl.close()
            except: pass

if __name__ == "__main__":
    main()
