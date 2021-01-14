import re
from datetime import datetime


def get_file_date(fn):

    date = re.search(r'(\d+_\d+_\d+_\d+)', fn)

    date = datetime.strptime(date.group(0), '%Y_%m_%d_%H%M')

    return(date)
