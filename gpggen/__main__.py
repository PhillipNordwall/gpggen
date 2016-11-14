"""GPG Gen Utility
Usage:
    gpggen.py
    gpggen.py (-h | --help)
    gpggen.py (-v | --version)
Options:
    -h --help       Show this screen.
    -v --version    Show version.
"""
from docopt import docopt
from gpggen import main


def cli():
    """Arg parser for cli.
    Args:
        None
    Returns:
        None
    Raises:
        None
    """
    args = docopt(__doc__, version='GPG Gen Utility 0.0.2.a1')
    main(args)

if __name__ == '__main__':
    cli()
