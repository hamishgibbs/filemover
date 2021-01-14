import os
import pytest
from process_fb import file


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

    res = file.watch_files(tmp_dir1, tmp_dir2, to=None)

    assert type(res) is list

    assert len(res) == 1
