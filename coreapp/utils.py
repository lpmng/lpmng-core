import hashlib
from base64 import b64encode


def hash_password(password):
    """ Return a hashed version of 'password' string

    currently use a naïve SHA1 algorithme for compatibility with opnsense
    """
    hashed = hashlib.sha1(password.encode('utf-8')).digest()
    # Password string formated for LDAP client
    return "{SHA}" + b64encode(hashed).decode()


def import_ldap_users(ldapdb_users, db_users):
    """ Function to import user from old ldap database.

    copy LdapUser to User
    will be removed as soon as it isn't needed anymore
    """
    from .models import User
    for user in ldapdb_users.objects.all():
        new_user = User()
        new_user.username = user.uid
        new_user.first_name = user.commonname
        new_user.last_name = user.surname
        new_user.password = user.password
        new_user.email = user.mail
        new_user.tel = user.tel
        new_user.save()
