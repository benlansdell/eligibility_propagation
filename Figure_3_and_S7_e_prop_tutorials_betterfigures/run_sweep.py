##Run a sweep with different parameters

import numpy as np
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('index', type = int, help='run the same params multiple times, this is the count index')

args = parser.parse_args()
n = args.index

CUDA_DEV = ''

N = 1
#N = 10

#Run one
# cs = np.linspace(0, 0.95, 4)        #Correlation coefficient
# ws = np.logspace(-1, 0, 4)          #Learning window
# sigmas = np.logspace(-3, -1, 4)     #Noise magnitude

#Run two
# cs = np.linspace(0, 0.99, 5)        #Correlation coefficient
# ws = np.logspace(-1, 0.5, 5)      #Learning window
# ws = np.logspace(-0.3, 0.3, 5)      #Learning window ## Not sure this line says this... pretty sure the line above is correct, if I check the files output
# sigmas = np.logspace(-3, 1, 5)      #Noise magnitude

#Run three
cs = np.linspace(0, 0.99, 5)        #Correlation coefficient
ws = np.logspace(-1+0.375/2, 0.125-0.375/2, 3)      #Learning window
sigmas = np.logspace(-3, 0, 4)      #Noise magnitude

#Test run
# cs = np.linspace(0, 0.95, 1)           #Correlation coefficient
# ws = np.logspace(0, 0, 1)             #Learning window
# sigmas = np.logspace(-3, -.5, 1)       #Noise magnitude

for c in cs:
    for w in ws:
        for sigma in sigmas:
            print("Running delayed XOR with c =", c, "w =", w, "sigma=", sigma, N, "times")
            out_file = f'./results_run3/delayed_xor_results_c_{c}_w_{w}_sigma_{sigma}_n_{n}.pkl'
            plot_file = f'./results_run3/delayed_xor_results_c_{c}_w_{w}_sigma_{sigma}_n_{n}.png'
            cmd = f'CUDA_VISIBLE_DEVICES={CUDA_DEV} python tutorial_delayed_xor_with_alif.py {out_file} {plot_file} {sigma} {c} {w}'
            os.system(cmd)