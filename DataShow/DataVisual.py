#!/usr/bin/python
# coding=utf-8
# Copyright 2019 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================
import os

__author__ = "yaitza"
__date__ = "2019-02-26 15:45"

from matplotlib import pyplot
from GenerateLotteryCode.SqliteOperator import *
from DataShow import DataHandle


sql = SqliteOperator()


def blue_statistics_visual():
    blue_ball, blue_statistics = sql.get_blue_statistics()
    show_ball = []
    for ball in blue_ball:
        show_ball.append(int(ball))
    pyplot.xlabel(r"Blue Balls")
    pyplot.ylabel(r"Blue Balls Count")
    pyplot.title(r"Blue Balls Statistics, Count:{0}".format(sum(blue_statistics)))
    pyplot.xlim((0, 17))
    pyplot.ylim((0, 100))
    pyplot.xticks(range(0, 17, 1))
    pyplot.yticks(range(0, 100, 10))

    pyplot.bar(show_ball, blue_statistics)
    for x, y in zip(show_ball, blue_statistics):
        pyplot.text(x, y+0.5, y, ha='center')
    pyplot.grid(axis="y")
    pyplot.savefig(r"{0}\..\image\BlueBallsStatistics.png".format(os.getcwd()), dpi=200)
    pyplot.show()


def red_statistics_visual():
    red_balls, red_statistics = DataHandle.red_statistics()
    pyplot.figure(figsize=(11, 7))
    pyplot.xlabel(r"red Balls")
    pyplot.ylabel(r"Red Balls Count")
    pyplot.title(r"Red Balls Statistics, Count:{0}".format(sum(red_statistics)))
    pyplot.xlim((0, 34))
    pyplot.ylim((0, 220))
    pyplot.xticks(range(0, 34, 1))
    pyplot.yticks(range(0, 220, 10))

    pyplot.bar(red_balls, red_statistics, facecolor='#f72422', edgecolor='white')
    for x, y in zip(red_balls, red_statistics):
        pyplot.text(x, y + 0.5, y, ha='center')
    pyplot.grid(axis="y")
    pyplot.savefig(r"{0}\..\image\RedBallsStatistics.png".format(os.getcwd()), dpi=300)
    pyplot.show()


def blue_visual():
    blue_ball = sql.get_single_value('blueballs')
    show_balls = []
    for ball in blue_ball:
        show_balls.append(int(ball))

    pyplot.figure('Scatter figure')
    ax = pyplot.gca()
    ax.scatter(range(0, 945), show_balls, c='r', s=3)
    pyplot.ylim((0, 16))
    pyplot.xlim((0, 1000))
    pyplot.yticks(range(0, 18, 1))
    pyplot.xticks(range(-10, 1000, 100))

    pyplot.grid()
    pyplot.show()


if __name__ == "__main__":
    # blue_visual()
    blue_statistics_visual()
    red_statistics_visual()
