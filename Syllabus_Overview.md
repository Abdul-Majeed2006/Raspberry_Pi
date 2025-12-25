# 🎓 The Engineering Syllabus

A detailed breakdown of every concept covered in the **Raspberry Pi Pico Mastery Course**.

---

## 🏛️ Phase 01: The Foundation (Essentials)
*Before we build, we prepare.*
- **Hardware Anatomy**: The RP2040 Chip, Pins, and Power logic.
- **The Deployment Cycle**: `main.py` vs. IDE execution.
- **Diagnostics**: Using the I2C Scanner to "see" invisible hardware.

## 💡 Phase 02: The Nervous System (Input/Output)
*Speaking the language of electricity.*
- **Digital Signals**: High (3.3V) vs. Low (GND).
- **PWM (Pulse Width Modulation)**: Simulating analog perception.
- **Human Input**: Debouncing buttons and reading state changes.
- **The Loop**: Understanding the `while True` realtime cycle.

## 🏎️ Phase 03: Kinetic Energy (Motion)
*Moving atoms in the physical world.*
- **The H-Bridge**: Isolating logic (3.3V) from power (9V).
- **Differential Drive**: Steering by speed difference (Tank Controls).
- **Newtonian Code**: Implementing acceleration curves and "Soft Start."
- **Power Management**: avoiding Brownouts and resets.

## 👁️ Phase 04: Visual Feedback (UI)
*Giving the machine a personality.*
- **I2C Communication**: The 2-wire protocol.
- **Memory Mapping**: The FrameBuffer concept.
- **Geometry**: Drawing primitives (Lines, Rects, Circles).
- **State Machines**: Implementing specific modes (Blinking, Looking, Sleeping).
- **Animation**: The "Clear-Update-Draw" refresh loop.

## 🛰️ Phase 05: System Integration (Capstone)
*The sum of all parts.*
- **Concurrency**: Doing two things at once (Driving + Drawing).
- **Telemetry**: Displaying real-time sensor data on the screen.
- **Autonomous Behaviors**: Combining sensors and motors for self-driving logic.
- **Final Deployment**: Packaging the project for the real world.

---
[⬅️ Back to Home](./README.md)
