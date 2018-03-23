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
    dates = pd.date_range('2017-10-17', periods=100, freq=us_bd)

    self_record = [round(random.uniform(-0.2, 0.2), 3) for _ in range(100)]
    mirror_record = [round(random.uniform(0.2, 0.5), 3) for _ in range(100)]
    overall = [round(self_record[i] + mirror_record[i], 3) for i in range(len(self_record))]

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

    portfolio = Pie("Portfolio", **style.init_style)
    sectors = ['Technology', 'Industrials', 'Financials', 'Consumer Cyclicals', 'Communications', 'Unclassified']
    self_placement = [random.randint(1000, 10000) for _ in range(len(sectors))]
    mirror_placement = [random.randint(1000, 10000) for _ in range(len(sectors))]
    over_placement = [self_placement[i] + mirror_placement[i] for i in range(len(sectors))]

    portfolio.add("Self", sectors, self_placement,
                  radius=[10, 30], center=[75, 50], is_random=True, rosetype='radius')
    portfolio.add("Mirror", sectors, mirror_placement,
                  radius=[40, 70], center=[75, 50], is_random=True, rosetype='radius')
    portfolio.add("Overall", sectors, over_placement,
                  radius=[0, 70], center=[25, 50], is_random=True, rosetype='radius', is_label_show=True)

    page.add(portfolio)
    return page
