import os
import glob
import pytest
from process_fb import file
from datetime import datetime


@pytest.fixture(scope="session")
def tmp_dir1(tmpdir_factory):

    path = tmpdir_factory.mktemp("tmp")

    return str(path)


@pytest.fixture(scope="session")
def tmp_dir2(tmpdir_factory):

    path = tmpdir_factory.mktemp("tmp")

    return str(path)


def test_watch_files_no_change(tmp_dir1, tmp_dir2):

    fn = []

    fn.append(tmp_dir1 + '/Britain_2020_01_01_0000.csv')
    fn.append(tmp_dir1 + '/Britain_2020_01_02_0000.csv')

    fn.append(tmp_dir2 + '/Britain_2020_01_01_0000.csv')

    for path in fn:

        with open(path, 'w') as f:

            f.write('test')

        assert os.path.exists(path)

    res = file.watch_file_dates(tmp_dir1, tmp_dir2, to=file.date_to_date, size = 1)

    assert type(res) is list

    assert len(res) == 1


def test_watch_files_day_to_weekly(tmp_dir1, tmp_dir2):

    files = glob.glob(tmp_dir1 + '/*')
    for f in files:
        os.remove(f)

    files = glob.glob(tmp_dir2 + '/*')
    for f in files:
        os.remove(f)

    fn = []

    fn.append(tmp_dir1 + '/Britain_2020_03_09_0000.csv')
    fn.append(tmp_dir1 + '/Britain_2020_03_10_0000.csv')
    fn.append(tmp_dir1 + '/Britain_2020_03_11_0000.csv')
    fn.append(tmp_dir1 + '/Britain_2020_03_12_0000.csv')
    fn.append(tmp_dir1 + '/Britain_2020_03_13_0000.csv')
    fn.append(tmp_dir1 + '/Britain_2020_03_14_0000.csv')
    fn.append(tmp_dir1 + '/Britain_2020_03_15_0000.csv')

    for path in fn:

        with open(path, 'w') as f:

            f.write('test')

        assert os.path.exists(path)

    res = file.watch_file_dates(tmp_dir1, tmp_dir2, to=file.date_to_weekly, size=7)

    assert type(res) is list

    assert len(res) == 1


def test_watch_files_hrs_to_daily(tmp_dir1, tmp_dir2):

    files = glob.glob(tmp_dir1 + '/*')
    for f in files:
        os.remove(f)

    files = glob.glob(tmp_dir2 + '/*')
    for f in files:
        os.remove(f)

    fn = []

    fn.append(tmp_dir1 + '/Britain_2020_03_10_0000.csv')
    fn.append(tmp_dir1 + '/Britain_2020_03_10_0800.csv')
    fn.append(tmp_dir1 + '/Britain_2020_03_10_1600.csv')

    for path in fn:

        with open(path, 'w') as f:

            f.write('test')

        assert os.path.exists(path)

    res = file.watch_file_dates(tmp_dir1, tmp_dir2, to=file.date_to_daily, size=3)

    assert type(res) is list

    assert len(res) == 1


def test_date_to_date():

    dates = [datetime(2020, 1, 1, 0),
             datetime(2020, 1, 1, 8),
             datetime(2020, 1, 1, 16)]

    res = file.date_to_daily(dates)

    assert type(res) is list
    assert type(res[0]) is dict
    assert res[0]['new_date'] == datetime(2020, 1, 1, 0)


def test_date_to_daily():

    dates = [datetime(2020, 1, 1, 0),
             datetime(2020, 1, 1, 8),
             datetime(2020, 1, 1, 16)]

    res = file.date_to_daily(dates)

    assert type(res) is list
    assert type(res[0]) is dict
    assert res[0]['new_date'] == datetime(2020, 1, 1)


def test_date_to_weekly():

    dates = [datetime(2020, 3, 10, 0),
             datetime(2020, 3, 11, 0),
             datetime(2020, 3, 12, 0)]

    res = file.date_to_weekly(dates)

    assert type(res) is list
    assert type(res[0]) is dict
    assert res[0]['new_date'] == datetime(2020, 3, 9)
