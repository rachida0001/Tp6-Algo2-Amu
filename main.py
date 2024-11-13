import matplotlib.pyplot as plt
from scipy.special import binom
import numpy as np

class Bézier:
    def __init__(self,c):
        self.c = c
        self.n = len(c[0]) -1
    
    def plot(self):
        t_values = np.linspace(0, 1, 100)
        bezier_points = np.zeros((100, 2))
        
        for i in range(self.n+1):
            bernstein_poly = binom(self.n, i) * (t_values ** i) * ((1 - t_values) ** (self.n - i))
            bezier_points[:, 0] += self.c[0][i] * bernstein_poly
            bezier_points[:, 1] += self.c[1][i] * bernstein_poly

        plt.plot(bezier_points[:, 0], bezier_points[:, 1], "r", lw=0.5)
        plt.plot(self.c[0], self.c[1], "bs-", lw=0.5)
        plt.scatter(self.c[0], self.c[1])
        plt.axis("equal")
        plt.show()
        plt.close()
            
              
if __name__ == "__main__":
    c = np.array(([1,2,5,8,13,15,12], [1,4,7,8,6,5,1.5]))
    obj1 = Bézier(c)
    obj1.plot()
    
    obj2 = Bézier(np.array(([1,2,5,8,13,3,12], [1,4,7,5,6,5,8])))
    obj2.plot()
    
    obj3 = Bézier(np.random.randint(0, 10, (2, 10)))
    obj3.plot()
    
    obj4 = Bézier(np.random.randint(0, 10, (2, 10)))
    obj4.plot()