from oauthio_python.injector import Injector

__author__ = 'valeriy.ilihmetov'


class Oauth(Injector):
    injector = None
    initialized = False

    def __init__(self):
        self.injector = Injector()