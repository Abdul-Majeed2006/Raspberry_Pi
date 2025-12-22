# LESSON 08: THE HARDWARE OF MOTION (L298N) 🏎️🔌

You can't write code for a motor until you understand the **Power Bridge**. The Pico is smart, but weak. The L298N is "dumb," but strong. We must connect them so the Pico can give the orders and the L298N can do the heavy lifting.

---

## 🏗️ 1. Identifying the L298N Board
Look at your L298N board. It has three main areas:

### A. The Power Terminals (Screw Terminals)
These are where the "Juice" comes from.
*   **12V Terminal**: Connect your 9V Battery **Positive (+)** here. (Don't worry, it handles 7V-35V).
*   **GND Terminal**: This is the **Shared Ground**. You connect the 9V Battery **Negative (-)** AND a **GND pin** from your Pico here.
*   **5V Terminal**: Leave this empty for now.

### B. The Logic Pins (Male Headers)
These are the "Ears" of the driver. They listen to the Pico. To understand these, think of a Car:

*   **ENA (The Gas Pedal)**: This pin controls the **Speed**. 
    > [!TIP]
    > **The Two-Pin Mystery**: Under that black cap, you will see **two pins**. 
    > 1. The pin **closer to the IN1/IN2 pins** is the **Signal Pin**. Connect your Pico wire here!
    > 2. The other pin is a 5V power pin. **Do NOT connect the Pico to this pin.**
*   **IN1 / IN2 (The Gear Shifter)**: These two pins control the **Direction**. 
    *   Think of it like choosing "Forward" or "Reverse."
    *   To go forward: One pin is ON (HIGH) and the other is OFF (LOW).
    *   To stop: We set both to OFF.
*   **IN3 / IN4**: These are just a second set of shifters for your **second motor** (Motor B).

### C. The Motor Outputs (Screw Terminals)
*   **OUT1 / OUT2**: Connect the wires of your first motor here.

---

## 🌉 2. Concept: The "H" in H-Bridge
Think of the H-Bridge as a set of 4 doors. 
- If doors 1 and 4 are open, electricity flows **Left-to-Right** (Motor goes Forward).
- If doors 2 and 3 are open, electricity flows **Right-to-Left** (Motor goes Backward).

The Pico controls these "doors" using the **IN1** and **IN2** pins.

---

## 🗺️ 3. Step-by-Step Wiring Map

| Pico 2 Pin | L298N Pin | Purpose |
| :--- | :--- | :--- |
| **GND** | **GND Terminal** | The Shared Reference (CRITICAL) |
| **GP15** | **ENA** | Speed Command (How fast?) |
| **GP14** | **IN1** | Path A (Direction) |
| **GP13** | **IN2** | Path B (Direction) |

---

## 🎓 4. The "Magic" of the Shared Ground
**Question**: Why do we connect the 9V Ground and the Pico Ground together?
**Answer**: Imagine two people shouting at each other from different mountains. If they don't have a common "floor" to measure the sound from, they can't understand the message. The Shared Ground ensures the Pico's "3.3V" signal is measured against the same 0V as the battery.

---

## 🌊 5. Speed Modulation: The PWM Gas Pedal 
So far, we have only turned the motor ON or OFF. But to drive a robot carefully, we need to control the **Speed**.

On the Pico, we use **PWM (Pulse Width Modulation)** on the `ENA` pin. 
- **The Concept**: We flip the ENA pin ON and OFF so fast (1,000 times a second) that the motor only feels the "Average" power.
- **The Scale**: In MicroPython, we use numbers from **0** (Stop) to **65535** (Full Speed).

### Why use Ramping?
If you tell a motor to go from 0 to 100% instantly, the gears take a lot of stress and the battery sees a huge "spike" in demand. We use **Ramping** to smoothly increase the speed over 1 or 2 seconds.

---

## ⚠️ ELECTRICAL SAFETY (CRITICAL)
When using your 9V Li-ion batteries:

1.  **COMMON GROUND**: You MUST connect the GND of the battery and the Pico together.
2.  **SEPARATE POWER**: NEVER connect 9V to any pin on the Pico except GND.
3.  **Pico 2 (RP2350)**: Your new Pico 2 is faster and has more drive strength, but the 3.3V limit is the same. Be careful!
