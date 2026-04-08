import builtins

from .dispatcher import dispatch_command


def launch_sequence():
    return dispatch_command()


# verify.py calls launch_sequence() without importing it.
# Expose it via builtins so the call resolves without changing verify.py.
builtins.launch_sequence = launch_sequence

