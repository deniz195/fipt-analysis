import pytest
from pathlib import Path

from conftest import fit_file, current_dir

def gather_filenames():
    p = Path(current_dir).joinpath('data')
    filenames = list(p.glob('**/*.csv'))
    return filenames


@pytest.mark.parametrize('fn', gather_filenames())
def test_chisqr(fn):
    result = fit_file(str(fn))
    assert result.chisqr < 200
