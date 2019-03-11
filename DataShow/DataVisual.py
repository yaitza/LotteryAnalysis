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

from collections import Counter
from matplotlib import pyplot
from GenerateLotteryCode.SqliteOperator import *
from DataShow import DataHandle

sql = SqliteOperator()


def blue_statistics_visual():
    blue_ball, blue_statistics = sql.get_blue_statistics()
    show_ball = []
    for ball in blue_ball:
        show_ball.append(int(ball))

    large_count = max(blue_statistics)

    pyplot.subplot(2, 1, 1)
    # pyplot.xlabel(r"Blue Balls")
    pyplot.ylabel(r"Blue Balls Count")
    pyplot.title(r"Blue Balls Statistics, Count:{0}".format(sum(blue_statistics)))
    pyplot.xlim((0, 17))
    pyplot.ylim((0, large_count + 10))
    pyplot.xticks(range(0, 17, 1))
    pyplot.yticks(range(0, large_count + 10, 10))

    pyplot.bar(show_ball, blue_statistics)
    for x, y in zip(show_ball, blue_statistics):
        pyplot.text(x, y + 0.5, y, ha='center')
    # pyplot.grid(axis="y")
    # pyplot.savefig(r"{0}\..\image\BlueBallsStatistics.png".format(os.getcwd()), dpi=200)
    # pyplot.show()

    blue_balls_temp = {}
    for key, value in zip(blue_ball, blue_statistics):
        blue_balls_temp[key] = value
    blue_balls_sort = []
    blue_statistics_sort = []
    for key, value in sorted(blue_balls_temp.items(), key=lambda item: item[1], reverse=True):
        blue_balls_sort.append(key)
        blue_statistics_sort.append(value)

    pyplot.subplot(2, 1, 2)
    pyplot.xlabel(r"Blue Balls")
    pyplot.ylabel(r"Blue Balls Count")
    # pyplot.title(r"Blue Balls Statistics, Count:{0}".format(sum(blue_statistics_sort)))
    pyplot.xlim((-1, 16))
    pyplot.ylim((0, large_count + 10))
    pyplot.xticks(range(0, 17, 1))
    pyplot.yticks(range(0, large_count + 10, 10))
    pyplot.bar(blue_balls_sort, blue_statistics_sort)
    for x, y in zip(blue_balls_sort, blue_statistics_sort):
        pyplot.text(x, y + 0.5, y, ha='center')
    # pyplot.grid(axis="y")
    pyplot.savefig(r"{0}\..\image\BlueBallsStatistics.png".format(os.getcwd()), dpi=200)

    pyplot.show()


def red_statistics_visual():
    red_balls, red_statistics = DataHandle.red_statistics()
    large_count = max(red_statistics)

    pyplot.figure(figsize=(10, 7))
    pyplot.subplot(2, 1, 1)
    # pyplot.xlabel(r"red Balls")
    pyplot.ylabel(r"Red Balls Count")
    pyplot.title(r"Red Balls Statistics, Count:{0}".format(sum(red_statistics)))
    pyplot.xlim((0, 34))
    pyplot.ylim((0, large_count + 20))
    pyplot.xticks(range(0, 34, 1))
    pyplot.yticks(range(0, large_count + 20, 20))

    pyplot.bar(red_balls, red_statistics, facecolor='#f72422', edgecolor='white')
    for x, y in zip(red_balls, red_statistics):
        pyplot.text(x, y + 0.5, y, ha='center', fontsize=7)
    # pyplot.grid(axis="y")
    # pyplot.savefig(r"{0}\..\image\RedBallsStatistics.png".format(os.getcwd()), dpi=300)
    # pyplot.show()

    red_ball_sort = []
    red_statistics_sort = []
    red_balls_temp = {}
    for key, value in zip(red_balls, red_statistics):
        red_balls_temp[str(key)] = value
    for key, value in sorted(red_balls_temp.items(), key=lambda item: item[1], reverse=True):
        red_ball_sort.append(str(key))
        red_statistics_sort.append(value)

    pyplot.subplot(2, 1, 2)
    pyplot.xlabel(r"red Balls")
    pyplot.ylabel(r"Red Balls Count")
    # pyplot.title(r"Red Balls Statistics, Count:{0}".format(sum(red_statistics)))
    pyplot.xlim((-1, 33))
    pyplot.ylim((0, large_count + 20))
    pyplot.xticks(range(0, 34, 1))
    pyplot.yticks(range(0, large_count + 20, 20))
    pyplot.bar(red_ball_sort, red_statistics_sort, facecolor='#f72422', edgecolor='white')
    for x, y in zip(red_ball_sort, red_statistics_sort):
        pyplot.text(x, y + 0.5, y, ha='center', fontsize=7)
    # pyplot.grid(axis="y")
    pyplot.savefig(r"{0}\..\image\RedBallsStatistics.png".format(os.getcwd()), dpi=300)
    pyplot.show()


def ball_sum_visual():
    blue_balls = sql.get_single_value("blueballs")
    red_balls = sql.get_single_value("redballs")

    balls_sum_array = []
    red_sum_array = []

    for blue_ball, red_balls in zip(blue_balls, red_balls):
        red_sum = 0
        for ball in red_balls.split(','):
            red_sum = red_sum + int(ball)
        red_sum_array.append(red_sum)
        balls_sum_array.append(red_sum + int(blue_ball))

    red_sum_count = sorted(Counter(red_sum_array).items(), key=lambda x: x[1], reverse=True)
    balls_sum_count = sorted(Counter(balls_sum_array).items(), key=lambda x: x[1], reverse=True)
    red_sum = [str(red_item[0]) for red_item in red_sum_count]
    red_count = [red_item[1] for red_item in red_sum_count]
    ball_sum = [str(ball_item[0]) for ball_item in balls_sum_count]
    ball_count = [ball_item[1] for ball_item in balls_sum_count]

    pyplot.figure(figsize=(30, 10))
    # pyplot.figure(figsize=(30, 3))
    pyplot.subplot(2, 1, 1)

    pyplot.xlabel(r"Red Balls Count")
    pyplot.ylabel(r"Red Balls Sum")
    pyplot.title(r"Balls Count & Sum")
    pyplot.xlim(-1, red_sum.__len__())
    pyplot.ylim((0, red_count[0] + 5))
    pyplot.yticks(range(0, red_count[0] + 5, 5))
    pyplot.grid(axis="y")

    pyplot.bar(red_sum, red_count, facecolor='#f72422', edgecolor='white')
    for x, y in zip(red_sum, red_count):
        pyplot.text(x, int(y) + 0.5, x, ha='center')

    pyplot.subplot(2, 1, 2)
    pyplot.xlabel(r"Red&Red Balls Count")
    pyplot.ylabel(r"Red&Red Balls Sum")
    pyplot.title(r"Red&Red Balls Count & Sum")
    pyplot.xlim((-1, red_sum.__len__()+2))
    pyplot.ylim((0, red_count[0]+5))
    pyplot.yticks(range(0, red_count[0]+5, 5))
    pyplot.grid(axis="y")

    pyplot.bar(ball_sum, ball_count, facecolor='#251256', edgecolor='white')
    for x, y in zip(ball_sum, ball_count):
        pyplot.text(x, int(y) + 0.5, x, ha='center')
    pyplot.savefig(r"{0}\..\image\BallsSumCount.png".format(os.getcwd()), dpi=300)
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
    # blue_statistics_visual()
    # red_statistics_visual()
    ball_sum_visual()
