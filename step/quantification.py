from collections import defaultdict
from math import atan, sqrt
import numpy as np


def quantify(tracked_storms: np.ndarray, precip_data: np.ndarray, lat_data: np.ndarray, long_data: np.ndarray,
             time_interval: float, pixel_size: float) -> tuple:
    """Quantitatively describes individual storms in terms of duration, size, mean intensity, and central location.
    :param tracked_storms: the tracked storms returned by the tracking algorithm, given as an array of dimensions
    Time x Rows x Cols.
    :param precip_data: the precipitation data corresponding to the tracked storms data, with the same dimensions as
    tracked_storms.
    :param lat_data: the latitude data corresponding to each [y][x] in tracked_storms, given as an array of
    dimensions 1 x Rows x Cols.
    :param long_data: the longitude data corresponding to each [y][x] in tracked_storms, given as an array of
    dimensions 1 x Rows x Cols.
    :param time_interval: the period between temporal 'snapshots', given as a float. The user should interpret the
    duration results in terms of the time unit implied here.
    :param pixel_size: the length/width one grid cell represents in the data. The user should interpret the size and
    average intensity results in terms of the distance unit implied here squared.
    :return: A tuple of size four containing the duration of each storm, as well as its size, intensity,
    and central location at each time step, in this order.
    """

    # find the duration of the storms
    durations = get_duration(tracked_storms, time_interval)

    # find the size of each storm in each time slice
    sizes = get_size(tracked_storms, pixel_size)

    # find the average precipitation amount for each storm in each time slice
    averages = get_average(tracked_storms, precip_data)

    # and find the central location for each storm in each time slice
    central_locs = get_central_loc(tracked_storms, precip_data, lat_data, long_data)

    return durations, sizes, averages, central_locs


def get_duration(storms: np.ndarray, time_interval: float) -> np.ndarray:
    """Computes the duration (in the time unit of time_interval) of each storm across all time slices given.
    :param storms: the tracked storms returned by the tracking algorithm, given as an array of dimensions
    Time x Rows x Cols.
    :param time_interval: the period between temporal 'snapshots', given as a float.
    :return: An array of length equal to the number of tracked storms + 1, where the value at [x] corresponds to
    the duration of the storm x. The index 0 (referring to the background) is always 0 and provided for ease of
    indexing.
    """

    # find the number of time slices in the data
    lifetime = storms.shape[0]

    # initialize a new dictionary
    duration_dict = defaultdict(int)

    # and the number of storms
    total_storms = len(np.unique(storms))

    # and an array to store the result in, where the value found at each index corresponds to the duration that storm
    result = np.zeros(total_storms)

    # then, for each time slice
    for time_index in range(lifetime):
        # compute the labels that appear in that time slice
        curr_labels = np.unique(storms[time_index])

        # for each label in the tracked storm data
        for label in range(total_storms):
            # if it appears in the current time slice
            if label and np.isin(label, curr_labels):
                # increment the number of time slices it appears in
                # (and if we haven't seen it before, set it to 1 in the dictionary (this is a property of defaultdict)
                duration_dict[label] += 1

    for key, value in duration_dict.items():
        if key:
            result[key] = value

    result = result * time_interval

    return result


def get_size(storms: np.ndarray, grid_cell_size: float) -> np.ndarray:
    """Computes the size (in the distance unit of grid_cell_size) of each storm across all time slices given.
    :param storms: the tracked storms returned by the tracking algorithm, given as an array of dimensions
    Time x Rows x Cols.
    :param grid_cell_size: the length/width one grid cell represents in the data, given as a float.
    :return: a lifetime x total_storms array where the value found at [y][x] corresponds to the size of the storm at t=y,
    storm=x. Except in the case of index 0, which is always 0 for any t.
    """

    # find the number of time slices in the data
    lifetime = storms.shape[0]

    # TODO: CHANGED TO LEN, NOT SURE HOW WORKING BEFORE
    # and the number of storms
    total_storms = len(np.unique(storms))

    # initialize an array with dimensions number of time slices by number of storms
    result = np.zeros((lifetime, total_storms))

    for time_index in range(lifetime):
        # find the unique labels
        labels = np.unique(storms[time_index])

        # for each label that appears in this time slice (that's not the background)
        for label in labels:
            if label:

                # compute its number of grid cells using a map and reduce technique
                storm_size = np.sum(np.where(storms[time_index] == label, 1, 0))

                # and place it at that correct location in the array to return
                result[time_index][label] = storm_size

    # multiply the number of grid cells in each storm by the grid cell size
    result = result * grid_cell_size

    return result


