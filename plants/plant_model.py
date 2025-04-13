# plant_model.py

class SimplePlant:
    def __init__(self, gain=1.0, time_constant=1.0):
        self.gain = gain
        self.time_constant = time_constant
        self.output = 0.0

    def update(self, control_input, dt):
        # First-order system dynamics
        self.output += dt * (-(self.output - self.gain * control_input) / self.time_constant)
        return self.output
