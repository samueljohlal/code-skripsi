import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

#syarat awal
jumlah_x = 10
jumlah_y = 10
jumlah_titik = jumlah_x*jumlah_y

titik_pusat = np.arange(1,jumlah_x) # nilai titik pusat
varian = np.arange(1,jumlah_x) # nilai varian
jumlah_data = len(varian)*len(titik_pusat)
data_rho = np.zeros((jumlah_data,100)) #disesuaikan dengan jumlah data yang mau diambil
rho_2d = np.zeros(jumlah_titik)

for k in (titik_pusat):
    for l in (varian):
        for m in range (jumlah_y):
            for n in range (jumlah_x):
                gauss_2dimensi = np.exp(-(((n-titik_pusat[k-1])**2/(2*varian[l-1]))+((m-titik_pusat[k-1])**2)/(2*varian[l-1])))
                o = 0
                rho_2d[o] = gauss_2dimensi
                o = o + 1
                if len(rho_2d) == 100:
                    p = 0
                    data_rho[p,:] = rho_2d
                    p = p + 1

print(data_rho)






                


