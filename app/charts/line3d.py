import math
import pandas as pd
from pyecharts import Line3D, Page, Style
from app.charts.constants import RANGE_COLOR, WIDTH, HEIGHT
import os

def create_charts():
    page = Page()

    style = Style(
        width=WIDTH, height=HEIGHT
    )
    original_data = pd.read_csv('app/data/nasdaq100.csv', engine='python')
    dates = list(original_data.columns.values[1:])
    names = list(original_data['id'])

    original_data = original_data.as_matrix()[:, 1:]
    m, n = original_data.shape
    _data = []
    for i in range(m):
        for j in range(n):
            _data.append([names[i], dates[j], original_data[i, j]])
    chart = Line3D("3D 折线图-默认", **style.init_style)
    chart.add("", _data, is_visualmap=True, visual_range_color=RANGE_COLOR,
              visual_range=[0, 30], grid3d_rotate_sensitivity=5)
    page.add(chart)

    _data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        _data.append([x, y, z])
    chart = Line3D("3D 折线图-自动旋转", **style.init_style)
    chart.add("", _data, is_visualmap=True, visual_range_color=RANGE_COLOR,
              visual_range=[0, 30], is_grid3d_rotate=True,
              grid3d_rotate_speed=180)
    page.add(chart)

    return page
