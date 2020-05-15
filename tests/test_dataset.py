from typing import TextIO

import pytest

import json 
from pathlib import Path

from conftest import fit_file, current_dir, module_logger

def gather_filenames():
    p = Path(current_dir).joinpath('data')
    filenames = list(p.glob('**/*.csv'))
    return filenames




def result_to_params(result):
    params_simp = result.params.valuesdict()
    params_simp['chisqr'] = result.chisqr    
    return params_simp

fit_result_last_filename = Path(current_dir).joinpath('fit_result_last.json')
fit_result_reference_filename = Path(current_dir).joinpath('fit_result_reference.json')

def add_fit_result(fn, params_simp):
    fn_simple = str(Path(fn).name)

    try:
        with open(fit_result_last_filename, 'r') as fp:
            fit_result_last = json.load(fp)
    except:
        fit_result_last = {}

    fit_result_last[fn_simple] = params_simp

    with open(fit_result_last_filename, 'w') as fp:
        json.dump(fit_result_last, fp, indent=4)


def get_reference_fit_result(fn):
    fn_simple = str(Path(fn).name)

    # try:
    with open(fit_result_reference_filename, 'r') as fp:
        fit_result_reference = json.load(fp)

    return fit_result_reference[fn_simple]
    # except:
    #     return None





@pytest.mark.parametrize('fn', gather_filenames())
def test_chisqr(fn):

    result = fit_file(str(fn))
    
    params_simp = result_to_params(result)
    add_fit_result(fn, params_simp)

    ref_params = get_reference_fit_result(fn)
    fn_simple = str(Path(fn).name)

    assert ref_params is not None,  f'No reference fit parameters for {fn_simple}'


    ### Check if parameters are ok:
    chisqr_error_margin = 1.20
    assert params_simp['chisqr'] < chisqr_error_margin * ref_params['chisqr']

    chisqr_improvement_margin = 0.90
    param_deviation_margin = 0.01

    if params_simp['chisqr'] < chisqr_improvement_margin * ref_params['chisqr']:
        module_logger.info(f'Chisqr has improved for {fn_simple}')

    for v in result.var_names:
        deviation = 2*abs(params_simp[v] - ref_params[v])/(params_simp[v] + ref_params[v])
        assert deviation < param_deviation_margin








