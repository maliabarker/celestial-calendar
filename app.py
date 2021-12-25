from flask import Flask, render_template
from flask_pymongo import pymongo
import datetime
from datetime import date, datetime

CONNECTION_STRING = 'mongodb+srv://maliabarker:tpofbawf@cluster0.hllse.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_default_database()
events = db.events

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/events')
def events_index():
    return render_template('events.html')

def find_closest_date():
    date = events.find_one( { 'date': { '$gte': datetime.now() } } )
    return date

print(find_closest_date())
# today = date.today()
# print(today)


if __name__ == '__main__':
    app.run(debug=True, port=5002)
