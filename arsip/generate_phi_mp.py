import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import os
from multiprocessing import Pool

#syarat awal
jumlah_x = 20
jumlah_y = 20
jumlah_titik = jumlah_x*jumlah_y

#syarat awal rho
jumlah_titik_x = np.arange(0, jumlah_x)
jumlah_titik_y = np.arange(0, jumlah_y)
titik_pusat = np.arange(1,jumlah_x) # nilai titik pusat
varian = np.arange(1,jumlah_x) # nilai varian

jumlah_data = (len(varian)**2)*(len(titik_pusat)**2)
o = p = f = d =0

data_rho = np.zeros((jumlah_data,jumlah_titik)) #disesuaikan dengan jumlah data yang mau diambil
rho_2d = np.zeros(jumlah_titik)

#syarat awal phi
delta_x = 0.5
delta_y = 0.5
jumlah_iterasi = 100
epsilon_nol = 1

iterasi = np.arange(0,jumlah_iterasi)
temp = np.zeros((jumlah_y,jumlah_x))
phi = np.zeros((jumlah_y,jumlah_x))
data_phi = np.zeros((jumlah_data, jumlah_x, jumlah_y)

data_training = np.loadtxt('rho_dua_dimensi_cartesian_data_tanpa_mp.csv', delimiter=',').reshape(len(data_rho),jumlah_y,jumlah_x)

def phi_hitung(g):    
    for h in (iterasi):
        #print(' h=',h)
        for j in range (1, jumlah_y-1):
            #print('   j=',j)
            for i in range (1, jumlah_x-1):
                    #print('     i=',i)
                    phi[j,i] = ((((temp[j, i+1]+temp[j, i-1])/delta_x**2)+((temp[j+1, i]+temp[j-1, i])/delta_y**2)+\
                                (data_training[g,j,i]/epsilon_nol))/2)*(delta_x**2 * delta_y**2)/(delta_y**2 + delta_x**2)
                    #print('rho=', data_training[g,j,i], 'phi=', phi[j,i])
                    temp[j,i] = phi[j,i]
    return phi

for g in range(len(data_training)):
    phi_hitung(g)
    data_phi[g,:,:]=phi