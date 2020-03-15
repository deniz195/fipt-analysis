# FIPT: Fast impedance tortuosity 

FIPT is a measurement technique that allows a fast determination of the ionic resistance for battery electrodes. The technique is based on the work by J. Landesfeind (Journal of The Electrochemical Society, 163 (7) A1373-A1387 (2016) A1373) and then optimized for execution speed by D. Bozyigit at Battrion.

The measurement setup can be built based on https://github.com/deniz195/fipt 

Once data has been aquired, this repository provides the data analysis and model fitting. 

For examples refer to the jupyter notebook `demo_fipt.ipynb` in the examples folder.

## Quick installation
To install the fipt-analysis, simply:

```bash
pip install fipt
```

## Requirements
Required packages are `numpy`, `scipy` for data and statistical models and `lmfit` to perform the model fitting.

It is recommended (but not necessary) to install matplotlib installed, so that fipt-analysis will be able to create plots of the fitting.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
