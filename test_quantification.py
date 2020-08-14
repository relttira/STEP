import quantification as quant
import numpy as np
import netCDF4 as nc

tracked_storms = np.load('tutorial_files/tracked_storms_1996.npy', allow_pickle=True)

precip_data = np.load('tutorial_files/precip_1996.npy', allow_pickle=True)

file = 'tutorial_files/lat_long_1996.nc'
data = nc.Dataset(file)
lat_data = data['XLAT'][:]
long_data = data['XLONG'][:]

THRESHOLD = 0.6 
trimmed_data = np.where(precip_data < THRESHOLD, 0, precip_data)

storm_characteristics = quant.quantify(tracked_storms, trimmed_data, lat_data, long_data, 3, 16)
# print(storm_characteristics[0], storm_characteristics[1], storm_characteristics[2])
# print(f'durations: {storm_characteristics[0]}')
# print(f'sizes: {storm_characteristics[1]}')
# print(f'average intensities: {storm_characteristics[2]}')

# np.savetxt("foo.csv", storm_characteristics[0], delimiter=",", header="duration")
# np.savetxt("foo.csv", storm_characteristics[1], delimiter=",", header="size")
# np.savetxt("foo.csv", storm_characteristics[2], delimiter=",", header="average intensity")
# np.savetxt("foo.csv", storm_characteristics[3][0], delimiter=",", header="central location")

# np.savetxt("foo.txt", storm_characteristics[0], newline="n", header="duration")
# np.savetxt("foo.txt", storm_characteristics[1], newline="n", header="size")
# np.savetxt("foo.txt", storm_characteristics[2], newline="n", header="average intensity")
# np.savetxt("foo.txt", storm_characteristics[3][0], delimiter=",", header="central location")

# create an array that's twice as wide as the central location array to convert all  to scalars
central_loc_csv = np.empty((storm_characteristics[3].shape[0], 2*storm_characteristics[3].shape[1])) 

# traverse both dimensions of the array and format for csv
print(storm_characteristics[3].shape[0])
for row_index in range(storm_characteristics[3].shape[0]):
    for col_index in range(storm_characteristics[3].shape[1]):
        central_loc_csv[row_index][2*col_index] = storm_characteristics[3][row_index][col_index][0]
        central_loc_csv[row_index][(2*col_index) + 1] = storm_characteristics[3][row_index][col_index][1]

np.savetxt("cent_loc.csv", central_loc_csv, delimiter=",", header="central location")