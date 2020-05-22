import pytest
import logging
import os
import sys
import inspect
from pathlib import Path

# create logger
module_logger = logging.getLogger(__name__)
module_logger.setLevel(logging.DEBUG)



current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

import fipt
from fipt import ImpedanceData
# from fipt.impedance_data import load_test_data_csv

            

def load_test_data_csv(fn):
    import pandas as pd

    df = pd.read_csv(fn)
    df.head()

    ipdata =  ImpedanceData(fn, fn, 
                       f_data = df['Frequency (Hz)'].values,  
                       z_real_data = df['Z\' (Ohms)'].values, 
                       z_imag_data = df['Z\" (Ohms)'].values)    
    return ipdata


def build_symmetric_impedance_fitter_from_file(fn, params=None):
    ipdata =  load_test_data_csv(fn)

    symimfit = fipt.SymmetricImpedanceFitter(impedance_data=ipdata)        
    return symimfit



def fit_file(fn, params=None):
    ipdata =  load_test_data_csv(fn)

    symimfit = fipt.SymmetricImpedanceFitter(impedance_data=ipdata)        
    result = symimfit.fit_auto(start_params=params)

    return result


def get_data_file(fn):
    return str(Path(current_dir).joinpath('data', fn))    


# # Testing mode database
# @pytest.fixture(scope="session")
# def bdb():
#     ''' Creates a barelydb instance using the test database. '''
#     return bdb_local
