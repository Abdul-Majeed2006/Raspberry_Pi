# ==========================================================
# SOLUTION: THE MARS ROVER
# ==========================================================
# This is the "Teacher's Reference" implementation.
# Uses:
# - AWD Driver (Motors)
# - SSD1306 (OLED)
# - Secrets (Wi-Fi)
# - Socket Server (Web Control)
# ==========================================================

import machine
import time
import network
import socket

try:
    from drivers.AWD import AWD
    from drivers.ssd1306 import SSD1306_I2C
    from drivers import secrets
except ImportError:
    print("Error: Drivers missing.")

# --- ONE CONFIG TO RULE THEM ALL ---
class RoverConfig:
    # I2C (OLED)
    I2C_ID = 0
    PIN_SCL = 1
    PIN_SDA = 0
    
    # Internal Temp Sensor
    PIN_TEMP = 4

# --- SUBSYSTEMS ---
def setup_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print(f"Connecting to {secrets.SSID}...")
        wlan.connect(secrets.SSID, secrets.PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
    return wlan.ifconfig()[0]

def setup_oled():
    i2c = machine.I2C(RoverConfig.I2C_ID, 
                      scl=machine.Pin(RoverConfig.PIN_SCL), 
                      sda=machine.Pin(RoverConfig.PIN_SDA))
    return SSD1306_I2C(128, 64, i2c)

def get_temp():
    sensor = machine.ADC(RoverConfig.PIN_TEMP)
    reading = sensor.read_u16() * (3.3 / 65535)
    temp_c = 27 - (reading - 0.706)/0.001721
    return temp_c

# --- UI HTML ---
def get_html(temp_val):
    return f"""<!DOCTYPE html>
<html>
<head> <title>Mars Rover</title> 
<style>
  body {{ background: #222; color: #0f0; font-family: monospace; text-align: center; }}
  button {{ width: 80px; height: 80px; font-size: 24px; margin: 5px; }}
  .stat {{ border: 1px solid #0f0; padding: 10px; display: inline-block; }}
</style>
<script>
  function move(dir) {{ fetch('/' + dir); }}
</script>
</head>
<body>
  <h1>MARS ROVER LINK</h1>
  <div class="stat">TEMP: {temp_val:.1f} C</div>
  <br><br>
  <button onmousedown="move('forward')" onmouseup="move('stop')">W</button><br>
  <button onmousedown="move('left')" onmouseup="move('stop')">A</button>
  <button onmousedown="move('stop')">STOP</button>
  <button onmousedown="move('right')" onmouseup="move('stop')">D</button><br>
  <button onmousedown="move('backward')" onmouseup="move('stop')">S</button>
</body>
</html>
"""

# --- MAIN LOOP ---
def main():
    # 1. Init Hardware
    robot = AWD()
    oled = setup_oled()
    ip = setup_wifi()
    
    # 2. Show Status
    oled.fill(0)
    oled.text("MARS ROVER", 0, 0)
    oled.text("IP Address:", 0, 16)
    oled.text(ip, 0, 26)
    oled.show()
    print(f"Rover Online at http://{ip}")
    
    # 3. Web Server
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1)

    while True:
        try:
            cl, addr = s.accept()
            request = cl.recv(1024).decode('utf-8')
            
            # PARSE COMMANDS
            if "GET /forward" in request:
                robot.forward()
            elif "GET /backward" in request:
                robot.backward()
            elif "GET /left" in request:
                robot.turn_left()
            elif "GET /right" in request:
                robot.turn_right()
            elif "GET /stop" in request:
                robot.stop()
            
            # SEND RESPONSE
            temp = get_temp()
            response = get_html(temp)
            cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            cl.send(response)
            cl.close()
            
            # Refresh Screen with Temp
            oled.fill_rect(0, 40, 128, 24, 0) # Clear bottom
            oled.text(f"Temp: {temp:.1f}C", 0, 45)
            oled.show()
            
        except Exception as e:
            # print("Loop Error:", e)
            try: cl.close()
            except: pass

if __name__ == "__main__":
    main()
