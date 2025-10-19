class PDController:
    def __init__(self, kp=0.15, kd=0.6):
        self.kp = kp 
        self.kd = kd 
        self.previous_error = 0.0

    def compute_control(self, reference, measurement, previous_error):
        error = reference - measurement

        control_output = self.kp * error + self.kd * (error - previous_error)
        self.previous_error = error
        return control_output