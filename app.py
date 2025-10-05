from flask import Flask, render_template, send_file
import pandas as pd
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    csv_file = "jobs.csv"
    jobs = []
    if os.path.exists(csv_file):
        jobs = pd.read_csv(csv_file).to_dict(orient="records")
    return render_template("index.html", jobs=jobs)

@app.route("/download")
def download_csv():
    return send_file("jobs.csv", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

