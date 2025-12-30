# ==========================================================
# TOOL: HARDWARE DIAGNOSTIC (H-BRIDGE)
# ==========================================================
# Goal: Validates physical wiring of the L298N Motor Driver.
# Logic: Cycles every input pin individually.
#
# USAGE:
# 1. Lift the Robot off the ground (Wheels in air).
# 2. Run this script.
# 3. Verify each wheel spins in the correct order.
# ==========================================================

from machine import Pin
import time

# We copy the config here so this tool is standalone (in case AWD.py is broken)
class HardwareConfig:
    # Front
    F_ENA = 15; F_IN1 = 14; F_IN2 = 13
    # Back
    B_ENB = 10; B_IN3 = 11; B_IN4 = 12

def test_pin(name, pin_id, duration=1.0):
    print(f"--> TESTING: {name} (GP{pin_id})")
    try:
        p = Pin(pin_id, Pin.OUT)
        p.value(1)
        time.sleep(duration)
        p.value(0)
    except Exception as e:
        print(f"    FAIL: {e}")
    time.sleep(0.5)

def main():
    print("--- H-BRIDGE DIAGNOSTIC START ---")
    
    # 1. Front Axle
    test_pin("Front ENA (Power)", HardwareConfig.F_ENA)
    test_pin("Front IN1 (Logic A)", HardwareConfig.F_IN1)
    test_pin("Front IN2 (Logic B)", HardwareConfig.F_IN2)
    
    # 2. Back Axle
    test_pin("Back ENB (Power)", HardwareConfig.B_ENB)
    test_pin("Back IN3 (Logic A)", HardwareConfig.B_IN3)
    test_pin("Back IN4 (Logic B)", HardwareConfig.B_IN4)
    
    print("--- DIAGNOSTIC COMPLETE ---")

if __name__ == "__main__":
    main()
