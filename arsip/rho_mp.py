import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import os
from multiprocessing import Pool

def gauss_2d(tp, var):
    for m in range (jumlah_y):
        for n in range (jumlah_x):
            gauss_2dimensi = np.exp(-(((n-tp[l-1])**2/(2*var[j-1]))+((m-tp[k-1])**2)/(2*var[i-1])))
            rho_2d[:] = gauss_2dimensi
            o = 0
            data_rho[o,:] = rho_2d
            o = o+1

def fung_data_rho(jumlah_datas):
    for i in range(jumlah_datas):
        for k in (1,10):
            for l in (1,10):
                gauss_2d(k, l)
                

if __name__ == '__main__':
    #syarat awal
    jumlah_x = 10
    jumlah_y = 10
    jumlah_titik = jumlah_x*jumlah_y
    cpus = os.cpu_count()

    titik_pusat = np.arange(1,jumlah_x) # nilai titik pusat
    varian = np.arange(1,jumlah_x) # nilai varian
    jumlah_data = len(varian)*len(titik_pusat)
    data_rho = np.zeros((jumlah_data,100)) #disesuaikan dengan jumlah data yang mau diambil
    rho_2d = np.zeros(100)

    p = Pool(cpus)
    result = p.map(fung_data_rho, jumlah_data)

#np.savetxt('rho_dua_dimensi_cartesian_data.csv', data_rho, fmt = '%.15f', delimiter=',') #penyimpanan rho