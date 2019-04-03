import matplotlib.pyplot as plt
import numpy as np 

#%matplotlib inline
x = np.arange(1,6)
y = np.arange(2,11,2) # iki artırarak bir array oluştur.
# plot tanımlama tek grafik
#plt.plot(x,y,"red")
#plt.show()
"""
#subplotlar
plt.subplot(2,2,1) # ikiye iki düzende grafik oluşturacak.
plt.plot(x,y,"blue") # ilk grafiğim
plt.subplot(2,2,2)
plt.plot(y,x,"yellow")
plt.subplot(2,2,3)
plt.plot(y,x,"red")
plt.subplot(2,2,4)
plt.plot(x,x ** 2,"black")
plt.show()
"""

"""
# figürler

fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.4,0.5,0.4,0.2])

axes1.plot(y,x)
axes1.set_xlabel("Outer X")
axes1.set_ylabel("Outer Y")
axes1.set_title("Outer Graph")

axes2.plot(x,y)
axes2.set_xlabel("Inner X")
axes2.set_ylabel("Inner Y")
axes2.set_title("Inner Graph")
plt.show()
"""

# https://matplotlib.org/
#https://nbviewer.jupyter.org/github/mustafamuratcoskun/Data-Analiz-Notebooklar/blob/master/Matplotlib%20%C3%96dev/Matplotlib%20%C3%96dev.ipynb
#https://nbviewer.jupyter.org/github/mustafamuratcoskun/Data-Analiz-Notebooklar/blob/master/Matplotlib%20%C3%96dev/Matplotlib%20%C3%96dev%20%C3%87%C3%B6z%C3%BCmleri.ipynb