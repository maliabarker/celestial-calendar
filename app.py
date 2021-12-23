from flask import Flask, render_template
from flask_pymongo import pymongo
import datetime

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
    events.find({'date': $gte: 25})
    # events.find( {{'date': { $gte: '2021, 12, 23' } }} )

if __name__ == '__main__':
    app.run(debug=True, port=5002)
