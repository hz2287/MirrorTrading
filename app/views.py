from flask import render_template
import app.charts as charts

from . import app


@app.route("/")
def search():
    return render_template('search.html', title='Search')

@app.route("/dashboard")
def hello():
    _dashboard = charts.dashboard.create_charts()
    return render_template('base.html',
                           title='dashboard_class',
                           source_file='dashboard',
                           myechart=_dashboard.render_embed(),
                           script_list=_dashboard.get_js_dependencies())


@app.route('/aboutus')
def dashboard():
    return render_template('aboutus.html', title='About Us')


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
