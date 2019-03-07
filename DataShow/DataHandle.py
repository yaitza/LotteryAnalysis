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

    for i in range(1, 34):
        print(red_balls_summary.count(i))
    return red_balls_int, red_balls_statistics


if __name__ == "__main__":
    print(red_statistics())



