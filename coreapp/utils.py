import hashlib
from base64 import b64encode


def hash_password(password):
    """ Return a hashed version of 'password' string

    currently use a naïve SHA1 algorithme for compatibility with opnsense
    """
    hashed = hashlib.sha1(password.encode('utf-8')).digest()
    # Password string formated for LDAP client
    return "{SHA}" + b64encode(hashed).decode()
