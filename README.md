# DVFS PID Control Simulation

This project simulates a **PID controller** applied to a simple dynamic system (plant) with disturbance handling and anti-windup strategies, supporting future Dynamic Voltage and Frequency Scaling (DVFS) research for GPUs.

---

📂 Project Structure

  dvfs_project/ 
              ├── controllers/ 
              │        └── pid_controller.py # PID controller with anti-windup 
              ├── plants/ 
              │      └── plant_model.py # Simple plant dynamics model 
              ├── simulations/ 
              │      └── main_simulation.py # Main script to simulate and plot 
              ├── plots/ 
              │      └── [Generated plots here] 
              ├── archive/ 
              │      └── [Old versions / experimental files] 
              ├── requirements.txt 
              └── README.md


---

## 🛠️ How to Run

1. **Clone this project** or download it.

2. **Create a Python virtual environment (optional but recommended)**:
   ```bash
   python3 -m venv dvfs_project_env
   source dvfs_project_env/bin/activate
Install the required libraries: pip install -r requirements.txt

Run the simulation: cd simulations

python3 main_simulation.py

View generated plots in the plots/ directory!

📈 Features
PID controller with anti-windup logic.

Disturbance handling (e.g., sudden drop in system gain).

Plotting of system response, setpoint tracking, and disturbance.

Structured modular code (controller, plant, simulation).

Future ready for extension into ML-based adaptive control.

🔥 Future Extensions
Implement DVFS simulations for real GPU models.

Add Machine Learning based adaptive PID tuning.

Benchmark energy efficiency improvements.

Integrate real-time simulation environments (e.g., Simulink, ROS).

📚 Requirements
Python 3.8+

numpy

matplotlib

👨‍💻 Author
Aswin P



📝 License
[MIT License]
