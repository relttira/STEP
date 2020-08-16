import quantification as quant
import numpy as np
import netCDF4 as nc

tracked_storms = np.load('tutorial_data/tracked_storms_1996.npy', allow_pickle=True)

precip_data = np.load('tutorial_data/precip_1996.npy', allow_pickle=True)

file = 'tutorial_data/lat_long_1996.nc'
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

# create an array that's twice as wide as the central location array to convert all the arrays of length 2 to numbers
central_locs_for_csv = np.empty((storm_characteristics[3].shape[0], 2*storm_characteristics[3].shape[1]))

# isolate the array of central locations
cen_locs = storm_characteristics[3]

# we want to traverse every cell in the array and format for csv
# so let's find the number of rows and number of columns in the cen_locs array
rows = cen_locs.shape[0]
cols = cen_locs.shape[1]

# then, for each row in the 2d array containing these
for row_index in range(rows):
    # and for each column
    for col_index in range(cols):
        # to test if we're doing this right, uncomment the following
        # print(cen_locs[row_index][col_index])
        # we should see the printed results from this line put into our csv left to right, top to bottom as they appear
        # in the console - note, as you'll see below, if it's a zero we put it in twice

        # if the type of the thing stored at that location is a float (meaning that storm doesn't exist in that time
        # slice we have a 0 there as a placeholder)
        if isinstance(cen_locs[row_index][col_index], float):
            # just put zeros in for the central locations
            central_locs_for_csv[row_index][(2 * col_index)] = 0
            central_locs_for_csv[row_index][((2 * col_index) + 1)] = 0
        else:
            # otherwise we've got an array here, so put the central location in as we'd wish
            central_locs_for_csv[row_index][(2*col_index)] = cen_locs[row_index][col_index][0]
            central_locs_for_csv[row_index][((2*col_index) + 1)] = cen_locs[row_index][col_index][1]

np.savetxt("cent_loc.csv", central_locs_for_csv, delimiter=",", header="central location")
