# An example where typing might have saved me a lot of pain.
from subprocess import Popen, PIPE


def print_some_info():
    # There were a lot of interfaces to shell stuff and file reading
    # In Rose:
    # On the move to Python 3, most of these caused widespread breakages
    # because they now returned bytes not str types.
    info = Popen(
        ['cat', 'stuff/02.stuffin'],
        stdout=PIPE
    )
    return info.communicate()[0]


print('[NOTE] ' + print_some_info().strip())
