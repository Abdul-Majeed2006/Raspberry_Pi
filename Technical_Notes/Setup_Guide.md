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

## Step 4: Verify System Communication

Run this simple logic test to ensure your computer can send instructions to the Pico's processor:

```python
import machine
import os

# Identify the chip
print(f"Controller: {os.uname().machine}")

# Perform a basic math operation in memory
result = 12 * 12
print(f"Math calculation verified: 12 * 12 = {result}")

# Check the main system frequency
print(f"CPU Frequency: {machine.freq() / 1000000} MHz")
```

**Expected Result**: The terminal should print the chip details and the math result.

✅ If you see the text, your communication channel is established and the Pico is processing code correctly.

---

## Troubleshooting

### "Device not found" error
- Make sure you flashed MicroPython (Step 1).
- Try a different USB cable (ensure it is a high-quality data cable).
- On Windows, verify the COM port in Device Manager.

### "Import Error: machine"
- You're running **standard Python** on your computer instead of **MicroPython** on the Pico.
- Ensure your editor's interpreter is set to "MicroPython (Raspberry Pi Pico)".

---

**All set?** You are ready to begin exploring the system logic.
