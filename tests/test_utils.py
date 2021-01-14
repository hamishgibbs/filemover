import pytest
from datetime import datetime
from process_fb import utils


def test_get_file_date():

    fn = 'Britain_2020_01_01_0000.csv'

    res = utils.get_file_date(fn)

    assert type(res) is datetime

    assert res == datetime(2020, 1, 1)
