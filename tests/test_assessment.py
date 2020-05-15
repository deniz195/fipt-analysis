import pytest
from pathlib import Path

from conftest import module_logger, fit_file, current_dir, build_symmetric_impedance_fitter_from_file

def gather_filenames():
    p = Path(current_dir).joinpath('data')
    filenames = list(p.glob('**/*.csv'))
    return filenames


assessment_table_raw = [
{'w_trans': 29.87453551634064, 'has_w_trans': True, 'has_short': False, 'filename': 'test_data_001.csv'},
{'w_trans': 11.89319014054795, 'has_w_trans': True, 'has_short': False, 'filename': 'test_data_003.csv'},
{'w_trans': 11.89319014054795, 'has_w_trans': True, 'has_short': False, 'filename': 'test_data_002.csv'},
{'w_trans': 47.34769686448863, 'has_w_trans': True, 'has_short': True, 'filename': 'test_data_004.csv'},
{'w_trans': 29.87453551634064, 'has_w_trans': True, 'has_short': False, 'filename': 'test_data_005.csv'},
{'w_trans': 29.87453551634064, 'has_w_trans': True, 'has_short': False, 'filename': 'test_data_006.csv'},
{'w_trans': 29.87453551634064, 'has_w_trans': True, 'has_short': False, 'filename': 'test_data_007.csv'},
{'w_trans': None, 'has_w_trans': False, 'has_short': True, 'filename': 'test_data_008.csv'},
{'w_trans': 0.7504071044217652, 'has_w_trans': True, 'has_short': True, 'filename': 'test_data_009.csv'},
{'w_trans': 0.7504071044217652, 'has_w_trans': True, 'has_short': False, 'filename': 'test_data_010.csv'},
{'w_trans': 11.89319014054795, 'has_w_trans': True, 'has_short': False, 'filename': 'test_data_011.csv'},
{'w_trans': 9.447083268609866, 'has_w_trans': True, 'has_short': False, 'filename': 'test_data_012.csv'},
{'w_trans': 31.415863704044863, 'has_w_trans': True, 'has_short': False, 'filename': 'test_data_013.csv'},
{'w_trans': 39.55020106642569, 'has_w_trans': True, 'has_short': False, 'filename': 'test_data_014.csv'},
{'w_trans': 31.415863704044863, 'has_w_trans': True, 'has_short': False, 'filename': 'test_data_015.csv'},
{'w_trans': 31.415863704044863, 'has_w_trans': True, 'has_short': False, 'filename': 'test_data_016.csv'},
{'w_trans': 49.790662143773126, 'has_w_trans': True, 'has_short': False, 'filename': 'test_data_017.csv'},
{'w_trans': 29.87453551634064, 'has_w_trans': True, 'has_short': False, 'filename': 'test_data_018.csv'},
{'w_trans': 5.960751086771051, 'has_w_trans': True, 'has_short': False, 'filename': 'test_data_019.csv'},
{'w_trans': 23.730145772596643, 'has_w_trans': True, 'has_short': False, 'filename': 'test_data_020.csv'},
]

assessment_table = {a['filename']: a for a in assessment_table_raw}


@pytest.mark.parametrize('fn', gather_filenames())
def test_assessment(fn):
    fn_simple = str(Path(fn).name)

    if fn_simple not in assessment_table:
    	module_logger.warning(f'No assesment data available for {fn_simple}! Skip!')
    	return True

    symimfit =  build_symmetric_impedance_fitter_from_file(fn)
    assessment = symimfit.assess_data()
    assessment['filename'] = fn_simple

    # print(assessment)

    for k, v in assessment_table[fn_simple].items():
        assert v == assessment[k], f'Failed on property: {k}'




