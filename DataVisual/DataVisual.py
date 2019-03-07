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
from GenerateLotteryCode.SqliteOperator import SqliteOperator


class DataVisual:
    def __init__(self):
        self.sql = SqliteOperator()
        print("init success!")

    def blue_statistics_visual(self):
        pyplot.figure('bar figure')
        blue_ball, blue_statistics = self.sql.get_blue_statistics()
        show_ball = []
        for ball in blue_ball:
            show_ball.append(int(ball))
        pyplot.xlabel(r"Blue Balls")
        pyplot.ylabel(r"Blue Balls Count")
        pyplot.title(r"Blue Balls Statistics")
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


    def blue_visual(self):
        blue_ball = self.sql.get_single_value('blueballs')
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
    dv = DataVisual()
    # dv.blue_visual()
    dv.blue_statistics_visual()
