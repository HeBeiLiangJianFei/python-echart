# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei

from pyecharts import Graph
import json
with open("..jsonweibo.json", "r", encoding="utf-8") as f:
    j =json.load(f)
    print(j)
    # nodes, links, categories, cont, mid, userl =j
    # graph =Graph("微博转发关系图", width=1200, height=600)
    # graph.add("", nodes, links, categories, label_pos="right", repulsion=50, is_legend_show=False, line_curve=0.2, label_text_color=None)
    # graph.show_config()
    # graph.render("render-09.html")
