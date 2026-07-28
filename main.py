import os

from flask import Flask, render_template
import core.database
import core.monitor
import core.reports

app = Flask(__name__)

# Make sure the SQLite table exists before any route tries to use it
core.database.init_db()

@app.route("/")
def home():
    return render_template("home.html", active="home")

@app.route("/monitor")
def monitor_page():
    data = core.monitor.monitor()
    return render_template("monitor.html", websites=data, active="monitor")

@app.route("/report")
def report_page():

    reports = core.reports.report()

    return render_template(
        "report.html",
        reports=reports,
        active="report"
    )

if __name__ == "__main__":
    # PORT / DEBUG are read from the environment so the same code runs
    # locally (defaults below) and on a hosting platform (which injects PORT).
    port = int(os.environ.get("PORT", 8080))
    debug = os.environ.get("FLASK_DEBUG", "true").lower() == "true"
    app.run(host="0.0.0.0", debug=debug, port=port)