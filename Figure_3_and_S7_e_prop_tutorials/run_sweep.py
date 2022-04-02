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
# N = 10

# cs = np.linspace(0, 0.95, 4)        #Correlation coefficient
# ws = np.logspace(-1, 0, 4)          #Learning window
# sigmas = np.logspace(-3, -1, 4)   #Noise magnitude

#Test run
cs = np.linspace(0, 0.95, 1)           #Correlation coefficient
ws = np.logspace(0, 0, 1)             #Learning window
sigmas = np.logspace(-3, -.5, 1)       #Noise magnitude

for c in cs:
    for w in ws:
        for sigma in sigmas:
            print("Running delayed XOR with c =", c, "w =", w, "sigma=", sigma, N, "times")
            out_file = f'delayed_xor_results_c_{c}_w_{w}_sigma_{sigma}_n_{n}.pkl'
            plot_file = f'delayed_xor_results_c_{c}_w_{w}_sigma_{sigma}_n_{n}.png'
            cmd = f'CUDA_VISIBLE_DEVICES={CUDA_DEV} python tutorial_delayed_xor_with_alif.py {out_file} {plot_file} {sigma} {c} {w}'
            os.system(cmd)