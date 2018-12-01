# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei

# 8 Liquid（水球图）
from pyecharts import Liquid
liquid =Liquid("水球图示例")
liquid.add("Liquid", [0.6])
liquid.show_config()
liquid.render("水球图例.html")