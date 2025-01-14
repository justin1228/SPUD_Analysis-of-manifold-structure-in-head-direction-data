'''March 22nd 2019
Create a few shared parameters and save them in a file.
'''

import os
import sys
gen_fn_dir = os.path.abspath('..') + '/shared_scripts'
sys.path.append(gen_fn_dir)

from general_file_fns import save_pickle_file

param_dict = {}
# Some commonly used paths
base_dir = '/Volumes/ThePassport/Research/Manifold learning with VAE/'
# Location where Peyrache et al data is unzipped
param_dict['raw_data_dir'] = base_dir + 'raw_data/'

# Contains the Peyrache et al data accumulated into single files.
# These files are created by read_in_data/preprocess_raw_data.py. Note that
# preprocess_raw_data will make this directory if it doesn't exist.
param_dict['processed_data_dir'] = base_dir + 'processed/'

# Spike counts in bins. Currently not used.
# param_dict['spike_counts_dir'] = base_dir + 'analyses/2016_06_spike_matrix_new/'

# Firing rates estimated by convolution with Gaussian kernel. Again, generated
# by read_in_data/preprocess_raw_data.py and directory created if needed.
param_dict['kernel_rates_dir'] = base_dir + 'analyses/2021_11_kernel_rates/'

# Analyses and results will be saved under this directory (and loaded from here too).
param_dict['results_dir'] = base_dir + 'analyses/'
param_dict['figures_dir'] = base_dir + 'figures/'

# Colors for the plots.
param_dict['cols'] = {'REM': (0.392, 0.549, 0.0784),
                      'SWS': (0.824, 0.627, 0.0392), 'Wake': (0.0118, 0.235, 0.392),
                      'measured': (0.3, 0.3, 0.3), 'fit': (0.490, 0.961, 0.961)}

print(param_dict)
save_pickle_file(param_dict, 'general_params.p')


#param_dictionary 현재까지의 구조
# 'raw_data_dir': base_dir + 'raw_data/',
# 'processed_data_dir': base_dir + 'processed/',
# 'kernel_rates_dir': base_dir + 'analyses/2019_03_kernel_rates/' it depends on session
# 'result_dir': base_dir + "analyses/",
# 'cols': {},
# }

