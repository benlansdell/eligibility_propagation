##Run a sweep with different parameters

import numpy as np
import os

sigma = 5

# N = 10
# cs = np.linspace(0, 0.95, 5)
# ws = np.logspace(0.1, 1, 5)
#sigmas = np.logspace(0.001, 0.5, 5)

#Test run
N = 1
cs = np.linspace(0, 0.95, 1)
ws = np.logspace(0.1, 1, 1)
sigmas = np.logspace(0.001, 0.5, 1)

for c in cs:
    for w in ws:
        for n in range(N):
            print("Running delayed XOR with c =", c, "w =", w, n, "times")
            out_file = f'delayed_xor_results_c_{c}_w_{w}_n_{n}.pkl'
            plot_file = f'delayed_xor_results_c_{c}_w_{w}_n_{n}.png'
            cmd = f'python tutorial_delayed_xor_with_alif.py {out_file} --plotfile {plot_file} --sigma {sigma} --c {c} --discont_w {w}'
            os.system(cmd)