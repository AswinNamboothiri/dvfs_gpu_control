# main_simulation.py

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Setup for folder structure
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.pid_controller import PIDController
from plants.gpu_plant_model import GpuPlantModel

# Simulation settings
dt = 0.01
t_max = 6
time = np.arange(0, t_max, dt)

# Controller settings
pid = PIDController(Kp=0.005, Ki=0.001, Kd=0.0005, setpoint=1500, output_limits=(-1, 1))
# (setpoint is 1500 MHz desired GPU frequency)

# Plant settings
gpu = GpuPlantModel(base_frequency=1000, max_frequency=2000, efficiency_constant=0.00001)

# Data logging
frequency_log = []
power_log = []
energy_log = []
setpoint_log = []
disturbance_applied = False

total_energy = 0

for t in time:
    # Apply disturbance at t = 3.0s
    if not disturbance_applied and t >= 3.0:
        gpu.max_frequency *= 0.8  # Simulate system limiting max clock speed (thermal limit)
        disturbance_applied = True

    measurement = gpu.frequency
    control_signal = pid.compute(measurement, dt)
    frequency, power = gpu.update(control_signal, dt)

    # Energy = Power * time interval
    total_energy += power * dt

    frequency_log.append(frequency)
    power_log.append(power)
    energy_log.append(total_energy)
    setpoint_log.append(pid.setpoint)

# Plotting Frequency over time
plt.figure(figsize=(12, 6))
plt.plot(time, frequency_log, label='GPU Frequency (MHz)')
plt.plot(time, setpoint_log, 'r--', label='Target Frequency')
plt.axvline(x=3.0, color='magenta', linestyle=':', label='Disturbance')
plt.title('GPU Frequency Control with PID and Disturbance')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (MHz)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('plots/frequency_control.png')
plt.show()

# Plotting Power over time
plt.figure(figsize=(12, 6))
plt.plot(time, power_log, label='Power Consumption (W)')
plt.title('GPU Power Consumption Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Power (Watts)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('plots/power_consumption.png')
plt.show()

# Plotting Cumulative Energy over time
plt.figure(figsize=(12, 6))
plt.plot(time, energy_log, label='Cumulative Energy Used (Joules)')
plt.title('Total Energy Usage Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Energy (Joules)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('plots/total_energy.png')
plt.show()

# Final Total Energy
print(f"Total energy consumed during simulation: {total_energy:.2f} Joules")

