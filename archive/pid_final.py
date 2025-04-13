import numpy as np
import matplotlib.pyplot as plt

# Simulation settings
dt = 0.01  # Time step
t = np.arange(0, 6, dt)  # Time vector

# PID Controller parameters
Kp = 2.0    # Proportional gain
Ki = 1.0    # Integral gain
Kd = 0.5    # Derivative gain

# Saturation limits (Anti-windup)
output_min = -100
output_max = 100

# System model parameters
a = 0.8    # decay rate (realistic damping)
b = 0.2    # input effect

# Setpoint
setpoint = 50

# Initialize variables
integral = 0
previous_error = 0
process_variable = 0  # starting point
output = 0

# Storage for plotting
pv_history = []
setpoint_history = []
output_history = []

# Disturbance settings
disturbance_time = 3  # when disturbance occurs
disturbance_magnitude = -20  # sudden drop

for i in range(len(t)):
    current_time = t[i]

    # Introduce disturbance
    disturbance = 0
    if current_time >= disturbance_time:
        disturbance = disturbance_magnitude

    # Calculate error
    error = setpoint - process_variable

    # Integrate error
    integral += error * dt

    # Derivative of error
    derivative = (error - previous_error) / dt

    # PID formula
    output = Kp * error + Ki * integral + Kd * derivative

    # Apply saturation limits (clamping)
    if output > output_max:
        output = output_max
        # Anti-windup: prevent further integration
        integral -= error * dt
    elif output < output_min:
        output = output_min
        # Anti-windup: prevent further integration
        integral -= error * dt

    previous_error = error

    # Process dynamics (simple first order system)
    process_variable += (b * output + disturbance - a * process_variable) * dt

    # Save for plotting
    pv_history.append(process_variable)
    setpoint_history.append(setpoint)
    output_history.append(output)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, pv_history, label="PID Output")
plt.plot(t, setpoint_history, 'r--', label="Setpoint")
plt.axvline(x=disturbance_time, color='magenta', linestyle=':', label="Disturbance")
plt.xlabel('Time (s)')
plt.ylabel('Value')
plt.title('PID Controller Simulation with Disturbance and Anti-Windup')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('pid_disturbance_final_fixed.png')