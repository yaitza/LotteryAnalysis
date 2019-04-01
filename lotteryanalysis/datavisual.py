#!/usr/bin/python
# coding=utf-8
# Copyright 2019 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2019-02-26 15:45"

import os
from matplotlib import pyplot
from sqliteoperator import sqliteoperator
import datahandle
from pylab import *
from PIL import Image, ImageFont, ImageDraw

sql = sqliteoperator()

file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)))

def winners_of_lottery():
    latest = sql.get_latest_lottery()
    info = "期数：{0} 开奖时间：{1} 红球号码：{2} 蓝球号码：{3}".format(latest[0], latest[1], latest[3], latest[4])
    im = Image.new("RGB", (550, 25), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    ttf_path = os.path.join(file_path, "..", "resources", "simhei.ttf")
    font = ImageFont.truetype(ttf_path, 14)

    dr.text((10, 5), info, font=font, fill="#000000")

    # im.show()
    winning_path = os.path.join(file_path, "..", "docs", "image", "Winning.png")
    im.save(winning_path)


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
    blue_statistics_path = os.path.join(file_path, "..", "docs", "image", "BlueBallsStatistics.png")
    pyplot.savefig(blue_statistics_path, dpi=200)
    # pyplot.show()


def red_statistics_visual():
    red_balls, red_statistics = datahandle.red_statistics()
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
    redballs_statistics_path = os.path.join(file_path, "..", "docs", "image", "RedBallsStatistics.png")
    pyplot.savefig(redballs_statistics_path, dpi=300)
    # pyplot.show()


def ball_sum_visual():
    red_count, red_sum, ball_count, ball_sum = datahandle.ball_sum_count()

    pyplot.figure(figsize=(35, 10))

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
    balls_sum_path = os.path.join(file_path, "..", "docs", "image", "BallsSumCount.png")
    pyplot.savefig(balls_sum_path, dpi=300)
    # pyplot.show()


def area_statistics_visual():
    area_data = datahandle.area_statistics()

    pyplot.figure(figsize=(12, 10))
    pyplot.subplot(2, 1, 1)
    pyplot.xlabel(r"中奖地区")
    pyplot.ylabel(r"中奖次数")
    pyplot.title(r"各地区中奖次数统计")
    pyplot.xlim((-1, area_data.__len__()))
    pyplot.ylim((0, max(area_data.values()) + 50))
    pyplot.xticks(range(0, area_data.__len__(), 1))
    pyplot.yticks(range(0, max(area_data.values()) + 50, 50))
    pyplot.grid(axis='y')
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    pyplot.bar(area_data.keys(), area_data.values())
    for x, y in zip(area_data.keys(), area_data.values()):
        pyplot.text(x, y + 3, x, ha='center', fontsize=7)

    area_data_sorted = sorted(area_data.items(), key=lambda x: x[1], reverse=True)
    pyplot.subplot(2, 1, 2)
    pyplot.xlabel(r"中奖地区")
    pyplot.ylabel(r"中奖次数")
    pyplot.title(r"排序后各地区中奖次数统计")
    pyplot.xlim((-1, area_data_sorted.__len__()))
    pyplot.ylim((0, max(area_data.values()) + 50))
    pyplot.xticks(range(0, area_data.__len__(), 1))
    pyplot.yticks(range(0, max(area_data.values()) + 50, 50))
    pyplot.grid(axis='y')
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    pyplot.bar([x[0] for x in area_data_sorted], [x[1] for x in area_data_sorted])
    for x, y in zip([x[0] for x in area_data_sorted], [x[1] for x in area_data_sorted]):
        pyplot.text(x, y + 3, x, ha='center', fontsize=7)
    area_path = os.path.join(file_path, "..", "docs", "image", "AreaWinningCount.png")
    pyplot.savefig(area_path.format(os.getcwd()), dpi=300)
    # pyplot.show()
    pyplot.clf()
    pyplot.figure()
    area_data_pie = sorted(area_data.items(), key=lambda x: x[0], reverse=False)
    pyplot.pie([x[1] for x in area_data_pie], labels=[x[0] for x in area_data_pie])
    area_pie_path = os.path.join(file_path, "..", "docs", "image", "RedBallsStatistics.png")
    pyplot.savefig(area_pie_path.format(os.getcwd()), dpi=300)
    # pyplot.show()


def sales_money_visual():
    sales_money = sql.get_single_value("sales")
    pool_sales_money = sql.get_single_value("poolmoney")

    prize_money, prize_summary = datahandle.handle_prize()

    pyplot.figure(figsize=(12, 6))
    pyplot.xlabel("期数")
    pyplot.ylabel("金额")
    pyplot.title("期数销售金额与奖池金额曲线图")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    pyplot.plot(range(0, prize_money.__len__()), prize_money, color="red",
                linewidth=1, linestyle="-", label="奖金金额")
    pyplot.plot(range(0, sales_money.__len__()), sales_money, color="blue",
                linewidth=1, linestyle="-", label="销售金额")
    pyplot.plot(range(0, pool_sales_money.__len__()), pool_sales_money, color="orange",
                linewidth=1, linestyle="-", label="奖池金额")
    legend(loc='upper left')
    sales_money_path = os.path.join(file_path, "..", "docs", "image", "RedBallsStatistics.png")
    pyplot.savefig(sales_money_path.format(os.getcwd()), dpi=300)
    # pyplot.show()


def difference_prize_visual():
    prize_money, prize_summary = datahandle.handle_prize()
    sales_money = sql.get_single_value("sales")
    pool_sales_money = sql.get_single_value("poolmoney")

    deference_prize = []
    deference = []
    for p, s in zip(prize_money, sales_money):
        deference.append(float(p/s))
        deference_mount = s - p
        deference_prize.append(deference_mount)

    pyplot.figure(figsize=(20, 14))
    pyplot.subplot(2, 1, 1)
    pyplot.xlabel("期数")
    pyplot.ylabel("金额")
    pyplot.title("销售与奖金差值累计金额与奖池金额曲线图")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    pyplot.grid(axis='y')
    pyplot.xlim((-1, deference_prize.__len__()))
    pyplot.plot(range(0, deference_prize.__len__()), deference_prize, color="blue",
                linewidth=1, linestyle="-", label="销售与奖金差值累计金额")
    pyplot.plot(range(0, pool_sales_money.__len__()), pool_sales_money, color="red",
                linewidth=1, linestyle="-", label="奖池金额")
    legend(loc='upper left')

    pyplot.subplot(2, 1, 2)
    pyplot.xlabel("期数")
    pyplot.ylabel("奖金金额与销售金额占比")
    pyplot.title("奖金金额与销售金额占比曲线图")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    pyplot.grid(axis='y')
    pyplot.xlim((-1, deference.__len__()))
    pyplot.plot(range(0, deference.__len__()), deference, color="blue",
                linewidth=1, linestyle="-", label="奖金金额与销售金额占比曲线图")
    legend(loc='upper left')
    diff_path = os.path.join(file_path, "..", "docs", "image", "DifferenceMoney.png")
    pyplot.savefig(diff_path, dpi=300)
    # pyplot.show()


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
    sales_money_visual()
    difference_prize_visual()
    blue_statistics_visual()
    red_statistics_visual()
    ball_sum_visual()
    area_statistics_visual()
    winners_of_lottery()
