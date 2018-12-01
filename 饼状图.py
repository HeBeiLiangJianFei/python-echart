# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei
# 11 Pie（饼图）
from pyecharts import Pie
attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子","手表"]
v1 =[11, 12, 13, 10, 10, 10,30]
pie =Pie("饼图示例")
pie.add("", attr, v1, is_label_show=True)
pie.show_config()
pie.render("饼状图2.html")