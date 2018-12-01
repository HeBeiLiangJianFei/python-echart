# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei

from pyecharts import Bar
bar =Bar("标记线和标记点示例")
bar.add("商家A", attr, v1, mark_point=["average"])
bar.add("商家B", attr, v2, mark_line=["min", "max"])
bar.render(path="render-02.html")
from pyecharts import Bar
bar =Bar("x 轴和 y 轴交换")
bar.add("商家A", attr, v1)
bar.add("商家B", attr, v2, is_convert=True)
bar.render()
