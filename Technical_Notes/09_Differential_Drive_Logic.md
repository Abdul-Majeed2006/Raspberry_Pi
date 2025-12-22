# TECHNICAL NOTE 09: SYNCHRONIZED AWD LOGIC 🏎️⚙️

Your robot has a powerful **4WD (All-Wheel Drive)** chassis. Instead of Turning by "fighting" the wheels (Differential), this design uses two motors to drive two axles (Front and Back). 

---

## 1. The Anatomy of your Chassis
- **Motor A (Front)**: Drives both front wheels through a gearbox.
- **Motor B (Back)**: Drives both back wheels through a gearbox.

This setup is built for **Power and Traction**. It can climb over obstacles much better than a standard 2-wheeled robot.

---

## 2. Wiring the Axles
We follow the same Pico-to-L298N bridge, but we label them by position.

| Pico 2 Pin | L298N Pin | Purpose |
| :--- | :--- | :--- |
| **GP15** | **ENA** | Front Axle Speed |
| **GP14** | **IN1** | Front Forward |
| **GP13** | **IN2** | Front Backward |
| **GP12** | **ENB** | Back Axle Speed |
| **GP11** | **IN3** | Back Forward |
| **GP10** | **IN4** | Back Backward |

---

## 3. Engineering Concept: Synchronization
When you have two motors driving the same car, they **MUST** work together.
- If Motor A spins Forward and Motor B spins Backward, the robot will sit still and make a grinding noise (fighting itself).
- If one motor is slightly faster than the other, it can cause the gears to wear out.

In the code, we will create a `DriveSystem` that sends the exact same PWM signal to both axles at the same time.

---

## 4. Future: Steering with a Servo
Since your axles don't have a "Pivot" center (like a tank), you will use a **Servo Motor** (coming with your 37-kit) to physically turn the front wheels left or right.

For today, the robot's goal is **Linear Mastery**: Precise Forward and Backward movement at different power levels (Eco vs. Sport mode).

---

**Next Step**: Finish the wiring for the second motor. Ensure they both spin the "Forward" direction when given a Forward command!
