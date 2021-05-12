import os

SENSENDGRID_API_KEY = (
    "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"
)
FROM_EMAIL = "commit.net.in@gmail.com"


class Database:
    NAME = os.getenv("POSTGRES_DB")
    USER = os.getenv("POSTGRES_USER")
    PASSWORD = os.getenv("POSTGRES_PASSWORD")
    HOST = os.getenv("DATABASE_HOST")
    PORT = os.getenv("DATABASE_PORT")


class Secrets:
    SECRET_KEY = "SuperSecretSecretKey"
    HOST_DOMAIN = "commit.net.in"
    HOST_IP = "157.245.248.104"
