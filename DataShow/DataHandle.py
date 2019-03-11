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

    red_sum_count = sorted(Counter(red_sum_array).items(), key=lambda x: x[1], reverse=True)
    balls_sum_count = sorted(Counter(balls_sum_array).items(), key=lambda x: x[1], reverse=True)
    red_sum = [str(red_item[0]) for red_item in red_sum_count]
    red_count = [red_item[1] for red_item in red_sum_count]
    ball_sum = [str(ball_item[0]) for ball_item in balls_sum_count]
    ball_count = [ball_item[1] for ball_item in balls_sum_count]
    return red_count, red_sum, ball_count, ball_sum


def area_statistics():
    so = SqliteOperator()
    area_count = so.get_single_value("content")

    area_dict = {}
    for item in area_count:
        print(item)
        item.replace("。其中复式或胆拖投注为：", ",")

        str_tmp ="其中复式或胆拖投注为"
        if str_tmp in item:
            item1 = item.split(str_tmp)
        else:
            for area in item.split(',')[0:-1]:
                print("{} {} {}".format(area, area[-2:-1], area[0:-2]))
                area_zone = area[0:-2]
                area_int = int(area[-2:-1])

                if area_zone in area_dict.keys():
                    area_dict[area_zone] = area_dict[area_zone] + area_int
                    continue
                area_dict[area_zone] = int(area_int)
        print(area_dict)


if __name__ == "__main__":
    # print(red_statistics())
    # ball_sum_count()
    area_statistics()


