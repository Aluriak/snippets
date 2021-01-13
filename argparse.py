
import os
import sys
import argparse


def parse_args(args:iter=None) -> dict:
    return cli_parser().parse_args(args)


def parse_cli() -> argparse.ArgumentParser:
    """Simpler version"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pages', nargs='+', type=str, help='pages to edit')
    default_ini = os.environ.get('XDG_CONFIG_HOME', '~/.config') + '/vimoku/vimoku.ini'
    parser.add_argument('--config', '-c', type=str, help='configuration file to use', default=default_ini)
    parser.add_argument('--message', '-m', type=str, help='version message for the wiki', default=DEFAULT_MESSAGE)
    parser.add_argument('--editor', '-e', type=str, help='the editor to use', default=None)
    parser.add_argument('--minor', action='store_true', help='whether the modification is minor or not', default=False)
    return parser.parse_args()


def cli_parser() -> argparse.ArgumentParser:
    """Complex version"""
    # main parser
    parser = argparse.ArgumentParser(description='CLI for PowerGrASP.')
    subs = parser.add_subparsers(dest='recipe name')

    # powergraph recipe
    parser_pwg = subs.add_parser('powergraph', description='Run a regular Powergraph compression.')
    _populate_compression_parser(parser_pwg)

    parser.add_argument('pos', type=existant_file, help='file containing the graph data')
    parser.add_argument('optpos', nargs='?', default=None, help='optional positional argument')
    parser.add_argument('--flag', '-f', action='store_true', help='flag equal to True if set')
    parser.add_argument('--outfile', '-o', type=writable_file, help='output file. Will be overwritted')
    parser.add_argument('--outformat', type=output_format, help='Format to use for output')
    parser.add_argument('--loglevel', type=loglevel, help='Logging level, one of DEBUG, INFO, WARNING, ERROR or CRITICAL')
    parser.add_argument('--logfile', type=writable_file, help='Logging file, where all logs are written')

    # flags
    parser.add_argument('--signal-profile', action='store_true',
                        help='Print information on signals that are raised by compression.')

    # Compression arguments
    parser.add_argument('--thread', type=thread_number, default=1,
                        help='number of thread to use during solving')

    # Standard version access
    parser.add_argument('--version', action='version', version='%(prog)s 2.0')

    return parser

def normalized(arg:str) -> str:
    """Normalize argument name to valid identifier.

    >>> normalized('--foo-bar')
    'foo_bar'

    """
    return arg.lstrip('-').replace('-', '_')


def loglevel(level:str) -> str:
    """Argparse type, raising an error if given loglevel does not exists"""
    if level.upper() not in commons.LOGLEVELS:
        raise argparse.ArgumentTypeError(
            "Given loglevel ({}) doesn't exists. "
            "Expected: {}.".format(level, ', '.join(commons.LOGLEVELS))
        )
    return level


def thread_number(nbt:int) -> int:
    """Argparse type, raising an error if given thread number is non valid"""
    if float(nbt) != int(nbt):
        raise argparse.ArgumentTypeError(
            "Given number of thread ({}) is a float, not an integer.".format(nbt)
        )
    if int(nbt) < 1:
        raise argparse.ArgumentTypeError(
            "Given number of thread ({}) is not valid.".format(nbt)
        )
    return int(nbt)


def existant_file(filepath:str) -> str:
    """Argparse type, raising an error if given file does not exists"""
    if not os.path.exists(filepath):
        raise argparse.ArgumentTypeError("file {} doesn't exists".format(filepath))
    return filepath


def writable_file(filepath:str) -> str:
    """Argparse type, raising an error if given file is not writable.
    Will delete the file !

    """
    try:
        with open(filepath, 'w') as fd:
            pass
        os.remove(filepath)
        return filepath
    except (PermissionError, IOError):
        raise argparse.ArgumentTypeError("file {} is not writable.".format(filepath))


def elem_in_list(elements:iter):
    def valid_element(element:str) -> str:
        """Argparse type, raising an error if given value is not expected"""
        if element not in elements:
            raise argparse.ArgumentTypeError(f"Value {element} is unexpected. Valid inputs: " + ', '.join(map(str, elements)))
        return element
    return valid_element