def get_average(storms: np.ndarray, precip: np.ndarray) -> np.ndarray:
    """Computes the average intensity of each storm across all time slices given.
    :param storms: the tracked storms returned by the tracking algorithm, given as an array of dimensions
    Time x Rows x Cols.
    :param precip: the precipitation data corresponding to the tracked storms, with the same dimensions as
    tracked_storms.
    :return: a lifetime x total_storms array where the value found at [y][x] corresponds to the mean intensity of the
    storm at t=y, storm=x. Except in the case of index 0, which is always 0 for any t.
    """

    # find the number of time slices in the data
    lifetime = storms.shape[0]

    # and the number of storms
    total_storms = len(np.unique(storms))

    # initialize an array with dimensions number of time slices by number of storms
    result = np.zeros((lifetime, total_storms))

    for time_index in range(lifetime):
        # find the unique labels
        labels = np.unique(storms[time_index])

        # for each label that appears in this time slice (that's not the background)
        for label in labels:

            if label:
                # find the precipitation where it appears in the current time slice
                storm_precip = np.where(storms[time_index] == label, precip[time_index], 0)

                # sum the precipitation
                storm_precip_sum = np.sum(storm_precip)

                # find the number of grid cells belonging to the storm
                storm_size = np.sum(np.where(storms[time_index] == label, 1, 0))

                # find the storm's average precipitation in this time slice
                storm_avg = storm_precip_sum / storm_size

                # and store it in the appropriate place in our result array
                result[time_index][label] = storm_avg

    return result


def get_central_loc(storms: np.ndarray, precip: np.ndarray, lats: np.ndarray, longs: np.ndarray) \
        -> np.ndarray:
    """Computes the central location on the earth's surface of each storm across all time slices given.
    :param storms: the tracked storms returned by the tracking algorithm, given as an array of dimensions
    Time x Rows x Cols.
    :param precip: the precipitation data corresponding to the tracked storms data, with the same dimensions as
    tracked_storms.
    :param lats: The latitude data corresponding to each [y][x] in tracked_storms, given as an array of dimensions
    1 x Rows x Cols.
    :param longs: The longitude data corresponding to each [y][x] in tracked_storms, given as an array of dimensions
    1 x Rows x Cols.
    :param size_array: the array returned by get_size(), a lifetime x total_storms array where the value found at [y][x]
    corresponds to the size of the storm at time=y, storm=x.
    :param lifetime: the number of time slices in the data, given as an integer.
    :param total_storms: the total number of storms INCLUDING the background, given as an integer.
    :return: a lifetime x total_storms array where the value found at [y][x] corresponds to the central location of the
    storm at t=y, storm=x. Except in the case of index 0, which is always 0 for any t.
    """

    lifetime = storms.shape[0]

    total_storms = len(np.unique(storms))

    # initialize an array to store our result, but of type object to allow us to store an array in each cell
    result = np.zeros((lifetime, total_storms)).astype(object)

    # convert lats and longs from degree to radian
    lats = lats / 180. * np.pi
    longs = longs / 180. * np.pi

    # create arrays of x, y, and z values for the cartesian grid in R3
    x_array = np.cos(lats) * np.cos(longs)
    y_array = np.cos(lats) * np.sin(longs)
    z_array = np.sin(lats)

    # create an array to hold each central location as we calculate it
    central_location = np.empty(2)

    for time_index in range(lifetime):
        # find the unique labels
        labels = np.unique(storms[time_index])

        for label in labels:
            # if the storm exists in this time slice
            if label:

                # find the sum of the precipitation values belonging to the storm
                sum_precipitation = np.sum(np.where(storms[time_index] == label, precip[time_index], 0))

                # and compute the intensity weighted averages
                x_avg = np.sum(np.where(storms[time_index] == label, ((x_array[0] * precip[time_index]) /
                                                                      sum_precipitation), 0))

                y_avg = np.sum(np.where(storms[time_index] == label, ((y_array[0] * precip[time_index]) /
                                                                      sum_precipitation), 0))

                z_avg = np.sum(np.where(storms[time_index] == label, ((z_array[0] * precip[time_index]) /
                                                                      sum_precipitation), 0))

                h_avg = sqrt((x_avg ** 2) + (y_avg ** 2))

                # the central location on earth's surface is given by the following
                tmp_lon = atan(y_avg / x_avg)/np.pi*180
                tmp_lat = atan(z_avg / h_avg)/np.pi*180
                if tmp_lon > 0:
                    ### convert to degree west is the longitude is consider in degree east
                    tmp_lon -= 180
                # put longitude and latitude to the first and second dimensions
                central_location[0] = tmp_lon
                central_location[1] = tmp_lat
                # and we place it in the appropriate spot in the array
                result[time_index][label] = central_location

                # reset the central location - this seems to be necessary here
                central_location = np.zeros(2)

    return result
