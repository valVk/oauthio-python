from oauthio_python.httpwrapper import HttpWrapper

__author__ = 'val'


class Injector(HttpWrapper):
    _instances = {}

    session = None
    ssl_verification = False
    config = {
        'oauthd_url': 'https://oauth.io',
        'oauthd_base': '/auth',
        'app_key': '',
        'app_secret': ''
    }

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Injector, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]

    def getrequest(self):
        return HttpWrapper()

    def setsession(self, session):
        Injector.sesion = session

