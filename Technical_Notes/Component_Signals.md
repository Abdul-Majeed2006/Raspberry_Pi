# Component Signal Categories 🔌

To control or read any hardware with the Raspberry Pi Pico, you must first understand what *type* of signal it uses. This guide categorizes common electronics by their interaction with the controller.

---

## 1. Digital Output (Binary Control)
These components are either "On" or "Off". They serve as the simplest form of physical interaction.

- **Conceptual Examples**: Anything that acts as a switch (Relays, Solenoids, simple visual indicators).
- **Control Signal**: 3.3V (HIGH) to activate, 0V (LOW) to deactivate.
- **MicroPython Tool**: `machine.Pin(p, machine.Pin.OUT)`

---

## 2. PWM Out (Variable Intensity)
Components that require a specific "level" of power or a specific timing signal.

- **Conceptual Examples**: Motors (speed control), Dimming circuits, or components that produce frequencies (Piezo elements).
- **Control Signal**: A rapid ON/OFF pulse where the "Duty Cycle" determines the average power.
- **MicroPython Tool**: `machine.PWM(machine.Pin(p))`

---

## 3. Digital Input (Listening for States)
The Pico "listens" to see if a circuit has been closed or opened by an external event.

- **Conceptual Examples**: Buttons, Switches, or sensors that output a simple YES/NO state (like a motion sensor).
- **Input Signal**: The Pico detects if a pin is being pulled to 3.3V or 0V.
- **MicroPython Tool**: `machine.Pin(p, machine.Pin.IN)`

---

## 4. Analog Input (ADC Sampling)
Nature is not binary. To measure things like temperature, pressure, or rotational position, we use the ADC.

- **Conceptual Examples**: Potentiometers (knobs), Temperature sensors, Light intensity sensors.
- **Input Signal**: A smooth voltage range between 0V and 3.3V.
- **MicroPython Tool**: `machine.ADC(p)`

---

## Summary Table

| Signal Type | Direction | Data Range | Purpose |
| :--- | :--- | :--- | :--- |
| **Digital** | OUT | 0 or 1 | Simple On/Off |
| **PWM** | OUT | 0 - 65535 | Intensity / Frequency |
| **Digital** | IN | 0 or 1 | Detecting Events |
| **ADC** | IN | 0 - 65535 | Measuring Reality |

---

> [!TIP]
> **Logic First:** Before wiring a new component, ask yourself: "Is this a Yes/No signal, or a 'How Much' signal?" This tells you exactly which code library and pin to use.
