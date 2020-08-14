# STEP (Storm Tracking and Evaluation Protocol)

STEP is a Python package that identifies, tracks, and computes physical characteristics of rainstorms given spatiotemporal precipitation data. The algorithms herein are implementations of those proposed by Chang et al. in [*Changes in Spatiotemporal Precipitation Patterns in Changing Climate Conditions*](https://geosci.uchicago.edu/~moyer/MoyerWebsite/Publications/Papers/Changes_Spatio-temporal_Precipitation_patterns.pdf), released by the [Center for Robust Decision-making on Climate and Energy Policy](https://www.rdcep.org). For implementation details, see the [wiki](https://github.com/bkleeman/STEP-suggestions/wiki).

To identify and track storms in a dataset:
1. Put the data in a 3D Numpy array with dimensions *Time x Rows x Columns*.
2. Run `identify()`.
3. Run `track()`.
4. Visualize with `storms()`.

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

To install STEP, use the package manager [pip](https://pip.pypa.io/en/stable/). This package was written using Python 3.8.0.

```bash
pip install STEP
```

## Dependencies
|Name|Version|
|--|--|
|[imageio](https://imageio.github.io)|2.8.0|
|[Matplotlib](https://matplotlib.org)|3.2.1|
|[netCDF4](https://unidata.github.io/netcdf4-python/netCDF4/index.html)|1.5.3|
|[NumPy](https://numpy.org)|1.18.5|
|[scikit-image](https://scikit-image.org)|0.17.2|
|[SciPy](https://scipy.org)|1.4.1|

 *Note: [Basemap](matplotlib.org/basemap) is necessary when using the example function in `plot_with_map.py`.*
## Usage

Please see the [Tutorial](https://github.com/relttira/STEP/wiki/Tutorial) for a comprehensive introduction to package use. See [Implementation Details](https://github.com/relttira/wiki/Implementation-Details) for function signatures and usage tips. You can also call [`help`](https://docs.python.org/3/library/functions.html#help)`(function)` for information on these and functions called therein. Depending on the function, calling `help` may provide more info.

## Notes on Methodology

For more detailed information, see the [Methodology](https://github.com/relttira/STEP/wiki/Methodology) or the [original publication](https://geosci.uchicago.edu/~moyer/MoyerWebsite/Publications/Papers/Changes_Spatio-temporal_Precipitation_patterns.pdf) and its supplemental materials. Please also see the original publication for more information on the reasoning behind the algorithms and the mathematics used.

## Contributing

Changes are certainly welcome, as there are a good deal of complexity improvements to make on the implementation and functionality additions to build out related to the publication. If you would like to propose a change and/or note an error, please open an issue first to discuss what needs improvement (and, if applicable, how that might be accomplished).

### Future Work

Below are a list of generally useful ideas for future additions to STEP:

 - Adding the ability to use the computed metrics to find and visualize the spatial distribution of rainstorm characteristics, as covered in the publication.
 - Implementing a speed-up for the similarity measure computation. This could at least be done by dividing the calculation into subsets and summing their results.

## License
STEP is released under the [MIT License???](https://choosealicense.com/licenses/mit/).

## Authors
* [Alex Rittler](Link_to_github_or_whatever_social_profile) - *developer*

## Acknowledgements
* [Won Chang](LinkedIn_or_RDCEP_profile_if_permission_given) - *research*
* [Michael Stein](LinkedIn_or_RDCEP_profile_if_permission_given) - *research*
* [Jiali Wang](LinkedIn_or_RDCEP_profile_if_permission_given) - *research*
* [Rao Kotamarthi](LinkedIn_or_RDCEP_profile_if_permission_given) - *research*
* [Elisabeth Moyer](LinkedIn_or_RDCEP_profile_if_permission_given) - *research*
* [Benjamin Kleeman](https://github.com/bkleeman) - *guidance on project structure and docs* 
