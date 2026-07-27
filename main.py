from flask import Flask, render_template
import core.database
import core.monitor
import core.reports

app = Flask(__name__)

# Make sure the SQLite table exists before any route tries to use it
core.database.init_db()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/monitor")
def monitor_page():
    data = core.monitor.monitor()
    return render_template("monitor.html", websites=data)

@app.route("/report")
def report_page():

    reports = core.reports.report()

    return render_template(
        "report.html",
        reports=reports
    )

if __name__ == "__main__":
    app.run(debug=True, port=8080)