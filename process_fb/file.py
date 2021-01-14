import os
import glob
import collections
from process_fb import utils
from datetime import datetime


def date_to_date(dates: list):

    ref_dates = []

    for date in dates:

        ref_dates.append({'new_date': date, 'orig_date': date})

    return(ref_dates)


def watch_file_dates(in_path, out_path, to=date_to_date, extension='/*.csv', size=1):
    # identify files in in directory that are not in out directory

    in_files = glob.glob(in_path + extension)

    in_file_dates = [utils.get_file_date(x) for x in in_files]

    out_files = glob.glob(out_path + extension)

    out_file_dates = [utils.get_file_date(x) for x in out_files]

    dates_transformed = to(list(in_file_dates))

    date_dict = collections.defaultdict(list)

    for d in dates_transformed:
        date_dict[d['new_date']].append(d)

    date_groups = list(date_dict.values())

    file_groups = []

    for group in date_groups:

        in_file_dates_transformed = [x['new_date'] for x in group]

        new_file_index = [i for i, x in enumerate(in_file_dates_transformed) if x not in out_file_dates]

        new_files = [in_files[x] for x in new_file_index]

        if len(new_files) == size:

            new_date = to([utils.get_file_date(new_files[0])])[0]['new_date']

            new_date = datetime.strftime(new_date, '%Y_%m_%d_%H%M')

            file_groups.append({'output_date': new_date, 'input_files': new_files})

    return(file_groups)


def date_to_daily(dates: list):

    ref_dates = []

    for date in dates:

        ref_date = date.replace(hour=0, minute=0)

        ref_dates.append({'new_date': ref_date, 'orig_date': date})

    return(ref_dates)


def date_to_weekly(dates: list):

    ref_dates = []

    for date in dates:

        ref_week = date.strftime('%Y_%W') + '_1'

        ref_date = datetime.strptime(ref_week, "%Y_%W_%w")

        ref_dates.append({'new_date': ref_date, 'orig_date': date})

    return(ref_dates)
