# 🛰️ Phase 05: System Integration

This is the "Final Boss" of the curriculum. Here, we combine everything we've learned into a single, complex system.

## 🚀 The Master Project: AWD Truck Dashboard

The `dashboard.py` script is your main controller. It uses a **Non-Blocking Loop** to drive the wheels and update the OLED screen simultaneously.

### 📋 Files
- **`dashboard.py`**: The Brain. Run this file!
- **`AWD.py`**: The Motor Driver Logic (copied from Phase 03).
- **`ssd1306.py`**: The Screen Driver (copied from Phase 04).

## 🎮 How to Run
1.  Open `dashboard.py` in Thonny or VS Code.
2.  Ensure your Pico is powered (9V BATTERY REQUIRED for motors).
3.  Run the script.
    - **Screen**: Should show "AWD TRUCK PRO".
    - **Wheels**: Should cycle Forward -> Stop -> Reverse.

## 🎯 Integration Goals
1.  **Parallel Tasks**: Running motor logic and screen updates simultaneously.
2.  **Telemetry**: Displaying internal data (like speed) on the visual interface.
3.  **Visualizer**: Watch the tiny truck icon on the OLED match your real truck's movement!

---
[⬅️ Back to Master Map](../README.md)
