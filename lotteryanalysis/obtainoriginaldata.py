#!/usr/bin/python
# coding=utf-8
# Copyright 2019 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================


__author__ = "yaitza"
__date__ = "2019-02-22 16:41"

import json
import requests


url = "http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice"
referer_url = "http://www.cwl.gov.cn/kjxx/ssq/kjgg/"


def requests_lottery(from_date, end_date):

    lottery_results = []
    page_num = 1
    querystring = {"name": "ssq", "issueCount": "",
                   "issueStart": "", "issueEnd": "",
                   "dayStart": from_date, "dayEnd": end_date,
                   "pageNo": page_num}
    headers = {'Referer': referer_url}
    payload = ""
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    response_json = json.loads(response.text)

    page_count = response_json["pageCount"]

    lottery_results.extend(response_json["result"])
    page_num = page_num + 1
    while page_num <= page_count:
        querystring_num = {"name": "ssq", "issueCount": "", "issueStart": "", "issueEnd": "", "dayStart": from_date,
               "dayEnd": end_date, "pageNo": page_num}

        response_num = requests.request("GET", url, data=payload, headers=headers, params=querystring_num)
        response_num_json = json.loads(response_num.text)
        lottery_results.extend(response_num_json["result"])

        page_num = page_num + 1

    if lottery_results.__len__() == response_json["countNum"]:
        print("Obtain Data Success!")
        return lottery_results
    else:
        print("Obtain Data Failure!")
        return None


if __name__ == "__main__":
    # url = "http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice"
    #
    # querystring = {"name": "ssq", "issueCount": "", "issueStart": "", "issueEnd": "", "dayStart": "2018-01-01",
    #                "dayEnd": "2019-01-01", "pageNo": "1"}
    #
    # payload = ""
    # headers = {
    #     'Referer': "http://www.cwl.gov.cn/kjxx/ssq/kjgg/",
    # }
    #
    # response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    #
    # print(response.text)

    requests_lottery("2018-01-01", "2019-03-11")

