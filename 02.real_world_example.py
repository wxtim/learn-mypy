# An example where typing might have saved me a lot of pain.
from subprocess import Popen, STDOUT, PIPE


def print_some_info():
    # There were a lot of interfaces to shell stuff and file reading
    # In Rose:
    # On the move to Python 3, most of these caused widespread breakages
    # because they now returned bytes not str types.
    p = Popen(['cat', '{}/stuff/02.stuffin'.format(__file__)], stdout=PIPE)
    return p.communicate()


print('[NOTE]' + print_some_info())
