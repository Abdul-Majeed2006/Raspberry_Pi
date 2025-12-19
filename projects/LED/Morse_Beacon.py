# ==========================================================
# MASTERY PROJECT 4: THE MORSE CODE BEACON
# Goal: Use a Python Dictionary to translate text into 
# a sequence of light and sound signals (Dots & Dashes).
# ==========================================================

from machine import Pin, PWM
from time import sleep

# ----------------------------------------------------------
# 1. HARDWARE SETUP
# ----------------------------------------------------------
# We use Blue for the Beacon (feels more tactical!)
red_led   = PWM(Pin(21), freq=1000)
green_led = PWM(Pin(22), freq=1000)
blue_led  = PWM(Pin(20), freq=1000)

buzzer = PWM(Pin(9))

# ----------------------------------------------------------
# 2. MORSE CODE DICTIONARY
# ----------------------------------------------------------
MORSE_MAP = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',  'E': '.',
    'F': '..-.', 'G': '--.',  'H': '....', 'I': '..',   'J': '.---',
    'K': '-.-',  'L': '.-..', 'M': '--',   'N': '-.',   'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',
    'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--',
    'Z': '--..', ' ': '/'     # Space becomes a forward slash
}

# TIMING (Standard Morse Ratios)
UNIT = 0.15 # 0.15 seconds per 'dot'
DOT  = UNIT
DASH = UNIT * 3
GAP  = UNIT    # Gap between dots/dashes
LETTER_GAP = UNIT * 3 

# ----------------------------------------------------------
# 3. SIGNAL FUNCTIONS
# ----------------------------------------------------------

def play_signal(duration):
    """Turns on Blue light and Buzzer for a set time."""
    blue_led.duty_u16(40000)
    buzzer.freq(1000)
    buzzer.duty_u16(10000)
    sleep(duration)
    
    # SILENCE
    blue_led.duty_u16(0)
    buzzer.duty_u16(0)
    sleep(GAP)

# ----------------------------------------------------------
# 4. DATA TRANSLATION LOOP
# ----------------------------------------------------------
MESSAGE = "HELLO PICO" # Change this message!

print(f"SYSTEM: Broadcasting Morse Message: '{MESSAGE}'")

try:
    while True:
        for character in MESSAGE.upper():
            if character in MORSE_MAP:
                code = MORSE_MAP[character]
                print(f"Blinking: {character} ({code})")
                
                # Check for space (Special case)
                if code == '/':
                    sleep(LETTER_GAP)
                    continue
                
                # Iterate through the dots and dashes in the character's code
                for symbol in code:
                    if symbol == '.':
                        play_signal(DOT)
                    elif symbol == '-':
                        play_signal(DASH)
                
                # Pause between letters
                sleep(LETTER_GAP)
        
        # Long pause before the message repeats
        print("--- End of Message ---")
        sleep(2.0)

except KeyboardInterrupt:
    blue_led.duty_u16(0)
    buzzer.duty_u16(0)
    print("\nMorse Beacon Deactivated.")
