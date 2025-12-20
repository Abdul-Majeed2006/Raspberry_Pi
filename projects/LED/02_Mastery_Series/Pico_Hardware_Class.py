# ==========================================================
# MASTERY PROJECT 10: THE VIRTUAL LIGHTBULB (OOP)
# Goal: Transition from "Scripting" to "Engineering."
# We will build a 'Class'—a blueprint for a smart LED object.
# ==========================================================

from machine import Pin, PWM
import time

# ----------------------------------------------------------
# 1. THE CLASS DEFINITION (The Blueprint)
# ----------------------------------------------------------

class PicoLight:
    """
    A professional-grade class to control the Pico's RGB LED.
    It handles Gamma correction and Pin management internally.
    """
    def __init__(self, r_pin, g_pin, b_pin):
        # Setup Pins
        self.red = PWM(Pin(r_pin), freq=1000)
        self.grn = PWM(Pin(g_pin), freq=1000)
        self.blu = PWM(Pin(b_pin), freq=1000)
        self.gamma = 2.8
        print(f"HARDWARE: PicoLight initialized on pins {r_pin}, {g_pin}, {b_pin}")

    def _get_duty(self, percent):
        """Internal helper for Gamma calculation."""
        return int((max(0, percent / 100) ** self.gamma) * 65535)

    def set_color(self, r, g, b):
        """Sets the color using 0-100% values."""
        self.red.duty_u16(self._get_duty(r))
        self.grn.duty_u16(self._get_duty(g))
        self.blu.duty_u16(self._get_duty(b))

    def off(self):
        """Quick kill switch for all colors."""
        self.set_color(0, 0, 0)
        
    def strobe(self, r, g, b, speed=0.1):
        """A simple strobe method built into the light itself!"""
        self.set_color(r, g, b)
        time.sleep(speed)
        self.off()
        time.sleep(speed)

# ----------------------------------------------------------
# 2. THE MAIN PROGRAM (The Implementation)
# ----------------------------------------------------------

# Instead of managing Pins 20, 21, 22 manually...
# We just create ONE "Light" object.
living_room_light = PicoLight(r_pin=21, g_pin=22, b_pin=20)

print("SYSTEM: Using the new 'PicoLight' Class object.")

try:
    while True:
        # Notice how clean the code is now! 
        # We just tell the "Object" what to do.
        
        print("ACTION: Setting color to Purple...")
        living_room_light.set_color(100, 0, 100)
        time.sleep(1)
        
        print("ACTION: Starting Strobe Test...")
        for _ in range(5):
            living_room_light.strobe(100, 100, 100, speed=0.05)
            
        print("ACTION: Fading to Blue...")
        for i in range(100, -1, -5):
            living_room_light.set_color(0, 0, i)
            time.sleep(0.05)

except KeyboardInterrupt:
    living_room_light.off()
    print("\nSystem Offline.")
