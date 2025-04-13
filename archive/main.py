import time
import matplotlib.pyplot as plt

# PID Controller Class
class PIDController:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint

        self.prev_error = 0
        self.integral = 0

    def compute(self, current_value, dt):
        error = self.setpoint - current_value
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt if dt > 0 else 0
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error = error
        return output

# Simulation settings
Kp = 1.5
Ki = 0.5
Kd = 0.3
setpoint = 50  # Target value (like desired GPU frequency)
initial_value = 20  # Starting value (initial frequency)

pid = PIDController(Kp, Ki, Kd, setpoint)

current_value = initial_value
values = []
time_steps = []

# Simulate for 60 steps
for step in range(60):
    dt = 0.1  # 100ms per iteration
    control_signal = pid.compute(current_value, dt)

    # Apply the control signal to current_value (simple model)
    current_value += control_signal * dt

    values.append(current_value)
    time_steps.append(step * dt)

    time.sleep(0.05)  # Simulate real time (optional)

# Plot the result
plt.plot(time_steps, values, label="PID Output")
plt.axhline(y=setpoint, color='r', linestyle='--', label="Setpoint")
plt.xlabel('Time (s)')
plt.ylabel('Value')
plt.title('PID Controller Simulation')
plt.legend()
plt.grid(True)
plt.savefig('dvfs_output_plot150503.png')

