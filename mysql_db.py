# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:05:09 2019

"""

import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pymysql
import os

def mysql_conn(sql_str):
    # 数据库连接参数
    conn = pymysql.connect(host='xxx',user='xxx',passwd='xxx',db='xxx',port=xxx,charset='utf8')
    cur = conn.cursor()
    cur.execute(sql_str)
    data = cur.fetchall()
    columnsname = [x[0] for x in cur.description]
    data=pd.DataFrame([list(x) for x in data],columns=columnsname)
    cur.close()
    conn.close()
    return data

def data_get(x):
    sql1='''select a.user_name,password,b.app_name,content,link,app_rank
                from user_info a left join rights_mang b
		            on a.user_name = b.user_name
		        left join app_link c
		            on b.app_name = c.app_name
		        where a.user_name = '{0}' ORDER BY app_rank'''
    data = mysql_conn(sql1.format(x))
    return data 
