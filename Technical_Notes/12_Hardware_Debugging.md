# Technical Note 12: Hardware Debugging & Logic Shifts

When working with physical computing, the code isn't the only thing that can break. This note covers how to handle "Dead Pins" and "Logic Phantoms."

## 1. The "Dead Pin" Phenomenon 🛰️💀
Sometimes, a specific GPIO pin on your Pico can stop functioning. 
- **Cause**: Static electricity, accidental short circuits, or internal manufacturing flaws.
- **Symptom**: Code runs perfectly, LEDs blink on the Pico, but no signal arrives at the component.
- **Fix**: **Signal Relocation.** Simply move your wire to a fresh GPIO pin (e.g., GP9 or GP16) and update your code mapping.

## 2. Logic Mismatch: Forward vs Backward 🔄🏎️
In AWD systems, even identical motors might be wired "inside-out" compared to each other.
- **Problem**: Sending a "Forward" command moves the front wheels forward but the back wheels backward.
- **Solution**: **Polarity Masking.** 
  Instead of rewiring the truck, we use a software multiplier:
  ```python
  # intent is 1 (forward) or -1 (backward)
  # result = intent * (inversion_flag)
  actual_dir = intent * (-1 if inverted else 1)
  ```

## 3. The "Breadboard Phantom" 👻🔌
Breadboards can be tricky.
- **Rule**: Standard breadboards use **Vertical** signal strips.
- **Common Mistake**: Connecting components in horizontal rows. This looks correct visually but results in zero electrical contact.
- **Verification**: Always ensure your Pico pin and your bridge wire are sharing the same **Numbered Column**.

## 4. Voltage Sag (The Red Blink) 🔋🚨
- **Symptom**: The H-bridge power LED blinks or flickers when you start the motors.
- **Diagnosis**: Your battery cannot provide enough current (strength) for the initial surge of the motors.
- **Fix**: **Staggered Start.** Turn on Axle A, wait 5ms, then turn on Axle B. This breaks the "punch" the battery has to take.
