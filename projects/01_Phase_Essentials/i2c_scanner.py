from machine import Pin, I2C

# Diagnostic: Using Alternative Pins GP16 and GP17
sda_pin = Pin(16)
scl_pin = Pin(17)

# Initialize I2C (Note: GP16/17 are on I2C channel 0)
i2c = I2C(0, sda=sda_pin, scl=scl_pin, freq=100000)

print("Scanning I2C bus...")
devices = i2c.scan()

if len(devices) == 0:
    print("No I2C devices found!")
    print("Checklist:")
    print("1. Are SDA and SCL swapped? (Try swapping GP16 and GP17 pins)")
    print("2. Is the screen getting 3.3V and GND?")
    print("3. Are the wires pushed all the way in?")
else:
    print(f"I2C device(s) found: {len(devices)}")
    for device in devices:
        print(f"Decimal address: {device} | Hex address: {hex(device)}")
