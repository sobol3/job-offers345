from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        "id": "1",
        "title": "Junior",
        "salary": "12.000$",
        "location": "New York, USA"
    },
    {
        "id": "2",
        "title": "Regular",
        "salary": "15.000$",
        "location": "London, UK"
    },
    {
        "id": "3",
        "title": "Senior",
        "salary": "22.000$",
        "location": "Warsaw, Poland"
    },
]https://github.com/sobol3/job-offers


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
