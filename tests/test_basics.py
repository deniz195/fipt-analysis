import pandas as pd
import pytest
# get module from parent directory
import os,sys,inspect
from pathlib import Path
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

import fipt
from fipt import ImpedanceData

from conftest import fit_file, get_data_file, current_dir


def test_full_single_fit():
    fn = get_data_file('test_data_001.csv')
    fit_file(fn)


def test_full_fit_with_params():
    fn = get_data_file('test_data_004.csv')
    params = dict(gamma=0.80, r_ion=217, r_sep=100, q_s=0.00226)
    # result = fit_file(fn, params)
    result = fit_file(fn, params=params)

    assert result.chisqr < 1200 # improve model to get better fit


def test_empty_dataset():
    fn = str(Path(current_dir).joinpath('test_empty_data.csv'))
    with pytest.raises(ValueError, match=r".*not enough data points.*"):
        fit_file(fn)


def test_impedance_data():
    import pandas as pd

    fn = get_data_file('test_data_001.csv')

    df = pd.read_csv(fn)
    df.head()

    f_data = df['Frequency (Hz)'].values
    z_real_data = df['Z\' (Ohms)'].values
    z_imag_data = df['Z\" (Ohms)'].values

    ipdata1 =  ImpedanceData(fn, fn,  
                       f_data = f_data,  
                       z_real_data = z_real_data, 
                       z_imag_data = z_imag_data,
                       )    

    ipdata2 =  ImpedanceData(fn, fn,  
                       f_data = f_data,  
                       z_data = z_real_data + 1j*z_imag_data,
                       )    

    assert all(ipdata1.z_data == ipdata2.z_data)








