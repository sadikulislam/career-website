from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'title': 'Python Developer',
        'location': 'Dhaka, Bangladesh',
        'salary': '40,000 taka'
    },
    {
        'id' : 2,
        'title': 'Data Analyist',
        'location': 'Remote',
        'salary': '30,000 taka'
    },
    {
        'id' : 3,
        'title': 'Fontend Engineer',
        'location': 'Dhaka, Bangladesh',
    },
    {
        'id' : 4,
        'title': 'Network Engineer',
        'location': 'Rajshahi, Bangladesh',
        'salary': '20,000 taka'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='127.0.0.0', debug=True)