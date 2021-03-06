# FIPT: Fast impedance tortuosity 

## A fast way to get ionic resistance

FIPT is a measurement technique that allows a fast determination of the ionic resistance for battery electrodes. The technique is based on the work by J. Landesfeind ([DOI: 10.1149/issn.1945-7111](https://dx.doi.org/10.1149/2.1141607jes)) and then optimized for execution speed and reliability at [Battrion](https://battrion.com).

The measurement setup can be built based on [https://github.com/deniz195/fipt](https://github.com/deniz195/fipt)

For a quick introduction to the measurement kit [check out our video here.](https://youtu.be/r1cBf72wSwA)

## How to analyse the data?

The data aquired in an FIPT measurement can be analyzed by the code in this repository. The code fits an analytical model to the data to determine the relevant parameters of the measurement:
```
r_ion - Ionic resistance
r_sep - Seperator resistance
chisqr - χ2 as quality of fit
gamma - Phase exponent
q_s   - Capacitance factor
```

The ionic resistance can be used to calculate the MacMullin number (and the tortuosity), which are important performance parameters of battery electrodes.

For a quick introduction to the data analysis [check out our video here.](https://youtu.be/HwfMSETXJz8)

## Quick analysis
If you want to quickly analyze your impedance data:

Install fipt-analysis:
```bash
pip install fipt[full]
```

Put the test data `test_data_001.csv` in your current folder ([download here](https://github.com/deniz195/fipt-analysis/raw/master/examples/test_data_001.csv) from the `examples` folder). Analyze the data:



```bash
python -m fipt ./test_data_001.csv
```

To analyze your own data, put it in a file with the same format as `test_data_001.csv`, which is:
```
Format: CSV
1st column, Frequency in [Hz]
2nd column, Z' in [Ohm] 
3rd column, Z'' in [Ohm]
(Name of columns is not important)
```

## Examples 
To see how to analyze fipt data in your own python code, refer to the jupyter notebook `demo_fipt.ipynb` in the examples folder.

## Features and known issues
The code was optimized to allow the fitting and analysis of large numbers of data files, with minimum user intervention. The key features of the code are:

- Robust estimation of starting parameters from raw data
- Resistance to outlier data points through use of Student-T likelihood function
- Ability to verify each fit, through automatic generation of result files (plots, statistics, etc.)

Known issues:
- The code is currently provided with a minimum of documentation.
- Calculation of MacMullin number and tortuosity not yet included

## Requirements
Required packages are `numpy`, `scipy` for data and statistical models and `lmfit` to perform the model fitting.

It is recommended (but not necessary) to have pandas and matplotlib installed, so that fipt-analysis will be able to create plots of the fitting. These packages are automatically installed when using the install configuration `full`:

```bash
pip install fipt[full]
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

For questions please feel free to reach out to Deniz Bozyigit ([dbozyigit@battrion.com](mailto:dbozyigit@battrion.com))

## License
[MIT](https://choosealicense.com/licenses/mit/)
