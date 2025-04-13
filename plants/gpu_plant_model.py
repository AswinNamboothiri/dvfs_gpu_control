# gpu_plant_model.py

class GpuPlantModel:
    def __init__(self, base_frequency=1000, max_frequency=2000, efficiency_constant=0.00001):
        """
        Simulates a GPU where:
        - Power Draw ≈ (Frequency)^2 * efficiency_constant
        """
        self.frequency = base_frequency  # starting frequency in MHz
        self.base_frequency = base_frequency
        self.max_frequency = max_frequency
        self.efficiency_constant = efficiency_constant
        self.power = self.calculate_power()

    def update(self, control_signal, dt):
        """
        Control signal adjusts the frequency.
        control_signal range: -1 to 1 (scale frequency up or down)
        """
        # Small step frequency control
        freq_adjustment = control_signal * 100  # Each control unit changes 100 MHz
        self.frequency += freq_adjustment * dt

        # Clamp frequency within [base_frequency, max_frequency]
        self.frequency = max(self.base_frequency, min(self.frequency, self.max_frequency))

        self.power = self.calculate_power()

        return self.frequency, self.power

    def calculate_power(self):
        # Simplified quadratic relationship
        return (self.frequency ** 2) * self.efficiency_constant
