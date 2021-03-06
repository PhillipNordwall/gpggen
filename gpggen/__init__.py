"""gpggen provides the capability of calling out to gpg to generate keys, and
check for a matching hex "word"
"""
import os
import re
import signal
import subprocess
import sys


OUTDIR = b"out"

WORDS = (b'BAD', b'DAD',
         b'DEAD', b'BEEF', b'FACE', b'1337', b'1234',
         b'([BDF])00\1', b'FB5D', b'2600', b'BE[AE]D'
         b'F00D', b'CAFE', b'DEAF', b'BABE', b'C0DE',
         b'[01]{5,}', b'ABCDEF',
         b'0FF1CE', b'C0FFEE', b'BADDAD', b'(.)\1{4,}',
         b'ABACABA')
RWORDS = re.compile(b'|'.join(WORDS))


def newname(gpgout):
    """newname takes output from gpg --gen-key and generates a new name based
    in the form of 'id-fingerprint-subid'
    Args:
        gpgout: The output from gpg --gen-key
    Returns:
        string of the form 'id-fingerprint-subid'
    Raises:
        None
    """
    exp = b'^[^/]*/([^ ]*).*\n.*Key fingerprint = (.*)\n[^/]*/([^ ]*).*'
    reg = re.compile(exp)
    return b'-'.join(b''.join(i.split(b' ')) for i in reg.findall(gpgout)[0])


def createkey():
    """createkey generates a public and private set of gpg keys.

    It calls gpg to create a key and parses it's output to return a string in
    the form of 'id-fingerprint-subid'. There is also the side effect of
    having leaving two files in the CWD. X.pub and X.sec.
    Args:
        None
    Returns:
        string of the form 'id-fingerprint-subid'
    Raises:
        None
    Side Effect:
        Two files in the CWD of the form X.sec and X.pub. These are the
        public and private keys generated by the gpg command
    """
    subprocess.run("gpg --batch --gen-key gpginp".split(" "),
                   stderr=subprocess.DEVNULL)
    proc = subprocess.run("gpg --with-fingerprint X.pub".split(" "),
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    return newname(proc.stdout)


def keeper(string):
    """keeper returns a true when a substring of s is in the WORDS list.
    Args:
        string : The string to check against.
    Returns:
        True if there is a substring in 'WORDS' that is in s, else false.
    Raises:
        None
    """
    words = RWORDS.findallt(string)
    if words:
        return True
    return False


def sigint(sig, frame):
    """sigint handler for SIGINT to do cleanup.
    Args:
        sig The signal number being called with.
        frame: The current stack frame.
    Returns:
        None
    Side Effect:
        Removal of the temporary outputs, X.pub, and X.sec.
    """
    os.remove('X.pub')
    os.remove('X.sec')
    sys.exit(0)


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
    signal.signal(signal.SIGINT, sigint)
    while True:
        name = createkey()
        print('.', end='', flush=True)
        if keeper(name):
            print(name)
            os.rename('X.pub', OUTDIR + b'/' + name + b'.pub')
            os.rename('X.sec', OUTDIR + b'/' + name + b'.sec')
