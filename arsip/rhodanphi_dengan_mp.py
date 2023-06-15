import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import os
from multiprocessing import Pool

#perhitungan phi gauss seidel
def phi(jumlah_data):
    for g in range (jumlah_data):
        for h in range (jumlah_iterasi):
            for j in range (1, jumlah_y-1):
                for i in range (1, jumlah_x-1):
                    phi[j,i] = ((((temp[j, i+1]+temp[j, i-1])/delta_x**2)+((temp[j+1, i]+temp[j-1, i])/delta_y**2)+(data_training[g,j,i]/epsilon_nol))/2)*(delta_x**2 * delta_y**2)/(delta_y**2 + delta_x**2)
                    print('rho=', data_training[g,j,i], 'phi=', phi[j,i])
                    temp[j,i] = phi[j,i]
                    if j == jumlah_y-1:
                        data_phi[f] = phi
                        f = f+1

if __name__ == '__main__':
    #syarat awal
    jumlah_x = 10
    jumlah_y = 10
    jumlah_titik = jumlah_x*jumlah_y


    titik_pusat = np.arange(1,jumlah_x) # nilai titik pusat
    varian = np.arange(1,jumlah_x) # nilai varian
    jumlah_data = len(varian)*len(titik_pusat)
    data_rho = np.zeros((jumlah_data,jumlah_titik)) #disesuaikan dengan jumlah data yang mau diambil
    rho_2d = np.zeros(jumlah_titik)
    o = p = f = 0

    delta_x = 0.5
    delta_y = 0.5
    jumlah_iterasi = 10_000
    epsilon_nol = 1

    temp = np.zeros((jumlah_y,jumlah_x))
    phi = np.zeros((jumlah_y,jumlah_x))
    data_phi = np.zeros((jumlah_data, jumlah_y, jumlah_x))

    for k in (titik_pusat):
        for l in (varian):
            for m in range (jumlah_y):
                for n in range (jumlah_x):
                    gauss_2dimensi = np.exp(-(((n-titik_pusat[k-1])**2/(2*varian[l-1]))+((m-titik_pusat[k-1])**2)/(2*varian[l-1])))
                    #print('n=',n, 'm=',m, 'tipus=', titik_pusat[k-1], 'varian=',varian[l-1], 'gauss=',gauss_2dimensi)
                    data_rho[o,p] = gauss_2dimensi
                    if p < jumlah_titik-1:
                        p = p+1
                    else:
                        p = 0
                        o = o + 1 

    np.savetxt('rho_dua_dimensi_cartesian_data_tanpa_mp.csv', data_rho, fmt = '%.11f', delimiter=',')
    data_latih = np.loadtxt('rho_dua_dimensi_cartesian_data_tanpa_mp.csv', delimiter=',')
    data_training = data_latih.reshape(len(data_latih),10,10)

