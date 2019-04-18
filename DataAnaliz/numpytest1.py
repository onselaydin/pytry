import numpy as np
import matplotlib.pyplot as matplot

grades = np.random.normal(80,30,1000)
np.mean(grades)

matplot.hist(grades,50)
matplot.show()