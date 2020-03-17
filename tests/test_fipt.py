import pandas as pd

# get module from parent directory
import os,sys,inspect
from pathlib import Path
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

import fipt

def test_full_fit():

    fn = str(Path(current_dir).joinpath('test_data_001.csv'))
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
    # start_params_1['gamma'].set(value=0.916)
    # start_params_1['r_ion'].set(value=50)
    # start_params_1['q_s'].set(value=0.004)

    # symimfit.plot_fit(params=start_params_1);        
    #         symimfit.set_max_z_abs(250)

    result = symimfit.fit()        

    fit_report_str = fipt.lmfit.fit_report(result, show_correl=False)

    f, ax = symimfit.plot_fit(start_params = start_params_1);
    # f.show()

    symimfit.save_results()


def test_many_full_fits():

    failed_fits = []
    p = Path(current_dir).joinpath('data')
    # print(list(p.glob('**/*.csv')))
    for fn in list(p.glob('**/*.csv')):
    # fn = str(Path(current_dir).joinpath('test_data_001.csv'))
        fn = str(fn)
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
        # start_params_1['gamma'].set(value=0.916)
        # start_params_1['r_ion'].set(value=50)
        # start_params_1['q_s'].set(value=0.004)

        # symimfit.plot_fit(params=start_params_1);        
        #         symimfit.set_max_z_abs(250)

        result = symimfit.fit()

        fit_report_str = fipt.lmfit.fit_report(result, show_correl=False)
        # print(fit_report_str)

        f, ax = symimfit.plot_fit(start_params = start_params_1);
        # f.show()

        symimfit.save_results()

        if result.chisqr > 200:
            failed_fits.append((fn,result.chisqr))

    assert_str = ''.join("\n File={} \t chisqr={}".format(a,b) for a,b in failed_fits)
    assert len(failed_fits) == 0, assert_str
