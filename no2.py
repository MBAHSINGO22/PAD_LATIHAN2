import matplotlib.pyplot as plt
import numpy as np

# Define the range for Q (quantity sold)
Q = np.linspace(0, 100, 100)  # we are going to plot from 0 to 100 toples

# Nastar price function
P_nastar = 1000 * Q + 40000

# Putri Salju price function
P_putri = -333.33 * Q + 50000

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(Q, P_nastar, label='Nastar')
plt.plot(Q, P_putri, label='Putri Salju')
plt.xlabel('Jumlah Penjualan (Toples)')
plt.ylabel('Harga (Rupiah)')
plt.title('Grafik Harga vs Penjualan untuk Nastar dan Putri Salju')
plt.legend()
plt.grid(True)
plt.show()  # Display the plot
