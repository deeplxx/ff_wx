# coding=utf8
from werobot import WeRoBot

robot = WeRoBot(token='ffwxwm2017')


@robot.handler
def hello(message):
    return 'hello world'
