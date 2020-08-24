import os

# database connection
DB_CONNECTION = {
    # "ELASTIC_INDEX": "",
    # "ELASTIC_USERNAME": "",
    # "ELASTIC_PASSWORD": "",
    # "ELASTIC_HOST": "localhost",
    # "ELASTIC_PORT": 9200
}

# database uri
# DATABASE_URI = ''

# flask vars
FLASK_VARS = {
    'SECRET_KEY': 'hO30R_API_PROD',
}

# another third party libs...
# PASSLIB = {
#     'HASH_ALGORITHM': 'SHA512',
# }

PATHS = {
    'IMAGES_ROOT': os.getenv('IMAGES_ROOT')
}
