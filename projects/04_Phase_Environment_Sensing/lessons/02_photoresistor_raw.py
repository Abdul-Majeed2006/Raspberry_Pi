"""
LESSON: The Physics of Light (Voltage Divider)
----------------------------------------------
Modules hide the truth. Today we build a sensor from scratch.

A Photoresistor (LDR) changes resistance based on light.
But a Microcontroller can only read Voltage, not Resistance.
Solution: The Voltage Divider.

CIRCUIT:
3.3V ---[ LDR ]---(Pin 26)---[ 10k Resistor ]--- GND

THEORY:
V_out = V_in * (R_bottom / (R_top + R_bottom))
Light Level ↑  =>  LDR Resistance ↓  =>  Voltage at Pin 26 ↑

ENGINEERING LOGIC: Hysteresis
We use a "Schmidt Trigger" logic to prevent flickering at twilight.
"""

import machine
import time

# --- CONFIGURATION ---
PIN_ID = 26       # ADC0 is usually Pin 26
adc = machine.ADC(PIN_ID)

# Hysteresis Thresholds (0-65535)
# Darker < 20000 < Deadband < 40000 < Brighter
THRESH_DARK = 20000 
THRESH_BRIGHT = 40000

# State Variable
is_light_on = False

print("--- Raw Light Sensor (Physics Mode) ---")

while True:
    # 1. Read Raw Physics
    raw_value = adc.read_u16()
    
    # 2. Convert to meaningful units (Voltage)
    voltage = raw_value * (3.3 / 65535)
    
    # 3. Calculate Resistance (Optional, for nerds)
    # R_ldr = R_fixed * (V_in - V_out) / V_out
    try:
        r_ldr = 10000 * (3.3 - voltage) / voltage
        print(f"V: {voltage:.2f}v | R: {int(r_ldr)} ohms | Raw: {raw_value}", end="")
    except ZeroDivisionError:
        print(f"V: {voltage:.2f}v | R: inf | Raw: {raw_value}", end="")

    # 4. Engineering Logic: Software Hysteresis
    # Only change state if we cross the thresholds
    if raw_value < THRESH_DARK and not is_light_on:
        print(" -> NIGHT DETECTED (Lights ON)")
        is_light_on = True
    elif raw_value > THRESH_BRIGHT and is_light_on:
        print(" -> DAY DETECTED (Lights OFF)")
        is_light_on = False
    else:
        # In the "Deadband" zone - do nothing (Stability)
        print(" .")
        
    time.sleep(0.5)
