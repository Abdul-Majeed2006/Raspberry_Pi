# ⚡ Raspberry Pi Pico: The Engineering Curriculum

![Status](https://img.shields.io/badge/Status-Active-success) ![Platform](https://img.shields.io/badge/Platform-RP2040-blue) ![Level](https://img.shields.io/badge/Level-Zero_to_Hero-orange)

> **"Don't just write code. Build systems."**

Welcome to the **Mastery-Level Physical Computing Course**. This repository is designed to transform you from a beginner into a systems engineer, capable of building integrated, autonomous robots.

---

## 🗺️ The Roadmap

Our curriculum is organized into **7 Distinct Phases**. Follow them in order to build your skills layer by layer.

| 🏁 Phase | 🏷️ Title | 🎯 Mission |
| :--- | :--- | :--- |
| **01** | [**Essentials**](./projects/01_Phase_Essentials/README.md) | **First Light.** Learn to deploy code and diagnose hardware. <br> *Tools: I2C Scanner, Deployment Guide* |
| **02** | [**Digital I/O**](./projects/02_Phase_Input_Output/README.md) | **The Nervous System.** Master LEDs, Buttons, and Signals. <br> *Projects: Traffic Light, Reaction Game* |
| **03** | [**Motion**](./projects/03_Phase_Motion_Control/README.md) | **Kinetic Power.** Control DC Motors, H-Bridges, and Physics. <br> *Projects: AWD Chassis logic* |
| **04** | [**Visual UI**](./projects/04_Phase_Visual_UI/README.md) | **The Face.** Build rich OLED interfaces and Animations. <br> *Projects: AI Eye, Status Dashboard* |
| **05** | [**Integration**](./projects/05_Phase_System_Integration/README.md) | **The Final Boss.** Combine everything into one system. <br> *Capstone: Autonomous AWD Truck* |
| **06** | [**Interface**](./projects/06_Phase_Human_Interface/README.md) | **The Controls.** Mechanical Buttons and HMI. <br> *Projects: Eye Controller, Mode Switching* |
| **07** | [**Networking**](./projects/07_Phase_Networking/README.md) | **The Internet.** Wi-Fi, NTP, and Web Data. <br> *Projects: World Clock Dashboard* |

---

## 🏗️ How to Use This Workspace

### 1. 📥 Setup
Before you write a single line of code, ensure your environment is ready.
👉 **[Read the Setup Guide](./Setup_Guide.md)**

### 2. 🧠 Theory & Concepts
We don't just paste code; we explain the engineering. Check the **[Notes Library](./projects/04_Phase_Visual_UI/notes/)** for Deep Dives into:
- **I2C Protocols** (How chips talk)
- **H-Bridge Logic** (How low power controls high power)
- **FrameBuffers** (How memory becomes pixels)

### 3. 🛠️ The Workbench
Inside the `projects/` folder, you will find:
- **`library/`**: The raw drivers (like `ssd1306.py`).
- **`lessons/`**: Step-by-step code files.
- **`notes/`**: Explanatory notebooks.

---

## ⚡ Quick Links
- [Deployment Guide](./projects/01_Phase_Essentials/Deployment_and_Main_PY.ipynb) (How to run on battery)
- [I2C Scanner Tool](./projects/01_Phase_Essentials/i2c_scanner.py) (Hardware debugger)
- [Full Syllabus](./Syllabus_Overview.md) (Detailed topic list)

---
*Created for future engineers.* 🏎️🛰️👁️
