# CHAPTER 7: HUMAN PERCEPTION & GAMMA 👁️✨

If you provide 50% power to an LED, it looks like it is 80% bright to a human. This is because the human eye is much more sensitive to dark colors than bright ones.

### 1. The Computer vs. The Eye
*   **Computer Logic (Linear)**: 1, 2, 3, 4, 5... (Changes are equal).
*   **Human Eye (Non-linear)**: We see the difference between "Off" and "Dim" much better than "Bright" and "Slightly Brighter."

If you use a standard loop to fade an LED, it will look like it "jumps" to full brightness almost instantly and then stays there.

### 2. The Solution: Gamma Correction
We use a mathematical formula called the **Power Law** to map our computer numbers to something that looks "Correct" to a human.

**The Formula**:
$CorrectedValue = ( \frac{Input}{Max} )^{\gamma} \times Max$

*   **Gamma ($\gamma$)**: Usually set to **2.8** for LEDs.
*   **Effect**: It compresses the lower values and expands the higher ones, making the fade look perfectly smooth.

### 3. Implementation in MicroPython
```python
gamma = 2.8

def set_brightness(percent):
    # Map 0-100% to 0-65535 using Gamma
    corrected = int(((percent / 100) ** gamma) * 65535)
    led.duty_u16(corrected)
```

### 4. Why this matters for RGB?
When mixing colors (like Orange), if you don't use Gamma, one color will often "overpower" the others, and you won't get the clean mix you want. Using Gamma is the secret to getting professional, vivid colors.
