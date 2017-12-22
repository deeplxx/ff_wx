# -*- coding: utf-8 -*-
from werobot import WeRoBot

token = 'ffwxwm2017'
myrobot = WeRoBot(token=token.encode('utf-8'))


@myrobot.handler
def hello(message):
    return 'hello world'
