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
        str_tmp = r"其中复式或胆拖投注为："
        str_tem = r"其中复式投注为："
        area_array = []
        if str_tmp in item:
            item_array = item.split(str_tmp)
            area_array.extend(item_array[0].split(',')[0:-1])
            area_array.extend((item_array[1][0:-1]).split(','))
        elif str_tem in item:
            item_array = item.split(str_tem)
            area_array.extend(item_array[0].split(',')[0:-1])
            area_array.extend((item_array[1][0:-1]).split(','))
        else:
            area_array.extend(item.split(',')[0:-1])
        for area in area_array:
            if "0注".__eq__(area): continue
            area_data = [''.join(list(g)) for k, g in itertools.groupby(area, key=lambda x: x.isdigit())]
            area_zone = area_data[0]
            area_int = int(area_data[1])
            if area_zone in area_dict.keys():
                area_dict[area_zone] = area_dict[area_zone] + area_int
                continue
            area_dict[area_zone] = area_int
    return area_dict


def handle_prize():
    so = SqliteOperator()
    bonus = so.get_single_value("prizegrades")

    prize_money = []
    for item in bonus:
        prize_array = []
        prize_dict = {}
        i_flag = 0
        for prize in item.strip('[]').split(','):
            prize_summary = prize.strip(' {} ').split(': ')
            prize_dict[prize_summary[0].strip('\'')] = prize_summary[1].strip('\'')
            i_flag = i_flag + 1
            if i_flag % 3 == 0:
                prize_array.append(prize_dict)
                prize_dict = {}
        prize_money.append(prize_array)
    return prize_money


if __name__ == "__main__":
    # print(red_statistics())
    # ball_sum_count()
    area_statistics()


