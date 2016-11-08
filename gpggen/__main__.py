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
from gpggen import createkey, keeper, outdir
import os


def cli():
    """Arg parser for cli.
    Args:
        None
    Returns:
        None
    Raises:
        None
    """
    args = docopt(__doc__, version='GPG Gen Utility 0.0.1.a1')
    main(args)


def main(args):
    """Program entry point.
    This takes the arguments and performs the encryption.
    Args:
        args: The dictionary of arguments parsed by docopt
    Returns:
        None
    Raises:
        None
    """
    while True:
        name = createkey()
        print('.', end='', flush=True)
        if keeper(name):
            print(name)
            os.rename('X.pub', outdir + b'/' + name + b'.pub')
            os.rename('X.sec', outdir + b'/' + name + b'.sec')

if __name__ == '__main__':
    cli()
