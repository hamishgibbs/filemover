import os
import glob
from process_fb import utils

def watch_files(in_path, out_path, to = None, extension = '/*.csv'):
    # identify files in in directory that are not in out directory

    in_files = glob.glob(in_path + extension)

    in_file_dates = [utils.get_file_date(x) for x in in_files]

    out_files = glob.glob(out_path + extension)

    out_file_dates = [utils.get_file_date(x) for x in out_files]

    if to is None:

        difference = set(in_file_dates).difference(set(out_file_dates))

        match_index = [i for i, x in enumerate([x in in_file_dates for x in difference]) if x]

        match_files = [in_files[i] for i in match_index]

    return(match_files)
