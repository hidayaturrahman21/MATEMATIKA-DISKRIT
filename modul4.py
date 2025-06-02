import numpy as np
import matplotlib.pyplot as plt

#Definisikan fungsi
def f(x):
    return x**2 - 4

# Cari akar-akar fungsi (akar dari persamaan x^2 - 4 = 0)
akar = np.roots([1, 0, -4])

#Generate nilai x dari -3 hingga 3
x = np.linspace(-3, 3, 400)
y = f(x)

#Plot grafik
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='$f(x) = x^2 - 4$',color='red')
plt.title("Grafik Fungsi Kuadrat")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
