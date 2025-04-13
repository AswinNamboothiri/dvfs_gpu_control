import numpy as np
import matplotlib.pyplot as plt

# PID coefficients
Kp = 2.0
Ki = 0.5
Kd = 1.0

# Simulation parameters
setpoint = 50
process_variable = 30
integral = 0
previous_error = 0

# Time settings
t_max = 6
dt = 0.01
time = np.arange(0, t_max, dt)

# Disturbance flag
disturbance_applied = False

# Store output for plotting
output_list = []

for i in range(1, len(time)):
    # Apply disturbance at 3 seconds
    if time[i] > 3 and not disturbance_applied:
        process_variable += 10  # Disturbance of +10 units
        disturbance_applied = True

    # PID calculations
    error = setpoint - process_variable
    integral += error * dt
    derivative = (error - previous_error) / dt
    output = Kp * error + Ki * integral + Kd * derivative

    process_variable += output * dt
    previous_error = error

    output_list.append(process_variable)

# Plotting
plt.figure(figsize=(8,6))
plt.plot(time[:-1], output_list, label='PID Output', linewidth=2)
plt.axhline(y=setpoint, color='r', linestyle='--', label='Setpoint')
plt.axvline(x=3, color='purple', linestyle=':', label='Disturbance')
plt.title('PID Controller Simulation with Disturbance')
plt.xlabel('Time (s)')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.savefig('pid_simulation_disturbed.png')
plt.close()  # Save without opening popup
