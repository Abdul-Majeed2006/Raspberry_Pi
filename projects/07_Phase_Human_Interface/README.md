# 🎹 Phase 06: Human Interface

Robots are cool, but control is better. In this phase, we learn how to read instructions from humans using Mechanical Switches.

## 📂 Contents
*   [**01_mechanical_switch.py**](./lessons/01_mechanical_switch.py): Basic Pull-Down logic.
*   [**02_debounced_toggle.py**](./lessons/02_debounced_toggle.py): Fixing the "bouncy" signal physics.
*   [**03_eye_controller.py**](./lessons/03_eye_controller.py): Controlling the Phase 04 OLED Eye with buttons.

## 📓 Notes & Theory
*   [**Switch Anatomy & Logic**](./notes/Switch_Anatomy_and_Logic.ipynb): Understanding precisely how to wire two pins and why Pull-Downs are required.

## 🎯 Learning Goals
1.  **Pull-Up/Pull-Down**: Why we can't just connect a button to a pin.
2.  **Debouncing**: The art of ignoring noise in a mechanical signal.
3.  **HMI (Human Machine Interface)**: Linking physical input to software logic.

## 🔌 Wiring Guide
- **Left Key**: Pin GP20 (3.3V power -> Switch -> GP20).
- **Right Key**: Pin GP21 (3.3V power -> Switch -> GP21).

---
[⬅️ Back to Master Map](../README.md)
