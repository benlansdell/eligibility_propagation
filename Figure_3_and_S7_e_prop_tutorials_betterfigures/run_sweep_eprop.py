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

#Run three
cs = np.linspace(0, 0.99, 5)                        #Correlation coefficient
ws = np.logspace(-1+0.375/2, 0.125-0.375/2, 3)      #Learning window
sigmas = np.logspace(-3, 0, 4)                      #Noise magnitude

for c in cs:
    for w in ws:
        for sigma in sigmas:
            print("Running delayed XOR with c =", c, "w =", w, "sigma=", sigma, N, "times")
            out_file = f'./results_run3_eprop/delayed_xor_results_c_{c}_w_{w}_sigma_{sigma}_n_{n}.pkl'
            plot_file = f'./results_run3_eprop/delayed_xor_results_c_{c}_w_{w}_sigma_{sigma}_n_{n}.pdf'
            cmd = f'CUDA_VISIBLE_DEVICES={CUDA_DEV} python tutorial_delayed_xor_with_alif.py {out_file} {plot_file} {sigma} {c} {w} --eprop'
            os.system(cmd)

#CUDA_VISIBLE_DEVICES= python tutorial_delayed_xor_with_alif.py test_results.pkl sample_image.pdf 0.1 0.75 1