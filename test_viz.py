import identification as idf
import matplotlib.pyplot as plt
import numpy as np
import visualization as viz
from skimage import draw
import tracking as tr

# load some initial precip data 
precip_data = np.load('tutorial_files/precip_1996.npy', allow_pickle=True)

# set a precip threshold and narrow your region of interest
THRESHOLD = 0.6 
trimmed_data = np.where(precip_data < THRESHOLD, 0, precip_data)

# create a structural set 
struct = np.zeros((16, 16))
rr, cc = draw.disk((7.5, 7.5), radius=8.5)
struct[rr, cc] = 1

# identify your storms
labeled_maps = idf.identify(trimmed_data, struct)

# visualize your data
cmap = plt.get_cmap('hsv')
viz.show_save_storms(labeled_maps, cmap, 'Identified Storms 1996', 1, show_save='save')