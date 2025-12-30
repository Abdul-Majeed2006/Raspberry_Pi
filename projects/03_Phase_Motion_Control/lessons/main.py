# ==========================================================
# ROBOT DEMO: AUTONOMOUS MANEUVERS
# ==========================================================
# Goal: Demonstrate the capabilities of the AWD Class.
#
# BEHAVIOR:
# 1. Drive Forward (2s)
# 2. Stop (1s)
# 3. Reverse (2s)
# 4. Turn Sequence
# ==========================================================

from AWD import AWD
import time

def main():
    # Initialize the Robot (uses HardwareConfig inside inputs)
    robot = AWD()
    
    print(">>> MISSION START: DEMO PATTERN <<<")
    time.sleep(1)
    
    try:
        # Leg 1: Deployment
        print("[1/4] Moving Out...")
        robot.forward()
        time.sleep(2)
        robot.stop()
        time.sleep(1)
        
        # Leg 2: Retreat
        print("[2/4] Returning...")
        robot.backward()
        time.sleep(2)
        robot.stop()
        time.sleep(1)
        
        # Leg 3: Evasion
        print("[3/4] Evasive Maneuvers...")
        robot.turn_left()
        time.sleep(1)
        robot.turn_right()
        time.sleep(1)
        robot.stop()
        
    except KeyboardInterrupt:
        print("!!! EMERGENCY STOP !!!")
    
    finally:
        robot.stop()
        print(">>> MISSION COMPLETE <<<")

if __name__ == "__main__":
    main()
