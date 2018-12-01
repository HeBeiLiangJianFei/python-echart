# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei

# 4 Gauge（仪表盘）
from pyecharts import Gauge
gauge =Gauge("仪表盘示例")
gauge.add("业务指标", "完成率", 66.66)
gauge.show_config()
gauge.render("rander-05.html")