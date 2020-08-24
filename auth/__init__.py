from flask_httpauth import HTTPBasicAuth
from hashlib import md5

auth = HTTPBasicAuth()

users = {
    "behzad": "73ef15440bffa84c91af20b15a596722"
}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@auth.hash_password
def hash_pw(password):
    return md5(password.encode("UTF-8")).hexdigest()
