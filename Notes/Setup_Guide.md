# Environment Setup Guide ⚙️

Before you can run code on your Pico, you need to:
1. Install MicroPython firmware on the Pico
2. Install an editor (Thonny or VS Code)
3. Connect and test

---

## Step 1: Install MicroPython on the Pico

### Download the Firmware
1. Go to [raspberrypi.com/documentation](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
2. Download the **latest `.uf2` file** for Raspberry Pi Pico

### Flash the Firmware
1. **Hold down the BOOTSEL button** on your Pico (the white button)
2. While holding it, **plug the Pico into your computer** via USB
3. Release the button. The Pico will appear as a USB drive called "RPI-RP2"
4. **Drag and drop** the `.uf2` file onto the drive
5. The Pico will **automatically reboot** and disappear as a drive

✅ **Done!** Your Pico is now running MicroPython.

---

## Step 2: Choose Your Editor

You have three main options:

### Option A: Mu Editor (Recommended - What This Course Uses)

#### Install Mu Editor
- **Windows/Mac/Linux**: [codewith.mu](https://codewith.mu/)
- Download and install (simple, beginner-friendly interface)

#### Configure Mu
1. Open Mu Editor
2. Click **Mode** button at the top
3. Select **"RP2040"** or **"Pico"** mode
4. Click **OK**

#### Test Connection
1. Plug in your Pico
2. Click the **REPL** button (bottom toolbar) to open the interactive shell
3. You should see:
   ```
   MicroPython v1.xx.x on 2024-xx-xx; Raspberry Pi Pico with RP2040
   >>>
   ```
4. Type: `print("Hello, Pico!")` and press Enter

✅ If you see the message, you're connected!

**Note on Notebooks**: Mu doesn't natively support `.ipynb` files. Simply copy/paste the code cells from each notebook into Mu's editor window.

---

### Option B: Thonny (Alternative)

#### Install Thonny
- **Windows/Mac/Linux**: [thonny.org](https://thonny.org/)
- Download and install

#### Configure Thonny
1. Open Thonny
2. Go to **Tools → Options → Interpreter**
3. Select **"MicroPython (Raspberry Pi Pico)"**
4. Click **OK**

---

### Option C: VS Code (For Advanced Users)

#### Install VS Code
- [code.visualstudio.com](https://code.visualstudio.com/)

#### Install the Pico Extension
1. Open VS Code
2. Go to **Extensions** (Ctrl+Shift+X)
3. Search for **"MicroPico"** or **"Pico-W-Go"**
4. Install the extension

#### Configure
1. Press `Ctrl+Shift+P` (Command Palette)
2. Type: `MicroPico: Configure Project`
3. Follow the prompts to set up your workspace

---

## Step 3: Open the Notebooks

### For Thonny Users
- Thonny doesn't natively support `.ipynb` files
- **Workaround**: Copy/paste code cells from the notebook into Thonny's editor

### For VS Code Users
1. Install the **Jupyter Extension** in VS Code
2. Open any `.ipynb` file
3. Select **MicroPython kernel** when prompted
4. Run cells with `Shift+Enter`

---

## Step 4: Test Your Setup

Run this simple test:

```python
import machine
import time

led = machine.Pin("LED", machine.Pin.OUT)

for i in range(5):
    led.toggle()
    time.sleep(0.5)
```

**Expected Result**: The onboard LED should blink 5 times.

✅ If it works, you're ready to start **Chapter 1**!

---

## Troubleshooting

### "Device not found" error
- Make sure you flashed MicroPython (Step 1)
- Try a different USB cable (some are power-only, no data)
- On Windows, you might need to install drivers

### "Import Error: machine"
- You're running **standard Python** instead of **MicroPython**
- Make sure your editor is connected to the Pico, not your computer's Python

### Code runs but LED doesn't blink
- Check your wiring
- Try the onboard LED first (no wiring needed): `machine.Pin("LED", machine.Pin.OUT)`

---

**All set?** Head to [01_Hello_Pico.ipynb](01_Hello_Pico.ipynb) and let's begin!
