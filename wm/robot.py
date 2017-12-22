# -*- coding: utf-8 -*-
from werobot import WeRoBot

myrobot = WeRoBot(token='ffwxwm2017')


@myrobot.handler
def hello(message):
    return 'hello world'
