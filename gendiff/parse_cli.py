import argparse


def parse_cli():
    """Parse command line args and/ or returns tuple filepaths 1, 2 & formats.

    :returns: (filepath1, filepath2, formats). Tuple of filepath to first_file,
    second_file and formats if any, else default."""

    available_formats = ['stylish', 'plain', 'json']

    parser = argparse.ArgumentParser(
        prog='gendiff',
        formatter_class=argparse.RawTextHelpFormatter,
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument(
        '-f', '--formats', default='stylish',
        help=f'''set formats of output (default: %(default)s).
Formats: {{{", ".join(available_formats)}}}.'''
    )

    args = parser.parse_args()
    return args.first_file, args.second_file, args.formats
