# ⚙️ Quick Start Guide

Get your environment ready in 5 minutes.

## 🚀 1. The Firmware (The Brain)
Your Pico needs an operating system to understand Python.
1.  Download the **[Latest MicroPython .uf2](https://micropython.org/download/rp2-pico/)**.
2.  Hold the **BOOTSEL** button on your Pico while plugging it in.
3.  Drag the `.uf2` file onto the new `RPI-RP2` drive.
4.  The Pico will reboot. Use a high-quality USB cable!

## 💻 2. The Editor (The Interface)
We recommend **Thonny** for beginners or **VS Code** for pros.

### Option A: Thonny (Recommended)
- **Download**: [thonny.org](https://thonny.org/)
- **Setup**: Bottom-right corner -> Select `MicroPython (Raspberry Pi Pico)`.
- **Verify**: Type `print("Hello")` in the shell. If it talks back, you win.

### Option B: VS Code (Advanced)
- Install the **MicroPico** extension.
- Use `Ctrl+Shift+P` -> `MicroPico: Configure Project`.

## 📦 3. The Libraries (The Tuning)
For Phase 04, you will need the OLED driver.
1.  Download `ssd1306.py` from our `projects/04_Phase_Visual_UI/library/` folder.
2.  Save it to the **root** of your Pico using your editor.

---
[⬅️ Back to Home](./README.md)
