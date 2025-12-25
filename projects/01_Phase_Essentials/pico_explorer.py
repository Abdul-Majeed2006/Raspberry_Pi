import machine
import time

# Usable GPIO pins for most students
ALL_DIGITAL = list(range(23)) 
ALL_ANALOG = [26, 27, 28]

def header(title):
    print("\n" + "="*30)
    print(f" {title}")
    print("="*30)

def pulse_outputs():
    header("OUTPUT PULSE SCAN")
    print("Pulsing every GP pin. Watch your LEDs/Buzzer!")
    for p in ALL_DIGITAL:
        print(f"Testing GP{p}...", end="\r")
        pin = machine.Pin(p, machine.Pin.OUT)
        # 3 fast pulses
        for _ in range(3):
            pin.value(1)
            time.sleep(0.05)
            pin.value(0)
            time.sleep(0.05)
        time.sleep(0.3)
    print("\nPulse Scan Complete.")

def live_monitor():
    header("LIVE INPUT MONITOR")
    print("Reading all pins. Press buttons or turn knobs!")
    print("Press Ctrl+C to stop.")
    
    # Initialize all digital pins as inputs with pull-downs
    pins = []
    for p in ALL_DIGITAL:
        try:
            pins.append(machine.Pin(p, machine.Pin.IN, machine.Pin.PULL_DOWN))
        except:
            pins.append(None)
            
    # Initialize ADCs
    adcs = [machine.ADC(p) for p in ALL_ANALOG]
    
    last_digital = [0] * len(pins)
    
    try:
        while True:
            changes = []
            # Check Digital
            for i, p in enumerate(pins):
                if p:
                    val = p.value()
                    if val != last_digital[i]:
                        changes.append(f"GP{ALL_DIGITAL[i]}:{val}")
                        last_digital[i] = val
            
            # Read Analog
            analog_vals = [f"ADC{p-26}:{adcs[i].read_u16():5}" for i, p in enumerate(ALL_ANALOG)]
            
            # Display
            if changes:
                print(f"[EVENT] {' | '.join(changes)}")
            
            print(f"[ANALOG] {' | '.join(analog_vals)}", end="\r")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

def menu():
    while True:
        header("UNIVERSAL HARDWARE EXPLORER")
        print("1. Pulse All Pins (Find LEDs/Buzzers)")
        print("2. Live Monitor (Find Buttons/Knobs)")
        print("3. Exit")
        
        choice = input("\nSelect (1-3): ")
        
        if choice == "1":
            pulse_outputs()
        elif choice == "2":
            live_monitor()
        elif choice == "3":
            print("Goodbye student! Happy coding.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
