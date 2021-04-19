***Please note that this is only a preliminary version of the package and is not actively maintained.***

# STEP (Storm Tracking and Evaluation Protocol)

STEP is a Python package that identifies, tracks, and computes physical characteristics of rainstorms given spatiotemporal precipitation data. The algorithms herein are implementations of those proposed by Chang et al. in [*Changes in Spatiotemporal Precipitation Patterns in Changing Climate Conditions*](https://geosci.uchicago.edu/~moyer/MoyerWebsite/Publications/Papers/Changes_Spatio-temporal_Precipitation_patterns.pdf), released by the [Center for Robust Decision-making on Climate and Energy Policy](https://www.rdcep.org). For implementation details, see the [wiki](https://github.com/relttira/STEP/wiki).

*Note: Due to the time and space complexity of the computations used to track storms, it is highly recommended that runs of any substance be done on machines designed specifically for tasks of such computational weight.*

## Summary
* Installation
* Dependencies
* Usage
* Notes on Methodology
* Contributing
* License
* Authors
* Acknowledgements

## Installation

To install STEP:
1. Download the repository and unzip it.
2. `cd` to the root directory where `setup.py` can be found.
3. Execute ```$ python setup.py install```.


<!--- To install STEP, use the package manager [pip](https://pip.pypa.io/en/stable/). --->

## Dependencies
|Name|Version|
|--|--|
|[imageio](https://imageio.readthedocs.io/en/stable/installation.html)|2.8.0|
|[Matplotlib](https://matplotlib.org/3.2.2/users/installing.html)|3.2.1|
|[netCDF4](https://unidata.github.io/netcdf4-python/netCDF4/index.html)|1.5.3|
|[NumPy](https://numpy.org/install/)|1.18.5|
|[scikit-image](https://scikit-image.org/docs/dev/install.html)|0.17.2|
|[SciPy](https://www.scipy.org/install.html)|1.4.1|

 *[Basemap](https://matplotlib.org/basemap/users/installing.html) is necessary when using the example plotting function `storms_with_map` found in the [Tutorial](https://github.com/relttira/STEP/wiki/Tutorial). Additionally, the results of the package can be plotted using your visualization library of choice.*
## Usage

Please see the [Tutorial](https://github.com/relttira/STEP/wiki/Tutorial) for a comprehensive introduction to package use. See [Implementation Details](https://github.com/relttira/wiki/Implementation-Details) for function signatures and usage tips. You can also call [`help`](https://docs.python.org/3/library/functions.html#help)`(function)` for information on these and functions called therein. Depending on the function, calling `help` may provide more info.

## Notes on Methodology

For more detailed information, see the [Methodology](https://github.com/relttira/STEP/wiki/Methodology) or the [original publication](https://geosci.uchicago.edu/~moyer/MoyerWebsite/Publications/Papers/Changes_Spatio-temporal_Precipitation_patterns.pdf) and its supplemental materials. Please also see the original publication for more information on the reasoning behind the algorithms and the mathematics used.

## Contributing

If you would like to propose a change and/or note an error, please open an issue first to discuss what needs improvement (and, if applicable, how that might be accomplished).

## License
STEP is released under the ['Add a license here' license]().

## Authors
* [Alex Rittler](https://www.linkedin.com/in/arittler) - *developer*

## Acknowledgements
* Won Chang - *research*
* Michael Stein - *research*
* Jiali Wang - *research*
* Rao Kotamarthi - *research*
* Elisabeth Moyer - *research*
* [Benjamin Kleeman](https://github.com/bkleeman) - *guidance on project structure and docs*
* Emily Padston - *project management and guidance*
