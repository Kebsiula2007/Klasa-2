from Function import Function
import numpy as np

class SinusFunction(Function):
    def __init__(self):
        self.x = []
        self.y = []
        self.step = 1
        self.x_min = 0
        self.x_max = 0
        self.type = "sinus"
        self.info = f"f(x) = sin({self.x})"
    
    def set_x_range(self, x_min, x_max):
        self.x_min = x_min
        self.x_max = x_max

    def set_step(self, step):
        self.step = step

    def calculate(self):
        self.x.clear()
        self.y.clear()
        self.x = np.linspace(self.x_min, self.x_max, 100)
        self.y = np.sin(self.x)

    @classmethod
    def create_function(cls, **kwargs):
            return SinusFunction()