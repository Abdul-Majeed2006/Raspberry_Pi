# =============================================================================
# DRIVER: SSD1306 OLED (ULTRA-EDUCATIONAL VERSION)
# =============================================================================
# This file is the "Manual" for the silicon chip (SSD1306) on your screen.
# Every number here was decided by the factory that built the chip.
# =============================================================================

from micropython import const
import framebuf

# --- THE COMMAND DICTIONARY (Registers) ---
# Each number is a "Function Code" hardcoded into the chip's internal wiring.
# If you send these numbers, the chip changes its physical state.

# Hex (0x81) | Decimal (129)
# Why 0x81? The manufacturer (Solomon Systech) designed the chip so that 
# when it receives 129, it knows the NEXT byte you send will set brightness.
SET_CONTRAST = const(0x81)       

# Hex (0xA4) | Decimal (164)
# This button tells the chip: "Stop being all white/black, follow my RAM."
SET_ENTIRE_ON = const(0xA4)      

# Hex (0xA6) | Decimal (166)
# 166 = Normal (Background is Black), 167 (0xA7) = Inverted (Background is White).
SET_NORM_INV = const(0xA6)       

# Hex (0xAE) | Decimal (174)
# Sleep mode. 174 = Display OFF, 175 (0xAF) = Display ON.
SET_DISP = const(0xAE)           

# Hex (0x20) | Decimal (32)
# Determines how the "pen" moves. Horizontal, Vertical, or Page mode.
SET_MEM_ADDR = const(0x20)       

# Hex (0x21) | Decimal (33)
# Sets the "Safe Zone" for X-coordinates (0 to 127).
SET_COL_ADDR = const(0x21)       

# Hex (0x22) | Decimal (34)
# Sets the "Safe Zone" for Y-coordinates (Rows are grouped in 8-pixel blocks).
SET_PAGE_ADDR = const(0x22)      

# Hex (0x8D) | Decimal (141)
# CRITICAL: This turns on the "Charge Pump." OLED cells need high voltage.
# This tells the screen to "Boost" the Pico's 3.3V up to a level that lights up.
SET_CHARGE_PUMP = const(0x8D)    

# Other system settings defined by the chip datasheet:
SET_DISP_START_LINE = const(0x40) # 64
SET_SEG_REMAP = const(0xA0)       # 160
SET_MUX_RATIO = const(0xA8)       # 168
SET_IREF_SELECT = const(0xAD)     # 173
SET_COM_OUT_DIR = const(0xC0)     # 192
SET_DISP_OFFSET = const(0xD3)     # 211
SET_COM_PIN_CFG = const(0xDA)     # 218
SET_DISP_CLK_DIV = const(0xD5)    # 213
SET_PRECHARGE = const(0xD9)       # 217
SET_VCOM_DESEL = const(0xDB)      # 219

# --- CLASS 1: THE BRAIN (Logic & Geometry) ---
# This class handles the "Virtual Sketchpad" (FrameBuffer).
# It's an "Abstract" class: it knows HOW to draw circles and lines, 
# but it doesn't know what wires (I2C or SPI) you are using.
class SSD1306(framebuf.FrameBuffer):
    def __init__(self, width, height, external_vcc):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        # The chip groups pixels in 8-pixel tall "Pages". 
        # 64 pixels high / 8 = 8 Pages.
        self.pages = self.height // 8
        
        # Create a "Buffer" (A big block of RAM in the Pico).
        # This is exactly where the image lives before you call .show()
        self.buffer = bytearray(self.pages * self.width)
        
        # 'super().__init__' tells Python to use the built-in FrameBuffer tool
        # that already knows how to draw text, lines, and boxes.
        super().__init__(self.buffer, self.width, self.height, framebuf.MONO_VLSB)
        self.init_display()

    def init_display(self):
        """The Startup Routine: A sequence of 'Wait' and 'Do This'."""
        # We loop through a list of commands the manufacturer requires to wake up.
        for cmd in (
            SET_DISP,            # Display OFF
            SET_MEM_ADDR, 0x00, # Set to Horizontal Mode (Fill row by row)
            SET_DISP_START_LINE,
            SET_SEG_REMAP | 0x01,
            SET_MUX_RATIO, self.height - 1,
            SET_COM_OUT_DIR | 0x08,
            SET_DISP_OFFSET, 0x00,
            SET_COM_PIN_CFG, 0x02 if self.width > 2 * self.height else 0x12,
            SET_DISP_CLK_DIV, 0x80,
            SET_PRECHARGE, 0x22 if self.external_vcc else 0xF1,
            SET_VCOM_DESEL, 0x30,
            SET_CONTRAST, 0xFF, # Max Brightness (0 to 255)
            SET_ENTIRE_ON,      # Resume to RAM content
            SET_NORM_INV,       # Non-inverted
            SET_IREF_SELECT, 0x30,
            SET_CHARGE_PUMP, 0x10 if self.external_vcc else 0x14, # BOOSTER ON
            SET_DISP | 0x01,    # Display ON!
        ):
            self.write_cmd(cmd)
        self.fill(0) # Start with a clean black screen
        self.show()

    def poweroff(self): self.write_cmd(SET_DISP)
    def poweron(self): self.write_cmd(SET_DISP | 0x01)
    
    def contrast(self, contrast):
        """Allows you to change the brightness (0-255)."""
        self.write_cmd(SET_CONTRAST) # The "Contrast Button"
        self.write_cmd(contrast)     # The "New Value"

    def show(self):
        """THE PUNCHLINE: Pushes your RAM Buffer out to the real glass."""
        # 1. We tell the screen: "I'm about to send everything from 0,0 to the end."
        self.write_cmd(SET_COL_ADDR)
        self.write_cmd(0)
        self.write_cmd(self.width - 1)
        self.write_cmd(SET_PAGE_ADDR)
        self.write_cmd(0)
        self.write_cmd(self.pages - 1)
        # 2. We dump the massive pile of pixel data.
        self.write_data(self.buffer)

# --- CLASS 2: THE HANDS (I2C Wiring) ---
# This class 'Inherits' from the one above. 
# It takes the logic of a screen and adds the specific I2C wire commands.
class SSD1306_I2C(SSD1306):
    def __init__(self, width, height, i2c, addr=0x3C, external_vcc=False):
        self.i2c = i2c   # Your I2C object (Pins 16/17)
        self.addr = addr # Usually 0x3C (60)
        self.temp = bytearray(2)
        # 0x40 (64) is a 'Control Byte' that tells the OLED: 
        # "Everything following this byte is PIXEL DATA, not a command."
        self.write_list = [b"\x40", None]  
        super().__init__(width, height, external_vcc)

    def write_cmd(self, cmd):
        """Sends a single COMMAND (The 'Remote Control' button)"""
        # 0x80 (128) tells the OLED: "The very next byte is a COMMAND."
        self.temp[0] = 0x80  
        self.temp[1] = cmd
        self.i2c.writeto(self.addr, self.temp)

    def write_data(self, buf):
        """Sends a massive block of PIXELS (The 'Movie' or image)"""
        self.write_list[1] = buf
        self.i2c.writevto(self.addr, self.write_list)
