# STANDALONE DEPLOYMENT: The 'main.py' Rule

When you are developing in Antigravity (VS Code), your code is usually "streaming" from the computer. If you unplug the USB, the code stops because it only exists in the Pico's temporary memory (RAM).

To build a **Robot**, a **Smart Safe**, or a **Wearable Device**, you need the Pico to run your code the second it gets power from a battery, without a computer.

### 1. The Startup Sequence
Every time the Raspberry Pi Pico powers up, it automatically performs two searches on its internal flash drive:
1.  **`boot.py`**: It runs this first (mostly for advanced setup like USB settings).
2.  **`main.py`**: It runs this second. This is where your actual project logic lives.

### 2. How to "Deploy" your Robot 🤖
If you have a script finished (e.g., `Rainbow_Hue.py`) and you want to make it permanent:
1.  Open the file system of the Pico (usually shows up as a "USB Drive" or via the extension).
2.  Save your finalized code to the Pico's storage.
3.  **RENAME THE FILE TO `main.py`**.

### 3. Testing Standalone
Once you have renamed your code to `main.py`:
1.  Unplug the Pico from your computer.
2.  Plug it into a battery pack or a wall outlet.
3.  **Magic**: The Pico will boot up and start running your code immediately!

> [!IMPORTANT]
> **Infinite Loops**: Since `main.py` runs on startup, always make sure you have a `try...except KeyboardInterrupt` block so you can still stop it if you plug it back into a computer later!
