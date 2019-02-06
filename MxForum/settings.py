import peewee_async

settings = {
    "secret_key": "xJ&U6q^%U4srWMpC",
    "static_path": "static",
    "static_url_prefix": "/static/",
    "template_path": "templates",
    "db": {
        "host": "106.12.104.43",
        "user": "root",
        "password": "mysql",
        "database": "db_mx_forum",
        "port": 3306
    },
    'redis': {
        'host': '106.12.104.43',
    },

}

database = peewee_async.MySQLDatabase(**settings['db'])
