# Created by Adam Thompson-Sharpe on 12/03/2020.
class InitError(Exception):
    """
    An error occured during a class' initialization.
    """
    pass

class AuthError(Exception):
    """
    An error occured when attempting to authorize.
    """
    pass
