import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
dt = 0.01
t_end = 6
time = np.arange(0, t_end, dt)

# System parameters
setpoint = 50
disturbance_time = 3

# PID gains
Kp = 0.8
Ki = 0.2
Kd = 0.4

# Limits
output_min = -100
output_max = 100

# Initialize
integral = 0
previous_error = 0
output_history = []
value_history = []
disturbance = np.zeros_like(time)

value = 30

for i, t in enumerate(time):
    if t > disturbance_time:
        disturbance[i] = 5  # step disturbance

    error = setpoint - value
    derivative = (error - previous_error) / dt
    previous_error = error

    # Predict next output without updating integral
    output = Kp * error + Ki * integral + Kd * derivative

    # Check if output would be saturated
    if output > output_max:
        output = output_max
        if error < 0:  # Only integrate when it helps to go back
            integral += error * dt
    elif output < output_min:
        output = output_min
        if error > 0:
            integral += error * dt
    else:
        integral += error * dt

    # Final output
    output = Kp * error + Ki * integral + Kd * derivative
    output = max(min(output, output_max), output_min)

    value += output * dt + disturbance[i]

    value_history.append(value)
    output_history.append(output)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(time, value_history, label="PID Output")
plt.axhline(setpoint, color='r', linestyle='--', label="Setpoint")
plt.axvline(disturbance_time, color='m', linestyle=':', label="Disturbance")
plt.title("PID Controller Simulation with True Anti-Windup")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("pid_disturbance_true_anti_windup.png")
