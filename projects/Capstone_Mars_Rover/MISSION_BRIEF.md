# 🚀 Mission Brief: The Mars Rover Challenge

**"Houston, we have a problem. The Rover is offline."**

Welcome to the **Final Exam**.
You have been given a prototype exploration vehicle ("The Rover"). It has motors, a camera (OLED), and a Wi-Fi radio.
**But it has no brain.**

## 🎯 Your Objective
Write the code to make the Rover:
1.  **Connect** to Mission Control (Wi-Fi).
2.  **Display** its Vital Signs (IP Address) on the OLED screen.
3.  **Drive** remotely via a Web Dashboard.

---

## 📂 The Mission Kit
We have provided the robust "Drivers" so you don't have to reinvent the wheel. You just need to wire them together.

*   `drivers/AWD.py`: The Motor Controller. (Usage: `robot = AWD()`)
*   `drivers/ssd1306.py`: The Screen Driver. (Usage: `oled.text("Hello", 0, 0)`)
*   `drivers/secrets.py`: Your Wi-Fi Password.
*   `main_starter.py`: **This is where you write your code.**

---

## 🧩 Phase 1: The Uplink (Wi-Fi)
**Goal**: Connect to Wi-Fi and print the IP Address.

> **💡 HINT:**
> Remember **Phase 8 (Networking)**?
> You need to use `network.WLAN(network.STA_IF)`.
> Don't forget to import `secrets`!

## 🧩 Phase 2: The Status Screen
**Goal**: The IP Address is useless if you can't see it when the robot is running on battery. Show it on the OLED!

> **💡 HINT:**
> Remember **Phase 5 (Visual UI)**?
> You need `I2C` on pins GP0 (SDA) and GP1 (SCL).
> `oled.fill(0)` clears the screen. `oled.show()` pushes the pixels.

## 🧩 Phase 3: The Motor Link
**Goal**: The Web Server will receive commands like `/forward` or `/stop`. Make the motors obey.

> **💡 HINT:**
> Remember **Phase 3 (Motion)**?
> Inside your Web Server loop, check the request:
> ```python
> if "/forward" in request:
>     robot.forward()
> ```

---

## � Level 99: The Need for Speed (Drifting)
The driver we gave you in `drivers/AWD.py` is **basic**. It turns the motors ON (100%) or OFF (0%).
This means your robot can only move in jerky "Tank Turns".

**The Challenge:**
Can you modify `drivers/AWD.py` to use `machine.PWM`?
If you can control the speed (0-65535), you can implement **Drifting**!

*   **Soft Turn**: Left Motor 100%, Right Motor 50%.
*   **Burnout**: Pulse the motors rapidly.

**Prove your mastery. Hack the driver.**

---

## �🆘 Troubleshooting Guide (If you get stuck)

**1. "The screen is black!"**
*   Check your wiring: SDA->GP0, SCL->GP1, VCC->3.3V, GND->GND.
*   Did you call `oled.show()`?

**2. "The motors just buzz!"**
*   Check your Battery Pack switch. The USB cable doesn't provide enough power for motors.
*   Check `AWD.HardwareConfig` to match your pin wiring.

**3. "I can't connect to the Website!"**
*   Are your computer and Pico on the exact same Wi-Fi network?
*   Did you type the IP address correctly? (e.g., `http://192.168.1.50`)
