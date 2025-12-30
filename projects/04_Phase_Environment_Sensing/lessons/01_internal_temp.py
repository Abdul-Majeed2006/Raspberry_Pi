"""
LESSON: Internal Temperature Sensor (ADC)
-----------------------------------------
The Raspberry Pi Pico (RP2040) has a hidden secret:
It can feel its own heat.

Inside the chip, there is a specialized sensor connected to ADC Channel 4.
We don't need to wire anything!

CONCEPTS:
1. ADC (Analog to Digital Converter): Converting 0-3.3V to 0-65535.
2. Conversion Factor: Turning "counts" back into Volts.
3. Datasheet Math: Using the formula T = 27 - (V - 0.706) / 0.001721
"""

import machine
import time

# --- CONFIGURATION ---
SENSOR_PIN = 4  # The internal temp sensor is always on ADC 4

# --- SETUP ---
# Initialize the ADC (Analog to Digital Converter)
sensor = machine.ADC(SENSOR_PIN)

def read_internal_temp():
    """
    Reads the raw ADC value, converts it to Voltage,
    and then calculates Celsius based on the RP2040 Datasheet.
    """
    # 1. Read Raw Value (0 to 65535)
    # The Pico's ADC is 12-bit (0-4095), but MicroPython scales it to 16-bit.
    reading = sensor.read_u16()
    
    # 2. Convert to Voltage
    # 3.3V is the reference voltage.
    voltage = reading * (3.3 / 65535)
    
    # 3. Calculate Temperature (Formula from RP2040 Datasheet)
    # 27 degrees @ 0.706V, with a slope of -1.721mV per degree.
    temperature_c = 27 - (voltage - 0.706) / 0.001721
    
    return temperature_c

# --- MAIN LOOP ---
print("--- Internal Body Temp Monitor ---")

while True:
    temp = read_internal_temp()
    
    # Debug print: Formatted to 2 decimal places
    print(f"Core Temp: {temp:.2f} °C")
    
    # Simple logic: Is the CPU working hard?
    if temp > 30:
        print("  -> Warm! (Normal operation)")
    else:
        print("  -> Cool.")
        
    time.sleep(1)
