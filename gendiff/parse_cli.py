import argparse

AVAILABLE_FORMATS = ['stylish', 'plain', 'json']


def parse_cli():
    """Parse command line args and/ or returns tuple filepaths 1, 2 & format.

    :returns: (filepath1, filepath2, format). Tuple of filepath to first_file,
    second_file and format if any, else default."""

    parser = argparse.ArgumentParser(
        prog='gendiff',
        formatter_class=argparse.RawTextHelpFormatter,
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument(
        '-f', '--format', default='stylish',
        help=f'''set format of output (default: %(default)s).
Formats: {{{", ".join(AVAILABLE_FORMATS)}}}.'''
    )

    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
