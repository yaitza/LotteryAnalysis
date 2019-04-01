#!/usr/bin/python
# coding=utf-8
# Copyright 2019 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================


__author__ = "yaitza"
__date__ = "2019-02-25 16:52"

import os
import sqlite3
import time
from obtainoriginaldata import requests_lottery


class sqliteoperator:

    def __init__(self):
        self.db_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "Resources", "lottery.db")
        print(self.db_file)
        self.conn = sqlite3.connect(self.db_file)

    def insert_lottery_results(self, lottery_results):
        c = self.conn.cursor()
        latest_lottery_date = self.get_latest_lottery()[1]
        for lottery in lottery_results:
            insert_sql = "INSERT INTO lottery_summary(ID,lottery_date,week,redballs,blueballs,content,sales,poolmoney,prizegrades)" \
                         " VALUES (\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\",\"{5}\",\"{6}\",\"{7}\",\"{8}\")".format(
                lottery["code"], lottery["date"][0:10], lottery["week"], lottery["red"], lottery["blue"],
                lottery["content"], lottery["sales"], lottery["poolmoney"], lottery["prizegrades"])
            if lottery["date"][0:10] > latest_lottery_date:
                c.execute(insert_sql)

        self.conn.commit()

    # def get_latest_date_lottery(self):
    #     c = self.conn.cursor()
    #     select_sql = "SELECT lottery_date FROM lottery_summary order BY lottery_date desc LIMIT 1"
    #     cursor = c.execute(select_sql)
    #     lottery_date = None
    #     for row in cursor:
    #         lottery_date = row[0]
    #     return lottery_date

    def get_latest_lottery(self):
        c = self.conn.cursor()
        select_sql = "SELECT * FROM lottery_summary ORDER BY lottery_date DESC LIMIT 1"
        cursor = c.execute(select_sql)
        lottery = []
        for row in cursor:
            lottery.extend(list(row))
        return lottery

    def get_single_value(self, item):
        c = self.conn.cursor()
        select_sql = "SELECT {0} FROM lottery_summary ORDER BY ID ASC".format(item)
        cursor = c.execute(select_sql)
        red_balls = []
        for row in cursor:
            red_balls.append(row[0])
        return red_balls

    def get_blue_statistics(self):
        c = self.conn.cursor()
        select_sql = r"SELECT blueballs,COUNT(blueballs) FROM lottery_summary GROUP BY blueballs"
        cursor = c.execute(select_sql)
        blue_balls = []
        blue_ball_statistics = []
        for row in cursor:
            blue_balls.append(row[0])
            blue_ball_statistics.append(row[1])

        return blue_balls, blue_ball_statistics

    def __del__(self):
        self.conn.close()


if __name__ == "__main__":
    response_lottery = requests_lottery("2013-01-01", time.strftime("%Y-%m-%d", time.localtime()))

    so = sqliteoperator()
    so.insert_lottery_results(response_lottery)
    print(so.get_latest_lottery())
    # so.get_latest_date_lottery()
    # so.get_blue_statistics()
    # print(so.get_single_value('redballs'))
    # print(so.get_single_value('blueballs'))
