import random
import pandas as pd

from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

from pyecharts import Bar, Pie, Line, Overlap, Page, Timeline, Grid, Style
from app.charts.constants import WIDTH, HEIGHT


def create_charts():
    page = Page()

    style = Style(
        width=WIDTH, height=HEIGHT
    )
    performance = Line("Performance Summary", **style.init_style)

    us_bd = CustomBusinessDay(calendar=USFederalHolidayCalendar())
    dates = pd.date_range('2017-10-26', periods=100, freq=us_bd)

    self_record = [0.135, 0.155, 0.108, 0.094, -0.052, 0.1, 0.16, -0.166, 0.198, 0.055, -0.04, 0.024, 0.077, 0.148,
                   0.035, -0.068, -0.108, -0.092, -0.016, 0.142, -0.034, -0.077, -0.185, 0.077, -0.158, 0.021, -0.111,
                   -0.1, 0.079, 0.092, 0.119, -0.139, -0.104, 0.045, -0.195, 0.053, -0.078, -0.046, -0.192, -0.05,
                   0.159, -0.058, 0.094, -0.072, 0.005, 0.057, 0.173, -0.077, -0.164, 0.071, -0.088, 0.007, 0.12, -0.07,
                   -0.091, 0.059, 0.177, 0.107, -0.122, 0.005, 0.09, -0.108, -0.102, -0.006, -0.07, 0.07, -0.111,
                   -0.164, -0.051, -0.129, -0.151, -0.192, -0.083, 0.144, 0.132, 0.013, 0.09, 0.123, 0.187, -0.12,
                   0.102, -0.064, -0.014, -0.19, -0.093, -0.199, -0.155, 0.078, -0.05, -0.123, 0.067, 0.186, -0.04,
                   -0.019, -0.146, -0.007, 0.167, -0.082, -0.17, 0.055]
    mirror_record = [0.079, 0.024, 0.073, 0.105, 0.034, 0.085, 0.07, 0.091, 0.084, 0.053, 0.14, 0.195, 0.2, 0.195,
                     0.068, 0.212, 0.15, 0.071, 0.138, 0.1, 0.256, 0.288, 0.292, 0.28, 0.323, 0.308, 0.252, 0.324,
                     0.275, 0.197, 0.369, 0.222, 0.336, 0.315, 0.393, 0.36, 0.362, 0.416, 0.324, 0.435, 0.32, 0.36, 0.4,
                     0.361, 0.505, 0.407, 0.559, 0.503, 0.473, 0.402, 0.471, 0.472, 0.491, 0.484, 0.543, 0.584, 0.656,
                     0.628, 0.555, 0.635, 0.581, 0.525, 0.597, 0.603, 0.584, 0.679, 0.617, 0.65, 0.701, 0.61, 0.684,
                     0.709, 0.671, 0.677, 0.81, 0.73, 0.769, 0.698, 0.788, 0.745, 0.785, 0.732, 0.808, 0.922, 0.797,
                     0.905, 0.811, 0.969, 0.834, 0.928, 0.812, 0.947, 0.961, 0.873, 0.844, 1.009, 0.93, 1.039, 1.022,
                     0.968]
    overall = [0.214, 0.179, 0.181, 0.199, -0.018, 0.185, 0.23, -0.075, 0.282, 0.108, 0.1, 0.219, 0.277, 0.343, 0.103,
               0.144, 0.042, -0.021, 0.122, 0.242, 0.222, 0.211, 0.107, 0.357, 0.165, 0.329, 0.141, 0.224, 0.354, 0.289,
               0.488, 0.083, 0.232, 0.36, 0.198, 0.413, 0.284, 0.37, 0.132, 0.385, 0.479, 0.302, 0.494, 0.289, 0.51,
               0.464, 0.732, 0.426, 0.309, 0.473, 0.383, 0.479, 0.611, 0.414, 0.452, 0.643, 0.833, 0.735, 0.433, 0.64,
               0.671, 0.417, 0.495, 0.597, 0.514, 0.749, 0.506, 0.486, 0.65, 0.481, 0.533, 0.517, 0.588, 0.821, 0.942,
               0.743, 0.859, 0.821, 0.975, 0.625, 0.887, 0.668, 0.794, 0.732, 0.704, 0.706, 0.656, 1.047, 0.784, 0.805,
               0.879, 1.133, 0.921, 0.854, 0.698, 1.002, 1.097, 0.957, 0.852, 1.023]

    performance.add("Overall", dates, overall,
                    mark_point=["max", "min"], mark_line=["average"], is_datazoom_show=True,
                    datazoom_type='both',
                    datazoom_range=[10, 50])
    performance.add("Self", dates, self_record,
                    mark_point=["max", "min"], mark_line=["average"], is_datazoom_show=True,
                    datazoom_type='both',
                    datazoom_range=[10, 50], legend_pos="40%")
    performance.add("Mirror", dates, mirror_record,
                    mark_point=["max", "min"], mark_line=["average"], is_datazoom_show=True,
                    datazoom_type='both',
                    datazoom_range=[10, 50], legend_pos="40%")
    page.add(performance)

    portfolio = Pie("Portfolio Summary", **style.init_style)
    sectors = ['Technology', 'Industrials', 'Financials', 'Consumer Cyclicals', 'Communications', 'Unclassified']
    self_placement = [7604, 4649, 8745, 5905, 6592, 7181]
    mirror_placement = [9521, 4902, 1065, 5416, 5150, 6042]
    over_placement = [17125, 9551, 9810, 11321, 11742, 13223]

    portfolio.add("Self", sectors, self_placement,
                  radius=[10, 30], center=[75, 50], is_random=True, rosetype='radius', legend_pos="25%")
    portfolio.add("Mirror", sectors, mirror_placement,
                  radius=[40, 70], center=[75, 50], is_random=True, rosetype='radius')
    portfolio.add("Overall", sectors, over_placement,
                  radius=[0, 70], center=[25, 50], is_random=True, rosetype='radius', is_label_show=True)

    page.add(portfolio)
    return page
