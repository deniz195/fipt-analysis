import pandas as pd
import pytest
# get module from parent directory
import os,sys,inspect
from pathlib import Path
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

import fipt

def gather_filenames():
    p = Path(current_dir).joinpath('data')
    filenames = list(p.glob('**/*.csv'))
    return filenames

def fit_filename(fn, params=None):
    df = pd.read_csv(fn)
    df.head()

    ipdata =  fipt.ImpedanceData(fn, fn, 
                       f_data = df['Frequency (Hz)'].values,  
                       z_real_data = df['Z\' (Ohms)'].values, 
                       z_imag_data = df['Z\" (Ohms)'].values)


    symimfit = fipt.SymmetricImpedanceFitter(impedance_data=ipdata)        
    symimfit.sanitize_data()

    # restrict data range
    symimfit.set_min_w(None)
    symimfit.set_max_z_abs(400)

    # use student t likelihood function
    symimfit.configure_likelihood(likelihood_config=dict(name='t', scale=1, df=1))

    # guess start parameters
    start_params = symimfit.guess(make_plots=False)

    # manual configuration of parameters
    start_params_1 = start_params

    if params is not None:
        for key,val in params.items():
            start_params[key].set(value=val)
        # start_params_1['gamma'].set(value=0.916)
        # start_params_1['r_ion'].set(value=50)
        # start_params_1['q_s'].set(value=0.004)

    # symimfit.plot_fit(params=start_params_1);        
    #         symimfit.set_max_z_abs(250)

    result = symimfit.fit()        

    fit_report_str = fipt.lmfit.fit_report(result, show_correl=False)

    f, ax = symimfit.plot_fit(start_params = start_params_1);
    # f.show()

    symimfit.save_results(plot_figure=f)

    return result


def test_full_fit():
    fn = str(Path(current_dir).joinpath('test_data_001.csv'))
    fit_filename(fn)


def test_full_fit_with_params():
    fn = str(Path(current_dir).joinpath('data','test_data_004.csv'))
    params = {"gamma":0.916, "r_ion":79}
    # result = fit_filename(fn, params)
    result = fit_filename(fn)
    assert result.chisqr < 200


def test_empty_dataset():
    fn = str(Path(current_dir).joinpath('test_empty_data.csv'))
    with pytest.raises(ValueError, match=r".* not enough data points .*"):
        fit_filename(fn)


@pytest.mark.parametrize('fn', gather_filenames())
def test_chisqr(fn):
    result = fit_filename(str(fn))
    assert result.chisqr < 200
