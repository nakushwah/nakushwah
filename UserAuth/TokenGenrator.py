"""
    creating email verification token , and validating
"""

import datetime
import jwt
from django.conf import settings


def token_create(user):
    """creating email verification token
        :param user
        :return token
    """
    payload = {
        'email': user.email,
        'id': str(user.id),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=300)
    }
    token = jwt.encode(payload, settings.SIMPLE_JWT['SIGNING_KEY'], settings.SIMPLE_JWT['ALGORITHM'])
    return token


def token_validator(token):
    """validating Token
    :param token
    :return payload
    """
    try:
        payload = jwt.decode(token, settings.SIMPLE_JWT['SIGNING_KEY'], settings.SIMPLE_JWT['ALGORITHM'])
        return payload
    except:
        return None
