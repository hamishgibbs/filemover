import os
import random


def scaffold(file, template):
    '''Function to scaffold a file from a template'''

    # Replace leading whitespace characters in block string, encode as bytes
    template = template().replace('        ', '').encode()

    # Prompt to overwrite an existing file
    if os.path.exists(file):

        overwrite = input('Found an existing file at %s.\nDo you want to overwrite this file? (Y/n)' % file)

        if overwrite != 'Y':

            print('Stopping.')
            exit()

    try:

        # Write template to file with bubble header.
        with open(file, 'wb') as f:

            f.write(template)

        # Success message
        print('Successfully created %s. %s' % (file, random_success()))

    except Exception:

        # Raise exception for any issues writing template to file
        raise Exception('Unable to write new file %s/' % file)


def random_success():

    success = ['\U0001F973',
               '\U0001F382',
               '\U0001F37E',
               '\U0001F389',
               '\U0001F38A']

    return(random.choice(success))
