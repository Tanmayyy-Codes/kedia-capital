from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

JOBS = [
        {
            "id": 1,
            "title": "Software Engineer",
            "location": "New York, USA",
            "salary": "$120,000"
        },
        {
            "id": 2,
            "title": "Data Analyst",
            "location": "Toronto, Canada",
            "salary": "$85,000"
        },
        {
            "id": 3,
            "title": "Marketing Manager",
            "location": "London, UK",
            "salary": "£75,000"
        },
        {
            "id": 4,
            "title": "Product Designer",
            "location": "Berlin, Germany",
            "salary": "€70,000"
        },
        {
            "id": 5,
            "title": "Cybersecurity Specialist",
            "location": "San Francisco, USA",
            "salary": "$130,000"
        },
        {
            "id": 6,
            "title": "AI Research Scientist",
            "location": "Tokyo, Japan",
            "salary": "¥15,000,000"
        }
    ]


@app.route('/')
def index():
  return render_template('home.html', jobs = JOBS, company_name = 'Kedia Capital')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if (__name__ == '__main__'):
  app.run(host = '0.0.0.0', port = 8080, debug = True)

# def hello_world():
#   return "Hello World!"

# print(hello_world())