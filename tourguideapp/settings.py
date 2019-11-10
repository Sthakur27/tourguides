#this settings file outlines connection to database


import os
basedir = os.path.abspath(os.path.dirname(__file__))
#sqlite database configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'config.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLITE_TEST = False
BOOTSTRAP_SERVE_LOCAL = True


