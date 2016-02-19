from functools import wraps
from pyechonest.util import EchoNestException
from pytest import skip

def skip_on_rate_limit_exceeded(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except EchoNestException as e:
            # see http://developer.echonest.com/docs/v4#response-codes
            if hasattr(e, 'code') and e.code == 3:
                skip('rate limit exceeded')
            else:
                raise e
    return wrapper
