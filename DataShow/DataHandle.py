#!/usr/bin/python
# coding=utf-8
# Copyright 2019 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2019-03-07 16:36"

import itertools
from collections import Counter
from GenerateLotteryCode.SqliteOperator import SqliteOperator


def red_statistics():
    so = SqliteOperator()
    red_balls = so.get_single_value("redballs")
    red_balls_summary = []
    for balls in red_balls:
        for ball in balls.split(','):
            red_balls_summary.append(int(ball))
    red_balls_int = []
    red_balls_statistics = []
    for key, group in itertools.groupby(sorted(red_balls_summary)):
        red_balls_int.append(int(key))
        red_balls_statistics.append(list(group).__len__())

    return red_balls_int, red_balls_statistics


def ball_sum_count():
    so = SqliteOperator()
    blue_balls = so.get_single_value(r"blueballs")
    red_balls = so.get_single_value(r"redballs")

    balls_sum_array = []
    red_sum_array = []

    for blue_ball, red_balls in zip(blue_balls, red_balls):
        red_sum = 0
        for ball in red_balls.split(','):
            red_sum = red_sum + int(ball)
        red_sum_array.append(red_sum)
        balls_sum_array.append(red_sum + int(blue_ball))

    print(red_sum_array)
    red_sum_count = sorted(Counter(red_sum_array).items(), key=lambda x: x[0], reverse=True)
    print(red_sum_count)
    # red_count_sum = sorted(Counter(red_sum_array).items(), key=lambda x: x[0], reverse=False)
    # print(red_count_sum)
    # print(sorted(Counter(balls_sum_array).items(), key=lambda x: x[1], reverse=True))
    # balls_sum_count = sorted(Counter(balls_sum_array).items(), key=lambda x: x[0], reverse=True)
    # red_sum = [str(red_item[0]) for red_item in red_sum_count]
    # print(red_sum)
    # red_count = [red_item[1] for red_item in red_sum_count]
    # print(red_count)


if __name__ == "__main__":
    # print(red_statistics())
    ball_sum_count()


